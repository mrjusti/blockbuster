import unittest
from typing import Any
from unittest.mock import MagicMock

from movies.application.transformers import MoviesJsonTransformer
from movies.application.use_cases import GetMovies
from movies.domain.services import GetMovies as GetMoviesService


class MoviesTestCases(unittest.TestCase):

    movies_repository: object

    def movie_repository_mock(self):
        if not hasattr(self, 'movie_repository'):
            print('not exist')
            self.movie_repository = MagicMock(name='movie_repository')

        return self.movie_repository

    def movie_repository_mock__find_all(self, response: Any):
        self.movie_repository_mock().find_all.return_value = response

    def get_movies_application(self):
        get_movies_services = GetMoviesService(self.movie_repository_mock())

        return GetMovies(get_movies_services, MoviesJsonTransformer())
