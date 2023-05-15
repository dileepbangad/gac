from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.core.exceptions import ValidationError
import random
import string
import smtplib
from random import randint
from email.message import EmailMessage


def gidgen(email):
    yr = email[:2]
    bc = email[5:7]
    no = email[7:10]
    gidgen = "G-"+no+bc.upper()+yr
    return gidgen

def get_password():
    result_str = "".join(random.choice(string.ascii_letters) for i in range(8))
    return result_str

def email_alert(subject,body,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to

    user = "globalaccesscenter@gmail.com"
    msg['from']=user
    password = "viyfuylqisvbeygk"

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()

def gaccredentials(name,gid,password,email):
    subject = "GAC Login Credentials"
    body = "Dear {},\n\nWelcome, We thank you for your registration at Global Access Center.\n\nYour login credentials are:-\nGID : {}\nPassword : {}\n\n\nYou will use above credentials to login on GLOBAL ACCESS CENTER. The GID cannot be changed and hence we recommend that you store this email for your future reference and change your password.\n\n\n\nIn case you require any further assistance, please mail us at globalaccesscenter@gmail.com.\n\n\nRegards,\nGLOBAL ACCESS CENTER".format(name,gid,password)
    email_alert(subject, body, email)

#validation
def validate_email(value):
    if("@gitjaipur.com" in value):
        return value
    else:
        raise ValidationError("please enter your college email address!")

def validate_student(value):
    user = Student.objects.filter(email=value)
    if(user):
        raise ValidationError("Student Already Exist")
    else:
        return value

# Create your models here.
class Student(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,validators=[validate_email,validate_student])
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
    gid = models.CharField(max_length=9,unique=True,null=True)
    password = models.CharField(max_length=50,null=True)
    USERNAME_FIELD = 'gid'
    REQUIRED_FIELDS = []

