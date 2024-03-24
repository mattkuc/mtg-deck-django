from django.shortcuts import render
from django.http import HttpResponse

def decks(request):
    return HttpResponse("Hello Decks!")

