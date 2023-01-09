from django import forms

class KasirForm(forms.Form):
    nama_menu = forms.CharField(max_length=50)
    harga = forms.IntegerField()
    jumlah = forms.IntegerField(min_value=0)
    subtotal = forms.IntegerField()

class OrderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        menu = kwargs.pop('menu')
        super(OrderForm, self).__init__(*args, **kwargs)
        for menu_item in menu:
            self.fields[menu_item.nama] = forms.IntegerField(min_value=0, initial=0)
