import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime, timedelta

# Daftar tanggal yang akan digunakan dalam looping
end_date = datetime(2022, 12, 1)
start_date = datetime(2021, 1, 1)

# Set untuk menyimpan semua tautan dari semua halaman
all_hrefs = set()

# Perulangan melalui setiap tanggal
current_date = start_date
max_links = 4005
counter = 0

while current_date <= end_date and counter < max_links:
    date_str = current_date.strftime("%Y/%m/%d")
    url = f"https://www.viva.co.id/indeks/berita/all/{date_str}"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Mencari semua elemen <a> dengan class "article-list-title"
    links = soup.find_all('a', class_='article-list-title')

    # Memastikan URL unik dan dimulai dengan domain yang diinginkan
    for link in links:
        href = link['href']
        if href.startswith('https://www.viva.co.id') or href.startswith('http://www.viva.co.id'):
            all_hrefs.add(href)

    # Menghitung jumlah tautan yang sudah diekstrak
    counter += len(links)

    # Menambahkan 1 hari ke tanggal saat ini
    current_date += timedelta(days=1)

# Menyimpan hasil ke dalam berkas CSV
with open('links.csv', 'w', newline='') as csvfile:
    fieldnames = ['Link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for href in sorted(list(all_hrefs)):
        writer.writerow({'Link': href})
