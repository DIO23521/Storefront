from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler (action)


def calculate():
    x = 1
    y = 2
    return x
# pull data from a database
# transfom data
# send emails 
# e.t.c
#       ⬇️
def say_hi(request):
    x = calculate() # всегда убирать брейкпоинты
    return render(request, 'hello.html', {'name': 'Dima'})



