from django.shortcuts import render

from .models import PriceInput

from .forms import PriceInputForm
# Create your views here.
# def cell_list(request):
#     '''Renders view of all previously registered cells
#     '''
#     return render([request], [template_name], [context])

def price_input(request):
    '''Renders form allowing users to input prices and 
    submit data to databse.
    '''
    my_form = PriceInputForm(request.POST)
    if my_form.is_valid():
        #we know the input data is good
        print(my_form.cleaned_data)
        # PriceInput.objects.create(**my_form.cleaned_data)
        # my_form = CellInputForm()

    context = {
        'form': my_form
    }
    return render(request, "price_input.html", context)

