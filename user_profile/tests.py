from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index
from django.http import HttpRequest
from .models import Person, Expertise 

# Create your tests here.
class user_profileUnitTest(TestCase):

    def test_user_profile_url_is_exist(self):
        response = Client().get('/user_profile/')
        self.assertEqual(response.status_code,200)

    def test_user_profile_using_index_func(self):
        found = resolve('/user_profile/')
        self.assertEqual(found.func, index)


    def test_user_profile_page_is_completed(self):
        request = HttpRequest()

        person = Person.objects.create(name="Johann Sebastian Bach", birthdate="1685-03-31", gender="Male", description="Master of contrapuntal composition and professional harpsichord player", email="jsbach@gmail.com")
        expertise = Expertise.objects.create(expertise ="Contrapuntal composition, Church leading musician, Glorifying God")

        
        response = Client().get('/user_profile/')
        html_response = response.content.decode('utf8')

        
        self.assertIn(Person.objects.all().count(),1)

        

