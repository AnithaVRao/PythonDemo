# Generated by Django 3.2.15 on 2022-09-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2022-09-14'),
            preserve_default=False,
        ),
    ]
