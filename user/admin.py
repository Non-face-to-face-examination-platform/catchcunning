from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname",)}),)
UserAdmin.fieldsets += (("Custom fields", {"fields": ("superintendent",)}),)
#기본적으로 어드민 페이지에 나타나지 않으므로 추가?