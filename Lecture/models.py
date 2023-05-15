from django.db import models

# Create your models here.
class Lecture(models.Model):
    class Semester(models.IntegerChoices):
        SEM1 = 1
        SEM2 = 2
        SEM3 = 3
        SEM4 = 4
        SEM5 = 5
        SEM6 = 6
        SEM7 = 7
        SEM8 = 8
    semid = models.IntegerField(choices=Semester.choices)
    class Section(models.TextChoices):
        A = 'A'
        B = 'B'
        C = 'C'
        D = 'D'
    section = models.CharField(max_length=1,choices=Section.choices,default="SECTION")
    schedule = models.FileField(upload_to='Schedule-Lectures/',null=False)
    updateDate = models.DateField()
    def __str__(self)->str:
        return self.section
