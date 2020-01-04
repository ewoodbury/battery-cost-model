from django.db import models

# Create your models here.
class CostResultsInfo(models.Model):
    '''Stores data on date model was created, version of model used, and cell_id
    and price_id that were plugged into the model.
    '''
    model_id = models.AutoField(primary_key=True)
    model_version = models.DecimalField(max_digits=20, decimal_places=2)
    date_created = models.DateTimeField()
    cell_id = models.PositiveIntegerField()
    price_id = models.PositiveIntegerField()

class CostResultsCell(models.Model):
    '''This class stores the cost per cell data for a given model_id
    '''
    model_id = models.AutoField(primary_key=True)
    #not sure if model_id here should be autofield or not
    cat_active_material = models.DecimalField(max_digits=20, decimal_places=2)
    cat_binder = models.DecimalField(max_digits=20, decimal_places=2)
    cat_conductor = models.DecimalField(max_digits=20, decimal_places=2)
    an_active_material = models.DecimalField(max_digits=20, decimal_places=2)
    an_binder = models.DecimalField(max_digits=20, decimal_places=2)
    an_conductor = models.DecimalField(max_digits=20, decimal_places=2)
    al_foil = models.DecimalField(max_digits=20, decimal_places=2)
    cu_foil = models.DecimalField(max_digits=20, decimal_places=2)
    can = models.DecimalField(max_digits=20, decimal_places=2)
    sep = models.DecimalField(max_digits=20, decimal_places=2)
    elyte = models.DecimalField(max_digits=20, decimal_places=2)
    manufacturing = models.DecimalField(max_digits=20, decimal_places=2)
    pack_integration = models.DecimalField(max_digits=20, decimal_places=2)


    class Meta:
        managed = True
        db_table = 'cost_results_cell'

class CostResultsKwh(models.Model):
    '''This class stores the cost per kWh data for a given model_id
    '''
    model_id = models.AutoField(primary_key=True)
    cat_active_material = models.DecimalField(max_digits=20, decimal_places=2)
    cat_binder = models.DecimalField(max_digits=20, decimal_places=2)
    cat_conductor = models.DecimalField(max_digits=20, decimal_places=2)
    an_active_material = models.DecimalField(max_digits=20, decimal_places=2)
    an_binder = models.DecimalField(max_digits=20, decimal_places=2)
    an_conductor = models.DecimalField(max_digits=20, decimal_places=2)
    al_foil = models.DecimalField(max_digits=20, decimal_places=2)
    cu_foil = models.DecimalField(max_digits=20, decimal_places=2)
    can = models.DecimalField(max_digits=20, decimal_places=2)
    sep = models.DecimalField(max_digits=20, decimal_places=2)
    elyte = models.DecimalField(max_digits=20, decimal_places=2)
    manufacturing = models.DecimalField(max_digits=20, decimal_places=2)
    pack_integration = models.DecimalField(max_digits=20, decimal_places=2)


    class Meta:
        managed = True
        db_table = 'cost_results_kwh'