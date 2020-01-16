from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") #string of HTML code
    return render(request, "home.html", {})

def login_view(request):
    return render(request, "login.html", {})