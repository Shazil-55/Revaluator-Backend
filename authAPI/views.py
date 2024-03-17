from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from authAPI.serializers import UserSerializer ,UserRegistrationSerializer  #,UserLoginSerializer,UserProfileSerializer,UserChangePasswordSerializer,SendPasswordResetEmailSerializer,UserPasswordResetSerializer
from authAPI.renderers import UserRenderer
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
 
  def post(self,request,format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token,'msg':'Registration Success'},status=status.HTTP_201_CREATED)


# class UserLoginView(APIView):
#   renderer_classes = [UserRenderer]
#   def post(self, request, format=None):
#     serializer = UserLoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     email = serializer.data.get('email')
#     password = serializer.data.get('password')
#     user = authenticate(email=email, password=password)
#     if user is not None:
#       token = get_tokens_for_user(user)
#       return Response({'token':token,'msg':'Login Success'}, status=status.HTTP_200_OK)
#     else:
#       return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
    

class UserProfileView(APIView):
    def get(self, request, id=None):
        if id:
            user = get_object_or_404(User, id=id)
            serializer = UserSerializer(user)  # Pass single instance to serializer
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)  # Pass queryset to serializer
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
# class UserChangePasswordView(APIView):
  # renderer_classes = [UserRenderer]
  # permission_classes = [IsAuthenticated]
#   def post(self, request, format=None):
#     serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
#     serializer.is_valid(raise_exception=True)
#     return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

  
# class SendPasswordResetEmailView(APIView):
#   renderer_classes = [UserRenderer]
#   def post(self, request, format=None):
#     serializer = SendPasswordResetEmailSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)

# class UserPasswordResetView(APIView):
#   renderer_classes = [UserRenderer]
#   def post(self, request, uid, token, format=None):
#     serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
#     serializer.is_valid(raise_exception=True)
#     return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
