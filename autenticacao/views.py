from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# pagina de cadastro e paghome
def cadastro(request):
    return render(request, 'cadastro.html')

# login

def logar(request):
    return render(request, 'logar.html')     #HttpResponse("Você esta na pagina de login")