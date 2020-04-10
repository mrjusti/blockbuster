from movies.application.transformers import MoviesTransformer
from movies.domain.services import GetMovies as GetMoviesService


class GetMovies:
    get_movies: GetMoviesService
    movies_transformer: MoviesTransformer

    def __init__(self, movies_transformer: MoviesTransformer, get_movies: GetMoviesService):
        self.get_movies = get_movies
        self.movies_transformer = movies_transformer

    def __call__(self):
        return self.movies_transformer.write(self.get_movies()).read()
