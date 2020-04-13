"""Module that contain all the client that the app need to connect."""

from typing import Any

import requests


class GhibliClient:
    """Connect with Ghibli API."""

    BASE_URL = 'https://ghibliapi.herokuapp.com'

    def movies(self, limit: int = 250) -> Any:
        """Get movies from Ghibli."""
        try:
            movies_response = requests.get(self.BASE_URL + f'/films?limit={limit}')
            movies_response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise FailedDependencyError(err)

        return movies_response.json()

    def people(self, limit: int = 250) -> Any:
        """Get people from Ghibli."""
        try:
            people_response = requests.get(self.BASE_URL + f'/people?limit={limit}')
            people_response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise FailedDependencyError(err)

        return people_response.json()


class FailedDependencyError(Exception):
    """Raise when th dependency is failing."""

    pass
