# Generated by Django 4.2.9 on 2024-12-07 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0003_experience_like_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='experiences/'),
        ),
    ]
