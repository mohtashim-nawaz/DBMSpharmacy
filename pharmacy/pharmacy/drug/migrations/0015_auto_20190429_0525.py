# Generated by Django 2.2 on 2019-04-29 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0014_auto_20190429_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 29, 5, 25, 53, 613227)),
        ),
    ]