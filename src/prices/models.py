from django.db import models

# Create your models here.
class PriceInput(models.Model):
    price_id = models.AutoField(db_column='priceId', primary_key=True)
    price_name = models.CharField(db_column='priceName', max_length=45)
    cat_active_material = models.DecimalField(db_column='catActiveMaterial', max_digits=20, decimal_places=2)
    cat_binder = models.DecimalField(db_column='catBinder', max_digits=20, decimal_places=2)
    cat_conductor = models.DecimalField(db_column='catConductor', max_digits=20, decimal_places=2)
    an_active_material = models.DecimalField(db_column='anActiveMaterial', max_digits=20, decimal_places=2)
    an_binder = models.DecimalField(db_column='anBinder', max_digits=20, decimal_places=2)
    an_conductor = models.DecimalField(db_column='anConductor', max_digits=20, decimal_places=2)
    al_foil = models.DecimalField(db_column='alFoil', max_digits=20, decimal_places=2)
    cu_foil = models.DecimalField(db_column='cuFoil', max_digits=20, decimal_places=2)
    can = models.DecimalField(max_digits=20, decimal_places=2)
    sep = models.DecimalField(max_digits=20, decimal_places=2)
    elyte = models.DecimalField(max_digits=20, decimal_places=2)
    cell_manufacturing = models.DecimalField(db_column='cellManufacturing', max_digits=20, decimal_places=2)
    pack_integration = models.DecimalField(db_column='packIntegration', max_digits=20, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'price_input'
