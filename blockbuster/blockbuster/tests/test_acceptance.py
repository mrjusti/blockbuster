"""Acceptance tests.

Basically these are end to end tests.
"""

from http import HTTPStatus

import django

from django.test import Client
from django.urls import reverse
from movies.tests.test_cases import MoviesTestCases


class TestGetMovies(MoviesTestCases):
    """Test the use case get_movies."""

    def test_get_movies(self):
        """Call the view get_movies."""
        # arrange
        django.setup()

        # act
        c = Client()
        resp = c.get(reverse('get_movies'))

        # assert
        self.assertEqual(HTTPStatus.OK, resp.status_code)
