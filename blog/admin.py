from django.contrib import admin
from .models import Blog
from .models import Profile

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "avatar")
    search_fields = ("user__username", "user__email")