from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

app_name = 'order'

urlpatterns = [
    
    path('create/', views.order_create, name='order_create'),
    path('invoice', views.invoice , name='invoice'),
    
    path('admin/order/<int:order_id>/', views.admin_order_detail,name='admin_order_detail'),
 
 
   
]