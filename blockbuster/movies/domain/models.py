from __future__ import annotations


class Movies:
    movies: list

    def __init__(self, movies: list):
        self.movies = movies

    def __eq__(self, other):
        is_instance_of = isinstance(other, Movies)
        is_content_eq = self.movies == other.movies

        return is_instance_of and is_content_eq


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

    def __eq__(self, other):
        is_instance_of = isinstance(other, Movie)
        is_main_eq = self.title == other.title and self.description == other.description
        is_prod_eq = self.producer == other.producer and self.director == other.director
        is_rel_eq = self.release_date == other.release_date
        is_rt_eq = self.rt_score == other.rt_score
        is_people_eq = self.people == other.people
        is_id_eq = self.movie_id == other.movie_id
        is_content_eq = is_main_eq and is_prod_eq and is_rel_eq and is_rt_eq and is_people_eq and is_id_eq

        return is_instance_of and is_content_eq


class MovieId:
    movie_id: str

    def __init__(self, movie_id: str):
        self.movie_id = movie_id

    def __eq__(self, other):
        is_instance_of = isinstance(other, MovieId)
        is_content_eq = self.movie_id == other.movie_id

        return is_instance_of and is_content_eq


class MovieIds:
    movie_ids: list

    def __init__(self, movie_ids: list):
        self.movie_ids = movie_ids

    def raw(self) -> list:
        return [movie_id.movie_id for movie_id in self.movie_ids]

    def __eq__(self, other):
        is_instance_of = isinstance(other, MovieIds)
        is_content_eq = self.movie_ids == other.movie_ids

        return is_instance_of and is_content_eq


class People:
    people: list

    def __init__(self, people: list):
        self.people = people

    def filter_by_movie_id(self, movie_id: MovieId) -> People:
        characters = [character for character in self.people if movie_id.movie_id in character.movie_ids.raw()]

        return People(characters)

    def __eq__(self, other):
        is_instance_of = isinstance(other, People)
        is_content_eq = self.people == other.people

        return is_instance_of and is_content_eq


class Character:
    movie_ids: MovieIds
    eye_color: str
    character_id: str
    name: str
    gender: str
    age: int
    hair_color: str

    def __init__(self, character_id: str, name: str, gender: str, age: int, eye_color: str, hair_color: str,
                 movie_ids: MovieIds):
        self.movie_ids = movie_ids
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.age = age
        self.gender = gender
        self.name = name
        self.character_id = character_id

    def __eq__(self, other):
        is_instance_of = isinstance(other, Character)
        is_main_eq = self.name == other.name and self.character_id == other.character_id
        is_movies_eq = self.movie_ids == other.movie_ids
        is_body_eq = self.eye_color == other.eye_color and self.hair_color == other.hair_color
        is_age_eq = self.age == other.age
        is_gender_eq = self.gender == other.gender
        is_content_eq = is_main_eq and is_movies_eq and is_body_eq and is_age_eq and is_gender_eq

        return is_instance_of and is_content_eq


class MovieRepository:

    def find_all(self) -> Movies:
        pass
