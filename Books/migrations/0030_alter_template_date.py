# Generated by Django 4.1.2 on 2023-05-09 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0029_alter_template_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 9, 21, 49, 48, 663784, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]
