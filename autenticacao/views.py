from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cadastro(request):
    return HttpResponse("Você está na pagina de cadastro")
    pass