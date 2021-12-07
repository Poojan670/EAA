from django.urls import path
from checkin import views

from . import views

urlpatterns = [
    path('', views.checkin, name='checkin'),
    path('signout', views.signout, name='signout'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),


]
