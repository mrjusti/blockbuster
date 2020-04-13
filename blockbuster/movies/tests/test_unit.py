"""Unit tests.

There are some classes that required to have a unit test given an specific logic that made in the behaviour test do it properly.
"""

from django.core.cache import cache

from movies.domain.models import MovieId, People, MovieIds, Movies
from movies.tests.stub import character_random_with_movie_ids, movie_random_with_movie_id_and_people
from movies.tests.test_cases import MoviesTestCases


class TestGhibliMovieRepository(MoviesTestCases):
    """Test the GhibliMovieRepository."""

    def test_find_all(self):
        """Test that the method find_all return what it has to return."""
        # arrange
        movie_id = MovieId('123')
        character = character_random_with_movie_ids(MovieIds([movie_id]))
        people = People([character])
        movie = movie_random_with_movie_id_and_people(movie_id, people)
        expected = Movies([movie])

        self.ghibli_client_mock__people([{'id': character.character_id, 'name': character.name,
                                          'gender': character.gender, 'age': character.age,
                                          'eye_color': character.eye_color, 'hair_color': character.hair_color,
                                          'films': [f'http://url/{movie_id.movie_id}']}])
        self.ghibli_client_mock__movies([{'id': movie_id.movie_id, 'title': movie.title,
                                          'description': movie.description, 'director': movie.director,
                                          'producer': movie.producer, 'release_date': movie.release_date,
                                          'rt_score': movie.rt_score}])

        # act
        repository = self.ghibli_movie_repository()
        movies = repository.find_all()

        # assert
        self.assertEqual(expected, movies)

    def test_find_all_with_two_movies_two_characters(self):
        """Test that the method find_all when there are more than a movie and people match each one with the film."""
        # arrange
        movie_id_one = MovieId('abc')
        character_one = character_random_with_movie_ids(MovieIds([movie_id_one]))
        people_one = People([character_one])
        movie_one = movie_random_with_movie_id_and_people(movie_id_one, people_one)

        movie_id_two = MovieId('def')
        character_two = character_random_with_movie_ids(MovieIds([movie_id_two]))
        people_two = People([character_two])
        movie_two = movie_random_with_movie_id_and_people(movie_id_two, people_two)

        self.ghibli_client_mock__people([{'id': character_one.character_id, 'name': character_one.name,
                                          'gender': character_one.gender, 'age': character_one.age,
                                          'eye_color': character_one.eye_color, 'hair_color': character_one.hair_color,
                                          'films': [f'http://url/{movie_id_one.movie_id}']},
                                         {'id': character_two.character_id, 'name': character_two.name,
                                          'gender': character_two.gender, 'age': character_two.age,
                                          'eye_color': character_two.eye_color, 'hair_color': character_two.hair_color,
                                          'films': [f'http://url/{movie_id_two.movie_id}']}])
        self.ghibli_client_mock__movies([{'id': movie_id_one.movie_id, 'title': movie_one.title,
                                          'description': movie_one.description, 'director': movie_one.director,
                                          'producer': movie_one.producer, 'release_date': movie_one.release_date,
                                          'rt_score': movie_one.rt_score},
                                         {'id': movie_id_two.movie_id, 'title': movie_two.title,
                                          'description': movie_two.description, 'director': movie_two.director,
                                          'producer': movie_two.producer, 'release_date': movie_two.release_date,
                                          'rt_score': movie_two.rt_score}])

        # act
        repository = self.ghibli_movie_repository()
        movies = repository.find_all()

        # assert
        expected = Movies([movie_one, movie_two])
        self.assertEqual(expected, movies)


class TestCacheMovieRepositoryDecorator(MoviesTestCases):
    """Test the CacheMovieRepositoryDecorator."""

    def setUp(self) -> None:
        """Set up the test."""
        cache.delete('test_blockbuster.movie_repository.find_all')

    def test_find_all_miss_cache(self):
        """Test that if there is not any value for a key, must miss the cache."""
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
        """Test that if already exist a value in the cache, must return that value."""
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
