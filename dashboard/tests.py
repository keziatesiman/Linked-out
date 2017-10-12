from django.test import TestCase, Client
from django.urls import resolve
from .views import index
from status.models import Update_Form
from friend.models import Friend
from user_profile.models import Person, PhotoURL


class DashboardUnitTest(TestCase):

    def test_url_dashboard_exist(self):
        response = Client().get('/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_using_index_func(self):
        found = resolve('/dashboard/')
        self.assertEqual(found.func, index)

    def test_status_count_is_correct(self):
        statusCount = Update_Form.objects.all().count()
        statusMsg = "Post" if statusCount <= 1 else "Posts"

        response = Client().get('/dashboard/')
        html_response = response.content.decode('utf8')
        self.assertIn(str(statusCount) + " " + statusMsg, html_response)

    def test_friend_count_is_correct(self):
        friendCount = Friend.objects.all().count()
        friendMsg = "Person" if friendCount <= 1 else "People"

        response = Client().get('/dashboard/')
        html_response = response.content.decode('utf8')
        self.assertIn(str(friendCount) + " " + friendMsg, html_response)

    def test_name_and_photo_exist(self):

        person = Person.objects.create(
            name="Johann Sebastian Bach",
            birthdate="1685-03-31", gender="Male",
            description="Master of contrapuntal composition \
            and professional harpsichord player", email="jsbach@gmail.com")
        model_pic = PhotoURL.objects.create(
            model_pic="http://www.bachsociety.org/wp-content/uploads/\
            2017/01/Johann-sunglasses.jpg")

        personName = person.name
        photo = model_pic.model_pic

        response = Client().get('/dashboard/')
        html_response = response.content.decode('utf8')
        self.assertIn(personName, html_response)
        self.assertIn(photo, html_response)
