from stochasticapi.configurations.exceptions.blog_core_exception import BlogError
from stochasticapi.configurations.utilities.api_response import BlogResponse
from rest_framework import viewsets
from stochasticapi.configurations.utilities.global_constants import (
    SUCCESSFULLY_CREATED,
    SUCCESSFULLY_UPDATED,
)

from stochasticapi.configurations.utilities.http_codes import BAD_REQUEST, CREATED, UPDATED
from .models import ContactUs
from .serializers import ContactUsSerializer



class ContactUsView(viewsets.ModelViewSet):

    queryset = ContactUs.objects.all()
    serializer_class = ContactUs

    def list(self, request):
        result = ContactUs.objects.all()
        serializer = ContactUsSerializer(result, context={"request": request}, many=True)
        return BlogResponse(data=serializer.data).build_response()

    def retrieve(self, request, pk):
        try:
            result = ContactUs.objects.get(id=pk)
        except ContactUs.DoesNotExist:
            raise BlogError(
                http_status=BAD_REQUEST,
                message="No Matching Record found"
            )

        serializer = ContactUsSerializer(result, context={"request": request})
        return BlogResponse(data=serializer.data).build_response()


    def create(self, request):
        serializer = ContactUsSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return BlogResponse(
            data=serializer.data,
            http_status=CREATED,
            message=SUCCESSFULLY_CREATED,
        ).build_response()

    def update(self, request, pk):
        try:
            instance = ContactUs.objects.get(id=pk)
        except ContactUs.DoesNotExist:
            raise BlogError(
                http_status=BAD_REQUEST,
                message="No Matching Record found"
            )
        serializer = ContactUsSerializer(
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
