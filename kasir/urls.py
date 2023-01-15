from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('list-transaksi', views.list_transaksi, name='list_transaksi'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('ubah-status/<int:id>', views.ubah_status, name='ubah_status'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)