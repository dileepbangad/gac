# Generated by Django 4.1.7 on 2023-05-07 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyDashboard', '0021_rename_attendence_report_attendencereport_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.CharField(max_length=10)),
                ('sid', models.IntegerField()),
                ('mid1', models.IntegerField()),
                ('mid2', models.IntegerField()),
                ('rtu', models.IntegerField()),
                ('max_marks', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='ProgressReport',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='sDate',
            field=models.DateField(default=datetime.datetime(2023, 5, 7, 17, 12, 23, 85613, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]
