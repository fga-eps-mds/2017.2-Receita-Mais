from django.db import models


class ActivePrinciple(models.Model):
    name = models.CharField(max_length=100)
