
from django.test import TestCase
from rest_framework.test import APIClient

from .models import MyUser

# Create your tests here.
class APITest(TestCase):
    

    def test_user_creation(self):
        response = self.client.post('http://127.0.0.1:8000/accounts/users/', {'first_name': 'TestUsername', 'email': 'test@test.com', 'password': '12345678', 'password2': '12345678', 'phone_number':'1245678'}, format='json')
        self.assertEqual(response.status_code, 201)
    
    def test_user_login(self):
        self.user = MyUser.objects.create_user(email='test@gmail.com', password='test1test', first_name='test')

        resp = self.client.post('http://127.0.0.1:8000/accounts/login/', {'email': 'test@gmail.com', 'password': 'test1test'})
        self.assertEqual(resp.status_code, 200)
    
    def test_user_get_by_id(self):
        self.user = MyUser.objects.create_user(email='test@gmail.com', password='test1test', first_name='test')

        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.get('http://127.0.0.1:8000/accounts/user/1/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_user_update(self):
        self.user = MyUser.objects.create_user(email='test@gmail.com', password='test1test', first_name='test')

        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.put('http://127.0.0.1:8000/accounts/users/1/', email='testtest@gmail.com', first_name='testname', phone_number='123123123')