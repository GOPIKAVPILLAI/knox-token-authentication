from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from knox.views import LoginView as KnoxLoginView
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import CreateUserSerializer, UpdateUserSerializer,UserSerializer,CustomAuthTokenSerializer,LoginSerializer
from knox import views as knox_views
from django.contrib.auth import login,authenticate
from rest_framework import permissions
from knox.auth import AuthToken
from knox.auth import TokenAuthentication


class CreateUserAPI(CreateAPIView):
    # queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

class ViewUserAPI(RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer

class UpdateUserAPI(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer


class LoginView(KnoxLoginView):
    
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [TokenAuthentication,]
    serializer_class=LoginSerializer
    def post(self, request, format=None):
        serializer = CustomAuthTokenSerializer(data=request.data)
        serializer.is_valid()
        user = serializer.validated_data.get('user')
        # _,token=AuthToken.objects.create(user)
        login(request, user)
        return super(LoginView, self).post(request, format=None)    
        # return Response({'user_info': {
        #     'email':user.email,
        #     'token':token,

        # }})
    
