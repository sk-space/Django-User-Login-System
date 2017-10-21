from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# from mezzanine.core.fields import FileField
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    # photo = FileField(verbose_name=_("Profile Picture"),
    #                   upload_to=upload_to("main.UserProfile.photo", "profiles"),
    #                   format="Image", max_length=255, null=True, blank=True)
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=100, default='', blank=True)


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)
