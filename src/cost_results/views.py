from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import RunModelForm
from .cost_model_class import CostModel
# from cells.models import CellInput
# from prices.models import PriceInput

def run_model(request):
    '''Renders view of dropdown menus to select the cell_id
    and price_id with which to create a cost model.

    Also will add a default plot showing some data
    '''
    if request.method == 'POST':
        my_form = RunModelForm(request.POST)
        print('Reached POST code block')
        if my_form.is_valid():
            cell_instance = my_form.cleaned_data['cell_choice']
            price_instance = my_form.cleaned_data['price_choice']
            print(type(my_form.cleaned_data['cell_choice'].avg_discharge_voltage))
            # print(my_form.cleaned_data['price_choice'])
            cost_model_instance = CostModel(cell_instance, price_instance)
            #NEED TO FIX DECIMALS VS FLOATS WTF
            cost_model_instance.run_full_model()
            print(cost_model_instance.cellsPerKwh)

            return HttpResponseRedirect(reverse('run_model_confirm'))

    else: #initial render
        my_form = RunModelForm() #blank form

    context = {
        'my_form':my_form
    }
    return render(request, "run_model.html", context)




def run_model_confirm(request):
    context = {}
    return render(request, 'run_model_confirm.html', context)