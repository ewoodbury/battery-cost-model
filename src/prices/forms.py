from django import forms
# from .forms import PriceInput

class PriceInputForm(forms.Form):
    #Need to fix the names to match names in model here.
    cat_active_material = forms.FloatField()
    cat_binder = forms.FloatField()
    cat_conductor = forms.FloatField()
    an_active_material = forms.FloatField()
    an_binder = forms.FloatField()
    an_conductor = forms.FloatField()
    al_foil = forms.FloatField( )
    cu_foil = forms.FloatField()
    can = forms.FloatField()
    sep = forms.FloatField()
    elyte = forms.FloatField()
    cell_manufacturing = forms.FloatField()
    pack_integration = forms.FloatField()