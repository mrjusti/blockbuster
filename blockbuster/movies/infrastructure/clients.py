from typing import Any

import requests


class GhibliClient:
    BASE_URL = 'https://ghibliapi.herokuapp.com'

    def movies(self) -> Any:
        movies_response = requests.get(self.BASE_URL + '/films?limit=250')
        return movies_response.json()

    def people(self) -> Any:
        people_response = requests.get(self.BASE_URL + '/people?limit=250')
        return people_response.json()
