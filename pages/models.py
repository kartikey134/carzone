from django.db import models

# Create your models here.

class Team(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebookLink = models.URLField(max_length=100)
    twitterLink = models.URLField(max_length=100)
    googlePlusLink = models.URLField(max_length=100)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName
