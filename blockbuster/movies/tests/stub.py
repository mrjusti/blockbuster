"""Stub the models."""

from movies.domain.models import Character, MovieIds, People, MovieId, Movie, CharacterId, Name, Gender, Age, EyeColor, \
    HairColor, Title, Description, Director, Producer, ReleaseDate, RatingScore


def character_random_with_movie_ids(movie_ids: MovieIds) -> Character:
    """Return a Character instance."""
    return Character(CharacterId('456'), Name('Luke Skywalker'), Gender('Male'), Age('18'), EyeColor('Green'),
                     HairColor('Brown'), movie_ids)


def movie_random_with_movie_id_and_people(movie_id: MovieId, people: People) -> Movie:
    """Return a Movie instance."""
    return Movie(movie_id, Title('Star Wars'), Description('Jedis vs Siths'), Director('George Lucas'),
                 Producer('JJ Abrams'), ReleaseDate('1977'), RatingScore('100'), people)
