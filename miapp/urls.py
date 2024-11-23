from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('grafica/', views.grafica, name='grafica'),  # Ruta para la gráfica
]
