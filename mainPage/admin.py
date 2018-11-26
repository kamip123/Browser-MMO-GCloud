from django.contrib import admin
from .models import Post
from .models import Server
from .models import Profile
from .models import CityPositions

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Server)
admin.site.register(CityPositions)
