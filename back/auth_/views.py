import logging

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from auth_.models import MainUser, Profile
from auth_.serializers import UserSerializer, ProfileSerializer, ProfileUpdateSerializer, ProfileDetailSerializer


# logger = logging.getLogger(__name__)


class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = MainUser.objects.all()
    permission_classes = (AllowAny, )

    def get_serializer_class(self):
        if self.action == 'create':
            return UserSerializer

    @action(methods=['POST'], detail=False, permission_classes = AllowAny )
    def post_user(self, request):
        user = request.data
        queryset = MainUser.objects.create_user(email=user['email'], password=user['password'], first_name=user['first_name'], last_name=user['last_name'])
        queryset.save()
        # logger.debug(f'User created ID: {queryset.id}' f' with email {queryset.email}')
        # logger.info(f'User created ID: {queryset.id}' f' with email {queryset.email}')
        # logger.warning(f'User created ID: {queryset.id}' f' with email {queryset.email}')
        # logger.error(f'User created ID: {queryset.id}' f' with email {queryset.email}')
        # logger.critical(f'User created ID: {queryset.id}' f' with email {queryset.email}')
        return Response(user, status=status.HTTP_201_CREATED)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = (AllowAny, )
    parser_classes = [FormParser, MultiPartParser, JSONParser]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProfileSerializer
        elif self.action == 'update':
            return ProfileUpdateSerializer
        elif self.action == 'destroy':
            return ProfileSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def profile_detail(self, request, pk):
        queryset = Profile.objects.filter(id=pk)
        serializer = ProfileDetailSerializer(queryset, many=True)
        return Response(serializer.data)
