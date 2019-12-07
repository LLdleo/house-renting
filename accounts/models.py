from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # create custom fields here
    phoneNumber = models.TextField(max_length=30, blank=True)
    dept = models.TextField(max_length=200, blank=True)
    academicYear = models.TextField(null=True, blank=True)
    gender = models.TextField(max_length=10, blank=True)
    dateOfBirth = models.DateField(null=True, blank=True)


def __str__(self):
    return self.user.username
