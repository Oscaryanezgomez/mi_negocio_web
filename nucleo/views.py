from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
    #return HttpResponse("<h1>Mi negocio web </h1>")
    return render(request, "nucleo/index.html")