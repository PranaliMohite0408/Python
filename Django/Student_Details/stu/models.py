from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    mob_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name