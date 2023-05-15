from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *

# Register your models here.
@admin.register(Template)
class Template(admin.ModelAdmin):
    list_display = ('category','date','image')

@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = ('title','content')

@admin.register(Note)
class Note(admin.ModelAdmin):
    list_display = ('title','content')

@admin.register(Lecture)
class Lecture(admin.ModelAdmin):
    list_display = ('title','link')

@admin.register(ExamPaper)
class ExamPaper(admin.ModelAdmin):
    list_display = ('subject','year','paper')
