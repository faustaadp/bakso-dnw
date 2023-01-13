from django.db import models

# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length = 50)

    def __str__(self):
        return self.nama

class Menu(models.Model):
    nama = models.CharField(max_length = 50)
    harga = models.PositiveIntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    gambar = models.ImageField(upload_to='menu_images/', null=True, blank=True)

class Transaksi(models.Model):
    status = models.BooleanField()
    waktu = models.DateTimeField()
    total_item = models.PositiveIntegerField()
    total_harga = models.PositiveIntegerField()

class DetailTransaksi(models.Model):
    transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField()
