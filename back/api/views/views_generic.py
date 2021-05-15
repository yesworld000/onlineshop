from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Category, Photo
from api.serializers import PhotoSerializer, CategoryWithPhotosSerializer
from auth_.models import MainUser


class PhotoListAPIView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', )


class PhotoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class UserPhotosAPIView(generics.ListAPIView):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        user = get_object_or_404(MainUser, id=self.kwargs.get('pk'))
        queryset = user.photos.all()
        return queryset
