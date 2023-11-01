from django.contrib import admin
from django.urls import path
from app1 import views

from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('',csrf_exempt(views.index), name='app1'),
    path('signin',csrf_exempt(views.signin), name='signin'),
    path('signup',views.signup, name='signup'),
    path('signout',views.signout, name='signout'),
    path('home',views.home, name='home'),
]