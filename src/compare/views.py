import plotly.graph_objs as go
from plotly.offline import plot
from django.shortcuts import render
from .forms import CompareForm
from cost_results.models import CostResultsInfo, CostResultsCell, CostResultsKwh
from cells.models import CellInput
from prices.models import PriceInput

def compare_view(request):
    '''Renders view with 5 dropdown menus allowing user to choose
    up to 6 cost models to view simultaneously. When submitted,
    plots a stacked bar chart for each model that was selected.
    '''
    if request.method == 'POST':
        my_form = CompareForm(request.POST)
        # print('Reached POST code block')
        if my_form.is_valid():
            selected_ids = []
            # Looping through each form item to store each selected model_id:
            for i in range(1,7): 
                if my_form.cleaned_data[f'ID{i}'] is not None: #if user selected an item for that field
                    if my_form.cleaned_data[f'ID{i}'].model_id not in selected_ids: #if model_id hasn't been added yet:
                        selected_ids.append(my_form.cleaned_data[f'ID{i}'].model_id) #appends that model_id to a list
            print(selected_ids)
            # Initializing variables for the main loop:
            display_names = []
            dict_kwh = CostResultsKwh.objects.filter(model_id=selected_ids[0]).values()[0]
            #Looping through fields of the kwh model to initialize empty dict:
            data_dict = {}
            for component in dict_kwh:
                data_dict[component] = []
            # Initialize dict to store totals for annotation labels:
            totals = {}

            # Loop through each selected model_id to process data into appropriate format:
            for model_id in selected_ids:
                # Running queries
                query_info = CostResultsInfo.objects.get(model_id=model_id)
                query_cellinput = CellInput.objects.get(cell_id=query_info.cell_id)
                query_priceinput = PriceInput.objects.get(price_id=query_info.price_id)
                dict_kwh = CostResultsKwh.objects.filter(model_id=model_id).values()[0] #processed into dict of values
                del dict_kwh['model_id'] #delete this so the id doesn't show up in costs

                # Creating list of display names, which are the labels for each bar:
                display_name = f"Model ID: {query_info.model_id} <br> Cell: {query_cellinput.cell_name} <br> Price: {query_priceinput.price_name}"
                display_names.append(display_name)

                # Loop through the components within a model, appending each value to the appropriate list
                for component in dict_kwh:
                    data_dict[component].append(dict_kwh[component])
                
                # Also calculate total cost to use for the annotations later:
                totals[query_info.model_id] = sum(dict_kwh.values())
            
            print(data_dict)
            # Now we have all of the necessary data in dictionary data_dict,
            # where the keys are cost components (i.e. cat_active_material) and
            # values are ordered lists of the costs, in order of the selected model_ids.

            # Plotting:
            fig = go.Figure()
            # Loop through cost components, adding a new trace each loop:
            for component in data_dict:
                fig.add_trace(go.Bar(
                    x=display_names, 
                    y=data_dict[component], 
                    name=component,
                    text=['%.2f'% elem for elem in data_dict[component]], #rounds to 2 decimals
                    textposition='auto',
                    width=.4,
                    hovertemplate='$%{y:.2f}'
                    ))
            
            # To add total labels for each bar, loop through selected_ids
            for i in range(len(selected_ids)):
                fig.add_annotation(
                    go.layout.Annotation(
                        x=display_names[i],
                        y=totals[selected_ids[i]],
                        text="Total: $" + str(round(totals[selected_ids[i]],2)),
                    )
                )
            #General graph formatting
            fig.update_layout(
                barmode='stack',
                yaxis=dict(title='USD/kWh',titlefont_size=16),
                autosize=False,
                width=225*len(selected_ids)+275, #auto-adjusts width based on # of models
                height=800,
            )
            plt_div = plot(fig, output_type='div',include_plotlyjs=False)

            context = {
                'my_form': my_form,
                'plt_div': plt_div,
            }
            return render(request, "compare_view.html", context)

    else:  # initial render (request method == GET)
        my_form = CompareForm()  # blank form

    context = {
        'my_form': my_form,
    }
    return render(request, "compare_view.html", context)
