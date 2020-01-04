from django.shortcuts import render

import sys
sys.path.append('..')

from cells.models import CellInput
from prices.models import PriceInput

# Create your views here.
def run_model(request):
    '''Renders view of dropdown menus to select the cell_id
    and price_id with which to create a cost model.

    Also will add a default plot showing some data
    '''
    cell_options = CellInput.objects.all()
    price_options = PriceInput.objects.all()
    context = {
        'cell_options': cell_options,
        'price_options': price_options,
    }
    return render(request, "run_model.html", context)