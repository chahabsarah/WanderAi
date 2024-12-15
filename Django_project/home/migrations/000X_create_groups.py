from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def create_groups(apps, schema_editor):
    User = apps.get_model('auth', 'User')

    super_admin_group, _ = Group.objects.get_or_create(name='super_admin')
    admin_group, _ = Group.objects.get_or_create(name='admin')
    client_group, _ = Group.objects.get_or_create(name='client')

    super_admin_group.permissions.set(Permission.objects.all())

    def get_permissions_for_model(app_label, model_name):
        return Permission.objects.filter(
            content_type__app_label=app_label,
            content_type__model=model_name.lower()
        )

    admin_models = ['Reclamations', 'Avis', 'Preference']
    admin_permissions = []
    for model in admin_models:
        admin_permissions.extend(get_permissions_for_model('home', model))

    admin_group.permissions.set(admin_permissions)

    client_permissions = []
    for model in admin_models:
        client_permissions.extend(Permission.objects.filter(
            content_type__app_label='home',
            content_type__model=model.lower(),
            codename__startswith='view_'
        ))

    client_group.permissions.set(client_permissions)

class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('home', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
