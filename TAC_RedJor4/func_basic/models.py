from django.db import models
import uuid

# Create your models here.
class User_Login(models.Model):
    
    id = models.CharField(max_length=50, primary_key=True, null=False, default=uuid.uuid4, editable=False)
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
    