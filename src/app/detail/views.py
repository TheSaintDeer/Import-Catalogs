import logging
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404

from core import services


logger = logging.getLogger('main')


class DetailList(APIView):

    def get(self, request, model_name):
        '''Endpoint for getting a list of all elements from a specific table'''

        logger.info(f'Open list of {model_name}')
        serializer = services.get_serializer(model_name)
        if not serializer:
            return Response(data=f"Unknown model type: {model_name}", status=status.HTTP_400_BAD_REQUEST)
        
        queryset = get_list_or_404(serializer.Meta.model)
        data = serializer(queryset, many=True)
        
        return Response(data=data.data, status=status.HTTP_200_OK)


class DetailRetrieve(APIView):

    def get(self, request, model_name, pk):
        '''Endpoint for taking an element from a specific table'''

        logger.info(f'Open detail of object from {model_name} model')
        serializer = services.get_serializer(model_name)
        if not serializer:
            return Response(data=f"Unknown model type: {model_name}", status=status.HTTP_400_BAD_REQUEST)
        
        queryset = get_object_or_404(serializer.Meta.model, pk=pk)
        data = serializer(queryset)
        
        return Response(data=data.data, status=status.HTTP_200_OK)