# Generated by Django 4.2.9 on 2024-12-07 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0003_remove_preference_preference_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preference',
            name='activities',
        ),
    ]
