from django.db import models
from django.contrib.auth.models import User


TYPE_CHOICES = [('back-end', 'back-end'), ('front-end', 'front-end'), ('IOS', 'IOS'), ('android', 'android')]
PERMISSION_CHOICES = [('CRUD', 'CRUD'), ('CR', 'CR')]
TAG_CHOICES = [('bug', 'bug'), ('tâche', 'tâche'), ('amélioration', 'amélioration')]
STATUS_CHOICES = [('à faire', 'à faire'), ('en cours', 'en cours'), ('terminé', 'terminé')]
PRIORITY_CHOICES = [('faible', 'faible'), ('moyenne', 'moyenne'), ('élevée', 'élevée')]
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

class Projects(models.Model):
    project_id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField('Project title', max_length=100)
    description = models.CharField('Project description', max_length=200)
    type = models.CharField('Project Type', max_length=50, choices=TYPE_CHOICES)
    author_user_id = models.ForeignKey(to=User,
                                       default=None,
                                       on_delete=models.CASCADE,
                                       blank=True,
                                       null=False,
                                       )
    '''
    contributors = models.ManyToManyField(to=User,
                                          through='Contributor',
                                          blank=True,
                                          related_name='contributors')
    '''
class Contributor(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True)
    project_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE, blank=True)
    permission = models.CharField(max_length=100, choices=PERMISSION_CHOICES)
    role = models.CharField(max_length=100)



class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    project_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE, related_name='issues')
    status = models.CharField(max_length=150, choices=STATUS_CHOICES)
    author_user_id = models.ForeignKey(to=User,
                                       on_delete=models.CASCADE,
                                       related_name='author_user_id',
                                       blank=True)
    assignee_user_id = models.ForeignKey(to=User,
                                         default=author_user_id,
                                         on_delete=models.CASCADE,
                                         related_name='assignee_user_id',
                                         blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment_id = models.AutoField(auto_created=True, primary_key=True)
    description = models.CharField(max_length=200)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE, related_name='comments')
    created_time = models.DateTimeField(auto_now_add=True)