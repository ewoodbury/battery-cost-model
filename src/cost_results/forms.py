from django import forms
from .models import CostResultsInfo, CostResultsCell, CostResultsKwh
from cells.models import CellInput
from prices.models import PriceInput

class RunModelForm(forms.Form):
    '''Form on the default run_model page. Includes a dropdown box to select 
    the desired cell and price input.
    '''
    # cell_options = CellInput.objects.all()
    # price_options = PriceInput.objects.all()

    cell_choice = forms.ModelChoiceField(
        queryset=CellInput.objects.all(), 
        # help_text = '(Cells displayed as cell_id - cell_name)'
        )
    price_choice = forms.ModelChoiceField(
        queryset=PriceInput.objects.all(),
        # help_text = '(Prices displayed as price_id - price_name)'
        )

