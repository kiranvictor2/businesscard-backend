from django.db import models

# Create your models here.

class BusinessCard(models.Model):
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    website = models.URLField()
    profession = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name