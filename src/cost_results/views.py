from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import RunModelForm
from .load_model_results import load_model_results
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
            load_data = load_model_results(
                my_form.cleaned_data['cell_choice'],
                my_form.cleaned_data['price_choice'],
            )
            print(load_data)
            return HttpResponseRedirect(reverse('run_model_confirm'))
    else:  # initial render
        my_form = RunModelForm()  # blank form

    context = {
        'my_form': my_form
    }
    return render(request, "run_model.html", context)


def run_model_confirm(request):
    context = {}
    return render(request, 'run_model_confirm.html', context)
