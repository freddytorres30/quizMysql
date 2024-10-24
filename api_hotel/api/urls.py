from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.ClientesListCreate.as_view(), name='clientes-list'),
    path('clientes/<int:pk>/', views.ClientesDetail.as_view(), name='clientes-detail'),
    
    path('reservas/', views.ReservasListCreate.as_view(), name='reservas-list'),
    path('reservas/<int:pk>/', views.ReservasDetail.as_view(), name='reservas-detail'),
    
    path('habitaciones/', views.HabitacionesListCreate.as_view(), name='habitaciones-list'),
    path('habitaciones/<int:pk>/', views.HabitacionesDetail.as_view(), name='Habitaciones-detail'),
    
    path('pagos/', views.PagosListCreate.as_view(), name='pagos-list'),
    path('pagos/<int:pk>/', views.PagosDetail.as_view(), name='pagos-detail'),
]