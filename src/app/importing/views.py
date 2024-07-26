from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import services


class Importing(APIView):
    '''This endpoint will receive data and parse data'''
    
    def post(self, request, format=None):
        if request.data:
            data, status_code = services.mode_handler(request.data)
            return Response(data=data, status=status_code)

        return Response(data="Request data is empty.", status=status.HTTP_400_BAD_REQUEST)