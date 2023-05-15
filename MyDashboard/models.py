from django.db import models
from django.utils.timezone import now

# Create your models here.

class Progress_Report(models.Model):
    gid = models.CharField(max_length=10,unique=False)
    sid = models.IntegerField()
    mid1 = models.IntegerField()
    mid2 = models.IntegerField()
    rtu = models.IntegerField()
    max_marks = models.IntegerField()

    class Meta:
        verbose_name = ("Progress Report")
    def __str__(self)->str:
        return self.gid

class Event(models.Model):
    class Branch_Code(models.TextChoices):
        ALL = 'All'
        CS = 'CS'
        ME = 'ME'
        IT = 'IT'
        EC = 'EC'
        EE = 'EE'
        CE = 'CE'
    branch = models.CharField(choices=Branch_Code.choices,max_length=5,default="Branch_Code")
    title = models.CharField(max_length=25)
    date = models.DateField()
    desc = models.CharField(max_length=200)
    class Event(models.TextChoices):
        Holiday = 'Holiday'
        Cultural = 'Cultural'
        Seminar = 'Seminar'
    event = models.CharField(choices=Event.choices,max_length=25,default='Event')
    def __str__(self)->str:
        return self.title

class AttendenceReports(models.Model):
    gid = models.CharField(max_length=10,unique=False)
    sid = models.IntegerField()
    current = models.IntegerField()
    required = models.IntegerField()
    def __str__(self)->str:
        return self.gid

class Semester_wise_subject(models.Model):
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
    class Branch_Code(models.TextChoices):
        CS = 'CS'
        ME = 'ME'
        IT = 'IT'
        EC = 'EC'
        EE = 'EE'
        CE = 'CE'
    branch_code = models.CharField(choices=Branch_Code.choices,max_length=5,default="Branch_Code")
    subject_name = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=5)
    class Category(models.TextChoices):
        Lecture = 'Lecture'
        Lab = 'Lab'
    subject_category = models.CharField(choices=Category.choices,max_length=7,default="Category")
    def __str__(self)->str:
        return self.subject_code

class Submission(models.Model):
    assignmentId = models.BigIntegerField()
    gid = models.CharField(max_length=10)
    submitted = models.FileField(upload_to='Submission/',null=False)
    submission_date = models.DateField(blank=True)
    submission_status = models.CharField(max_length=20,default='pending')
    def __str__(self)->str:
        return self.gid

class Assignment(models.Model):
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
    class Branch_Code(models.TextChoices):
        CS = 'CS'
        ME = 'ME'
        IT = 'IT'
        EC = 'EC'
        EE = 'EE'
        CE = 'CE'
    branch_code = models.CharField(choices=Branch_Code.choices,max_length=5,default="Branch_Code")
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    sDate = models.DateField(default=now(),editable=False)
    eDate = models.DateField()
    Assigned = models.FileField(upload_to='Assignments/',null=False)

    def __str__(self)->str:
        return self.title

class Student_Document(models.Model):
    gid = models.CharField("GID",max_length=9,help_text='Format: G-079CS19, G-(last three digits of Roll.No)+ BranchCode + Enrolled year')
    title = models.CharField("Title",max_length=25)
    document = models.FileField(upload_to="Documents/",null=False)

    class Meta:
        verbose_name = ("Student Document")

    def __str__(self)->str:
        return self.gid

class Profile_Detail(models.Model):
    #Personal details
    gid = models.CharField("GID",max_length=9,help_text='Format: G-079CS19, G-(last three digits of Roll.No)+ BranchCode + Enrolled year')
    contact_no = models.CharField("Contact No.",max_length=10)
    father_name = models.CharField("Father Name",max_length=25)
    father_contact_no = models.CharField("Father Contact No.",max_length=10)
    dob = models.DateField("DOB",help_text='yyyy-mm-dd')
    gender = models.CharField(max_length=10)
    personal_email = models.EmailField("Personal Email",max_length=50)
    address = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to="ProfilePic/",null=False)

    #college details
    section = models.CharField("Section Name",max_length=1,default="A")
    college_name = models.CharField("College Name",max_length=50, default="Global Institute Of Technology, Jaipur")
    course_enrolled = models.CharField("Course Enrolled",max_length=50, default="B. Tech.")
    enrollment_no = models.CharField("Enrollment No.",max_length=50,blank=True)

    #Academin details
    x = models.FloatField("10th Grade")
    xii = models.FloatField("12th Grade")
    sem1 = models.FloatField("1st SEMESTER",blank=True)
    sem2 = models.FloatField("2nd SEMESTER",blank=True) 
    sem3 = models.FloatField("3rd SEMESTER",blank=True)
    sem4 = models.FloatField("4th SEMESTER",blank=True)
    sem5 = models.FloatField("5th SEMESTER",blank=True)
    sem6 = models.FloatField("6th SEMESTER",blank=True)
    sem7 = models.FloatField("7th SEMESTER",blank=True)
    sem8 = models.FloatField("8th SEMESTER",blank=True)
    Aggregate = models.FloatField("Aggregate CGPA",blank=True)

    class Meta:
        verbose_name = ("Profile Detail")

    def __str__(self)->str:
        return self.gid
