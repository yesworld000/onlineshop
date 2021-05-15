from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from auth_.views import CreateUserViewSet, ProfileViewSet

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', CreateUserViewSet.as_view({'post': 'post_user'})),
    path('profile/', ProfileViewSet.as_view({'get': 'list'})),
    path('profile/<int:pk>/', ProfileViewSet.as_view({'get': 'profile_detail',
                                                      'put': 'update',
                                                      'delete': 'destroy'})),
    # path('update/', UserRetrieveUpdateAPIView.as_view()),
    # path('get/', UserRetrieveUpdateAPIView.as_view())
]
