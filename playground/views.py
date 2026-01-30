from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
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

    queryset = Customer.objects.filter(email__icontains='.com')
    queryset2 = Collection.objects.filter(featured_product__isnull=True)
    queryset3 = Product.objects.filter(inventory__lt=(10))
    queryset4 = Order.objects.filter(customer__id=1)
    queryset5 = OrderItem.objects.filter(product__collection__id=3)

#    for product in query_set:
#        print(product)

    return render(request, 'hello.html', {'name': 'Dima', 'customers': list(queryset),'collection': list(queryset2) ,'products': list(queryset3), 'orders': list(queryset4), 'orderitems': list(queryset5)})

#