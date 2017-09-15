#django components
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User (AbstractBaseUser):
    '''
        Abstract User.
    '''

    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
