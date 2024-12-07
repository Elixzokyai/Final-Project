from django.db import models

# Create your models here.

class ApplicationUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    SpecifyAccount = models.CharField(max_length=50)
    numberOfFollowers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    socialMediaLink = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.email}, {self.SpecifyAccount},{self.numberOfFollowers}, {self.following}, {self.socialMediaLink}"




