from django.contrib import admin
from .models import Kategori, Menu, Transaksi, DetailTransaksi, DetailPembayaran

# Register your models here.
class KategoriAdmin(admin.ModelAdmin):
	list_display    = ['nama']
admin.site.register(Kategori, KategoriAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display    = ['nama', 'harga', 'kategori', 'gambar']
admin.site.register(Menu, MenuAdmin)

class TransaksiAdmin(admin.ModelAdmin):
    list_display    = ['waktu', 'total_harga', 'waktu_selesai']
admin.site.register(Transaksi, TransaksiAdmin)

class DetailTransaksiAdmin(admin.ModelAdmin):
    list_display    = ['menu', 'jumlah', 'transaksi']
admin.site.register(DetailTransaksi, DetailTransaksiAdmin)

class DetailPembayaranAdmin(admin.ModelAdmin):
    list_display    = ['subtotal', 'nominal_bayar', 'catatan']
admin.site.register(DetailPembayaran, DetailPembayaranAdmin)
