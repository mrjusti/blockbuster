"""Infrastructure tests.

Basically we test here our app against infrastructure and third party APIs.
"""

import json
import jsonschema
import os

from movies.tests.test_cases import MoviesTestCases


class TestGhibliClient(MoviesTestCases):
    """Test the Ghibli Client againt the Ghibli API."""

    def test_movies(self):
        """Test that the endpoint movies from Ghibli return a json with the expected schema."""
        # arrange
        with open(os.path.dirname(os.path.abspath(__file__)) + '/schemas/movies.json', 'r') as f:
            schema_data = f.read()
        schema = json.loads(schema_data)

        # act
        response = self.ghibli_client().movies(1)

        # assert
        jsonschema.validate(response, schema)

    def test_people(self):
        """Test that the endpoint people from Ghibli return a json with the expected schema."""
        # arrange
        with open(os.path.dirname(os.path.abspath(__file__)) + '/schemas/people.json', 'r') as f:
            schema_data = f.read()
        schema = json.loads(schema_data)

        # act
        response = self.ghibli_client().people(1)

        # assert
        jsonschema.validate(response, schema)
