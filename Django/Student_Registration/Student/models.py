from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    mob_no = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

