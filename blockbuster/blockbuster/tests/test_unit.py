"""Module that make unit test over the middleware of the app."""

import unittest
from unittest.mock import MagicMock
from requests import request
from http import HTTPStatus

from django.http import JsonResponse

from blockbuster.middleware import JsonExceptions
from movies.infrastructure.clients import FailedDependencyError


class _FakeError(Exception):
    pass


class TestJsonExceptionsMiddleware(unittest.TestCase):
    """Test the JsonException middleware."""

    def test_process_exception_should_return_json_response(self):
        """Test the pretty response when a controlled exception is raised."""
        # arrange
        get_response = MagicMock(name='get_response')
        expected = JsonResponse(
            {'status': HTTPStatus.INTERNAL_SERVER_ERROR, 'message': 'Something went wrong, try again in a few moment.'},
            safe=False,
            status=HTTPStatus.INTERNAL_SERVER_ERROR)

        # act
        middleware = JsonExceptions(get_response)
        response = middleware.process_exception(request, FailedDependencyError())

        # assert
        self.assertEqual(expected.content, response.content)
        self.assertEqual(expected.status_code, response.status_code)

    def test_process_exception_should_raise_exception(self):
        """Test that the exception when is not controlled should be raised."""
        # arrange
        get_response = MagicMock(name='get_response')

        # act
        middleware = JsonExceptions(get_response)
        response = middleware.process_exception(request, _FakeError(Exception()))

        # assert
        self.assertIsNone(response)
