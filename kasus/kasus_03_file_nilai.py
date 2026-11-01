# Kasus 03 - Perbaikan Bug File Nilai

def baca_nilai(nama_file):
    try:
        with open(nama_file, "r") as file:
            nilai = []

            for baris in file:
                baris = baris.strip()

                if baris:
                    nilai.append(int(baris))

        if len(nilai) == 0:
            print("File tidak memiliki data nilai.")
            return None

        rata_rata = sum(nilai) / len(nilai)

        return rata_rata

    except FileNotFoundError:
        print("Error: File tidak ditemukan.")
        return None

    except ValueError:
        print("Error: Data dalam file harus berupa angka.")
        return None


hasil = baca_nilai("data/nilai.txt")

if hasil is not None:
    print("Rata-rata nilai:", hasil)