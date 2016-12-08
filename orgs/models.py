from django.db import models

class user(models.Model):
    org_name = models.CharField(max_length=150)
    org_address_line_1 = models.CharField(max_length=100)
    org_address_line_2 = models.CharField(max_length=100)
    org_city = models.CharField(max_length=50)
    org_country = models.CharField(max_length=50)
    org_website = models.URLField
    org_phone_fixed = models.CharField(max_length=25)
    org_phone_mobile = models.CharField(max_length=25)

    def __str__(self):
        return 'Organisation: {}'.format(self.org_name)
