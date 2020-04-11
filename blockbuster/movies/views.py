from django.http import JsonResponse

from blockbuster.settings.dev import BASE_DIR
from movies.application.use_cases import GetMovies
from movies.application.transformers import MoviesJsonTransformer
from movies.domain.services import GetMovies as GetMoviesService
from movies.infrastructure.clients import GhibliClient
from movies.infrastructure.decorators import CacheMovieRepositoryDecorator
from movies.infrastructure.repositories import GhibliMovieRepository


def movies(request):
    print(BASE_DIR)
    repository = CacheMovieRepositoryDecorator(GhibliMovieRepository(GhibliClient()), 'blockbuster')
    get_movies_services = GetMoviesService(repository)
    app = GetMovies(get_movies_services, MoviesJsonTransformer())

    return JsonResponse(app(), safe=False)
