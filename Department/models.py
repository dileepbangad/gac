from django.db import models

# Create your models here.
class Faculty(models.Model):
    class Departments(models.TextChoices):
        CSIT = "Computer Science & IT"
        ME = "Mechanical Engineering"
        AIDS = "AI & Data Science"
        AS = "Applied Science"
        CE = "Civil Engineering"
        EE = "Electrical Engineering"
    department = models.CharField(choices=Departments.choices,max_length=25,default=Departments.CSIT)
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    research = models.CharField(max_length=200)
    email = models.EmailField(max_length=50,null=False)
    photo = models.ImageField(upload_to='facultyPic/',null=False)

    class Meta:
        verbose_name = ("Facultie")
    def __str__(self)->str:
        return self.name

