# Generated by Django 4.2.9 on 2024-12-07 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiences', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.CharField(choices=[('like', "J'aime"), ('dislike', "Je n'aime pas")], max_length=7)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiences.experience')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'experience')},
            },
        ),
    ]
