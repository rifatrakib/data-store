from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models as gis_models
from django.db import models


class AutomobileRepairShop(models.Model):
    shop_id = models.CharField(_('shop number'), max_length=30, unique=True)
    business_name = models.CharField(_('name of the shop'), max_length=200, unique=True)
    business_address = models.CharField(_('full address'), max_length=500)
    city = models.CharField(_('city'), max_length=100)
    state = models.CharField(_('state'), max_length=100)
    zip_code = models.CharField(_('zip code'), max_length=10)
    license_num = models.CharField(_('license number'), max_length=100, unique=True)
    license_type = models.CharField(_('license type'), max_length=100)
    license_expiration = models.DateField(_('license expiration date'))
    location = gis_models.PointField(_('geographic coordinate'), srid=4326)
    
    def __str__(self):
        return self.business_name
