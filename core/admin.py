from django.contrib import admin
from .models import Profile,Post, likePost
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(likePost)
