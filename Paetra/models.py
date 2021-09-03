from django.db import models

# Create your models here.
class Person (models.Model):
    Hair = models.CharField(null=True, blank=True, max_length=50)
    Complexion = models.CharField(null=True, blank=True, max_length=50)
    Height = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.Hair  