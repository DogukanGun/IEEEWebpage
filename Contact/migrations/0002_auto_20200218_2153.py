# Generated by Django 2.2.3 on 2020-02-18 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=500, verbose_name='message'),
        ),
    ]
