from django.db import models

class user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField
    phone = models.CharField(max_length=20)

    def __str__(self):
        return 'User: {}'.format(self.first_name)


