CAPSTONE PROJECT MODULE 1
CASE STUDY: RENTAL MOBIL AKBAR

Program Rental Mobil Akbar dibuat sebagai proyek akhir Capstone Project Module 1 untuk menerapkan konsep dasar pemrograman Python menggunakan CRUD (Create, Read, Update, Delete). Tujuan program ini adalah untuk mengelola data mobil dalam sistem rental secara sederhana — menambah, melihat, mengubah, dan menghapus data menggunakan regular function serta data collection type berupa list of dictionaries.

Struktur Data:
Data utama dalam program disimpan dalam variabel data_mobil, yang berbentuk list berisi beberapa dictionary, dengan setiap dictionary mewakili satu data mobil.

Contoh:
data_mobil = [
    {'nama': 'Avanza', 'merk': 'Toyota', 'tahun': 2020, 'harga': 300000},
    {'nama': 'Brio', 'merk': 'Honda', 'tahun': 2019, 'harga': 250000},
    {'nama': 'Xenia', 'merk': 'Daihatsu', 'tahun': 2021, 'harga': 280000}
]

Setiap mobil memiliki 4 atribut utama:
- nama : Nama mobil (string)
- merk : Merk atau pabrikan (string)
- tahun : Tahun pembuatan mobil (integer)
- harga : Harga sewa per hari (integer)

Fitur CRUD (Create, Read, Update, Delete)
1. Fitur Create
Tujuan: Menambahkan data mobil baru ke dalam daftar.
Fungsi: create_menu()

Langkah kerja:
- Program meminta input data baru dari pengguna: nama, merk, tahun, dan harga.
- Program melakukan pengecekan duplikasi agar nama mobil tidak sama dengan data yang sudah ada.
- Jika valid, data baru disimpan dengan perintah:
- data_mobil.append({'nama': nama, 'merk': merk, 'tahun': tahun, 'harga': harga})
- Program menampilkan pesan “Data successfully saved.”

2. Fitur Read
Tujuan: Menampilkan seluruh data mobil atau mencari data tertentu berdasarkan nama.
Fungsi: read_menu()

Opsi menu:
a. Menampilkan semua data mobil.
Program menggunakan perulangan:
for mobil in data_mobil:
    print(f"- {mobil['nama']} | {mobil['merk']} | {mobil['tahun']} | Rp{mobil['harga']}/hari")

b. Mencari data berdasarkan nama mobil.
Menggunakan variabel logika:
ditemukan = False
Jika data ditemukan, tampilkan hasilnya. Jika tidak, program menampilkan pesan “Data tidak ditemukan.”

c. Fitur Update
Tujuan: Mengubah data mobil yang sudah ada.
Fungsi: update_menu()

Langkah kerja:
- Pengguna memasukkan nama mobil yang ingin diubah.
- Program mencari data yang cocok dan menampilkannya.
- Pengguna memilih kolom yang ingin diubah (nama, merk, tahun, atau harga).
- Nilai baru dimasukkan, kemudian dikonfirmasi sebelum disimpan:
- mobil_ditemukan[kolom] = nilai_baru

Jika nama diubah, program memastikan tidak terjadi duplikasi dengan nama mobil lain.

4. Fitur Delete
Tujuan: Menghapus data mobil dari daftar.
Fungsi: delete_menu()

Langkah kerja:
- Pengguna memasukkan nama mobil yang ingin dihapus.
- Program mencari data dan meminta konfirmasi:
- konfirmasi = input(f"Yakin ingin menghapus '{nama}'? (y/n): ").lower()
- Jika “y”, data dihapus dari list menggunakan:
- data_mobil.remove(mobil)

Program menampilkan pesan “Data berhasil dihapus.”

Best Practice yang Diterapkan:
- Setiap fitur CRUD dibuat dalam fungsi terpisah (regular function) untuk menjaga modularitas.
- Semua fungsi saling terhubung melalui fungsi utama main_menu(), sehingga program berjalan secara berkesinambungan.
- Penggunaan while True pada setiap menu memastikan program tetap berjalan sampai pengguna memilih keluar.
- Terdapat validasi input dan konfirmasi tindakan (y/n) untuk menghindari kesalahan pengguna.
- Menggunakan penamaan variabel yang deskriptif seperti data_mobil, mobil_ditemukan, dan ditemukan agar mudah dibaca.
- Kode diberi spasi, indentasi, dan struktur yang rapi agar mudah dipelihara (maintainable).

Alur Program (Main Menu)
Fungsi utama main_menu() berisi struktur logika untuk memanggil setiap fitur CRUD:

def main_menu():
    while True:
        print("====================================")
        print("RENTAL MOBIL AKBAR")
        print("====================================")
        print("1. Tampilkan daftar mobil")
        print("2. Tambah mobil")
        print("3. Update data mobil")
        print("4. Hapus mobil")
        print("5. Keluar")
        print("====================================")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            read_menu()
        elif pilihan == '2':
            create_menu()
        elif pilihan == '3':
            update_menu()
        elif pilihan == '4':
            delete_menu()
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Data yang dimasukkan tidak valid.\n")

Saat program dijalankan, pengguna dapat memilih fitur CRUD secara berulang hingga memilih keluar.

Cara Menjalankan Program
- Pastikan Python sudah terinstal di komputer Anda (versi 3.7 atau lebih baru).
- Simpan file program ini dengan nama rental_mobil.py.
- Jalankan melalui terminal atau command prompt: python rental_mobil.py

Pilih menu sesuai kebutuhan:
1 → Tampilkan daftar mobil
2 → Tambah mobil
3 → Update data mobil
4 → Hapus mobil
5 → Keluar dari program

🧾 Contoh Tampilan Program
====================================
RENTAL MOBIL AKBAR
====================================
1. Tampilkan daftar mobil
2. Tambah mobil
3. Update data mobil
4. Hapus mobil
5. Keluar
====================================
Pilih menu (1-5): 1

=== DAFTAR MOBIL ===
- Avanza | Toyota | 2020 | Rp300000/hari
- Brio | Honda | 2019 | Rp250000/hari
- Xenia | Daihatsu | 2021 | Rp280000/hari

Penutup:
- Program ini memenuhi seluruh kriteria Capstone Project Module 1, yaitu:
- Menggunakan Python murni tanpa library tambahan,
- Menerapkan fitur CRUD lengkap,
- Menggunakan regular function untuk setiap menu utama,
- Dan menjaga keterhubungan antar fitur serta keterbacaan kode.
- Program ini dapat dikembangkan lebih lanjut, misalnya dengan menambahkan penyimpanan data ke file .csv atau fitur pemesanan pelanggan.

Dibuat oleh:
Akbar Rahmatullah Adhiputra
Dalam rangka Purwadhika Capstone Project Module 1
2025
