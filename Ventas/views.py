from django.shortcuts import render
from django.http import HttpResponse

def Catalogo(request):
    return render(request, "Catalogo.html")
