# Generated by Django 2.2.3 on 2020-02-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0004_auto_20200219_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
