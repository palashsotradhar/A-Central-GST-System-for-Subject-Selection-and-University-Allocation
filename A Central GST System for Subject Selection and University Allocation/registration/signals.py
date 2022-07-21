from unicodedata import name
from urllib import request
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from registration.models import Registration_Model
from django.dispatch import receiver


@receiver(post_save, sender=User)
def user_profile(sender, instance, created, **kwargs):
    if created:
        Registration_Model.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email
        )
        # print('Hello 2')


post_save.connect(user_profile, sender=User)