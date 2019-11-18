from django.db import models
from datetime import datetime
from managers.models import Manager


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)
    replied = models.BooleanField(default=False)
    reply_message = models.TextField(blank=True)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
