from django.db import models


class AutomobileRepairShop(models.Model):
    shop_id = models.CharField(max_length=30, unique=True)
    business_name = models.CharField(max_length=200, unique=True)
    business_address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    license_num = models.CharField(max_length=100, unique=True)
    license_type = models.CharField(max_length=100)
    license_expiration = models.DateField()
