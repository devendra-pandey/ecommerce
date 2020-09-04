from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('cart', views.cart , name='cart'),
    
    path('checkout', views.checkout , name='checkout'),
    path('invoice', views.invoice , name='invoice'),
    
    
   
]