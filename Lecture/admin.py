from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *
# Register your models here.

@admin.register(Lecture)
class Lecture(admin.ModelAdmin):
    list_display = ('id','semid','section','updateDate','schedule')