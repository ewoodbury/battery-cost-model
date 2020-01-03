from django import forms
# from .forms import PriceInput

class PriceInputForm(forms.Form):
    #Need to fix the names to match names in model here.
    catactivematerial = forms.DecimalField(max_digits=20, decimal_places=2)
    catbinder = forms.DecimalField(max_digits=20, decimal_places=2)
    catconductor = forms.DecimalField(max_digits=20, decimal_places=2)
    anactivematerial = forms.DecimalField(max_digits=20, decimal_places=2)
    anbinder = forms.DecimalField(max_digits=20, decimal_places=2)
    anconductor = forms.DecimalField(max_digits=20, decimal_places=2)
    alfoil = forms.DecimalField( max_digits=20, decimal_places=2)
    cufoil = forms.DecimalField(max_digits=20, decimal_places=2)
    can = forms.DecimalField(max_digits=20, decimal_places=2)
    sep = forms.DecimalField(max_digits=20, decimal_places=2)
    elyte = forms.DecimalField(max_digits=20, decimal_places=2)
    cellmanufacturing = forms.DecimalField(max_digits=20, decimal_places=2)
    packintegration = forms.DecimalField(max_digits=20, decimal_places=2)