# Generated by Django 2.2 on 2021-03-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210323_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='due_date',
            field=models.DateField(),
        ),
    ]