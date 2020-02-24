from django.urls import path,include
from . import views 

urlpatterns = [
    path('cliente', views.ListaCliente.as_view(),name="ListaCliente"),
    path('main', views.ListaMain.as_view(),name="ListaMain"),
    path('',views.Principal.as_view(), name='Principal')
  
]