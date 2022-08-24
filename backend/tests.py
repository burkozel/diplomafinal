from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from backend.models import ConfirmEmailToken, Shop
import json


class TestAPI(APITestCase):

  def test_create_activate_user(self, user_type='buyer', test_email="xxxxxxxxxx"):
        test_password = "xxxxxxxxxx"
        url = '/api/v1/user/register'
        data = {'first_name': 'test_first',
                'last_name': 'test_last',
                'email': test_email,
                'password': test_password,
                'type': user_type}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        token = str(ConfirmEmailToken.objects.get(user__email=test_email))
        url = '/api/v1/user/register/confirm'
        data = {'token': token,
                'email': test_email}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return test_email, test_password
      
  def test_login(self, user_type='buyer'):
        if user_type == 'shop':
            test_email = "xxxxxxxxxx"
        elif user_type == 'buyer':
            test_email = "xxxxxxxxxxx"
        test_email, test_password = self.test_create_activate_user(user_type=user_type, test_email=test_email)
        url = '/api/v1/user/login'
        data = {'password': test_password,
                'email': test_email}
        response = self.client.post(url, data, format='json')
        response_dict_content = json.loads(response.content.decode("UTF-8"))
        self.assertTrue('Token' in response_dict_content.keys())
        return response_dict_content['Token']
      
  def test_logout(self):
        test_token = self.test_login(user_type='buyer')
        url = '/api/v1/user/login'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + test_token)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)      
