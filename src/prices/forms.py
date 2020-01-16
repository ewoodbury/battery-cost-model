from django import forms
# from .forms import PriceInput

class PriceInputForm(forms.Form):
    #Need to fix the names to match names in model here.
    price_name = forms.CharField(max_length=45)
    cat_active_material = forms.FloatField(initial=50)
    cat_binder = forms.FloatField(initial=10)
    cat_conductor = forms.FloatField(initial=5)
    an_active_material = forms.FloatField(initial=20)
    an_binder = forms.FloatField(initial=10)
    an_conductor = forms.FloatField(initial=5)
    al_foil = forms.FloatField(initial=5)
    cu_foil = forms.FloatField(initial=10)
    can = forms.FloatField(initial=0.2)
    sep = forms.FloatField(initial=60)
    elyte = forms.FloatField(initial=0.2)
    cell_manufacturing = forms.FloatField(initial=0.5)
    pack_integration = forms.FloatField(initial=0.4)