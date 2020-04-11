from movies.domain.models import Movies, People, MovieId, MovieIds, Character, Movie, MovieRepository
from movies.infrastructure.clients import GhibliClient


class GhibliMovieRepository(MovieRepository):
    client: GhibliClient

    def __init__(self, client: GhibliClient):
        self.client = client

    def find_all(self) -> Movies:

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
