def hitung_deret_diskon(n):
    total_deret = 0
    for i in range(1, n + 1):
        total_deret = total_deret + i
    return total_deret

print("=== Jus ===")

jumlah_jenis_jus = int(input("Masukkan jumlah jenis jus yang dibeli: "))

total_belanja = 0
total_unit_jus = 0

for i in range(1, jumlah_jenis_jus + 1):
    print(f"\n--- Barang ke-{i} ---")
    nama_jus = input("Nama jus  : ")
    harga = int(input("Harga satuan : Rp "))
    jumlah = int(input("Jumlah beli  : "))
    
    subtotal = harga * jumlah
    total_belanja = total_belanja + subtotal
    total_unit_jus = total_unit_jus + jumlah

poin_deret = hitung_deret_diskon(jumlah_jenis_jus) 

if total_belanja >= 100000:
    persen_diskon = poin_deret + (2 ** 2)
else:
    persen_diskon = poin_deret

diskon = total_belanja * (persen_diskon / 100)
total_bayar = total_belanja - diskon

print("\n" + "="*40)
print("           STRUK PEMBAYARAN")
print("="*40)
print(f"Total Belanja  : Rp {total_belanja:,}")
print(f"Total Unit     : {total_unit_jus} pcs")
print(f"Poin Deret (Sn): {poin_deret}%")
print(f"Total Diskon ({persen_diskon}%): Rp {int(diskon):,}")
print("-" * 40)
print(f"Total Bayar    : Rp {int(total_bayar):,}")
print("="*40)

uang_bayar = int(input("\nMasukkan Uang Pembayaran: Rp "))
kembalian = uang_bayar - total_bayar

print(f"Kembalian      : Rp {int(kembalian):,}")
print("\nTerima kasih telah berbelanja!")