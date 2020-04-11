from movies.domain.models import MovieId, People, Movies, MovieIds
from movies.tests.movies_test_cases import MoviesTestCases
from movies.tests.stub.models import character_random_with_movie_ids, movie_random_with_movie_id_and_people


class TestGhibliMovieRepository(MoviesTestCases):

    def test_find_all(self):
        # arrange
        movie_id = MovieId('123')
        character = character_random_with_movie_ids(MovieIds([movie_id]))
        people = People([character])
        movie = movie_random_with_movie_id_and_people(movie_id, people)
        expected = Movies([movie])

        self.ghibli_client_mock__people([{'id': character.character_id, 'name': character.name,
                                          'gender': character.gender, 'age': character.age,
                                          'eye_color': character.eye_color, 'hair_color': character.hair_color,
                                          'films': ['http://url/123']}])
        self.ghibli_client_mock__movies([{'id': movie_id.movie_id, 'title': movie.title,
                                          'description': movie.description, 'director': movie.director,
                                          'producer': movie.producer, 'release_date': movie.release_date,
                                          'rt_score': movie.rt_score}])

        # act
        repository = self.ghibli_movie_repository()
        movies = repository.find_all()

        # assert
        self.assertEqual(expected, movies)
