from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

@api_view(['GET'])
def welcome_api(request):
    return Response("Welcome to Blogs API")
