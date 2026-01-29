from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


# Create your views here.
# request -> response
# request handler (action)


# pull data from a database
# transfom data
# send emails 
# e.t.c
#       ⬇️
def say_hi(request):
#    query_set = Product.objects.all()
#    query_set.filter().filter().order_by() <-- complex query

#    product = Product.objects.get(pk=0) <- нужно обернуть в "try"
#    product = Product.objects.filter(pk=0).first()       *<-- ways to retreat data
    exists = Product.objects.filter(pk=0).exists()


#    for product in query_set:
#        print(product)

    return render(request, 'hello.html', {'name': 'Dima'})



