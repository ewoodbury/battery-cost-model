from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import PriceInput
from .forms import PriceInputForm

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
    if request.method == 'POST':
        my_form = PriceInputForm(request.POST)
        if my_form.is_valid():
            PriceInput.objects.create(**my_form.cleaned_data)
            return HttpResponseRedirect(reverse('price_list'))
    else: #if it's an initial rendering with method == GET, generate blank page
        my_form = PriceInputForm()

    context = {
        'form': my_form
    }
    return render(request, "price_input.html", context)

