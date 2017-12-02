from django.db import models
from user.models import User
from chat.models import Response
from chat import constants


class Message(models.Model):
    """
    Create a Message model in database.
    """

    user_from = models.ForeignKey(User, related_name="user_from")
    user_to = models.ForeignKey(User, related_name="user_to")

    subject = models.CharField(max_length=constants.MAX_LENGTH_TEXT_SUBJECT)
    date = models.DateField(auto_now=True)

    is_active_patient = models.BooleanField(default=True)
    is_active_health_professional = models.BooleanField(default=True)

    # List of response in Message.
    messages = models.ManyToManyField(Response, default=None)
