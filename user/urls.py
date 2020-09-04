from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('signup', views.signup , name='signup'),
    path('login', views.login , name='login'),
    path('user_dashboard', views.user_dashboard , name='user_dashboard'),
    path('user_info', views.user_info , name='user_info'),
    path('message', views.message , name='message'),
    path('message_comp', views.message_comp , name='message_comp'),
    path('recover_pass', views.recover_pass , name='recover_pass'),
    
    # path('logout', views.logout , name='logout'),
]