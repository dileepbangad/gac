# Generated by Django 4.1.7 on 2023-05-06 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lecture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='schedule',
            field=models.FileField(upload_to='Schedule-Lectures/'),
        ),
    ]
