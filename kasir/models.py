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
