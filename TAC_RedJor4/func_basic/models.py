from tkinter import Place
from django.db import models
import uuid
from datetime import datetime

def upload_path(instance, filename):
    return '/'.join(['files', str(instance.title)], filename)

# Create your models here.
class User_Login(models.Model):
    
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=150, unique=False, null=False)
    email = models.CharField(max_length=50, unique=True, null=False)
    
class Basic_Metadata(models.Model):
    
    id = models.CharField(max_length=50, primary_key=True, null=False, default=uuid.uuid4, editable=False)
    version = models.CharField(max_length=150, unique=False)
    language = models.CharField(max_length=150, unique=False)
    catalog_ref = models.CharField(max_length=150, unique=False)
    rights_info = models.CharField(max_length=150, unique=False)
    item_meta_itemclass = models.CharField(max_length=150, unique=False)
    item_meta_versioncreated = models.CharField(max_length=150, unique=False)
    
    # arquivado? usado? sendo feito?
    item_meta_publicationstatus = models.CharField(max_length=150, unique=False)
    
    item_meta_provider = models.CharField(max_length=150, unique=False)
    content_meta_creator = models.CharField(max_length=150, unique=False)
    content_meta_located = models.CharField(max_length=150, unique=False)
    content_meta_subject = models.CharField(max_length=150, unique=False)
    content_meta_headline = models.CharField(max_length=150, unique=False)
    
    # informação de parte do dado
    part_meta = models.CharField(max_length=150, unique=False)
    
    inline_ref = models.CharField(max_length=150, unique=False)
    
    # derivado de algo? referenciar aqui
    derived_from = models.CharField(max_length=150, unique=False)
    
    hop_history = models.CharField(max_length=150, unique=False)
    uploaded_at = models.DateTimeField(default=datetime.now, blank=True)

class NewsItem_Text(models.Model):
    
    metadata = models.OneToOneField(
    Basic_Metadata,
    on_delete=models.CASCADE,
    )
    
    title = models.CharField(max_length=150, unique=False)  
    sutien = models.CharField(max_length=150, unique=False) 
    authors = models.CharField(max_length=150, unique=False) 
    editors = models.CharField(max_length=150, unique=False)
    
    # texto em si
    news_text = models.CharField(max_length=15000, unique=False) 
    
    keywords = models.CharField(max_length=1500, unique=False) 
    related_news = models.CharField(max_length=1500, unique=False) 
    
    # pra qual editoria isso vai
    related_publisher = models.CharField(max_length=350, unique=False) 
    
    # em qual qual midia isso circulou
    posted_on = models.CharField(max_length=150, unique=False)

class NewsItem_Photo(models.Model):
    
    metadata = models.OneToOneField(
    Basic_Metadata,
    on_delete=models.CASCADE,
    )
    
    title = models.CharField(max_length=150, unique=False)
    place = models.CharField(max_length=350, unique=False) 
    photographer = models.CharField(max_length=350, unique=False)
    keywords = models.CharField(max_length=350, unique=False)
    used_equipament = models.CharField(max_length=350, unique=False)
    description = models.CharField(max_length=350, unique=False)
    image = models.FileField(upload_to=upload_path, blank=True, null=True)

class NewsItem_Graphics(models.Model):
    
    metadata = models.OneToOneField(
    Basic_Metadata,
    on_delete=models.CASCADE,
    )
    
    description = models.CharField(max_length=350, unique=False)
    data = models.CharField(max_length=350, unique=False)
    type_graphic = models.CharField(max_length=350, unique=False)
    designer = models.CharField(max_length=350, unique=False)
    graphic_image = models.FileField(upload_to=upload_path, blank=True, null=True)
    