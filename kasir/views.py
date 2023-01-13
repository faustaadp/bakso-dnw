import datetime
from django.shortcuts import render, redirect
from .models import DetailTransaksi, Menu, Transaksi
from .forms import OrderForm

def index(request):
    menus = Menu.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST, menu=menus)
        if form.is_valid():
            transaksi = Transaksi.objects.create(waktu=datetime.datetime.now(), total_harga=0, total_item=0, status=False)
            for key, value in request.POST.items():
                if(Menu.objects.filter(nama=str(key)).exists()):
                    transaksi.total_harga += int(Menu.objects.filter(nama=str(key)).first().harga) * int(value)
                    transaksi.total_item += int(value)
                    DetailTransaksi.objects.create(transaksi=transaksi, menu=Menu.objects.filter(nama=str(key)).first(), jumlah=value)
            transaksi.save()
            return redirect('list_transaksi')
    else:
        form = OrderForm(menu=menus)
    return render(request, 'kasir/index.html', {'form': form, 'menus': menus})

def list_transaksi(request):
    transaksis = Transaksi.objects.all().order_by('status')
    return render(request, 'kasir/list_transaksi.html', {'transaksis': transaksis})