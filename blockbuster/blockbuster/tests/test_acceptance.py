from http import HTTPStatus

import django

from django.test import Client
from django.urls import reverse
from movies.tests.movies_test_cases import MoviesTestCases


class TestGetMovies(MoviesTestCases):

    def test_get_movies(self):
        # arrange
        django.setup()

        # act
        c = Client()
        resp = c.get(reverse('view_movies'))

        # assert
        self.assertEqual(HTTPStatus.OK, resp.status_code)
