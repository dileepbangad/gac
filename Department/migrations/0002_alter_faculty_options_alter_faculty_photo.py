# Generated by Django 4.1.7 on 2023-05-06 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name': 'Facultie'},
        ),
        migrations.AlterField(
            model_name='faculty',
            name='photo',
            field=models.ImageField(upload_to='facultyPic/'),
        ),
    ]