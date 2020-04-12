from typing import Any

import requests


class GhibliClient:
    BASE_URL = 'https://ghibliapi.herokuapp.com'

    def movies(self, limit: int = 250) -> Any:
        movies_response = requests.get(self.BASE_URL + f'/films?limit={limit}')
        return movies_response.json()

    def people(self, limit: int = 250) -> Any:
        people_response = requests.get(self.BASE_URL + f'/people?limit={limit}')
        return people_response.json()
