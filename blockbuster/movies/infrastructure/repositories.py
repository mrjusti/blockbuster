"""Module that contain all the implementation of the repositories.

Also include any decorator that the repositories need.
"""

from django.core.cache import cache

from movies.domain.models import Movies, People, MovieId, MovieIds, Character, Movie, MovieRepository
from movies.infrastructure.clients import GhibliClient


class GhibliMovieRepository(MovieRepository):
    """Ghibli implementation for the MovieRepository."""

    client: GhibliClient

    def __init__(self, client: GhibliClient):
        """Init the repository with the GhibliClient in order to could connect with the Ghibli API."""
        self.client = client

    def find_all(self) -> Movies:
        """Return the Movies object with all the movies and people fron Ghibli."""
        people = People(list(map(_character_factory, self.client.people())))
        movies = Movies(list(map(lambda movie: _movie_factory(movie, people), self.client.movies())))

        return movies


def _character_factory(character: dict):
    films_ids = [MovieId(film.split('/')[-1]) for film in character['films']]
    movie_ids = MovieIds(films_ids)
    return Character(character['id'], character['name'], character['gender'], character['age'],
                     character['eye_color'], character['hair_color'], movie_ids)


def _movie_factory(movie: dict, people: People):
    movie_id = MovieId(movie['id'])
    return Movie(movie_id, movie['title'], movie['description'], movie['director'], movie['producer'],
                 movie['release_date'],
                 movie['rt_score'], people.filter_by_movie_id(movie_id))


class CacheMovieRepositoryDecorator(MovieRepository):
    """Decorator for the MovieRepository that implement a Cache using the django module."""

    prefix: str
    movie_repository: MovieRepository

    def __init__(self, movie_repository: MovieRepository, prefix: str):
        """Init the decorator, need the repository and a prefix to the cache system."""
        self.prefix = prefix
        self.movie_repository = movie_repository

    def find_all(self) -> Movies:
        """Overwrite the find_all from the repository with the cache system.

        The timeout of the cache is 60 seconds.
        """
        movies = cache.get(f'{self.prefix}.movie_repository.find_all')
        if movies is not None:
            return movies

        movies = self.movie_repository.find_all()
        cache.set(f'{self.prefix}.movie_repository.find_all', movies, timeout=60)

        return movies
