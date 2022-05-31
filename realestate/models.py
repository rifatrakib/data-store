from django.utils.translation import gettext_lazy as _
from django.db import models


class Property(models.Model):
    property_number = models.IntegerField(_('Property Number'), blank=True, null=True)
    county_number = models.IntegerField(_('County Number'), blank=True, null=True)
    county_name = models.IntegerField(_('County Name'), blank=True, null=True)
    city_number = models.IntegerField(_('City Name'), blank=True, null=True)
    gnr = models.IntegerField(_('Cadastral Unit Number'), blank=True, null=True)
    bnr = models.IntegerField(_('Property Unit Number'), blank=True, null=True)
    fnr = models.IntegerField(_('Lease Number'), blank=True, null=True)
    snr = models.IntegerField(_('Unit Number'), blank=True, null=True)
    bruksnavn = models.CharField(_('Subfarm Name'), max_length=100, blank=True, null=True)
    antall_teiger = models.IntegerField(_('Number of plots'), blank=True, null=True)
    area = models.DecimalField(_('Property Area'), max_digits=15, decimal_places=4)
    arealkilde_nr = models.IntegerField(_('Source Number'), blank=True, null=True)
    arealkilde_navn = models.CharField(_('Source Name'), max_length=50, blank=True, null=True)
    natrings_kode = models.CharField(_('Industry Code'), blank=True, null=True)
    natrings_kode_navn = models.CharField(_('Industry Code Name'), max_length=50, blank=True, null=True)
    tinglyst = models.BooleanField(_('Written Contract Exists'), blank=True, null=True)
    sameie_teller = models.IntegerField(_('Number of co-ownership'), blank=True, null=True)
    sameie_nevner = models.IntegerField(_('Maximum allowed co-ownership'), blank=True, null=True)
    etablert_dato = models.IntegerField(_('Date of Establishment'), blank=True, null=True)
    etablert_aar = models.IntegerField(_('Year of Establishment'), blank=True, null=True)
    eiendomstype_kode = models.IntegerField(_('Property Type Code'), blank=True, null=True)
    eiendomstype_navn = models.CharField(_('Property Type'), max_length=30, blank=True, null=True)
    antall_bygninger = models.IntegerField(_('Number of Buildings'), blank=True, null=True)
    antall_addresser = models.IntegerField(_('Number of Addresses'), blank=True, null=True)
    lkoord_sys_nr = models.IntegerField(_('Coordinate System Number'), blank=True, null=True)
    lkoord_sys_navn = models.CharField(_('Coordinate System Name'), max_length=25, blank=True, null=True)
    lkooelokx = models.DecimalField(_('UTM X coordinate'), max_digits=30, decimal_places=10)
    lkooeloky = models.DecimalField(_('UTM Y coordinate'), max_digits=30, decimal_places=10)
    
    def __str__(self):
        return self.bruksnavn
