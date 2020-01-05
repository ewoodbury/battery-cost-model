from django.db import models

# Create your models here.
class CellInput(models.Model):
    #Might have to change these to separated by _ to behave with forms?
    cell_id = models.AutoField(db_column='cellId', primary_key=True)
    cell_name = models.CharField(db_column='cellName', max_length=45)
    #Will change cellname to dropdown of options, still stored in db as str
    CELL_TYPE_CHOICES = [
    ('18650', '18650'),
    ('2170', '2170'),
]
    cell_type = models.CharField(db_column='cellType', max_length=45, choices = CELL_TYPE_CHOICES, default = '18650')
    # np_ratio = models.DecimalField(db_column='npRatio', max_digits=20, decimal_places=3)
    # electrode_length = models.DecimalField(db_column='electrodeLength', max_digits=20, decimal_places=3)
    # electrode_width = models.DecimalField(db_column='electrodeWidth', max_digits=20, decimal_places=3)
    # cat_formula_id = models.IntegerField(db_column='catFormulaId', blank=True, null=True)
    # cat_grav_capacity = models.DecimalField(db_column='catGravCapacity', max_digits=20, decimal_places=2)
    # cat_total_loading = models.DecimalField(db_column='catTotalLoading', max_digits=20, decimal_places=2)
    # cat_active_frac = models.DecimalField(db_column='catActiveFrac', max_digits=20, decimal_places=4)
    # cat_binder_frac = models.DecimalField(db_column='catBinderFrac', max_digits=20, decimal_places=4)
    # cat_conductor_frac = models.DecimalField(db_column='catConductorFrac', max_digits=20, decimal_places=4)
    # an_grav_capacity = models.DecimalField(db_column='anGravCapacity', max_digits=20, decimal_places=2)
    # an_active_frac = models.DecimalField(db_column='anActiveFrac', max_digits=20, decimal_places=4)
    # an_binder_frac = models.DecimalField(db_column='anBinderFrac', max_digits=20, decimal_places=4)
    # an_conductor_frac = models.DecimalField(db_column='anConductorFrac', max_digits=20, decimal_places=4)
    # al_foil_thickness = models.DecimalField(db_column='alFoilThickness', max_digits=20, decimal_places=2)
    # cu_foil_thickness = models.DecimalField(db_column='cuFoilThickness', max_digits=20, decimal_places=2)
    # elyte = models.CharField(max_length=45, blank=True, null=True)
    # separator_name = models.CharField(db_column='separatorName', max_length=45, blank=True, null=True)
    # can = models.CharField(max_length=45, blank=True, null=True)
    # avg_discharge_voltage = models.DecimalField(db_column='avgDischargeVoltage', max_digits=20, decimal_places=3)
    np_ratio = models.FloatField(db_column='npRatio')
    electrode_length = models.FloatField(db_column='electrodeLength')
    electrode_width = models.FloatField(db_column='electrodeWidth')
    cat_formula_id = models.IntegerField(db_column='catFormulaId')
    cat_grav_capacity = models.FloatField(db_column='catGravCapacity')
    cat_total_loading = models.FloatField(db_column='catTotalLoading')
    cat_active_frac = models.FloatField(db_column='catActiveFrac')
    cat_binder_frac = models.FloatField(db_column='catBinderFrac')
    cat_conductor_frac = models.FloatField(db_column='catConductorFrac')
    an_grav_capacity = models.FloatField(db_column='anGravCapacity')
    an_active_frac = models.FloatField(db_column='anActiveFrac')
    an_binder_frac = models.FloatField(db_column='anBinderFrac')
    an_conductor_frac = models.FloatField(db_column='anConductorFrac')
    al_foil_thickness = models.FloatField(db_column='alFoilThickness')
    cu_foil_thickness = models.FloatField(db_column='cuFoilThickness')
    elyte = models.CharField(max_length=45, blank=True, null=True)
    separator_name = models.CharField(db_column='separatorName', max_length=45, blank=True, null=True)
    can = models.CharField(max_length=45, blank=True, null=True)
    avg_discharge_voltage = models.FloatField(db_column='avgDischargeVoltage')

    def __str__(self):
        return str(self.cell_id) + " - " + self.cell_name

    class Meta:
        managed = True
        db_table = 'cell_input'