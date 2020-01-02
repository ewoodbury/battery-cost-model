from django.db import models

# Create your models here.
class PriceInput(models.Model):
    priceid = models.AutoField(db_column='priceId', primary_key=True)  # Field name made lowercase.
    catactivematerial = models.FloatField(db_column='catActiveMaterial', blank=True, null=True)  # Field name made lowercase.
    catbinder = models.FloatField(db_column='catBinder', blank=True, null=True)  # Field name made lowercase.
    catconductor = models.FloatField(db_column='catConductor', blank=True, null=True)  # Field name made lowercase.
    anactivematerial = models.FloatField(db_column='anActiveMaterial', blank=True, null=True)  # Field name made lowercase.
    anbinder = models.FloatField(db_column='anBinder', blank=True, null=True)  # Field name made lowercase.
    anconductor = models.FloatField(db_column='anConductor', blank=True, null=True)  # Field name made lowercase.
    alfoil = models.FloatField(db_column='alFoil', blank=True, null=True)  # Field name made lowercase.
    cufoil = models.FloatField(db_column='cuFoil', blank=True, null=True)  # Field name made lowercase.
    can = models.FloatField(blank=True, null=True)
    sep = models.FloatField(blank=True, null=True)
    elyte = models.FloatField(blank=True, null=True)
    cellmanufacturing = models.FloatField(db_column='cellManufacturing', blank=True, null=True)  # Field name made lowercase.
    packintegration = models.FloatField(db_column='packIntegration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'price_input'
