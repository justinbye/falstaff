from django.db import models

class orgs(models.Model):
    org_name = models.CharField(max_length=150)
    org_address_line_1 = models.CharField(max_length=100, null=True)
    org_address_line_2 = models.CharField(max_length=100, null=True)
    org_city = models.CharField(max_length=50, null=True)
    org_country = models.CharField(max_length=50, null=True)
    org_website = models.URLField(null=True)
    org_phone_fixed = models.CharField(max_length=25, null=True)
    org_phone_mobile = models.CharField(max_length=25, null=True)

    def __str__(self):
        return 'Organisation: {}'.format(self.org_name)
