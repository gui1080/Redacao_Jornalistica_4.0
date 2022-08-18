from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .serializers import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import generics


# dependencias 
# pip3 install djangorestframework

# Create your views here.

# Usuários
class LoginView(generics.CreateAPIView):
    queryset = User_Login.objects.all()
    serializer_class = LoginUserSerializer

# NewsItem (Texto)

# NewsItem (Gráfico)

# NewsItem (Imagem)