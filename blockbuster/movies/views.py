"""Views for the package movies."""

from django.http import JsonResponse

from movies.application.use_cases import GetMovies
from movies.application.transformers import MoviesDtoTransformer
from movies.domain.services import GetMovies as GetMoviesService
from movies.infrastructure.clients import GhibliClient
from movies.infrastructure.repositories import GhibliMovieRepository, CacheMovieRepositoryDecorator


def get_movies(request):
    """Return a json from the use case GetMovies in the package application."""
    repository = CacheMovieRepositoryDecorator(GhibliMovieRepository(GhibliClient()), 'blockbuster')
    get_movies_services = GetMoviesService(repository)
    app = GetMovies(get_movies_services, MoviesDtoTransformer())

    return JsonResponse(app(), safe=False)
