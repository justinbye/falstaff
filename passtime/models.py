from __future__ import unicode_literals

from django.db import models

class super_set(models.Model):
    category_type = models.CharField(max_length=100)
    category_description = models.CharField(max_length=1000)
    sport = models.CharField(max_length=100)


