from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Store additional user details that are not covered in Profile
    """
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
