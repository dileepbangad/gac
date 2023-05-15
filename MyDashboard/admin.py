from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *

# Register your models here.
# @admin.register(Student)
# @admin.register(Student_Profile)


# class Student(admin.ModelAdmin):
#     list_display = ('gid','name','email')

@admin.register(Assignment)

class Assignment(admin.ModelAdmin):
    list_display = ('semid','section','subject','title','branch_code')


@admin.register(Submission)

class Submission(admin.ModelAdmin):
    list_display = ('assignmentId','gid','submission_date','submission_status','submitted')

@admin.register(Semester_wise_subject)

class Semester_wise_subject(admin.ModelAdmin):
    list_display = ('id','semid','subject_name','subject_code','branch_code','subject_category')

@admin.register(Progress_Report)

class ProgressReport(admin.ModelAdmin):
    list_display = ('id','gid','sid','mid1','mid2','rtu','max_marks')

@admin.register(AttendenceReports)

class AttendenceReports(admin.ModelAdmin):
    list_display = ('id','gid','sid','current','required')


@admin.register(Event)

class Event(admin.ModelAdmin):
    list_display = ('title','date','branch','desc','event')
    search_fields = ('title','event')
    list_filter = ('event',)

@admin.register(Profile_Detail)
 
class Profile_Detail(admin.ModelAdmin):
    fieldsets = (
        ("Personal Details",{
            "fields":(
                ('gid','contact_no'),('father_name','father_contact_no'),'dob','gender',('personal_email','address'),'profile_pic'
            ),
        }),
        ("College Details",{
            "fields":(
                ('college_name','course_enrolled'),'enrollment_no','section'
            ),
        }),
        ("Academin details",{
            "fields":(
                ('x','xii'),('sem1','sem2'),('sem3','sem4'),('sem5','sem6'),('sem7','sem8'),'Aggregate'
            ),
        }),
    )
    list_display = ('gid','father_name','contact_no','profile_pic')

    @admin.register(Student_Document)

    class Student_Document(admin.ModelAdmin):
        list_display = ('gid','title','document')







