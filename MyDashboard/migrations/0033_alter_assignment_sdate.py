# Generated by Django 4.1.2 on 2023-05-09 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyDashboard', '0032_alter_assignment_sdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='sDate',
            field=models.DateField(default=datetime.datetime(2023, 5, 9, 21, 49, 48, 658781, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]
