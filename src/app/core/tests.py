from django.test import TestCase

from . import services, models, serializers


class ServiceTests(TestCase):

    def setUp(self) -> None:
        models.AttributeValue.objects.create(hodnota='yes')
        models.AttributeValue.objects.create(hodnota='no')

    def test_get_serializer(self):
        "Test for function get_serializer"
        correct_serializer = services.get_serializer('AttributeName')
        incorrect_serializer = services.get_serializer('NotAttributeName')
        self.assertEqual(correct_serializer, serializers.AttributeNameSerializer)
        self.assertEqual(incorrect_serializer, None)

    def test_update_or_create_object(self):
        "Test for function update_or_create_object"
        serializer = serializers.AttributeValueSerializer
        object_exist = models.AttributeValue.objects.get(id=1)
        object_not_exist = None

        value = {'hodnota': 'value'}

        self.assertEqual((services.update_or_create_object(serializer, object_exist, value)),
                         ({'id': 1, 'hodnota': 'value'}, 200))
        self.assertEqual((services.update_or_create_object(serializer, object_not_exist, value)),
                         ({'id': 3, 'hodnota': 'value'}, 201))
        
    def test_get_object_or_none(self):
        "Test for function get_object_or_none"
        object = models.AttributeValue.objects.get(id=1)
        object_exist = services.get_object_or_none(models.AttributeValue, 1)
        object_not_exist = services.get_object_or_none(models.AttributeValue, 10)

        self.assertEqual(object_exist, object)
        self.assertEqual(object_not_exist, None)

    def test_get_key_and_value_from_dict(self):
        "Test for function get_key_and_value_from_dict"
        test_dict = {
            'key': {
                'inner_key1': 'value1',
                'inner_key2': 'value2'
            }
        }

        key, value = services.get_key_and_value_from_dict(test_dict)
        self.assertEqual(key, 'key')
        self.assertEqual(value, {'inner_key1': 'value1', 'inner_key2': 'value2'})

    def test_sigle_object_mode(self):
        "Test for function sigle_object_mode"
        data = {
            "AttributeValue": {
                "id": 1,
                "hodnota": "modra"
            }
        }
        new_data = {
            "AttributeValue": {
                "id": 3,
                "hodnota": "modra"
            }
        }

        self.assertEqual((services.sigle_object_mode(data)), 
                         ({"id": 1, "hodnota": "modra"}, 200))
        self.assertEqual((services.sigle_object_mode(new_data)), 
                         ({"id": 3, "hodnota": "modra"}, 201))
        
    def test_multi_object_mode(self):
        "Test for function multi_object_mode"
        data = [
            {"AttributeValue": {
                "id": 1,
                "hodnota": "modra"
            }},
            {"AttributeValue": {
                "id": 3,
                "hodnota": "modra"
            }},
        ]
        result = [
            {
                "status_code": 200,
                "data": {
                    "id": 1,
                    "hodnota": "modra"
                }
            },
            {
                "status_code": 201,
                "data": {
                    "id": 3,
                    "hodnota": "modra"
                }
            }
        ]

        self.assertEqual((services.multi_object_mode(data)), (result, 200))