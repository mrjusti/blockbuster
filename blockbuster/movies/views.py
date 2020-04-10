from django.http import JsonResponse


from movies.application.services import GetMovies
from movies.application.transformers import MoviesJsonTransformer
from movies.domain.services import GetMovies as GetMoviesService
from movies.infrastructure.clients import GhibliClient
from movies.infrastructure.repositories import GhibliMoviesRepository


def movies(request):
    app = GetMovies(MoviesJsonTransformer(), GetMoviesService(GhibliMoviesRepository(GhibliClient())))

    return JsonResponse(app(), safe=False)
