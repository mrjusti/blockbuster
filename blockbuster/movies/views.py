from http import HTTPStatus

from django.http import JsonResponse

from movies.application.use_cases import GetMovies
from movies.application.transformers import MoviesJsonTransformer
from movies.domain.services import GetMovies as GetMoviesService
from movies.infrastructure.clients import GhibliClient, BadRequestError, NotFoundError
from movies.infrastructure.decorators import CacheMovieRepositoryDecorator
from movies.infrastructure.repositories import GhibliMovieRepository


def movies(request):
    repository = CacheMovieRepositoryDecorator(GhibliMovieRepository(GhibliClient()), 'blockbuster')
    get_movies_services = GetMoviesService(repository)
    app = GetMovies(get_movies_services, MoviesJsonTransformer())

    try:
        response = app()
        code = HTTPStatus.OK
    except BadRequestError:
        response = {'status': HTTPStatus.BAD_REQUEST, 'message': 'Bad Request'}
        code = HTTPStatus.BAD_REQUEST
    except NotFoundError:
        response = {'status': HTTPStatus.NOT_FOUND, 'message': 'Not Found'}
        code = HTTPStatus.NOT_FOUND
    except Exception:
        response = {'status': HTTPStatus.INTERNAL_SERVER_ERROR, 'message': 'Internal Server Error'}
        code = HTTPStatus.INTERNAL_SERVER_ERROR

    return JsonResponse(response, safe=False, status=code)
