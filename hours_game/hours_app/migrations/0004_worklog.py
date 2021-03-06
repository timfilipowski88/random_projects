# Generated by Django 2.2 on 2021-05-15 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hours_app', '0003_auto_20210421_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worklog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=100)),
                ('description', models.TextField()),
                ('hours', models.DecimalField(decimal_places=3, max_digits=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_worklogs', to='hours_app.User')),
            ],
        ),
    ]
