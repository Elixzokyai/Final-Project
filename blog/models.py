from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    Amount = MoneyField(max_digits=10, default=0, decimal_places=2, default_currency='USD')
    Requirements= models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}, {self.description}, {self.Amount}, {self.Requirements}"






