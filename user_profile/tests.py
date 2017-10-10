from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index
from django.http import HttpRequest
from .models import Person, Expertise, PhotoURL 

# Create your tests here.
class user_profileUnitTest(TestCase):

    def test_user_profile_url_is_exist(self):
        person = Person.objects.create(name="Johann Sebastian Bach", birthdate="1685-03-31", gender="Male", description="Master of contrapuntal composition and professional harpsichord player", email="jsbach@gmail.com")
        expertise = Expertise.objects.create(expertise ="Contrapuntal composition, Church leading musician, Glorifying God")
        model_pic = expertise = PhotoURL.objects.create(model_pic ="http://www.bachsociety.org/wp-content/uploads/2017/01/Johann-sunglasses.jpg")

        response = Client().get('/user_profile/')
        self.assertEqual(response.status_code,200)

    def test_user_profile_using_index_func(self):
        person = Person.objects.create(name="Johann Sebastian Bach", birthdate="1685-03-31", gender="Male", description="Master of contrapuntal composition and professional harpsichord player", email="jsbach@gmail.com")
        expertise = Expertise.objects.create(expertise ="Contrapuntal composition, Church leading musician, Glorifying God")
        model_pic = expertise = PhotoURL.objects.create(model_pic ="http://www.bachsociety.org/wp-content/uploads/2017/01/Johann-sunglasses.jpg")
        found = resolve('/user_profile/')
        self.assertEqual(found.func, index)


    def test_user_profile_page_is_completed(self):
        request = HttpRequest()

        person = Person.objects.create(name="Johann Sebastian Bach", birthdate="1685-03-31", gender="Male", description="Master of contrapuntal composition and professional harpsichord player", email="jsbach@gmail.com")
        expertise = Expertise.objects.create(expertise ="Contrapuntal composition, Church leading musician, Glorifying God")
        model_pic = expertise = PhotoURL.objects.create(model_pic ="http://www.bachsociety.org/wp-content/uploads/2017/01/Johann-sunglasses.jpg")
        
        response = Client().get('/user_profile/')
        html_response = response.content.decode('utf8')

        
        self.assertEqual(Person.objects.all().count(),1)
        self.assertIn(Person.objects.all()[0].name, html_response)
        self.assertIn("March 31, 1685", html_response)
        self.assertIn(Person.objects.all()[0].gender, html_response)
        self.assertIn(Expertise.objects.all()[0].expertise, html_response)
        self.assertIn(Person.objects.all()[0].description, html_response)
        self.assertIn(PhotoURL.objects.all()[0].model_pic, html_response)

        

