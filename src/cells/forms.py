from django import forms
from .models import CellInput

class CellInputForm(forms.Form):
    #Need to fix the names to match names in model here.
    cell_name = forms.CharField(max_length=45)
    cell_type = forms.CharField(max_length=45)
    np_ratio = forms.DecimalField(max_digits=20, decimal_places=3)
    electrode_length = forms.DecimalField(max_digits=20, decimal_places=3)
    electrode_width = forms.DecimalField(max_digits=20, decimal_places=3)
    cat_formula_id = forms.IntegerField()
    cat_grav_capacity = forms.DecimalField(max_digits=20, decimal_places=2)
    cat_total_loading = forms.DecimalField(max_digits=20, decimal_places=2)
    cat_active_frac = forms.DecimalField(max_digits=20, decimal_places=4)
    cat_binder_frac = forms.DecimalField(max_digits=20, decimal_places=4)
    cat_conductor_frac = forms.DecimalField(max_digits=20, decimal_places=4)
    an_grav_capacity = forms.DecimalField(max_digits=20, decimal_places=2)
    an_active_frac = forms.DecimalField(max_digits=20, decimal_places=4)
    an_binder_frac = forms.DecimalField(max_digits=20, decimal_places=4)
    an_conductor_frac = forms.DecimalField(max_digits=20, decimal_places=4)
    al_foil_thickness = forms.DecimalField(max_digits=20, decimal_places=2)
    cu_foil_thickness = forms.DecimalField(max_digits=20, decimal_places=2)
    elyte = forms.CharField(max_length=45)
    separator_name = forms.CharField(max_length=45)
    can = forms.CharField(max_length=45)
    avg_discharge_voltage = forms.DecimalField(max_digits=20, decimal_places=3)
