from django.contrib import admin
from .models import Post
from .models import Server
from .models import Profile
from .models import CityPositions
from .models import Comment


admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Server)
admin.site.register(CityPositions)
admin.site.register(Comment)
