from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from core.models import AttributeValue, AttributeName


class DetailTests(APITestCase):

    def setUp(self) -> None:
        AttributeValue.objects.create(hodnota='first')
        AttributeValue.objects.create(hodnota='second')
        AttributeName.objects.create(nazev='name')

    def test_get_list(self):
        response = self.client.get('/detail/AttributeValue/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_get_retrieve(self):
        response = self.client.get('/detail/AttributeName/1/', format='json')
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['nazev'], 'name')