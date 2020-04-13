"""Test cases.

Help with the all the test related with movies package
"""

import os
import unittest
from typing import Any
from unittest.mock import MagicMock

from movies.application.transformers import MoviesDtoTransformer
from movies.application.use_cases import GetMovies
from movies.domain.services import GetMovies as GetMoviesService
from movies.infrastructure.clients import GhibliClient
from movies.infrastructure.repositories import GhibliMovieRepository, CacheMovieRepositoryDecorator

os.environ['DJANGO_SETTINGS_MODULE'] = 'blockbuster.settings.test'


class MoviesTestCases(unittest.TestCase):
    """Movies test cases."""

    ghibli_client_fake: object
    movies_repository: object

    def movie_repository_mock(self):
        """Return a movie_repository mock."""
        if not hasattr(self, 'movie_repository'):
            self.movie_repository = MagicMock(name='movie_repository')

        return self.movie_repository

    def movie_repository_mock__find_all(self, response: Any):
        """Fix the return value to find_all from movie_repository."""
        self.movie_repository_mock().find_all.return_value = response

    def get_movies_application(self):
        """Return use case GetMovies."""
        get_movies_services = GetMoviesService(self.movie_repository_mock())

        return GetMovies(get_movies_services, MoviesDtoTransformer())

    def ghibli_client_mock(self):
        """Return ghibli_client mock."""
        if not hasattr(self, 'ghibli_client_fake'):
            self.ghibli_client_fake = MagicMock(name='ghibli_client_fake')

        return self.ghibli_client_fake

    def ghibli_client_mock__movies(self, response: Any):
        """Return a fixed value to the movies method."""
        self.ghibli_client_mock().movies.return_value = response

    def ghibli_client_mock__people(self, response: Any):
        """Return a fixed value to the people method."""
        self.ghibli_client_mock().people.return_value = response

    def ghibli_movie_repository(self):
        """Return the GhibliMovieRepository."""
        return GhibliMovieRepository(self.ghibli_client_mock())

    def cache_movie_repository_decorator(self):
        """Return the CacheMovieRepositoryDecorator."""
        return CacheMovieRepositoryDecorator(self.movie_repository_mock(), 'test_blockbuster')

    def ghibli_client(self) -> GhibliClient:
        """Return the GhibliClient."""
        return GhibliClient()
