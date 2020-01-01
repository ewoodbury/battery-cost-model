# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CellInput(models.Model):
    cellid = models.IntegerField(db_column='cellId', primary_key=True)  # Field name made lowercase.
    cellname = models.CharField(db_column='cellName', unique=True, max_length=45)  # Field name made lowercase.
    celltype = models.CharField(db_column='cellType', max_length=45)  # Field name made lowercase.
    npratio = models.FloatField(db_column='npRatio')  # Field name made lowercase.
    electrodelength = models.FloatField(db_column='electrodeLength')  # Field name made lowercase.
    electrodewidth = models.FloatField(db_column='electrodeWidth')  # Field name made lowercase.
    catformulaid = models.IntegerField(db_column='catFormulaId', blank=True, null=True)  # Field name made lowercase.
    catgravcapacity = models.FloatField(db_column='catGravCapacity')  # Field name made lowercase.
    cattotalloading = models.FloatField(db_column='catTotalLoading')  # Field name made lowercase.
    catactivefrac = models.FloatField(db_column='catActiveFrac')  # Field name made lowercase.
    catbinderfrac = models.FloatField(db_column='catBinderFrac')  # Field name made lowercase.
    catconductorfrac = models.FloatField(db_column='catConductorFrac')  # Field name made lowercase.
    angravcapacity = models.FloatField(db_column='anGravCapacity')  # Field name made lowercase.
    anactivefrac = models.FloatField(db_column='anActiveFrac')  # Field name made lowercase.
    anbinderfrac = models.FloatField(db_column='anBinderFrac')  # Field name made lowercase.
    anconductorfrac = models.FloatField(db_column='anConductorFrac')  # Field name made lowercase.
    alfoilthickness = models.FloatField(db_column='alFoilThickness')  # Field name made lowercase.
    cufoilthickness = models.FloatField(db_column='cuFoilThickness')  # Field name made lowercase.
    elyte = models.CharField(max_length=45, blank=True, null=True)
    separatorname = models.CharField(db_column='separatorName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    can = models.CharField(max_length=45, blank=True, null=True)
    avgdischargevoltage = models.FloatField(db_column='avgDischargeVoltage')  # Field name made lowercase.

    class Meta:
        # managed = True
        db_table = 'cell_input'


class PriceInput(models.Model):
    priceid = models.IntegerField(db_column='priceId', primary_key=True)  # Field name made lowercase.
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
        # managed = Trues
        db_table = 'price_input'
