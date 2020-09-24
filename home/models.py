from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()