from __future__ import annotations


class Movies:
    movies: list

    def __init__(self, movies: list):
        self.movies = movies


class Movie:
    people: People
    description: str
    director: str
    producer: str
    release_date: int
    rt_score: int
    movie_id: MovieId
    title: str

    def __init__(self, movie_id: MovieId, title: str, description: str, director: str, producer: str, release_date: int,
                 rt_score: int, people: People):
        self.rt_score = rt_score
        self.release_date = release_date
        self.producer = producer
        self.director = director
        self.description = description
        self.movie_id = movie_id
        self.title = title
        self.people = people


class MovieId:
    movie_id: str

    def __init__(self, movie_id: str):
        self.movie_id = movie_id


class MovieIds:
    movie_ids: list

    def __init__(self, movie_ids: list):
        self.movie_ids = movie_ids

    def raw(self) -> list:
        return [movie_id.movie_id for movie_id in self.movie_ids]


class People:
    people: list

    def __init__(self, people: list):
        self.people = people

    def filter_by_movie_id(self, movie_id: MovieId) -> People:
        characters = [character for character in self.people if movie_id.movie_id in character.movie_ids.raw()]

        return People(characters)


class Character:
    movie_ids: MovieIds
    eye_color: str
    character_id: str
    name: str
    gender: str
    age: str
    hair_color: str

    def __init__(self, character_id: str, name: str, gender: str, age: str, eye_color: str, hair_color: str,
                 movie_ids: MovieIds):
        self.movie_ids = movie_ids
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.age = age
        self.gender = gender
        self.name = name
        self.character_id = character_id


class MovieRepository:

    def find_all(self) -> Movies:
        pass
