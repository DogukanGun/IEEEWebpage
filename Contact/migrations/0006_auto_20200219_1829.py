# Generated by Django 2.2.3 on 2020-02-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0005_auto_20200219_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
