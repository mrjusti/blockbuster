from django.core.cache import cache

from movies.domain.models import MovieId, People, MovieIds, Movies
from movies.tests.movies_test_cases import MoviesTestCases
from movies.tests.stub.models import character_random_with_movie_ids, movie_random_with_movie_id_and_people


class TestCacheMovieRepositoryDecorator(MoviesTestCases):

    def setUp(self) -> None:
        cache.delete('test_blockbuster.movie_repository.find_all')

    def test_find_all_miss_cache(self):
        # arrange
        movie_id = MovieId('123')
        character = character_random_with_movie_ids(MovieIds([movie_id]))
        people = People([character])
        movie = movie_random_with_movie_id_and_people(movie_id, people)
        expected = Movies([movie])
        self.movie_repository_mock__find_all(expected)

        # act
        repository = self.cache_movie_repository_decorator()
        response = repository.find_all()

        # assert
        self.assertEqual(expected, response)
        self.assertEqual(1, self.movie_repository_mock().find_all.call_count)

    def test_find_all_hit_cache(self):
        # arrange
        movie_id_one = MovieId('123')
        movie_id_two = MovieId('789')
        character = character_random_with_movie_ids(MovieIds([movie_id_one, movie_id_two]))
        people = People([character])

        movie_one = movie_random_with_movie_id_and_people(movie_id_one, people)
        not_expected = Movies([movie_one])

        movie_two = movie_random_with_movie_id_and_people(movie_id_two, people)
        expected = Movies([movie_two])

        self.movie_repository_mock__find_all(not_expected)
        cache.set('test_blockbuster.movie_repository.find_all', expected, timeout=180)

        # act
        repository = self.cache_movie_repository_decorator()
        response = repository.find_all()

        # assert
        self.assertNotEqual(not_expected, response)
        self.assertEqual(expected, response)
        self.assertEqual(0, self.movie_repository_mock().find_all.call_count)
