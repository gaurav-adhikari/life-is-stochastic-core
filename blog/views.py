from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

from stochasticapi.utilities.api_response import BlogResponse


@api_view(["GET"])
def welcome_api(request):
    return BlogResponse(message="Welcome to Blogs API v0.1").build_response()
