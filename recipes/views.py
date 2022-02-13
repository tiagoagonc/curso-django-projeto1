from django.http import HttpResponse

# from django.shortcuts import render


def home(request):
    return HttpResponse('Homeee')


def contato(request):
    return HttpResponse('Contatooo')


def sobre(request):
    return HttpResponse('Sobreee')
