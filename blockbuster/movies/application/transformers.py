from __future__ import annotations

import json

from movies.domain.models import Movies, Movie, Character


class MoviesTransformer:

    def write(self, movies: Movies) -> MoviesTransformer:
        return self

    def read(self):
        pass


class MoviesJsonTransformer(MoviesTransformer):
    movies: Movies

    def write(self, movies: Movies) -> MoviesTransformer:
        self.movies = movies

        return self

    def read(self) -> json:
        return [_movies_to_json(movie) for movie in self.movies.movies]


def _movies_to_json(movie: Movie) -> json:
    people = [_character_to_json(character) for character in movie.people.people]

    return {'id': movie.movie_id.movie_id, 'title': movie.title, 'description': movie.description,
            'director': movie.director,
            'producer': movie.producer, 'release_date': movie.release_date,
            'rt_score': movie.rt_score, 'people': people}


def _character_to_json(character: Character) -> json:
    return {'name': character.name, 'gender': character.gender, 'age': character.age,
            'eye_color': character.eye_color, 'hair_color': character.hair_color}
