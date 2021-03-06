from django.db import models
from managers.models import Manager
from accounts.models import Profile
from listings.models import Listing
from django.contrib.auth.models import User


class Contract(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    if_signed = models.BooleanField(default=False)
    sign_name = models.CharField(max_length=100)
    sign_date = models.DateField(blank=False)
    valid = models.BooleanField(default=False)
