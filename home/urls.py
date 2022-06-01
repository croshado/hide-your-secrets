from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
   path('', views.index, name = 'home'),
   path('decrypt/', views.indexd, name='homed'),
   path("chlo/", views.chlo, name='aagyatu'),
   path("decrypt/cho/", views.cho, name='where' ),
  
]

