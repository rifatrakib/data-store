from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models as gis_models
from django.db import models


class SalesRecord(models.Model):
    class PropertyTypeChoices(models.TextChoices):
        SINGLE_FAMILY = 'Single Family', _('Single Family')
        CONDO = 'Condo', _('Condo')
    
    class ResidentialTypeChoices(models.TextChoices):
        SINGLE_FAMILY = 'Single Family', _('Single Family')
        CONDO = 'Condo', _('Condo')
    
    sales_number = models.CharField(_('sales identifier'), max_length=50, blank=True, null=True)
    serial_number = models.CharField(_('serial number'), max_length=20, blank=True, null=True)
    list_year = models.CharField(_('year of sale'), max_length=10, blank=True, null=True)
    date_recorded = models.DateTimeField(_('timestamp of sale'), blank=True, null=True)
    town = models.CharField(_('town of the property'), max_length=100, blank=True, null=True)
    address = models.CharField(_('address of the property'), max_length=250, blank=True, null=True)
    assessed_value = models.CharField(_('estimated value'), max_length=20, blank=True, null=True)
    sales_amount = models.CharField(_('sales amount'), max_length=20, blank=True, null=True)
    sales_ratio = models.CharField(_('ratio of sales amount and estimated value'), max_length=20, blank=True, null=True)
    property_type = models.CharField(_('type of property'), max_length=50, choices=PropertyTypeChoices.choices, blank=True, null=True)
    residential_type = models.CharField(_('genre of residence'), max_length=50, choices=ResidentialTypeChoices.choices, blank=True, null=True)
    non_use_code = models.CharField(_('use state code'), max_length=50, blank=True, null=True)
    assessor_remarks = models.CharField(_('professional remarks'), max_length=1000, blank=True, null=True)
    opm_remarks = models.CharField(_('official comment'), max_length=1000, blank=True, null=True)
    location = gis_models.PointField(_('geographic coordinate'), srid=4326, blank=True, null=True)
    
    def __str__(self):
        return self.address
