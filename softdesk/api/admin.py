from django.contrib import admin

# Register your models here.
from .models import Person, ModelTest, Projects, Contributor, Issue , Comment
admin.site.register(Person)
admin.site.register(ModelTest)
admin.site.register(Projects)
admin.site.register(Contributor)
admin.site.register(Issue)
admin.site.register(Comment)