from django.urls import path
from .views import *

urlpatterns = [
    path('cadastro', CadastroView.as_view()), 
    path('text_news', TextView.as_view()), 
    path('photo_news', PhotoView.as_view()), 
    path('graphic_news', GraphicsView.as_view()), 
]