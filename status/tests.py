from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, add_status
from .models import Update_Form
from .forms import Update_Bar

class StatusPageUnitTest(TestCase):
    def test_status_page_url_is_exist(self):
        response = Client().get('/status/')
        self.assertEqual(response.status_code, 200)

    def test_statuspage_using_index_func(self):
        found = resolve('/status/')
        self.assertEqual(found.func, index)

    def test_model_can_create_new_status(self):
        # Create a new status
        new_status = Update_Form.objects.create(description = 'Hi yall')

        # Retrieving all status have made
        counting_all_status = Update_Form.objects.all().count()
        self.assertEqual(counting_all_status, 1)

    def test_form_validation_for_blank_items(self):
        form = Update_Bar(data={'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['description'],
            ["This field is required."]
        )

    def test_statuspage_post_success_and_render_the_result(self):
        test = 'Anonymous'
        response_post = Client().post('/status/add_status', {'description': test})
        self.assertEqual(response_post.status_code, 302)

        response = Client().get('/status/')
        html_response = response.content.decode('utf8')
        self.assertNotIn(test, html_response)

    def test_statuspage_post_error_and_render_the_result(self):
        test = 'Anonymous'
        response_post = Client().post('/status/add_status', {'description': ''})
        self.assertEqual(response_post.status_code, 302)

        response= Client().get('/status/')
        html_response = response.content.decode('utf8')
        self.assertNotIn(test, html_response)
