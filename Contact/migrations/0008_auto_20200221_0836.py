# Generated by Django 2.2.3 on 2020-02-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0007_auto_20200219_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]