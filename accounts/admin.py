from django.contrib import admin
from .models import BlogUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(BlogUser)
class BlogUserAdmin(UserAdmin):
    model = BlogUser
    list_display = ('username', 'email', 'date_joined', 'last_login','is_active','is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'email')

    ordering = ('username',)
