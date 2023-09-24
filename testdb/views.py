from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Produk
from .forms import ProductForm

# Create your views here.
def products(request):
  myproducts = Produk.objects.select_related('kategori', 'status').filter(status__nama_status='bisa dijual')
  template = loader.get_template('allProduct.html')
  context = {
    'myproducts': myproducts
  }
  return HttpResponse(template.render(context, request))

def detail_product(request, id):
  myproduct = Produk.objects.get(id_produk=id)
  template = loader.get_template('detailsProduct.html')
  context = {
    'myproduct': myproduct
  }
  return HttpResponse(template.render(context, request))

def add_product(request):
  if request.method == "POST":
    form = ProductForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('products')
  else:
    form = ProductForm()
  return render(request, 'addProduct.html', {'form': form})

def update_product(request):
  if request.method == "POST":
    product_id = request.POST.get('product')
    product = Produk.objects.get(pk=product_id)

    form = ProductForm(request.POST, instance=product)

    if form.is_valid():
      form.save()
      return redirect('products')
  else:
    form = ProductForm()
  
  all_products = Produk.objects.all()
  return render(request, 'updateProduct.html', {'form': form, 'products': all_products})

def delete_product(request, productId):
  if request.method == "POST":
    product = Produk.objects.get(pk=productId)
    product.delete()
    return redirect('products')

def main(request):
  myproducts = Produk.objects.select_related('kategori', 'status')
  template = loader.get_template('main.html')
  context = {
    'myproducts': myproducts
  }
  return HttpResponse(template.render(context, request))