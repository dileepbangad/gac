# Generated by Django 4.1.2 on 2022-12-31 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyDashboard', '0014_alter_submission_submission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='sDate',
            field=models.DateField(default=datetime.date(2023, 1, 1), editable=False),
        ),
    ]