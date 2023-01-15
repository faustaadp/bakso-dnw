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
                    DetailTransaksi.objects.create(
                        transaksi=transaksi, 
                        menu=Menu.objects.filter(nama=str(key)).first(), 
                        jumlah=value, 
                        harga=int(Menu.objects.filter(nama=str(key)).first().harga),
                        subtotal=int(value) * int(Menu.objects.filter(nama=str(key)).first().harga))
            transaksi.save()
            return redirect('list_transaksi')
    else:
        form = OrderForm(menu=menus)
    return render(request, 'kasir/index.html', {'form': form, 'menus': menus})

def list_transaksi(request):
    transaksis = Transaksi.objects.all().order_by('status')
    return render(request, 'kasir/list_transaksi.html', {'transaksis': transaksis})

def detail(request, id):
    transaksi = Transaksi.objects.get(id=id)
    return render(request, 'kasir/detail.html', {'transaksi': transaksi})

def ubah_status(request, id):
    transaksi = Transaksi.objects.get(id=id)
    transaksi.status = True
    transaksi.save()
    return redirect(list_transaksi)

def hapus(request, id):
    transaksi = Transaksi.objects.get(id=id)
    transaksi.delete()
    return redirect(list_transaksi)

def ubah(request, id):
    menus = Menu.objects.all()
    transaksi = Transaksi.objects.get(id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, menu=menus)
        if form.is_valid():
            transaksi.total_harga = 0
            transaksi.total_item = 0
            for key, value in request.POST.items():
                if(Menu.objects.filter(nama=str(key)).exists()):
                    transaksi.total_harga += int(Menu.objects.filter(nama=str(key)).first().harga) * int(value)
                    transaksi.total_item += int(value)
                    detail_transaksi = DetailTransaksi.objects.get(
                        transaksi=transaksi,
                        menu = Menu.objects.filter(nama=str(key)).first()
                    )
                    detail_transaksi.jumlah = value
                    detail_transaksi.harga=int(Menu.objects.get(nama=str(key)).harga)
                    detail_transaksi.subtotal=int(value) * int(Menu.objects.filter(nama=str(key)).first().harga)
                    detail_transaksi.save()
            transaksi.save()
            return redirect('detail', id=id)
    else:
        form = OrderForm(menu=menus)
    for menu in menus:
        menu.jumlah = transaksi.detailtransaksi_set.filter(menu=menu).first().jumlah
    total_harga = transaksi.total_harga
    transaksi_id = transaksi.id
    return render(request, 'kasir/ubah.html', {'form': form, 'menus': menus, 'total_harga': total_harga, 'transaksi_id': transaksi_id})