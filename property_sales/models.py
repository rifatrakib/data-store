from django.utils.translation import gettext_lazy as _
# from django.contrib.gis.db import models as gis_models
from django.db import models


class SalesRecord(models.Model):
    class PropertyTypeChoices(models.TextChoices):
        SINGLE_FAMILY = 'Single Family', _('Single Family')
        CONDO = 'Condo', _('Condo')
    
    class ResidentialTypeChoices(models.TextChoices):
        SINGLE_FAMILY = 'Single Family', _('Single Family')
        CONDO = 'Condo', _('Condo')
    
    serial_number = models.IntegerField(_('serial number'))
    list_year = models.IntegerField(_('year of sale'))
    date_recorded = models.DateTimeField(_('timestamp of sale'))
    town = models.CharField(_('town of the property'), max_length=100)
    address = models.CharField(_('address of the property'), max_length=250)
    assessed_value = models.DecimalField(_('estimated value'), decimal_places=2)
    sales_amount = models.DecimalField(_('sales amount'), decimal_places=2)
    sales_ratio = models.DecimalField(_('ratio of sales amount and estimated value'), decimal_places=4)
    property_type = models.CharField(_('type of property'), max_length=50, choices=PropertyTypeChoices)
    residential_type = models.CharField(_('genre of residence'), max_length=50, choices=ResidentialTypeChoices)
    non_use_code = models.CharField(_('use state code'), max_length=50)
    assessor_remarks = models.CharField(_('professional remarks'), max_length=1000)
    opm_remarks = models.CharField(_('official comment'), max_length=1000)
    # location = gis_models.PointField(_('geographic coordinate'))
