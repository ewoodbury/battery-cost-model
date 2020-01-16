from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import CellInput
from .forms import CellInputForm

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

    If it's an initial rendering, request.method == 'GET' and will render blank form
    If input data is not valid, it re-renders the form with submitted data still present,
    but also includes error messages.
    If data is valid, it creates a new object and redirects to confirmation page.
    '''
    if request.method == 'POST':
        my_form = CellInputForm(request.POST)
        if my_form.is_valid(): # if we know the input data is good
            CellInput.objects.create(**my_form.cleaned_data)
            # my_form = CellInputForm() #Re-renders page as blank
            return HttpResponseRedirect(reverse('cell_list'))
    else: #if method is GET (it's an initial rendering)
        my_form = CellInputForm()

    context = {
        'my_form': my_form
    }
    return render(request, "new_cell.html", context)
