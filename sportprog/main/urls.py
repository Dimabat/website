from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact1', views.contact1, name='contact1'),
    path('sh1', views.sh1, name='sh1'),
    path('bis1', views.bis1, name='bis1'),
    path('tric', views.tric, name='tric'),
    path('legs', views.legs, name='legs'),
    path('pres', views.pres, name='pres'),
    path('fore', views.fore, name='fore')
]