from django import forms
from .models import Produk, Kategori, Status

class ProductForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # If you want to display choices for the foreign key fields as select options:
        self.fields['kategori'].queryset = Kategori.objects.all()
        self.fields['status'].queryset = Status.objects.all()
