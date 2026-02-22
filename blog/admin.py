from django.contrib import admin
from .models import Post #import post model from models.py

admin.site.register(Post)  #register post model with admin site