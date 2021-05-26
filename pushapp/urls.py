from django.urls import path, include
from  django.contrib import  admin
from django.views.generic.base import TemplateView # new

from . import views

urlpatterns = [
    #path('accounts/', include('django.contrib.auth.urls')),  # new
    path('', views.home, name='home'),
    path('myhistory/', views.myhistory, name='myhistory'),
    path('records/', views.records, name='records'),
    #path('create/', views.PushUpForm),
    path ('add_pushups/', views.addPushups, name="add_pushups")
]