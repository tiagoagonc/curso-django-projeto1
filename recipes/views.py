from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Homee')


def contato(request):
    return HttpResponse('Contatoo')


def sobre(request):
    return HttpResponse('Sobree')
