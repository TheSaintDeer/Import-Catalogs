from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.request import Request
from rest_framework.generics import ListAPIView

from . import services
from core import models, serializers


class Importing(APIView):
    '''This endpoint will receive data and parse data'''
    
    def post(self, request, format=None):
        if request.data:
            data, status_code = services.mode_handler(request.data)
            return Response(data=data, status=status_code)

        return Response(data="Request data is empty.", status=status.HTTP_400_BAD_REQUEST)
    

class DetailList(APIView):

    def get(self, request, model_name):
        serializer = services.get_serializer(model_name)
        if not serializer:
            return Response(data=f"Unknown model type: {model_name}", status=status.HTTP_400_BAD_REQUEST)
        
        queryset = get_list_or_404(serializer.Meta.model)
        data = serializer(queryset, many=True)
        
        return Response(data=data.data, status=status.HTTP_200_OK)


class DetailRetrieve(APIView):

    def get(self, request, model_name, pk):
        serializer = services.get_serializer(model_name)
        if not serializer:
            return Response(data=f"Unknown model type: {model_name}", status=status.HTTP_400_BAD_REQUEST)
        
        queryset = get_object_or_404(serializer.Meta.model, pk=pk)
        data = serializer(queryset)
        
        return Response(data=data.data, status=status.HTTP_200_OK)