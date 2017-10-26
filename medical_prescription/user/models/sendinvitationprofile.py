# standard library
import datetime

# Django
from django.db import models

# Local Django
from user.models import Patient


# This class defines the fields necessary to invite a patient to register in
# the system.
class SendInvitationProfile(models.Model):
    patient = models.OneToOneField(Patient)
    activation_key = models.CharField(blank=False, max_length=100)
    key_expires = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.patient.email

    class Meta:
        verbose_name_plural = u'Send Invitation Profile'
