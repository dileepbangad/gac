# Generated by Django 4.1.2 on 2023-01-07 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0017_student_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_document',
            name='document',
            field=models.FileField(upload_to='Documents/'),
        ),
    ]
