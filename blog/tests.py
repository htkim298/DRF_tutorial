from django.test import TestCase
from rest_framework.test import APIClient

class APITest(TestCase):
  def test_change_password(self):
    client = APIClient()
    response = client.patch('/login', {'new_password': 'password'})
    self.assertEqual(response.status_code, 200)
