# Generated by Django 4.1.2 on 2023-05-09 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0028_alter_template_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 9, 21, 46, 33, 955596, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]