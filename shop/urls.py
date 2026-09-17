from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('detalle/<int:id>/', views.detalle, name='detalle'),
]
