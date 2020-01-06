from django.db import models

# Create your models here.
class PriceInput(models.Model):
    price_id = models.AutoField(db_column='priceId', primary_key=True)
    price_name = models.CharField(db_column='priceName', max_length=45)
    cat_active_material = models.FloatField(db_column='catActiveMaterial')
    cat_binder = models.FloatField(db_column='catBinder')
    cat_conductor = models.FloatField(db_column='catConductor')
    an_active_material = models.FloatField(db_column='anActiveMaterial')
    an_binder = models.FloatField(db_column='anBinder')
    an_conductor = models.FloatField(db_column='anConductor')
    al_foil = models.FloatField(db_column='alFoil')
    cu_foil = models.FloatField(db_column='cuFoil')
    can = models.FloatField()
    sep = models.FloatField()
    elyte = models.FloatField()
    cell_manufacturing = models.FloatField(db_column='cellManufacturing')
    pack_integration = models.FloatField(db_column='packIntegration')

    def __str__(self):
        return str(self.price_id) + " - " + self.price_name

    class Meta:
        managed = True
        db_table = 'price_input'
