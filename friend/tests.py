from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from .views import index
from .models import Friend

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Create your tests here.
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

# class AddFriendFunctionalTest(TestCase):

# 	def setUp(self):
# 		chrome_options = Options()
# 		chrome_options.add_argument('--dns-prefetch-disable')
# 		chrome_options.add_argument('--no-sandbox')
# 		chrome_options.add_argument('--headless')
# 		chrome_options.add_argument('disable-gpu')
# 		super(AddFriendFunctionalTest, self).setUp()

# 	def tearDown(self):
# 		self.selenium.quit()
# 		super(AddFriendFunctionalTest, self).tearDown()

# 	def test_add_friend(self):
# 		selenium = self.selenium
# 		# Opening the link we want to test
# 		selenium.get('http://127.0.0.1:8000/add-friend/')
# 		# find the form element
# 		name = selenium.find_element_by_id('id_name')
# 		url = selenium.find_element_by_id('id_url')

# 		submit = selenium.find_element_by_id('submit')

# 		# Fill the form with data
# 		name.send_keys('Dummy-chan')
# 		url.send_keys('http://dummy.com')

# 		# submitting the form
# 		submit.send_keys(Keys.RETURN)
