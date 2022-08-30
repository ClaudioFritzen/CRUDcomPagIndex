from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# pagina de cadastro e paghome
def cadastro(request):
    return HttpResponse("Você está na pagina de cadastro")

# login

def logar(request):
    return HttpResponse("Você esta na pagina de login")