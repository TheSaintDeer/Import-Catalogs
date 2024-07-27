from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from core.models import AttributeValue, AttributeName


class ImportingTests(APITestCase):

    def setUp(self) -> None:
        AttributeValue.objects.create(hodnota='first')
        AttributeValue.objects.create(hodnota='second')
        AttributeName.objects.create(nazev='name')

    def test_importing_in_single_mode_update(self):
        data = {
            "AttributeValue": {
                "id": 1,
                "hodnota": "value"
            }
        }

        url = reverse('importing:importing')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AttributeValue.objects.count(), 2)
        self.assertEqual(AttributeValue.objects.get(id=1).hodnota, 'value')

    def test_importing_in_single_mode_create(self):
        data = {
            "AttributeValue": {
                "id": 3,
                "hodnota": "value"
            }
        }

        url = reverse('importing:importing')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AttributeValue.objects.count(), 3)
        self.assertEqual(AttributeValue.objects.get(id=3).hodnota, 'value')


    def test_importing_in_multi_mode(self):
        data = [{
            "AttributeName": {
                "id": 2,
                "nazev": "Barva"
            }
        },
        {
            "AttributeValue": {
                "id": 3,
                "hodnota": "modrá"
            }
        }]

        url = reverse('importing:importing')
        response = self.client.post(url, data, format='json')

        print(response.json(), response.status_code)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AttributeValue.objects.count(), 3)
        self.assertEqual(AttributeName.objects.count(), 2)