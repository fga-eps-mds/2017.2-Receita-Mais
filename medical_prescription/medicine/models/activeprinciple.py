from django.db import models


class ActivePrinciple(models.Model):
    name = models.CharField(min_lenght=5, max_lenght=100)

    def __str__(self):
        return self.name
