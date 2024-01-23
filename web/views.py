from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):

    cas = datetime.now().time()
    if cas < datetime.strptime('12:00', '%H:%M').time():
        pozdrav = 'Dobré ráno'
    elif cas < datetime.strptime('17:00', '%H:%M').time():
        pozdrav = 'Dobré odpoledne'
    elif cas < datetime.strptime('20:00', '%H:%M').time():
        pozdrav = 'Dobrý večer'
    else:
        pozdrav = 'Dobrou noc'
    return render(request, 'web/index.html', {'pozdrav': pozdrav})
def form(request):
    return render(request, 'web/form.html')

