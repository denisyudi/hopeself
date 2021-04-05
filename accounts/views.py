from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/index.html')

def historico(request):
    return render(request, 'accounts/historico.html')

def consultas(request):
    return render(request, 'accounts/consultas.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')