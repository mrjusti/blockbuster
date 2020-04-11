from movies.domain.models import Movies, People, MovieIds, MovieId
from movies.tests.movies_test_cases import MoviesTestCases
from movies.tests.stub.models import character_random_with_movie_ids, movie_random_with_movie_id_and_people


class TestGetMovies(MoviesTestCases):

    def test_get_movies(self):
        # arrange
        movie_id = MovieId('123')
        character = character_random_with_movie_ids(MovieIds([movie_id]))
        people = People([character])
        movie = movie_random_with_movie_id_and_people(movie_id, people)
        self.movie_repository_mock__find_all(Movies([movie]))

        # act
        app = self.get_movies_application()
        response = app()

        # assert
        expect = [{'id': movie_id.movie_id, 'title': movie.title, 'description': movie.description,
                   'director': movie.director,
                   'producer': movie.producer, 'release_date': movie.release_date,
                   'rt_score': movie.rt_score,
                   'people': [{'name': character.name, 'gender': character.gender, 'age': character.age,
                               'eye_color': character.eye_color, 'hair_color': character.hair_color}]}]
        self.assertEqual(expect, response)
