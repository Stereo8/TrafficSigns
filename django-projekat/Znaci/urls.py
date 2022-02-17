from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pojediEksel', views.pojediExcel, name='pojediEksel'),
    path('pitanje/<int:pitanje_id>', views.prikazi_pitanje, name="prikazi_pitanje")
]
