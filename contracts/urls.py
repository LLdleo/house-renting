from django.urls import path

from . import views

urlpatterns = [
  path('contract_create', views.contract_create, name='contract_create'),
  path('deny', views.deny, name='deny')
]
