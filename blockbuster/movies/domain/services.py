from movies.domain.models import Movies
from movies.domain.repositories import MoviesRepository


class GetMovies:
    movies_repository: MoviesRepository

    def __init__(self, movies_repository: MoviesRepository):
        self.movies_repository = movies_repository

    def __call__(self) -> Movies:
        return self.movies_repository.find_all()
