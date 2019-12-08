from django.urls import path

from . import views

urlpatterns = [
  path('contract_create', views.contract_create, name='contract_create'),
  path('contract_deny', views.contract_deny, name='contract_deny'),
  path('contract_sign', views.contract_sign, name='contract_sign'),
  path('end_contract', views.end_contract, name='end_contract'),
  path('<int:contract_id>', views.contract, name='contract'),
]
