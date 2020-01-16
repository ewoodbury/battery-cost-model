from django import forms
from cost_results.models import CostResultsInfo, CostResultsCell, CostResultsKwh
from cells.models import CellInput
from prices.models import PriceInput


class CompareForm(forms.Form):
    '''Form on the default compare page. Includes 5 dropdown boxes to select 
    the desired models to compare.
    '''

    model_choices = queryset=CostResultsInfo.objects.all()
    ID1 = forms.ModelChoiceField(model_choices)
    ID2 = forms.ModelChoiceField(model_choices, required=False)
    ID3 = forms.ModelChoiceField(model_choices, required=False)
    ID4 = forms.ModelChoiceField(model_choices, required=False)
    ID5 = forms.ModelChoiceField(model_choices, required=False)
    ID6 = forms.ModelChoiceField(model_choices, required=False)
