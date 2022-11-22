from . import views
from django.urls import path

urlpatterns = [    
    path('entregador-list', views.entregadorList, name='entregador-list'),
    path('entregador-create', views.entregadorCreate, name='entregador-create'),
    path('entregador-update/<int:id>', views.entregadorUpdate, name='entregador-update'),
    path('entregador-delete/<int:id>', views.entregadorDelete, name='entregador-delete'),
    path('farmacia-list', views.farmaciaList, name='farmacia-list'),
    path('farmacia-create', views.farmaciaCreate, name='farmacia-create'),
    path('farmacia-update/<int:id>', views.farmaciaUpdate, name='farmacia-update'),
    path('farmacia-delete/<int:id>', views.farmaciaDelete, name='farmacia-delete'),
    path('entrega-list', views.entregaList, name='entrega-list'),
    path('entrega-create', views.entregaCreate, name='entrega-create'),
    path('entrega-update/<int:id>', views.entregaUpdate, name='entrega-update'),
    path('entrega-delete/<int:id>', views.entregaDelete, name='entrega-delete'),
]