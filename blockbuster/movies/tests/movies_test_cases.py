import os
import unittest
from typing import Any
from unittest.mock import MagicMock

from movies.application.transformers import MoviesJsonTransformer
from movies.application.use_cases import GetMovies
from movies.domain.services import GetMovies as GetMoviesService
from movies.infrastructure.decorators import CacheMovieRepositoryDecorator
from movies.infrastructure.repositories import GhibliMovieRepository

os.environ['DJANGO_SETTINGS_MODULE'] = 'blockbuster.settings.test'


class MoviesTestCases(unittest.TestCase):
    ghibli_client: object
    movies_repository: object

    def movie_repository_mock(self):
        if not hasattr(self, 'movie_repository'):
            self.movie_repository = MagicMock(name='movie_repository')

        return self.movie_repository

    def movie_repository_mock__find_all(self, response: Any):
        self.movie_repository_mock().find_all.return_value = response

    def get_movies_application(self):
        get_movies_services = GetMoviesService(self.movie_repository_mock())

        return GetMovies(get_movies_services, MoviesJsonTransformer())

    def ghibli_client_mock(self):
        if not hasattr(self, 'ghibli_client'):
            self.ghibli_client = MagicMock(name='ghibli_client')

        return self.ghibli_client

    def ghibli_client_mock__movies(self, response: Any):
        self.ghibli_client_mock().movies.return_value = response

    def ghibli_client_mock__people(self, response: Any):
        self.ghibli_client_mock().people.return_value = response

    def ghibli_movie_repository(self):

        return GhibliMovieRepository(self.ghibli_client_mock())

    def cache_movie_repository_decorator(self):

        return CacheMovieRepositoryDecorator(self.movie_repository_mock(), 'test_blockbuster')
