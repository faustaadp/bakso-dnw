from django.contrib import admin
from .models import Kategori, Menu

# Register your models here.
class KategoriAdmin(admin.ModelAdmin):
	list_display    = ['nama']
admin.site.register(Kategori, KategoriAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display    = ['nama']
admin.site.register(Menu, MenuAdmin)
