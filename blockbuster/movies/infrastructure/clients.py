from http import HTTPStatus
from typing import Any

import requests


class GhibliClient:
    """Connect with Ghibli API"""

    BASE_URL = 'https://ghibliapi.herokuapp.com'

    def movies(self, limit: int = 250) -> Any:
        """Get movies from Ghibli"""

        movies_response = requests.get(self.BASE_URL + f'/films?limit={limit}')

        try:
            movies_response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            if movies_response.status_code == HTTPStatus.BAD_REQUEST:
                raise BadRequestError(err)
            elif movies_response.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError(err)

            raise InternalServerError(err)

        return movies_response.json()

    def people(self, limit: int = 250) -> Any:
        """Get people from Ghibli"""

        people_response = requests.get(self.BASE_URL + f'/people?limit={limit}')

        try:
            people_response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            if people_response.status_code == HTTPStatus.BAD_REQUEST:
                raise BadRequestError(err)
            elif people_response.status_code == HTTPStatus.NOT_FOUND:
                raise NotFoundError(err)

            raise InternalServerError(err)

        return people_response.json()


class BadRequestError(Exception):
    """Raise when the request is bad"""
    pass


class NotFoundError(Exception):
    """Raise when the request is not found"""
    pass


class InternalServerError(Exception):
    """Raise when the request error is unknow"""
    pass
