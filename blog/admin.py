from django.contrib import admin

# Register your models here.
from .models import Blog

class BlogAdmin(admin.ModelAdmin):

    pass

admin.site.register(Blog, BlogAdmin)



