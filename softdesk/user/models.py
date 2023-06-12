from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UserTest(models.Model):

    Test_FirstName = models.CharField(max_length=30)
    Test_LastName = models.CharField(max_length=30)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AccountManager(User):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    '''
    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account
    '''

