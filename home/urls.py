from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

app_name = 'home'

urlpatterns = [
    path('', views.index , name='home'),
    path('contact', views.contact , name='contact'),
    path('about', views.about , name='about'),
    path('term', views.term_condition , name='term'),
    
    
   
]