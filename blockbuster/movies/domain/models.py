"""Domain models.

Here we can find the entities, value objects and repositories for the application.
"""

from __future__ import annotations


class Movies(list):
    """Contain a list with all the Movie objects."""

    pass


class Movie:
    """Entity movie.

    It is the aggregate root that contain all the data from the film and the people that appear on it.
    """

    people: People
    description: Description
    director: Director
    producer: Producer
    release_date: ReleaseDate
    rt_score: RatingScore
    movie_id: MovieId
    title: Title

    def __init__(self, movie_id: MovieId, title: Title, description: Description, director: Director,
                 producer: Producer, release_date: ReleaseDate, rt_score: RatingScore, people: People):
        """Init the instance for the Movie entity."""
        self.rt_score = rt_score
        self.release_date = release_date
        self.producer = producer
        self.director = director
        self.description = description
        self.movie_id = movie_id
        self.title = title
        self.people = people

    def __eq__(self, other):
        """Check if two instances of the class are the same.

        We don't check if has the same instance, we actually don't care. If act as a duck, it is a duck.
        """
        is_main_eq = self.title == other.title and self.description == other.description
        is_prod_eq = self.producer == other.producer and self.director == other.director
        is_rel_eq = self.release_date == other.release_date
        is_rt_eq = self.rt_score == other.rt_score
        is_people_eq = self.people == other.people
        is_id_eq = self.movie_id == other.movie_id
        is_content_eq = is_main_eq and is_prod_eq and is_rel_eq and is_rt_eq and is_people_eq and is_id_eq

        return is_content_eq


class MovieId(str):
    """MovieId it is a value object that represent the identifier for a movie."""

    pass


class Title(str):
    """Title it is a value object that represent the title for a movie."""

    pass


class Description(str):
    """Description it is a value object that represent the description for a movie."""

    pass


class Director(str):
    """Director it is a value object that represent the director for a movie."""

    pass


class Producer(str):
    """Producer it is a value object that represent the producer for a movie."""

    pass


class ReleaseDate(str):
    """ReleaseDate it is a value object that represent the release date for a movie."""

    pass


class RatingScore(str):
    """RatingScore it is a value object that represent the rating score for a movie."""

    pass


class MovieIds(list):
    """Contain a list with MovieId."""

    pass


class People(list):
    """Object that contain a list of Character."""

    def filter_by_movie_id(self, movie_id: MovieId) -> People:
        """Filter the list of Characters returning only the ones that appear in the MovieId given."""
        characters = [character for character in self if movie_id in character.movie_ids]

        return People(characters)


class Character:
    """Entity that represent a Character fron a movie."""

    movie_ids: MovieIds
    eye_color: EyeColor
    character_id: CharacterId
    name: Name
    gender: Gender
    age: Age
    hair_color: HairColor

    def __init__(self, character_id: CharacterId, name: Name, gender: Gender, age: Age, eye_color: EyeColor,
                 hair_color: HairColor, movie_ids: MovieIds):
        """Init the Character with all the attributes need it."""
        self.movie_ids = movie_ids
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.age = age
        self.gender = gender
        self.name = name
        self.character_id = character_id

    def __eq__(self, other):
        """Check if two instances of the class are the same.

        We don't check if has the same instance, we actually don't care. If act as a duck, it is a duck.
        """
        is_main_eq = self.name == other.name and self.character_id == other.character_id
        is_movies_eq = self.movie_ids == other.movie_ids
        is_body_eq = self.eye_color == other.eye_color and self.hair_color == other.hair_color
        is_age_eq = self.age == other.age
        is_gender_eq = self.gender == other.gender
        is_content_eq = is_main_eq and is_movies_eq and is_body_eq and is_age_eq and is_gender_eq

        return is_content_eq


class CharacterId(str):
    """CharacterId it is a value object that represent the character id for a character."""

    pass


class Name(str):
    """Name it is a value object that represent the name for a character."""

    pass


class Gender(str):
    """Gender it is a value object that represent the gender for a character."""

    pass


class EyeColor(str):
    """EyeColor it is a value object that represent the eye color for a character."""

    pass


class HairColor(str):
    """HairColor it is a value object that represent the hair color for a character."""

    pass


class Age(str):
    """Age it is a value object that represent the age for a character."""

    pass


class MovieRepository:
    """It is the interface for the repository that will return all related with the Movie entity."""

    def find_all(self) -> Movies:
        """Return a Movies object."""
        pass
