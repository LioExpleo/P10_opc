from django.contrib import admin

# Register your models here.
from .models import Person, ModelTest, Projects
admin.site.register(Person)
admin.site.register(ModelTest)
admin.site.register(Projects)