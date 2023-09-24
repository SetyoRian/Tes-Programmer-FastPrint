from django.db import models

# Create your models here.
class Kategori(models.Model):
    id_kategori = models.BigAutoField(primary_key=True, null=False)
    nama_kategori = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'Kategori'

    def __str__(self):
        return self.nama_kategori
    

class Status(models.Model):
    id_status = models.BigAutoField(primary_key=True, null=False)
    nama_status = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'Status'

    def __str__(self):
        return self.nama_status
    

class Produk(models.Model):
    id_produk = models.BigAutoField(primary_key=True, null=False)
    nama_produk = models.CharField(max_length=100)
    harga = models.IntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Produk'

    def __str__(self):
        return self.nama_produk