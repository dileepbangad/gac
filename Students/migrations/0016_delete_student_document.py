# Generated by Django 4.1.2 on 2023-01-07 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0015_alter_student_document_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student_Document',
        ),
    ]
