import email
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# pagina de cadastro e paghome
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        # pegando os dados enviados quando preenchemos o cadastro
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        return HttpResponse (f'{usuario} {email}')

# login

def logar(request):
    return render(request, 'logar.html')     #HttpResponse("Você esta na pagina de login")