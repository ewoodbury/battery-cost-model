from django import forms
from .models import CellInput

class CellInputForm(forms.Form):
    #Need to fix the names to match names in model here.
    cell_name = forms.CharField(max_length=45)
    cell_type = forms.ChoiceField(choices = CellInput.CELL_TYPE_CHOICES)
    np_ratio = forms.FloatField(initial=1.02)
    electrode_length = forms.FloatField(initial=100)
    electrode_width = forms.FloatField(initial=5.5)
    cat_formula_id = forms.IntegerField(initial=1)
    cat_grav_capacity = forms.FloatField(initial=160)
    cat_total_loading = forms.FloatField(initial=25)
    cat_active_frac = forms.FloatField(initial=0.98)
    cat_binder_frac = forms.FloatField(initial=0.01)
    cat_conductor_frac = forms.FloatField(initial=0.01)
    an_grav_capacity = forms.FloatField(initial=360)
    an_active_frac = forms.FloatField(initial=0.98)
    an_binder_frac = forms.FloatField(initial=0.02)
    an_conductor_frac = forms.FloatField(initial=0)
    al_foil_thickness = forms.FloatField(initial=20)
    cu_foil_thickness = forms.FloatField(initial=10)
    elyte = forms.CharField(max_length=45, initial='1.2M LiPF6 in 1:1 EC:DMC')
    separator_name = forms.CharField(max_length=45, initial='Polypropylene, 20um thickness')
    can = forms.CharField(max_length=45, initial='Stainless steel 18650 can')
    avg_discharge_voltage = forms.FloatField(initial=3.6)
