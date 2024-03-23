# from django.contrib import admin
from django.urls import path , include
from authAPI.views import UserProfileView , UserRegistrationView
# from rest_framework import routers, serializers, viewsets

# router = routers.DefaultRouter()
# router.register(r'users' , UserViewSet)


urlpatterns = [

    path('register/',UserRegistrationView.as_view(),name="register"),
    path('', UserProfileView.as_view()),


]