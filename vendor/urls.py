from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('vendor_dashboard', views.vendor_dashboard , name='vendor_dashboard'),
    path('become_vendor', views.become_vendor , name='become_vendor'),
    path('vendor_message', views.vendor_message , name='vendor_message'),
    path('vendor_message_comp', views.vendor_message_comp , name='vendor_message_comp'),
    path('vendor_dashboard_purchase', views.vendor_dashboard_purchase , name='vendor_dashboard_purchase'),
    path('vendor_dashboard_statement', views.vendor_dashboard_statement , name='vendor_dashboard_statement'),
    path('vendor_edit_item', views.vendor_edit_item , name='vendor_edit_item'),
    path('vendor_items', views.vendor_items , name='vendor_items'),
    path('vendor_uploads', views.vendor_uploads , name='vendor_uploads'),
    path('vendor_reviews', views.vendor_reviews , name='vendor_reviews'),
    path('vendor_withdrawal', views.vendor_withdrawal , name='vendor_withdrawal'),
    path('vendor_signup', views.vendor_signup , name='vendor_signup'),
    
   
]