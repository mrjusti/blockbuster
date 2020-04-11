from django.core.cache import cache

from movies.domain.models import MovieRepository, Movies


class CacheMovieRepositoryDecorator(MovieRepository):

    movie_repository: MovieRepository

    def __init__(self, movie_repository: MovieRepository):
        self.movie_repository = movie_repository

    def find_all(self) -> Movies:

        movies = cache.get('movie_repository.find_all')
        if movies is not None:
            return movies

        movies = self.movie_repository.find_all()
        cache.set('movie_repository.find_all', movies, timeout=180)

        return movies
