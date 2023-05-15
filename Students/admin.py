from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *

@admin.register(Student)
    
class Student(admin.ModelAdmin):
    list_display = ('id','gid','name','email','semid','section','password')




