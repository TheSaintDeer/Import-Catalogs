from rest_framework import status

from core import models, serializers


# depending on the key return the serializer type
group_to_serializer = {
    'AttributeName': serializers.AttributeNameSerializer,
    'AttributeValue': serializers.AttributeValueSerializer,
    'Attribute': serializers.AttributeSerializer,
    'Product': serializers.ProductSerializer,
    'ProductAttribute': serializers.ProductAttributeSerializer,
    'Image': serializers.ImageSerializer,
    'ProductImage': serializers.ProductImageSerializer,
    'Catalog': serializers.CatalogSerializer,
}

def get_key_and_value_from_dict(data: dict): 
    '''Take the key from the given dictionary'''
    key = list(data.keys())[0]
    return key, data[key]

def get_object_or_none(model: models.models.Model, id: int):
    '''Find an object in the tablipo by its ID'''
    try:
        return model.objects.get(id=id)
    except:
        return None
    
def update_or_create_object(serializer: serializers.serializers.ModelSerializer,
                            object: models.models.Model|None,
                            value: dict):
    '''Updates an object's data if it exists or creates a new entry in a table'''
    instance = None
    status_code = None
    if object:
        # update object
        instance = serializer(object, data=value, partial=True)
        status_code = status.HTTP_200_OK
    else:
        # create new object
        instance = serializer(data=value)
        status_code = status.HTTP_201_CREATED

    if instance.is_valid():
        instance.save()
        return instance.data, status_code
    return instance.errors, status.HTTP_400_BAD_REQUEST


def mode_handler(data: dict|list):
    '''Select the mode in which to process the post request'''
    if type(data) == dict:
        return sigle_object_mode(data)
    elif type(data) == list:
        return multi_object_mode(data)

def sigle_object_mode(data: dict):
    '''Handler if only one object is submitted in a post request'''
    
    key, value = get_key_and_value_from_dict(data)
    serializer = group_to_serializer[key]

    if not 'id' in value:
        return f"Object {str(data)} has not id", status.HTTP_400_BAD_REQUEST
    object = get_object_or_none(serializer.Meta.model, id=value['id'])
    
    return update_or_create_object(serializer, object, value)

def multi_object_mode(data: list):
    '''Handler if multiple objects are submitted in a post request'''
    response_data = list()
    for item in data:
        response, status_code = sigle_object_mode(item)
        response_data.append({
            "status_code": status_code,
            "data": response
        })

    return response_data, status.HTTP_200_OK