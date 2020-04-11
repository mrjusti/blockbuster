from movies.domain.models import Movies, MovieRepository


class GetMovies:
    movie_repository: MovieRepository

    def __init__(self, movie_repository: MovieRepository):
        self.movie_repository = movie_repository

    def __call__(self) -> Movies:
        return self.movie_repository.find_all()
