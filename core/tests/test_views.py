import pprint
from ddt import ddt, data, unpack, file_data
from knox.models import AuthToken


from rest_framework import status
from django.urls import reverse

from .base import BaseTestCase

@ddt
class TestViews(BaseTestCase):
    def setUp(self):
        super(TestViews, self).setUp()

    @file_data('data/data_get_movies_as_per_city.json')
    def test_get_movies_as_per_city(self, sr_no, status, case, input_data, output_data):
        if status == 'active':
            print (f'[ {case} ]')

            response = self.client.post(reverse(input_data.get('name')), data=input_data.get('data'), format='json')
            result = response.json()
            
            self.assertEqual(result, output_data)
        else:
            pass

    @file_data('data/data_get_cinemas_as_per_movie.json')
    def test_get_cinemas_as_per_movie(self, sr_no, status, case, input_data, output_data):
        if status == 'active':
            print (f'[ {case} ]')

            response = self.client.post(reverse(input_data.get('name')), data=input_data.get('data'), format='json')
            result = response.json()
            
            self.assertEqual(result, output_data)
        else:
            pass

    @file_data('data/data_get_seats_as_per_showtime.json')
    def test_get_seats_as_per_showtime(self, sr_no, status, case, input_data, output_data):
        if status == 'active':
            print (f'[ {case} ]')

            response = self.client.post(reverse(input_data.get('name')), data=input_data.get('data'), format='json')
            result = response.json()
            
            self.assertEqual(result, output_data)
        else:
            pass

    @file_data('data/data_reserve_tickets.json')
    def test_reserve_tickets(self, sr_no, status, case, input_data, output_data):
        if status == 'active':
            print (f'[ {case} ]')
            if sr_no != 3:
                response_register = self.client.post(reverse('user-register'), data={ "username": "test", "email": "test@example.com", "password": "test" }, format='json')
                response_login = self.client.post(reverse('user-login'), data={ "username": "test", "password": "test" }, format='json')
                token = response_login.json().get('token')
                self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(token))

            response = self.client.post(reverse(input_data.get('name')), data=input_data.get('data'), format='json')
            result = response.json()

            if result.get('data') and sr_no != 4:
                del result['data'][0]['created_at']
                del result['data'][0]['updated_at']
            
            self.assertEqual(result, output_data)
        else:
            pass

    def tearDown(self):
        pass