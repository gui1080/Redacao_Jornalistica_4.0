from rest_framework import serializers
from .models import User_Login, NewsItem_Text, NewsItem_Photo, NewsItem_Graphics

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Login
        fields = ('id', 'name', 'password', 'email')
        

class NewsItem_TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem_Text
        fields = ('metadata', 'title', 'sutien', 'authors', 'editors', 'news_text', 'keywords', 'related_news', 'related_publisher', 'posted_on')
        

class NewsItem_PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem_Photo
        fields = ('metadata', 'title', 'place', 'photographer', 'keywords', 'used_equipament', 'description', 'image')

class NewsItem_GraphicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem_Graphics
        fields = ('metadata', 'description', 'data', 'type_graphic', 'designer', 'graphic_image')