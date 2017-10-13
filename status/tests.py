# Create your tests here.
from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, add_status
from .models import Status
from .forms import Status_Form

    # Create your tests here.
class UpdateStatusUnitTest(TestCase):

    def test_status_url_is_exist(self):
        response = Client().get('/status/')
        self.assertEqual(response.status_code, 200)

    def test_updatestatus_using_index_func(self):
        found = resolve('/status/')
        self.assertEqual(found.func, index)

    def test_model_can_create_new_status(self):
        # Creating a new activity
        new_activity = Status.objects.create(status='mengerjakan lab_5 ppw')

        # Retrieving all available activity
        counting_all_available_status = Status.objects.all().count()
        self.assertEqual(counting_all_available_status, 1)

    def test_form_status_input_has_placeholder_and_css_classes(self):
        form = Status_Form()
        self.assertIn('class="status-form-textarea', form.as_p())
        self.assertIn('id="id_status', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = Status_Form(data={'status': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['status'],
            ["This field is required."]
        )
    def test_updatestatus_post_success_and_render_the_result(self):
        test = 'Anonymous'
        response_post = Client().post('/status/add_status', {'status': test})
        self.assertEqual(response_post.status_code, 302)

        response= Client().get('/status/')
        html_response = response.content.decode('utf8')
        self.assertIn(test, html_response)

    def test_updatestatus_post_error_and_render_the_result(self):
        test = 'Anonymous'
        response_post = Client().post('/status/add_status', {'status': ''})
        self.assertEqual(response_post.status_code, 302)

        response= Client().get('/status/')
        html_response = response.content.decode('utf8')
        self.assertNotIn(test, html_response)

    def test_updatestatus_delete(self):
        stat = Status.objects.create(
            status='description'
        )
        response_post = Client().get('/status/delete/{}/'.format(stat.id))
        self.assertEqual(response_post.status_code, 302)
        self.assertEqual(Status.objects.count(), 0)


