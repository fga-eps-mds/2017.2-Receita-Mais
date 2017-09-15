# django components
from django.db import models
from django.db.models import EmailField
from django.contrib.auth.base_user import AbstractBaseUser


class Email(EmailField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 250
        kwargs['default'] = ''
        kwargs['unique'] = True
        super(EmailField, self).__init__(*args, **kwargs)


class Name(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 250
        kwargs['default'] = ''
        kwargs['unique'] = True
        super(models.CharField, self).__init__(*args, **kwargs)


class LastName(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 250
        kwargs['default'] = ''
        kwargs['unique'] = True
        super(models.CharField, self).__init__(*args, **kwargs)


class User (AbstractBaseUser):

    '''
    Abstract User.
'''
    USERNAME_FIELD = "email"

    name = Name()
    last_name = LastName()
    email = Email()
