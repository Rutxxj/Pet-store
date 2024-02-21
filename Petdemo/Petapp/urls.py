"""
URL configuration for Petdemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:pid>', views.details, name='details'),
    path('cart/', views.cart, name='cart'),
    path('addcart/<int:pid>', views.add_cart, name='addcart'),
    path('delete/<int:pid>', views.delete, name='delete'),
    path('search', views.search, name='search'),
    path('range/', views.range, name='range'),
    path('catList/', views.catList, name='catList'),
    path('dogList/', views.dogList, name='dogList'),
    path('fishList/', views.fishList, name='fishList'),
    path('birdList/', views.birdList, name='birdList'),
    path('tortoiseList/', views.tortoiseList, name='tortoiseList'),
]
