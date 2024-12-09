from django.contrib import admin
from .models import ApplicationUser
# Register your models here.

class ApplicationUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(ApplicationUser, ApplicationUserAdmin)


