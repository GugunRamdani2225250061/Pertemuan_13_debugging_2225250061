# PERTEMUAN 13_DEBUGGING
### A. Identitas Mahasiswa
- Nama: Gugun Ramdani
- NIM: 2225250061
- Program Studi: S1 Pendidikan Matematika
- Mata Kuliah: Algoritma dan Pemrograman

### B. Deskripsi Praktikum
Praktikum ini membahas debugging, tracing, testing, dan test case menggunakan Python di Visual Studio Code. Tujuannya adalah memahami kesalahan program, menelusuri alur eksekusi, memperbaiki kode, serta menguji hasil program.

### C. Struktur Folder
```text
Pertemuan_13_debugging_2225250061
├── data/
│   └── nilai.txt
├── kasus/
│   ├── kasus_01_batas_kelulusan.py
│   ├── kasus_02_rata_rata.py
│   └── kasus_03_file_nilai.py
├── latihan/
│   ├── 01_trace_loop.py
│   ├── 02_trace_fungsi.py
│   ├── 03_test_case.py
│   └── 04_debug_breakpoint.py
├── praktik/
│   └── praktik_4_debugging.py
├── .gitignore
├── kuis formatif_pertemuan 13.docx
└── README.md
```
### D. Hasil Pengerjaan
1. Kasus
- Kasus 1: Memperbaiki kesalahan batas kelulusan menggunakan operator `>=`.
- Kasus 2: Memperbaiki perhitungan rata-rata menggunakan `len()`.
- Kasus 3: Membaca file nilai dan menangani kesalahan menggunakan `try-except`.

2. Latihan
- Latihan 1: Tracing perulangan dengan hasil akhir 24.
- Latihan 2: Tracing fungsi diskon dengan hasil Rp180.000.
- Latihan 3: Menguji status kelulusan menggunakan test case.
- Latihan 4: Mempraktikkan debugging menggunakan breakpoint di VS Code.

3. Praktik 4
Memperbaiki kesalahan perhitungan rata-rata, penentuan kelulusan, dan pencarian nilai tertinggi.

### E. Hasil Pengujian
| Pengujian | Input | Hasil |
|---|---|---|
| Rata-rata file | 80, 90, 70, 85 | 81.25 |
| Rata-rata | [80, 60, 90, 70] | 75 |
| Status nilai | 60 | Lulus |
| Status nilai | 59 | Tidak lulus |
| Nilai tertinggi | [80, 60, 90, 70] | 90 |

### F. Kuis Formatif
Kuis formatif dikerjakan berdasarkan materi Pertemuan 13 dan disimpan dalam file `kuis formatif_pertemuan 13.docx`.

### G. Kesimpulan
Melalui praktikum ini, mahasiswa memahami cara menemukan dan memperbaiki kesalahan program menggunakan debugging, menelusuri alur program dengan tracing, serta menguji program menggunakan test case. Praktikum ini juga meningkatkan kemampuan menggunakan Visual Studio Code untuk mengembangkan program Python.
