from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Max, Min, Avg, Sum
from django.db.models.functions import Concat
from store.models import Product
from store.models import Customer
from store.models import Collection
from store.models import Order
from store.models import OrderItem  
from tags.models import TaggedItem


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
    
#    queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

#    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

#    result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))

#    queryset = Customer.objects.annotate(new_id=F('id') + 1)

#    queryset = Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))

#    discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
#    queryset = Product.objects.annotate(discounted_price=discounted_price)

    queryset = TaggedItem.objects.get_for_model(Product, 1)
    
    return render(request, 'hello.html', {'name': 'Dima','result': list(queryset)})

#