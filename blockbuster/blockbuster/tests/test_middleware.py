import unittest
from http import HTTPStatus
from unittest.mock import MagicMock

from django.http import JsonResponse
from requests import request

from blockbuster.middleware import JsonExceptions
from movies.infrastructure.clients import FailedDependencyError


class FakeError(Exception):
    pass


class TestMiddleware(unittest.TestCase):

    def test_process_exception_should_return_json_response(self):
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
        # arrange
        get_response = MagicMock(name='get_response')

        # act
        middleware = JsonExceptions(get_response)
        response = middleware.process_exception(request, FakeError(Exception()))

        # assert
        self.assertIsNone(response)
