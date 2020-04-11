from movies.domain.models import Character, MovieIds, People, MovieId, Movie


def character_random_with_movie_ids(movie_ids: MovieIds) -> Character:
    return Character('456', 'Luke Skywalker', 'Male', 18, 'Green', 'Brown', movie_ids)


def movie_random_with_movie_id_and_people(movie_id: MovieId, people: People) -> Movie:
    return Movie(movie_id, 'Star Wars', 'Jedis vs Siths', 'George Lucas', 'JJ Abrams', 1977, 100, people)
