# Generated by Django 2.2 on 2021-03-23 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210323_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='due_date',
        ),
    ]
