from django.test import TestCase, Client
from django.urls import resolve
from .views import index
from status.models import Update_Form
from friend.models import Friend
from user_profile.models import Person, PhotoURL


class DashboardUnitTest(TestCase):

    def make_person(self):
        person = Person.objects.create(
            name="Johann Sebastian Bach",
            birthdate="1685-03-31", gender="Male",
            description="Master of contrapuntal composition \
            and professional harpsichord player", email="jsbach@gmail.com")
        model_pic = PhotoURL.objects.create(
            model_pic="http://www.bachsociety.org/wp-content/uploads/\
            2017/01/Johann-sunglasses.jpg")
        return (person, model_pic)

    def test_url_dashboard_exist(self):
        self.make_person()

        response = Client().get('/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_using_index_func(self):
        self.make_person()

        found = resolve('/dashboard/')
        self.assertEqual(found.func, index)

    def test_status_count_is_correct(self):
        self.make_person()

        statusCount = Update_Form.objects.all().count()
        statusMsg = "Post" if statusCount <= 1 else "Posts"

        response = Client().get('/dashboard/')
        html_response = response.content.decode('utf8')
        self.assertIn(str(statusCount) + " " + statusMsg, html_response)

    def test_friend_count_is_correct(self):
        self.make_person()

        friendCount = Friend.objects.all().count()
        friendMsg = "Person" if friendCount <= 1 else "People"

        response = Client().get('/dashboard/')
        html_response = response.content.decode('utf8')
        self.assertIn(str(friendCount) + " " + friendMsg, html_response)

    def test_name_and_photo_exist(self):

        data = self.make_person()

        personName = data[0].name
        photo = data[1].model_pic

        response = Client().get('/dashboard/')
        html_response = response.content.decode('utf8')
        self.assertIn(personName, html_response)
        self.assertIn(photo, html_response)

    def test_last_status_exists(self):
        self.make_person()
        statusCount = Update_Form.objects.all().count()
        if (statusCount <= 0):
            Update_Form.objects.create(description = "This is last")
            statusCount += 1

        lastStatus = Update_Form.objects.all()[statusCount - 1]
        lastDesc = lastStatus.description

        response = Client().get('/dashboard/')
        html_response = response.content.decode('utf8')

        self.assertIn(lastDesc, html_response)

    def test_last_status_not_exists(self):
        self.make_person()
        statusCount = Update_Form.objects.all().count()

        response = Client().get('/dashboard/')
        html_response = response.content.decode('utf8')

        self.assertIn("No Status", html_response)
