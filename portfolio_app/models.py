from django.db import models

# Create your models here.


class Message(models.Model):

    name = models.CharField(max_length=200, null=False, blank=False)
    subject = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    
    def __str__(self):
        return self.subject