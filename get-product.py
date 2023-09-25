import requests
import psycopg2
from datetime import datetime
from datetime import date
import hashlib


def getProducts():
  url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

  # Get Date
  hour = datetime.now().hour + 1
  hour = str(hour)
  today = str(date.today())
  today = today.split('-')
  year, month, day = today
  year = year[2:]

  # MD5 Encrypt
  password = f'bisacoding-{day}-{month}-{year}'
  password = hashlib.md5(password.encode())
  password = password.hexdigest()
  username = f'tesprogrammer{day}{month}{year}C{hour}'

  payload = {'username': username,
            'password': password}

  response = requests.request(
      "POST", url, data=payload
  )
  
  return response.json()


def insert_kategori(kategori):
  for data in kategori:
    cursor = conn.cursor()
    query = """INSERT INTO "Kategori" (nama_kategori) VALUES (%s);"""
    value = (data,)
    try:
      cursor.execute(query, value)
      conn.commit()
      print("Data inserted successfully!")
    except psycopg2.Error as e:
      conn.rollback()
      print("Error: Failed to insert data into the database")
      print(e)

  cursor.close()

def insert_status(status):
  for data in status:
    cursor = conn.cursor()
    query = """INSERT INTO "Status" (nama_status) VALUES (%s);"""
    value = (data,)
    try:
      cursor.execute(query, value)
      conn.commit()
      print("Data inserted successfully!")
    except psycopg2.Error as e:
      conn.rollback()
      print("Error: Failed to insert data into the database")
      print(e)

  cursor.close()

def insert_product(products):
  for data in products:
    cursor = conn.cursor()

    idProduk = data['id_produk']
    namaProduk = data['nama_produk']
    harga = data['harga']
    namaKategori = data['kategori']
    status = data['status']

    insert_query = """
      INSERT INTO "Produk" 
      (id_produk, nama_produk, harga, kategori_id, status_id) 
      VALUES (%s, %s, %s, (
        SELECT "id_kategori" FROM "Kategori"
        WHERE "nama_kategori" = %s
      ), (
        SELECT "id_status" FROM "Status"
        WHERE "nama_status" = %s
      ));
    """
    value = (idProduk, namaProduk, harga, namaKategori, status)
    try:
      cursor.execute(insert_query, value)
      conn.commit()
      print("Data inserted successfully!")
    except psycopg2.Error as e:
      conn.rollback()
      print("Error: Failed to insert data into the database")
      print(e)

  cursor.close()

if __name__ == "__main__":
  # Connect Database
  try:
    conn = psycopg2.connect(database='testdjango',
                        host='localhost',
                        user='postgres',
                        password='Postgres123',
                        port='5432')
  except psycopg2.Error as e:
    print("Error: Unable to connect to the database")
    print(e)  
  
  dict_product = getProducts()
  arr_data = dict_product['data']
  state = 1
  while state < 4:
    if state == 1:
      set_kategori = set()
      for value in arr_data:
        set_kategori.add(value['kategori'])
      insert_kategori(set_kategori)
    elif state == 2:
      set_status = set()
      for value in arr_data:
        set_status.add(value['status'])
      insert_status(set_status)
    elif state == 3:
      insert_product(arr_data)
    state += 1
  conn.close()
