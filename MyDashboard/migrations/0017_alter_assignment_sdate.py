# Generated by Django 4.1.2 on 2023-01-07 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyDashboard', '0016_alter_assignment_sdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='sDate',
            field=models.DateField(default=datetime.date(2023, 1, 8), editable=False),
        ),
    ]
