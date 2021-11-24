from django.shortcuts import render
from django.http import HttpResponse

def ejemplo(request):
    return HttpResponse("hola mundo")
