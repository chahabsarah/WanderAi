# Generated by Django 4.2.9 on 2024-10-29 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0002_userprofile_and_more'),
        ('recommendations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendation',
            old_name='recommended_at',
            new_name='date_recommended',
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='product',
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='reason',
        ),
        migrations.AddField(
            model_name='recommendation',
            name='experience_name',
            field=models.CharField(default='Expérience non spécifiée', max_length=200),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='preferences.userprofile'),
        ),
    ]
