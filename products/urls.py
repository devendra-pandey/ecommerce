from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('products', views.products , name='products'),
    path('detailed', views.detailed , name='detailed'),
    
    
   
]