from django.contrib import admin

from .models import UserRegis

# Register your models here.

class UserRegisAdmin(admin.ModelAdmin) :
    class Meta :
        model=UserRegis

admin.site.register(UserRegis,UserRegisAdmin)
