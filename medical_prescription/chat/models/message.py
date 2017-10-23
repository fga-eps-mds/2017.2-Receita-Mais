from django.db import models
from user.models import User
from chat import constants


class Message(models.Model):

    # TODO (Felipe) add file field and IMAGE (PIL).

    user_from = models.ForeignKey(User, related_name="user_from")
    user_to = models.ForeignKey(User, related_name="user_to")

    text = models.CharField(max_length=constants.MAX_LENGTH_TEXT_MESSAGE)
    subject = models.CharField(max_length=constants.MAX_LENGTH_TEXT_SUBJECT)

    date = models.DateField(auto_now=True)
