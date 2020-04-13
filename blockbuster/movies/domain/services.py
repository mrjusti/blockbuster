"""Domain services.

Here we can find some domain logic but not related with entities.
Normally are the entry points from the application package.
"""

from movies.domain.models import Movies, MovieRepository


class GetMovies:
    """Domain logic to get the movies."""

    movie_repository: MovieRepository

    def __init__(self, movie_repository: MovieRepository):
        """Init the class need the MovieRepository."""
        self.movie_repository = movie_repository

    def __call__(self) -> Movies:
        """Return the Movies."""
        return self.movie_repository.find_all()
