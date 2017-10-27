from django.db import models
from user.models import User
from chat import constants
from django.contrib.postgres.fields import ArrayField


class Message(models.Model):

    # TODO (Felipe) add file field.

    user_from = models.ForeignKey(User, related_name="user_from")
    user_to = models.ForeignKey(User, related_name="user_to")

    text = models.CharField(max_length=constants.MAX_LENGTH_TEXT_MESSAGE)
    subject = models.CharField(max_length=constants.MAX_LENGTH_TEXT_SUBJECT)

    date = models.DateField(auto_now=True)

    message = ArrayField(models.ForeignKey("self"))
