from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    query = models.TextField(max_length=150)
    date = models.DateField()

    def __str__(self):
        return self.email
