from django.contrib import admin
from .models import Post
from .models import Server

admin.site.register(Post)
admin.site.register(Server)
