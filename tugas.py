#IF ELSE, FOR

matpel = ["Matematika", "B. Indonesia", "B. Inggris"]
total_nilai = 0

for semester in range(1, 6):
    print(f" SEMESTER {semester} ".center(30, "="))
    
    for mp in matpel:
        nilai = float(input(f"Nilai {mp} : "))
        total_nilai += nilai
    print() 

jumlah_nilai = 4 * len(matpel)
rata_rata = total_nilai / jumlah_nilai

if rata_rata >= 85:
    status = "Lolos Jalur Prestasi (Beasiswa)"
elif rata_rata >= 70:
    status = "Lolos Jalur Reguler"
else:
    status = "Tidak Lolos (Harus Remedial)"

print("=" * 30)
print(f"Total Nilai Seluruh Semester : {total_nilai:.0f}")
print(f"Rata-rata Nilai             : {rata_rata:.2f}")
print(f"Status Kualifikasi          : {status}")

#PERHITUNGAN MATEMATIK FACTORIAL

import math

print("=== PROGRAM PERHITUNGAN FAKTORIAL ===")

n= int(input("Masukkan angka bulat (contoh: 5): "))

if n < 0:
    print("Faktorial tidak berlaku untuk angka negatif.")
else:
    hasil= math.factorial(n)

    proses= " x ".join(str(i) for i in range(n, 0, -1)) if n > 0 else "1"

    print("\n--- HASIL ---")
    print(f"Proses : {n}! = {proses}")
    print(f"Hasil  : {n}! = {hasil}")

    #POLA