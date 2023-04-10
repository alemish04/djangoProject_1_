from django.contrib import admin
from .models import Post, Category

admin.site.register(Post)  # Регистрация модели нашего поста
admin.site.register(Category)
