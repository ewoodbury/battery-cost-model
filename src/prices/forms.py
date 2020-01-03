from django import forms
# from .forms import PriceInput

class PriceInputForm(forms.Form):
    #Need to fix the names to match names in model here.
    cat_active_material = forms.DecimalField(max_digits=20, decimal_places=2)
    cat_binder = forms.DecimalField(max_digits=20, decimal_places=2)
    cat_conductor = forms.DecimalField(max_digits=20, decimal_places=2)
    an_active_material = forms.DecimalField(max_digits=20, decimal_places=2)
    an_binder = forms.DecimalField(max_digits=20, decimal_places=2)
    an_conductor = forms.DecimalField(max_digits=20, decimal_places=2)
    al_foil = forms.DecimalField( max_digits=20, decimal_places=2)
    cu_foil = forms.DecimalField(max_digits=20, decimal_places=2)
    can = forms.DecimalField(max_digits=20, decimal_places=2)
    sep = forms.DecimalField(max_digits=20, decimal_places=2)
    elyte = forms.DecimalField(max_digits=20, decimal_places=2)
    cell_manufacturing = forms.DecimalField(max_digits=20, decimal_places=2)
    pack_integration = forms.DecimalField(max_digits=20, decimal_places=2)