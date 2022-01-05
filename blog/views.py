from rest_framework.decorators import api_view
from stochasticapi.configurations.utilities.api_response import BlogResponse
from rest_framework import viewsets
from stochasticapi.configurations.utilities.global_constants import (
    SUCCESSFULLY_CREATED,
    SUCCESSFULLY_UPDATED,
)

from stochasticapi.configurations.utilities.http_codes import CREATED, UPDATED
from .models import Blogs
from .serializers import BlogSerializer


@api_view(["GET"])
def welcome_api(request):
    return BlogResponse(message="Welcome to Blogs API v0.1").build_response()


class BlogView(viewsets.ModelViewSet):

    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer

    def list(self, request):
        result = Blogs.objects.all()
        serializer = BlogSerializer(result)
        return BlogResponse(data=serializer.data).build_response()

    def create(self, request):
        serializer = BlogSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return BlogResponse(
            data=serializer.data,
            http_status=CREATED,
            message=SUCCESSFULLY_CREATED,
        ).build_response()

    def put(self, request, pk):
        instance = Blogs.objects.get(id=pk)
        serializer = BlogSerializer(
            instance=instance,
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return BlogResponse(
            data=serializer.data,
            http_status=UPDATED,
            message=SUCCESSFULLY_UPDATED,
        ).build_response()
