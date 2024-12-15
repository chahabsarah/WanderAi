# home/signals.py

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def assign_user_role(sender, instance, created, **kwargs):
    if created:
        if '@esprit.tn' in instance.email:
            super_admin_group, created = Group.objects.get_or_create(name='super_admin')
            instance.groups.add(super_admin_group)
            instance.is_staff = True
            instance.is_superuser = True
            instance.save()
        elif '@gmail.com' in instance.email:
            client_group, created = Group.objects.get_or_create(name='client')
            instance.groups.add(client_group)

        elif '@yahoo.fr' in instance.email:
            admin_group, created = Group.objects.get_or_create(name='admin')
            instance.groups.add(admin_group)
