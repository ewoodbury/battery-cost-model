import plotly.graph_objs as go
from plotly.offline import plot
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import RunModelForm
from .load_model_results import load_model_results
from .models import CostResultsInfo, CostResultsCell, CostResultsKwh


def run_model(request):
    '''Renders view of dropdown menus to select the cell_id
    and price_id with which to create a cost model.
    '''
    if request.method == 'POST':
        my_form = RunModelForm(request.POST)
        print('Reached POST code block')
        if my_form.is_valid():
            load_data = load_model_results(
                my_form.cleaned_data['cell_choice'],
                my_form.cleaned_data['price_choice'],
            )
            # print(load_data) #Should print "Results loaded successfully!"
            # Getting latest model_id by querying db with latest:
            this_model_id = CostResultsInfo.objects.latest('model_id').model_id
            # Redirecting to the view_model page for the model that was just calculated:
            return HttpResponseRedirect(reverse('view_model', kwargs={'model_id_input': this_model_id}))
    
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


def view_model(request, model_id_input):
    #First, retrieve items as queryset object:
    query_result_info = CostResultsInfo.objects.filter(model_id=model_id_input)
    query_result_cell = CostResultsCell.objects.filter(model_id=model_id_input)
    query_result_kwh = CostResultsKwh.objects.filter(model_id=model_id_input)
    print(type(query_result_kwh.values()))  # queryset
    print(type(query_result_kwh.values()[0]))  # dict

    dict_plot_kwh = process_queryset(query_result_kwh)
    # fig = go.Figure()
    # print(pd.DataFrame.from_dict(query_result_kwh.values()))
    data = go.Pie(
        labels=list(dict_plot_kwh.keys()),
        values=list(dict_plot_kwh.values()),
        hovertemplate='%{label} <br> <i>Price</i>: $%{value:.2f}'
    )
    layout = go.Layout(
        autosize=False,
        width=1000,
        height=600,
        title='Cost Breakdown (USD/kWh)',
        title_x=0.5
    )

    fig = go.Figure(data=data, layout=layout)
    plt_div = plot(fig, output_type='div',include_plotlyjs=False)

    context = {
        'query_result_info': query_result_info[0],
        'plt_div': plt_div,
    }
    return render(request, 'view_model.html', context)


def process_queryset(queryset):
    '''Takes a Django queryset and returns a dictionary of values to be plotted.
    The function removes the model_id field and combines values comprising 
    less than x% of the total cost into an 'Other' category.
    '''
    dict_data = queryset.values()[0]
    del dict_data['model_id']
    # Looping through dict to get total cost:
    total_cost = 0
    for i in dict_data:
        total_cost += dict_data[i]

    # Combining small elements into 'Other' category
    fraction = 0.01  # Will filter elements with <1% of total cost
    new_dict_data = {}
    total_other = 0
    for j in dict_data:
        if dict_data[j] < (fraction * total_cost):
            total_other += dict_data[j]
        else:
            new_dict_data[j] = dict_data[j]
    new_dict_data['Other'] = total_other
    return new_dict_data
