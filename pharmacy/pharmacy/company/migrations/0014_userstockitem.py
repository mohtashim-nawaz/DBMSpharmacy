# Generated by Django 2.2 on 2019-04-29 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_auto_20190429_0525'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStockItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('unit', models.IntegerField()),
                ('desc', models.CharField(max_length=200, null=True)),
                ('type', models.CharField(max_length=200, null=True)),
                ('cost_per_tab', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('profit_per_tab', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_item', to='company.UserStock')),
            ],
        ),
    ]
