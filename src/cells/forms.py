from django import forms
from .models import CellInput

class CellInputForm(forms.Form):
    #Need to fix the names to match names in model here.
    cell_name = forms.CharField(max_length=45)
    cell_type = forms.ChoiceField(choices = CellInput.CELL_TYPE_CHOICES)
    np_ratio = forms.FloatField()
    electrode_length = forms.FloatField()
    electrode_width = forms.FloatField()
    cat_formula_id = forms.IntegerField()
    cat_grav_capacity = forms.FloatField()
    cat_total_loading = forms.FloatField()
    cat_active_frac = forms.FloatField()
    cat_binder_frac = forms.FloatField()
    cat_conductor_frac = forms.FloatField()
    an_grav_capacity = forms.FloatField()
    an_active_frac = forms.FloatField()
    an_binder_frac = forms.FloatField()
    an_conductor_frac = forms.FloatField()
    al_foil_thickness = forms.FloatField()
    cu_foil_thickness = forms.FloatField()
    elyte = forms.CharField(max_length=45)
    separator_name = forms.CharField(max_length=45)
    can = forms.CharField(max_length=45)
    avg_discharge_voltage = forms.FloatField()
