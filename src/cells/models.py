from django.db import models

# Create your models here.
class CellInput(models.Model):
    #Might have to change these to separated by _ to behave with forms?
    cellid = models.AutoField(db_column='cellId', primary_key=True)
    cellname = models.CharField(db_column='cellName', unique=True, max_length=45)
    #Will change cellname to dropdown of options, still stored in db as str
    celltype = models.CharField(db_column='cellType', max_length=45)
    npratio = models.DecimalField(db_column='npRatio', max_digits=20, decimal_places=3)
    electrodelength = models.DecimalField(db_column='electrodeLength', max_digits=20, decimal_places=3)
    electrodewidth = models.DecimalField(db_column='electrodeWidth', max_digits=20, decimal_places=3)
    catformulaid = models.IntegerField(db_column='catFormulaId', blank=True, null=True)
    catgravcapacity = models.DecimalField(db_column='catGravCapacity', max_digits=20, decimal_places=2)
    cattotalloading = models.DecimalField(db_column='catTotalLoading', max_digits=20, decimal_places=2)
    catactivefrac = models.DecimalField(db_column='catActiveFrac', max_digits=20, decimal_places=4)
    catbinderfrac = models.DecimalField(db_column='catBinderFrac', max_digits=20, decimal_places=4)
    catconductorfrac = models.DecimalField(db_column='catConductorFrac', max_digits=20, decimal_places=4)
    angravcapacity = models.DecimalField(db_column='anGravCapacity', max_digits=20, decimal_places=2)
    anactivefrac = models.DecimalField(db_column='anActiveFrac', max_digits=20, decimal_places=4)
    anbinderfrac = models.DecimalField(db_column='anBinderFrac', max_digits=20, decimal_places=4)
    anconductorfrac = models.DecimalField(db_column='anConductorFrac', max_digits=20, decimal_places=4)
    alfoilthickness = models.DecimalField(db_column='alFoilThickness', max_digits=20, decimal_places=2)
    cufoilthickness = models.DecimalField(db_column='cuFoilThickness', max_digits=20, decimal_places=2)
    elyte = models.CharField(max_length=45, blank=True, null=True)
    separatorname = models.CharField(db_column='separatorName', max_length=45, blank=True, null=True)
    can = models.CharField(max_length=45, blank=True, null=True)
    avgdischargevoltage = models.DecimalField(db_column='avgDischargeVoltage', max_digits=20, decimal_places=3)

    class Meta:
        managed = True
        db_table = 'cell_input'