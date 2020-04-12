import json
import os

import jsonschema

from movies.tests.movies_test_cases import MoviesTestCases


class TestGhibliClient(MoviesTestCases):

    def test_movies(self):
        # arrange
        with open(os.path.dirname(os.path.abspath(__file__)) + '/movies.json', 'r') as f:
            schema_data = f.read()
        schema = json.loads(schema_data)

        # act
        response = self.ghibli_client().movies(1)

        # assert
        jsonschema.validate(response, schema)

    def test_people(self):
        # arrange
        with open(os.path.dirname(os.path.abspath(__file__)) + '/people.json', 'r') as f:
            schema_data = f.read()
        schema = json.loads(schema_data)

        # act
        response = self.ghibli_client().people(1)

        # assert
        jsonschema.validate(response, schema)
