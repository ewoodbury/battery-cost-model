from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import RunModelForm
from .load_model_results import load_model_results
from .models import CostResultsInfo, CostResultsCell, CostResultsKwh

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
        query_results = CostResultsInfo.objects.all()

    context = {
        'my_form': my_form,
        'query_results': query_results,
    }
    return render(request, "run_model.html", context)


def run_model_confirm(request):
    context = {}
    return render(request, 'run_model_confirm.html', context)

import numpy as np
import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px

def view_model(request, model_id_input):
    query_result_info = CostResultsInfo.objects.filter(model_id=model_id_input)
    query_result_cell = CostResultsCell.objects.filter(model_id=model_id_input)
    query_result_kwh = CostResultsKwh.objects.filter(model_id=model_id_input)
    print(list(query_result_kwh.values()))

    # fig = go.Figure()
    # print(pd.DataFrame.from_dict(query_result_kwh.values()))
    fig = px.pie(pd.DataFrame.from_dict(query_result_kwh.values()))
    # fig.add_trace(pie)
    plt_div = plot(fig, output_type='div', include_plotlyjs=False)

    context = {
        'query_result_info': query_result_info[0],
        'plt_div':plt_div,
    }
    return render(request, 'view_model.html', context)
