from http import HTTPStatus

from django.http import JsonResponse

from movies.infrastructure.clients import FailedDependencyError


class JsonExceptions:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_exception(self, request, exception):
        if not isinstance(exception, FailedDependencyError):
            return None

        return JsonResponse(
            {'status': HTTPStatus.INTERNAL_SERVER_ERROR, 'message': 'Something went wrong, try again in a few moment.'},
            safe=False,
            status=HTTPStatus.INTERNAL_SERVER_ERROR)
