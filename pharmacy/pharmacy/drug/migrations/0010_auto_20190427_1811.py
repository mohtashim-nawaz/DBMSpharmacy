# Generated by Django 2.2 on 2019-04-27 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0009_auto_20190427_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 27, 18, 11, 8, 255758)),
        ),
    ]
