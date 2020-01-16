from django.db import models
from cells.models import CellInput
from prices.models import PriceInput

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

    class Meta:
        managed = True
        db_table = 'cost_results_info'
    
    def __str__(self):
        query_cellinput = CellInput.objects.get(cell_id=self.cell_id)
        query_priceinput = PriceInput.objects.get(price_id=self.price_id)
        return f"Model ID {self.model_id}, {query_cellinput.cell_name} + {query_priceinput.price_name}"

class CostResultsCell(models.Model):
    '''This class stores the cost per cell data for a given model_id
    '''
    model_id = models.AutoField(primary_key=True)
    # model_id = models.OneToOneField(CostResultsInfo, on_delete=models.CASCADE)
    #not sure if model_id here should be autofield or not
    # Have to make sure this all works with float instead of decimal
    cat_active_material = models.FloatField()
    cat_binder = models.FloatField()
    cat_conductor = models.FloatField()
    an_active_material = models.FloatField()
    an_binder = models.FloatField()
    an_conductor = models.FloatField()
    al_foil = models.FloatField()
    cu_foil = models.FloatField()
    can = models.FloatField()
    sep = models.FloatField()
    elyte = models.FloatField()
    manufacturing = models.FloatField()
    pack_integration = models.FloatField()


    class Meta:
        managed = True
        db_table = 'cost_results_cell'

class CostResultsKwh(models.Model):
    '''This class stores the cost per kWh data for a given model_id
    '''
    model_id = models.AutoField(primary_key=True)
    # model_id = models.OneToOneField(CostResultsInfo, on_delete=models.CASCADE)
    cat_active_material = models.FloatField()
    cat_binder = models.FloatField()
    cat_conductor = models.FloatField()
    an_active_material = models.FloatField()
    an_binder = models.FloatField()
    an_conductor = models.FloatField()
    al_foil = models.FloatField()
    cu_foil = models.FloatField()
    can = models.FloatField()
    sep = models.FloatField()
    elyte = models.FloatField()
    manufacturing = models.FloatField()
    pack_integration = models.FloatField()


    class Meta:
        managed = True
        db_table = 'cost_results_kwh'