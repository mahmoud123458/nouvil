# Generated by Django 5.1 on 2024-08-19 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0003_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
