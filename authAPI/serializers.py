from rest_framework import serializers
from authAPI.models import User

# creating serializers 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class User:
        model:User
        fields ="__all__"