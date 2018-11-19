from django.contrib import admin
from .models import Post
from .models import Server
from .models import Profile

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Server)
