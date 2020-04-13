"""Middlewares that are execute by django in each request."""
from http import HTTPStatus

from django.http import JsonResponse

from movies.infrastructure.clients import FailedDependencyError


class JsonExceptions:
    """Convert all the controlled exception to a pretty json response."""

    def __init__(self, get_response):
        """Init the middleware."""
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        """Code to be executed for each request before."""
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_exception(self, request, exception):
        """Intercept the exception and return a pretty response."""
        if not isinstance(exception, FailedDependencyError):
            return None

        return JsonResponse(
            {'status': HTTPStatus.INTERNAL_SERVER_ERROR, 'message': 'Something went wrong, try again in a few moment.'},
            safe=False,
            status=HTTPStatus.INTERNAL_SERVER_ERROR)
