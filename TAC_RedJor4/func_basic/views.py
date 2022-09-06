from django.shortcuts import render
from .models import *
from .serializers import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response

# dependencias 
# pip3 install djangorestframework

# Create your views here.

# Usuários
class LoginView(generics.CreateAPIView):
    
    queryset = User_Login.objects.all()
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        id = request.data['id']
        name = request.data['name']
        password = request.data['password']
        email = request.data['email']
        User_Login.objects.create(id=id, name=name, password=password, email=email)
        return HttpResponse({'message': 'User Created'}, status=200)

# NewsItem (Texto)
class TextView(generics.CreateAPIView):

    queryset = NewsItem_Text.objects.all()
    serializer_class = NewsItem_TextSerializer
    
    def get(self, request, format=None):
        text_news = [news for news in NewsItem_Text.objects.all()]
        return Response(text_news)

    def post(self, request, *args, **kwargs):
        metadata = request.data['metadata']
        title = request.data['title']
        sutien = request.data['sutien']
        authors = request.data['authors']
        editors = request.data['editors']
        news_text = request.data['news_text']
        keywords = request.data['keywords']
        related_news = request.data['related_news']
        related_publisher = request.data['related_publisher']
        posted_on = request.data['posted_on']
        NewsItem_Text.objects.create(metadata=metadata, title=title, sutien=sutien, authors=authors, editors=editors, news_text=news_text, keywords=keywords, related_news=related_news, related_publisher=related_publisher, posted_on=posted_on)
        return HttpResponse({'message': 'News Created'}, status=200)


# NewsItem (Imagem)
class PhotoView(generics.CreateAPIView):
    
    queryset = NewsItem_Photo.objects.all()
    serializer_class = NewsItem_PhotoSerializer
    
    def get(self, request, format=None):
        photo_news = [photo_news for photo_news in NewsItem_Photo.objects.all()]
        return Response(photo_news)

    def post(self, request, *args, **kwargs):
        metadata = request.data['metadata']
        title = request.data['title']
        place = request.data['place']
        photographer = request.data['photographer']
        keywords = request.data['keywords']
        used_equipament = request.data['used_equipament']
        description = request.data['description']
        image = request.data['image']
        NewsItem_Photo.objects.create(metadata=metadata, title=title, place=place, photographer=photographer, keywords=keywords, used_equipament=used_equipament, description=description, image=image)
        return HttpResponse({'message': 'Photo Created'}, status=200)


# NewsItem (Gráfico)
class GraphicsView(generics.CreateAPIView):
    
    queryset = NewsItem_Graphics.objects.all()
    serializer_class = NewsItem_GraphicsSerializer
    
    def get(self, request, format=None):
        graphic_news = [graphic_news for graphic_news in NewsItem_Graphics.objects.all()]
        return Response(graphic_news)

    def post(self, request, *args, **kwargs):
        metadata = request.data['metadata']
        description = request.data['description']
        data = request.data['data']
        type_graphic = request.data['type_graphic']
        designer = request.data['designer']
        graphic_image = request.data['graphic_image']
        NewsItem_Graphics.objects.create(metadata=metadata, description=description, data=data, type_graphic=type_graphic, designer=designer, graphic_image=graphic_image)
        return HttpResponse({'message': 'Graphic Created'}, status=200)


