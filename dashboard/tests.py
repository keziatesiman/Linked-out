from django.test import TestCase, Client
from django.urls import resolve
from .views import index


class DashboardUnitTest(TestCase):

    def test_url_dashboard_exist(self):
        response = Client().get('/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_using_index_func(self):
        found = resolve('/dashboard/')
        self.assertEqual(found.func, index)
