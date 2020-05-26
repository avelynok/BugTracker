from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.
class MyUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    displayname = models.CharField(max_length=50, unique=True)

"""
Title
Time / Date filed
Description
Name of user who filed ticket
Status of ticket (New / In Progress / Done / Invalid)
Name of user assigned to ticket
Name of user who completed the ticket
"""
    

class Bug(models.Model):
    #https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices
    #https://stackoverflow.com/questions/4604814/django-model-field-default-to-null
    NEW = 'New'
    IN_PROGRESS = 'In Progress'
    DONE = 'Done'
    INVALID = 'Invalid'
    TICKET_STATUS = [
        (NEW, 'New'),
        (IN_PROGRESS,'In Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid')
    ]
    
    title = models.CharField(max_length=30)
    time = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author = models.ForeignKey(get_user_model(), related_name='author', null=True, blank=True, default=None, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default=NEW, choices=TICKET_STATUS)
    assigned_to = models.ForeignKey(get_user_model(), related_name='assigned_to', null=True, blank=True, default=None, on_delete=models.CASCADE)
    completed_by = models.ForeignKey(get_user_model(), related_name='completed_by', null=True, blank=True, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    