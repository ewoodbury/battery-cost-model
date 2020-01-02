from django.shortcuts import render

from .models import CellInput
from .forms import CellInputForm
# Create your views here.
# def cell_list(request):
#     '''Renders view of all previously registered cells
#     '''
#     return render([request], [template_name], [context])

def cell_input(request):
    '''Renders form allowing users to input cell parameters and 
    submit data to databse.
    '''
    my_form = CellInputForm(request.POST)
    if my_form.is_valid():
        #we know the input data is good
        print(my_form.cleaned_data)
        # CellInput.objects.create(**my_form.cleaned_data)

    context = {
        'form': my_form
    }
    return render(request, "cell_input.html", context)
