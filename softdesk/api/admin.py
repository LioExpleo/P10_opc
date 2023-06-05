from django.contrib import admin

# Register your models here.
from .models import Person, ModelTest
admin.site.register(Person)
admin.site.register(ModelTest)