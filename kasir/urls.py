from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('list-transaksi', views.list_transaksi, name='list_transaksi'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('detail-pembayaran/<int:id>', views.detail_pembayaran, name='detail_pembayaran'),
    path('ubah-status/<int:id>', views.ubah_status, name='ubah_status'),
    path('hapus/<int:id>', views.hapus, name='hapus'),
    path('ubah/<int:id>', views.ubah, name='ubah'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)