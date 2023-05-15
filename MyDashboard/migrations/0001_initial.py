# Generated by Django 4.1.2 on 2022-10-28 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('sem1', 'Sem1'), ('sem2', 'Sem2'), ('sem3', 'Sem3'), ('sem4', 'Sem4'), ('sem5', 'Sem5'), ('sem6', 'Sem6'), ('sem7', 'Sem7'), ('sem8', 'Sem8')], default='SEMESTER', max_length=5)),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='SECTION', max_length=1)),
                ('branch_code', models.CharField(choices=[('CS', 'Cs'), ('ME', 'Me'), ('IT', 'It'), ('EC', 'Ec'), ('EE', 'Ee'), ('CE', 'Ce')], default='Branch_Code', max_length=5)),
                ('subject', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('sDate', models.DateField(default=datetime.date(2022, 10, 29), editable=False)),
                ('eDate', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('submitted', 'Submitted')], default='pending', max_length=15)),
                ('Assigned', models.FileField(upload_to='Assignments/')),
            ],
        ),
        migrations.CreateModel(
            name='Attendence_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.CharField(max_length=10)),
                ('subject_id', models.IntegerField()),
                ('current', models.IntegerField()),
                ('required', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Progress_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.CharField(max_length=10)),
                ('subject_id', models.IntegerField()),
                ('mid1', models.IntegerField()),
                ('mid2', models.IntegerField()),
                ('rtu', models.IntegerField()),
                ('max_marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Semester_wise_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('sem1', 'Sem1'), ('sem2', 'Sem2'), ('sem3', 'Sem3'), ('sem4', 'Sem4'), ('sem5', 'Sem5'), ('sem6', 'Sem6'), ('sem7', 'Sem7'), ('sem8', 'Sem8')], default='SEMESTER', max_length=5)),
                ('branch_code', models.CharField(choices=[('CS', 'Cs'), ('ME', 'Me'), ('IT', 'It'), ('EC', 'Ec'), ('EE', 'Ee'), ('CE', 'Ce')], default='Branch_Code', max_length=5)),
                ('subject_name', models.CharField(max_length=50)),
                ('subject_code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('gid', models.CharField(default='G-000BC00', max_length=50)),
                ('password', models.CharField(default='000000', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('age', models.CharField(max_length=10)),
                ('aadhar', models.CharField(max_length=12)),
                ('father_name', models.CharField(max_length=50)),
                ('father_contact', models.CharField(max_length=10)),
                ('college_name', models.CharField(max_length=50)),
                ('course_enrolled', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('sem', models.CharField(max_length=50)),
                ('enrollment_no', models.CharField(max_length=50)),
                ('roll_no', models.CharField(max_length=50)),
                ('x_percent', models.CharField(max_length=10)),
                ('x_year', models.CharField(max_length=10)),
                ('x_marksheet', models.FileField(default=None, max_length=250, null=True, upload_to='{}marksheets/')),
                ('xii_percent', models.CharField(max_length=10)),
                ('xii_year', models.CharField(max_length=10)),
                ('xii_marksheet', models.FileField(default=None, max_length=250, null=True, upload_to='marksheets/')),
                ('sem_marksheets', models.FileField(default=None, max_length=250, null=True, upload_to='marksheets/')),
                ('img', models.ImageField(upload_to='image/')),
                ('resume', models.FileField(upload_to='resume/')),
                ('sign', models.FileField(upload_to='sign/')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignmentId', models.BigIntegerField()),
                ('gid', models.CharField(max_length=10)),
                ('submitted', models.CharField(max_length=50)),
                ('submission_date', models.DateField()),
                ('submission_status', models.CharField(default='pending', max_length=20)),
            ],
        ),
    ]
