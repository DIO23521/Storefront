from django.urls import path
from . import views # so we can reference our views func

# URLConf
urlpatterns = [
    path('hello/', views.say_hi)  # always end with /
]