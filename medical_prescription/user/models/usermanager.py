# Django
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email),
                          password=password,
                          is_active=False,
                          **extra_fields)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.model(email=self.normalize_email(email),
                          password=password,
                          is_active=True,
                          is_staff=True,
                          is_superuser=True,
                          **extra_fields)

        user.set_password(password)
        user.save(using=self.db)

        return user
