from django.db import models
from managers.models import Manager
from accounts.models import Profile
from listings.models import Listing


class Contract(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    if_signed = models.BooleanField(default=False)
