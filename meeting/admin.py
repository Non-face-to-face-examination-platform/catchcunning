from django.contrib import admin

# Register your models here.

from .models import RoomMember, Post

admin.site.register(RoomMember)
admin.site.register(Post)
    