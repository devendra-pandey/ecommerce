from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


app_name = 'products'


urlpatterns = [
    path('products', views.products , name='products'),
    
    path('detailed/<int:id>/<slug:slug>/', views.detailed , name='detailed'),
    
    path('<slug:category_slug>/', views.products,name='product_list_by_category'),
    
]