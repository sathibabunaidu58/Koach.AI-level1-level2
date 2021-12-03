from django.db import models

# Create your models here.
class Register(models.Model):
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    def __str__(self):
        return self.email
