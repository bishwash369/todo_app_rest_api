# Generated by Django 3.0.9 on 2020-08-07 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200807_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='employee',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
