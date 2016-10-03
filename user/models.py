from django.db import models

class user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField
    phone = models.CharField(max_length=20)


