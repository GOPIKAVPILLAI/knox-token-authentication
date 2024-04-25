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
from django.http import HttpResponse
from knox.auth import TokenAuthentication
from auth_app.models import User


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

def my_view(request):
    # Assuming user is authenticated and you have access to request.user
    t=()
    user,t= TokenAuthentication().authenticate(request)
    print(user)

    if user and user.is_admin():
        # User is authenticated and is an admin
        # Your admin-specific logic here
        return HttpResponse("You are an admin!")
    else:
        # User is not an admin or not authenticated
        # Your non-admin logic here
        return HttpResponse("You are not an admin!")
