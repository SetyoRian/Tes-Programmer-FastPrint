from django.urls import path
from . import views

urlpatterns = [
  path('', views.main, name='main'),
  path('products/', views.products, name='products'),
  path('products/details/<int:id>', views.detail_product, name='detail_product'),
  path('products-add/', views.add_product, name='add_product'),
  path('products-update/', views.update_product, name='update_product'),
  path('products-delete/<int:productId>/', views.delete_product, name='delete_product')
]