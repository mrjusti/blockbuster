from django.core.cache import cache

from movies.domain.models import MovieRepository, Movies


class CacheMovieRepositoryDecorator(MovieRepository):
    prefix: str
    movie_repository: MovieRepository

    def __init__(self, movie_repository: MovieRepository, prefix: str):
        self.prefix = prefix
        self.movie_repository = movie_repository

    def find_all(self) -> Movies:
        movies = cache.get(f'{self.prefix}.movie_repository.find_all')
        if movies is not None:
            return movies

        movies = self.movie_repository.find_all()
        cache.set(f'{self.prefix}.movie_repository.find_all', movies, timeout=180)

        return movies
