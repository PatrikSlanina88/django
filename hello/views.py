from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Jebat Baník")

def jebat(request):
    return HttpResponse("Jebat Pražáky")

def nevim(request):
    return HttpResponse("nevím už")
