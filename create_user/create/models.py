from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User)
    position = models.CharField(max_length=20, choices=[('teacher', 'Teacher'), ('student', 'Student')], null=True)

    @receiver(post_save, sender=User)
    def user_post_save(sender, **kwargs):
        instance = kwargs.get('instance')
        created = kwargs.get('created')
        if created:
            Profile.objects.create(user=instance)
