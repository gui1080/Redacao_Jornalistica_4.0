from rest_framework import serializers
from .models import User_Login, NewsItem_Text

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Login
        fields = ('id', 'name', 'password', 'email')
        

class NewsItem_TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem_Text
        fields = ('metadata', 'title', 'sutien', 'authors', 'editors', 'news_text', 'keywords', 'related_news', 'related_publisher', 'posted_on')