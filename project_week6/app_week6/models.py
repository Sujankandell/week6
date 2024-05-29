from django.db import models

# Create your models here.



from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Project Coordinator'),
        (2, 'Supervisor'),
        (3, 'Student'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

class Thesis(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    supervisor = models.ForeignKey(User, limit_choices_to={'user_type': 2}, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    students = models.ManyToManyField(User, related_name='theses', limit_choices_to={'user_type': 3})

class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, limit_choices_to={'user_type': 3})
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)
