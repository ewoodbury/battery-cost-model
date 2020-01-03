from django.db import models

# Create your models here.
class PriceInput(models.Model):
    priceid = models.AutoField(db_column='priceId', primary_key=True)
    catactivematerial = models.DecimalField(db_column='catActiveMaterial', max_digits=20, decimal_places=2)
    catbinder = models.DecimalField(db_column='catBinder', max_digits=20, decimal_places=2)
    catconductor = models.DecimalField(db_column='catConductor', max_digits=20, decimal_places=2)
    anactivematerial = models.DecimalField(db_column='anActiveMaterial', max_digits=20, decimal_places=2)
    anbinder = models.DecimalField(db_column='anBinder', max_digits=20, decimal_places=2)
    anconductor = models.DecimalField(db_column='anConductor', max_digits=20, decimal_places=2)
    alfoil = models.DecimalField(db_column='alFoil', max_digits=20, decimal_places=2)
    cufoil = models.DecimalField(db_column='cuFoil', max_digits=20, decimal_places=2)
    can = models.DecimalField(max_digits=20, decimal_places=2)
    sep = models.DecimalField(max_digits=20, decimal_places=2)
    elyte = models.DecimalField(max_digits=20, decimal_places=2)
    cellmanufacturing = models.DecimalField(db_column='cellManufacturing', max_digits=20, decimal_places=2)
    packintegration = models.DecimalField(db_column='packIntegration', max_digits=20, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'price_input'
