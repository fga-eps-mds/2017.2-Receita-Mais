from django.db import models

#  This class create objects generals active principle


class ActivePrinciple(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
