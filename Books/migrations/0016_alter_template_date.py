# Generated by Django 4.1.2 on 2023-01-11 20:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0015_alter_lecture_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='date',
            field=models.DateField(default=datetime.date(2023, 1, 12), editable=False),
        ),
    ]
