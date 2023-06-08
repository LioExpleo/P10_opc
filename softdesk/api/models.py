from django.db import models

# Create your models here.
class Person(models.Model):
    person_FirstName = models.CharField(max_length=30)
    person_LastName = models.CharField(max_length=30)

class ModelTest(models.Model):
    Test_FirstName = models.CharField(max_length=30)
    Test_LastName = models.CharField(max_length=30)
    active = models.BooleanField(default=False)

    def __str__(self):
        return (self.Test_LastName, self.Test_LastName, self.pk, self.active)
