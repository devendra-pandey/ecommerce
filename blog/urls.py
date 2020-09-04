from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('blog',views.blog,name='blog'),
    
    path('detail_blog', views.detail_blog , name='detail_blog'),
]