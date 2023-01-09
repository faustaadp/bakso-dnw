from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list-transaksi', views.list_transaksi, name='list_transaksi'),
]