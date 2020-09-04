from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

app_name = 'cart'

urlpatterns = [
    path('cart', views.cart_detail , name='cart_detail'),
    path('add/<int:product_id>/',views.cart_add,name='cart_add'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
]