# Generated by Django 4.1.2 on 2022-12-30 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyDashboard', '0009_alter_assignment_sdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='sDate',
            field=models.DateField(default=datetime.date(2022, 12, 30), editable=False),
        ),
    ]
