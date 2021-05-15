from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from api.views.views_fbv import category_list, category_detail, photo_by_category, comment_by_photo
# from api.views.views_cbv import VacancyListAPIView, VacancyDetailAPIView
from api.views.views_cbv import PhotoListAPIView, PhotoDetailAPIView
from api.views.views_generic import UserPhotosAPIView
from api.views.views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView


urlpatterns = [
    # path('login/', obtain_jwt_token),
    path('photos/<int:pk>/comments/', comment_by_photo),

    path('categories/', category_list),
    path('categories/<int:category_id>/', category_detail),
    path('categories/<int:pk>/photos/', photo_by_category),


    path('photos/', PhotoListAPIView.as_view()),
    path('photos/<int:pk>/', PhotoDetailAPIView.as_view()),

    path('get/<int:pk>/photos/', UserPhotosAPIView.as_view()),
    # path('create/', CreateUserAPIView.as_view()),
    # path('obtain_token/', authenticate_user),
    # path('update/', UserRetrieveUpdateAPIView.as_view()),
    # path('get/', UserRetrieveUpdateAPIView.as_view())
]

