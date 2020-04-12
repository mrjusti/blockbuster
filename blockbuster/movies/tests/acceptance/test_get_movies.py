import os

from django.test import TestCase
from django.urls import reverse

os.environ['DJANGO_SETTINGS_MODULE'] = 'blockbuster.settings.test'


class TestGetMovies(TestCase):

    def test_get_movies(self):
        resp = self.client.get(reverse('movies'))
        self.assertEqual(resp.status_code, 200)
