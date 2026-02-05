from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product
from store.models import Customer
from store.models import Collection
from store.models import Order
from store.models import OrderItem  


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
#    exists = Product.objects.filter(pk=0).exists()

#    queryset5 = OrderItem.objects.filter(product__collection__id=3) <-- искать в в

#    queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))
    
    queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

#    for product in query_set:
#        print(product)

    return render(request, 'hello.html', {'name': 'Dima','products': list(queryset)})

#