
# Praktik 4 - Debugging dan Testing
# Program Pengolahan Nilai Mahasiswa

# Fungsi menghitung rata-rata
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0

    return sum(nilai) / len(nilai)


# Fungsi menentukan status kelulusan
def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


# Fungsi mencari nilai tertinggi
def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]

    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x

    return tertinggi


# Data nilai mahasiswa
nilai = [80, 60, 90, 70]

# Menampilkan hasil program
print("=== HASIL PENGOLAHAN NILAI ===")
print("Data nilai:", nilai)
print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))


# Pengujian test case
print("\n=== PENGUJIAN TEST CASE ===")

test_cases = [
    ("T1", hitung_rata_rata([80, 60, 90, 70]), 75.0),
    ("T2", hitung_rata_rata([100, 80]), 90.0),
    ("T3", status(60), "Lulus"),
    ("T4", status(59), "Tidak lulus"),
    ("T5", nilai_tertinggi([80, 60, 90, 70]), 90),
    ("T6", hitung_rata_rata([]), 0),
    ("T7", nilai_tertinggi([]), None)
]

for id_test, actual, expected in test_cases:
    if actual == expected:
        hasil = "PASS"
    else:
        hasil = "FAIL"

    print(
        id_test,
        "| Expected:", expected,
        "| Actual:", actual,
        "|", hasil
    )