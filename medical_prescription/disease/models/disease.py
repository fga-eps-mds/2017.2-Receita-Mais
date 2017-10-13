# Django imports.
from django.db import models

# Local Django imports.
from disease import constants


# Model that defines diseases.
class Disease(models.Model):
    # Disease fields.
    id_cid_10 = models.CharField(max_length=constants.ID_CID_MAX_LENGTH, unique=True)
    description = models.CharField(max_length=constants.DESC_CID_MAX_LENGTH)

    def __str__(self):
        return self.description
