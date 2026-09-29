print("PERHITUNGAN NILAI".center(30, "="))

matpel = ["Matematika", "B. Indonesia", "B. Inggris"]
total_nilai = 0

for semester in range(1, 6):
    print(f" SEMESTER {semester} ".center(30, "="))
    
    for mp in matpel:
        nilai = float(input(f"Nilai {mp} : "))
        total_nilai += nilai
    print() 

jumlah_nilai = 5 * len(matpel)
rata_rata = total_nilai / jumlah_nilai

if rata_rata >= 85:
    status = "Anda Lulus"
elif rata_rata > 70:
    status = "Harus Remedial"
else:
    status = "Tidak Lulus"

print("=" * 30)
print(f"Total Nilai Seluruh Semester : {total_nilai:.0f}")
print(f"Rata-rata Nilai             : {rata_rata:.2f}")
print(f"Status Kualifikasi          : {status}")
print()
print()

print("PERHITUNGAN FAKTORIAL".center(30, "="))

n = int(input("Masukan Angka Bulat (contoh: 5): "))

if n < 0:
    print("Faktorial tidak bisa menggunakan angka negatif")
else:
    hasil = 1
    for i in range(1, n + 1):
        hasil= hasil * i

    if n == 0:
        proses = "1"
    else:
        proses = " x ".join(str(i) for i in range(n, 0, -1))

    print("HASIL".center(30, "="))
    print(f"Proses : {n}! = {proses}")
    print(f"Hasil  : {n}! = {hasil}")
    print()
    print()

print("MEMBUAT POLAL".center(30, "="))

print("Angka Pilihan (3 = Segitiga, 4 = Persegi, >4 = Persegi Panjang)")
n = int(input("Masukan Angka: "))

if n == 3:
    print("=== POLA SEGITIGA (3) ===")
    tinggi= 5
    for i in range(1, n + 1):
        print(" ".join("*" * i))

elif n == 4:
    print("=== POLA PERSEGI (4x4) ===")
    for i in range(4):
        print(" ".join("*" * 4))

elif n > 4:
    print("=== POLA PERSEGI PANJANG ===")
    panjang = 3 * n
    for i in range(3):
        print("*" * panjang)

else:
    print("Masukan Angka Minimal 3")
