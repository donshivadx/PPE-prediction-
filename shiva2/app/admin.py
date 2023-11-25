from django.contrib import admin

# Register your models here.
from .models import UserDetails,UserProduct

admin.site.register(UserDetails)
admin.site.register(UserProduct)