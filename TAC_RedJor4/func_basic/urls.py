from django.urls import path
from .views import *

urlpatterns = [
    path('login', LoginView.as_view()), 
    path('text_news', TextView.as_view()), 
]