# Generated by Django 4.1.2 on 2023-01-08 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0010_alter_template_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('frontpage', models.ImageField(upload_to='Frontpage/')),
                ('content', models.FileField(upload_to='Books/')),
            ],
        ),
        migrations.AlterField(
            model_name='template',
            name='date',
            field=models.DateField(default=datetime.date(2023, 1, 9), editable=False),
        ),
        migrations.AlterField(
            model_name='template',
            name='image',
            field=models.ImageField(upload_to='Template/'),
        ),
    ]
