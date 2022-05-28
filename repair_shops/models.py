from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models as gis_models
from django.db import models


class AutomobileRepairShop(models.Model):
    shop_number = models.CharField(_('shop number'), max_length=30, null=True, blank=True)
    business_name = models.CharField(_('name of the shop'), max_length=200, null=True, blank=True)
    business_address = models.CharField(_('full address'), max_length=500, null=True, blank=True)
    city = models.CharField(_('city'), max_length=100, null=True, blank=True)
    state = models.CharField(_('state'), max_length=100, null=True, blank=True)
    zip_code = models.CharField(_('zip code'), max_length=10, null=True, blank=True)
    license_num = models.CharField(_('license number'), max_length=100, null=True, blank=True)
    license_type = models.CharField(_('license type'), max_length=100, null=True, blank=True)
    license_expiration = models.DateField(_('license expiration date'), null=True, blank=True)
    location = gis_models.PointField(_('geographic coordinate'), srid=4326, null=True, blank=True)
    
    def __str__(self):
        return self.business_name
