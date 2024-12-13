from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import ProfileParent

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        # Jika user baru dibuat, buat ProfileParent yang terhubung
        ProfileParent.objects.create(user=instance, email=instance.email)
    else:
        # Jika user diperbarui, sinkronkan data profil (opsional)
        profile = ProfileParent.objects.filter(user=instance).first()
        if profile:
            profile.email = instance.email  # Sinkronisasi email jika diperbarui
            profile.save()
