from django.db import models

# Create your models here.
class Person(models.Model):
    person_FirstName = models.CharField(max_length=30)
    person_LastName = models.CharField(max_length=30)

class ModelTest(models.Model):
    Test_FirstName = models.CharField(max_length=30)
    Test_LastName = models.CharField(max_length=30)