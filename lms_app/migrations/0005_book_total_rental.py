# Generated by Django 5.1 on 2024-08-20 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0004_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rental',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
