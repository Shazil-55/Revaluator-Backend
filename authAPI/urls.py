# from django.contrib import admin
from django.urls import path , include
from authAPI.views import UserProfileView
# from rest_framework import routers, serializers, viewsets

# router = routers.DefaultRouter()
# router.register(r'users' , UserViewSet)


urlpatterns = [

    path('auth/', UserProfileView.as_view())


]