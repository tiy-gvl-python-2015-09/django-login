from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User)
    credit_card = models.CharField(max_length=20, blank=True)
    classification = models.IntegerField(choices=[(1, 'Teacher'), (2, 'Student')], null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def user_post_save(sender, **kwargs):
    instance = kwargs.get('instance')
    created = kwargs.get('created')
    if created:
        Profile.objects.create(user=instance)
