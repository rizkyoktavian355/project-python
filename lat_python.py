print("--- MiniMarket cecep ---")
nama_barang = input("Masukkan Nama Barang: ")
jumlah_barang = int(input("Masukkan jumlah barang: "))
harga = int(input("Harga barang: Rp"))

total_asli = harga * jumlah_barang

if total_asli >= 100000:
  diskon = total_asli * 0.1
  total_bayar = total_asli - diskon
else:
  diskon = 0
  total_bayar = total_asli

print("\n--- STRUK BELANJA ---")
print(f"Nama Barang    : {nama_barang}")
print(f"Jumlah Beli    : {jumlah_barang}")
print(f"Harga Satuan   : Rp{harga:,}")
print("-------------------------------------")
print(f"Total Asli     : Rp{total_asli:,}")
print(f"Diskon 10%     : Rp{int(diskon):,}")
print("-------------------------------------")
print(f"Total Bayar    : Rp{int(total_bayar):,}")