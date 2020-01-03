from django.shortcuts import render

from .models import CellInput
from .forms import CellInputForm
# Create your views here.
# def cell_list(request):
#     '''Renders view of all previously registered cells
#     '''
#     return render([request], [template_name], [context])

def cell_list(request):
    '''Display table of all cells models in the databse.
    '''
    query_results = CellInput.objects.all()

    context = {
        'query_results':query_results
    }
    return render(request, "cell_list.html", context)

def new_cell(request):
    '''Renders form allowing users to input cell parameters and 
    submit data to databse.
    '''
    my_form = CellInputForm(request.POST)
    if my_form.is_valid():
        #we know the input data is good
        print(my_form.cleaned_data)
        #Need to fix names to match before enabling this code:
        CellInput.objects.create(**my_form.cleaned_data)
        my_form = CellInputForm()

    context = {
        'form': my_form
    }
    return render(request, "new_cell.html", context)
