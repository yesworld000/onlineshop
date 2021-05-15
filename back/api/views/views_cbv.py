from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser,JSONParser,MultiPartParser
from api.models import Photo
from api.serializers import PhotoSerializer


class PhotoListAPIView(generics.ListCreateAPIView):
    parser_classes = [FormParser, MultiPartParser, JSONParser]
    serializer_class = PhotoSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Photo.objects.all()
        return queryset

class PhotoDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Photo.objects.get(id=pk)
        except Photo.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, pk):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

    def put(self, request, pk):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(instance=photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, pk):
        photo = self.get_object(pk)
        photo.delete()

        return Response({'deleted': True})

