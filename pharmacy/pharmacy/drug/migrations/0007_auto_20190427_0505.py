# Generated by Django 2.2 on 2019-04-27 05:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0006_auto_20190425_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 27, 5, 5, 5, 975575)),
        ),
    ]