from django.contrib import admin
from .models import Post, UserProfile

# Register your models here.
admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'content', 'created_at']
    search_fields = ['title', 'author']

admin.site.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user',)
