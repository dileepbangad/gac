# Generated by Django 4.1.2 on 2023-05-09 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lecture', '0002_alter_lecture_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('sem1', 'Sem1'), ('sem2', 'Sem2'), ('sem3', 'Sem3'), ('sem4', 'Sem4'), ('sem5', 'Sem5'), ('sem6', 'Sem6'), ('sem7', 'Sem7'), ('sem8', 'Sem8')], default='SEMESTER', max_length=5, unique=True)),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='SECTION', max_length=1, unique=True)),
                ('schedule', models.FileField(upload_to='Schedule-Lectures/')),
                ('scheduleDate', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
    ]
