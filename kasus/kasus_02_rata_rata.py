# Kasus 02 - Perbaikan Bug Rata-rata

def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0

    total = sum(nilai)
    return total / len(nilai)


print("Rata-rata:", hitung_rata_rata([80, 90, 70]))
print("Rata-rata:", hitung_rata_rata([100, 80]))
print("Rata-rata:", hitung_rata_rata([60]))
print("Rata-rata:", hitung_rata_rata([]))