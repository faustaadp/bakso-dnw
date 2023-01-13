from django.contrib import admin
from .models import Kategori, Menu, Transaksi, DetailTransaksi

# Register your models here.
class KategoriAdmin(admin.ModelAdmin):
	list_display    = ['nama']
admin.site.register(Kategori, KategoriAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display    = ['nama', 'harga', 'kategori', 'gambar']
admin.site.register(Menu, MenuAdmin)

class TransaksiAdmin(admin.ModelAdmin):
    list_display    = ['waktu', 'total_harga']
admin.site.register(Transaksi, TransaksiAdmin)

class DetailTransaksiAdmin(admin.ModelAdmin):
    list_display    = ['menu', 'jumlah', 'transaksi']
admin.site.register(DetailTransaksi, DetailTransaksiAdmin)
