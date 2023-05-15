from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *

# Register your models here.
@admin.register(Faculty)
class Faculty(admin.ModelAdmin):
    list_display = ('name','department','designation','email','photo')