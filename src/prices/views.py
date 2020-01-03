from django.shortcuts import render

from .models import PriceInput

from .forms import PriceInputForm
# Create your views here.
def price_list(request):
    '''Renders view of all previously registered price datasets
    '''
    query_results = PriceInput.objects.all()
    context = {
        'query_results':query_results
    }
    return render(request, "price_list.html", context)


def new_price(request):
    '''Renders form allowing users to input prices and 
    submit data to databse.
    '''
    my_form = PriceInputForm(request.POST)
    if my_form.is_valid():
        #we know the input data is good
        # print(my_form.cleaned_data)
        PriceInput.objects.create(**my_form.cleaned_data)
        my_form = PriceInputForm()

    context = {
        'form': my_form
    }
    return render(request, "price_input.html", context)

