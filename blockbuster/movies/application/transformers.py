"""Transformer module.

Transformer the entities from the domain in a type that could be understand outside the application package.
"""

from __future__ import annotations

from movies.domain.models import Movies, Movie, Character


class MoviesTransformer:
    """Interface for the MoviesTransformer."""

    def write(self, movies: Movies) -> MoviesTransformer:
        """Receive a Movies object and return the self class."""
        return self

    def read(self):
        """Return the Movies class already transformed."""
        pass


class MoviesDtoTransformer(MoviesTransformer):
    """Transform the Movies object into a dictionary."""

    movies: Movies

    def write(self, movies: Movies) -> MoviesTransformer:
        """Receive a Movies object and return the self class."""
        self.movies = movies

        return self

    def read(self) -> list:
        """Return a dictionary with the Movies data."""
        return [_movies_to_json(movie) for movie in self.movies.movies]


def _movies_to_json(movie: Movie) -> dict:
    people = [_character_to_json(character) for character in movie.people.people]

    return {'id': movie.movie_id.movie_id, 'title': movie.title, 'description': movie.description,
            'director': movie.director,
            'producer': movie.producer, 'release_date': movie.release_date,
            'rt_score': movie.rt_score, 'people': people}


def _character_to_json(character: Character) -> dict:
    return {'name': character.name, 'gender': character.gender, 'age': character.age,
            'eye_color': character.eye_color, 'hair_color': character.hair_color}
