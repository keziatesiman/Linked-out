from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from .views import index, url_is_valid
from .models import Friend

class AddFriendUnitTest(TestCase):
	def test_add_friend_url_is_exist(self):
		response = Client().get('/friend/')
		self.assertEqual(response.status_code, 200)

	def test_add_friend_using_index_func(self):
		found = resolve('/friend/')
		self.assertEqual(found.func, index)

	def test_model_can_create_new_friend(self):
		new_friend = Friend.objects.create(name='test', url='http://test.com')
		counting_all_available_friend = Friend.objects.all().count()
		self.assertEqual(counting_all_available_friend, 1)

	def test_add_friend_post_succes_and_render_the_result(self):
		test_name = 'Test'
		test_url = 'http://test.com'
		response_post = Client().post('/friend/add_friend', {'name':test_name, 'url':test_url})
		self.assertEqual(response_post.status_code, 302)

		response= Client().get('/friend/')
		html_response = response.content.decode('utf8')
		self.assertIn(test_name, html_response)
		self.assertIn(test_url, html_response)

	def test_add_friend_post_error_and_render_the_result(self):
		test_name = 'Test'
		test_url = 'http://test.com'
		response_post = Client().post('/friend/add_friend', {'name':'', 'url':''})
		self.assertEqual(response_post.status_code, 302)

		response= Client().get('/friend/')
		html_response = response.content.decode('utf8')
		self.assertNotIn(test_name, html_response)
		self.assertNotIn(test_url, html_response)

	def test_url_validator(self):
		not_valid_url = 'http://jkhrginkjer.com'
		valid_url = 'http://google.com'
		self.assertEqual(url_is_valid(not_valid_url), False)
		self.assertEqual(url_is_valid(valid_url), True)
