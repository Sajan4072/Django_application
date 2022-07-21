from django.test import TestCase

# Create your tests here.

import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class PostTestCase(APITestCase):
    def test_post_request(self):
        url = reverse('calculate_fare')
        data = {
            "time": "12:00",
            "distance": "2"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'fare': '100.0'})