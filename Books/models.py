from django.db import models
from django.utils.timezone import now
# Create your models here.
class Template(models.Model):
    class Category(models.TextChoices):
        Computer = 'Computer'
        Mechanical = 'Mechanical'
        Electronics = 'Electronics'
        Civil = 'Civil'
        Placements = 'Placements'
    category = models.CharField(choices=Category.choices,max_length=25,default="Category")
    image = models.ImageField(upload_to="Template/",null=False)
    date = models.DateField(default=now(),editable=False)
    def __str__(self)->str:
        return self.category

class Book(models.Model):
    title = models.CharField(max_length=100)
    frontpage = models.ImageField(upload_to="Frontpage/",null=False)
    content = models.FileField(upload_to="Books/",null=False)
    def __str__(self)->str:
        return self.title

class Note(models.Model):
    class Category(models.TextChoices):
        Teacher = 'teacher-notes'
        Student = 'student-notes'
        Other = 'web-notes'
    category = models.CharField(choices=Category.choices,max_length=25,default="Category")
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to="Notes/",null=False)
    def __str__(self)->str:
        return self.title  

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=100)  
    def __str__(self)->str:
        return self.title

class ExamPaper(models.Model):
    subject = models.CharField(max_length=100)
    year = models.IntegerField(help_text="e.g.:2023 Format - yyyy")
    paper = models.FileField(upload_to="ExamPapers/",null=False)
