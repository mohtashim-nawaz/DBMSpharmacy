# Generated by Django 2.2 on 2019-04-27 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20190423_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='desc',
            new_name='Description',
        ),
        migrations.RemoveField(
            model_name='company',
            name='type',
        ),
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
