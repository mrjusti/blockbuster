"""Use cases module.

Here you can find the use case for the application package. This is the entry point for the domain package.
"""

from movies.application.transformers import MoviesTransformer
from movies.domain.services import GetMovies as GetMoviesService


class GetMovies:
    """Return the movies list with the people involve on it."""

    get_movies: GetMoviesService
    movies_transformer: MoviesTransformer

    def __init__(self, get_movies: GetMoviesService, movies_transformer: MoviesTransformer):
        """Init the use case with all the dependencies need it. The domain logic and the transformer."""
        self.get_movies = get_movies
        self.movies_transformer = movies_transformer

    def __call__(self):
        """Execute the domain logic and transformed to returned to the view."""
        return self.movies_transformer.write(self.get_movies()).read()
