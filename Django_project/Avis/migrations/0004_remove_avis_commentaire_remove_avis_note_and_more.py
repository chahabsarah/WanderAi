# Generated by Django 4.2.9 on 2024-12-06 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0002_userprofile_and_more'),
        ('Avis', '0003_remove_avis_experience_name_remove_avis_feedback_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avis',
            name='commentaire',
        ),
        migrations.RemoveField(
            model_name='avis',
            name='note',
        ),
        migrations.RemoveField(
            model_name='avis',
            name='voyage',
        ),
        migrations.AddField(
            model_name='avis',
            name='experience_name',
            field=models.CharField(default='Experience sans nom', max_length=200),
        ),
        migrations.AddField(
            model_name='avis',
            name='feedback',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='avis',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='avis',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='preferences.userprofile'),
        ),
    ]
