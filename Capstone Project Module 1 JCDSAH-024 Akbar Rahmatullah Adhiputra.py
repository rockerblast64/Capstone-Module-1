# CAPSTONE PROJECT MODULE 1
# CASE STUDY: RENTAL MOBIL

# Data (3 Mobil)
data_mobil = [
    {'nama': 'Avanza', 'merk': 'Toyota', 'tahun': 2020, 'harga': 300000},
    {'nama': 'Brio', 'merk': 'Honda', 'tahun': 2019, 'harga': 250000},
    {'nama': 'Xenia', 'merk': 'Daihatsu', 'tahun': 2021, 'harga': 280000}
]

# READ MENU
def read_menu():
    while True:
        print("\n=== DAFTAR MOBIL ===")
        print("1. Tampilkan semua data mobil")
        print("2. Cari data mobil berdasarkan nama")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            print("\nDaftar Mobil:")
            for mobil in data_mobil:
                print(f"- {mobil['nama']} | {mobil['merk']} | {mobil['tahun']} | Rp{mobil['harga']}/hari")
            print()
        elif pilihan == '2':
            if not data_mobil:
                print("Data tidak ditemukan.\n")
            else:
                nama = input("Masukkan nama mobil yang ingin dicari: ").title()
                ditemukan = False
                for mobil in data_mobil:
                    if mobil['nama'] == nama:
                        print(f"{mobil['nama']} | {mobil['merk']} | {mobil['tahun']} | Rp{mobil['harga']}/hari\n")
                        ditemukan = True
                        break
                if not ditemukan:
                    print("Data tidak ditemukan.\n")
        elif pilihan == '3':
            print("Kembali ke Menu Utama...\n")
            break
        else:
            print("Data yang dimasukkan tidak valid.\n")

# CREATE MENU
def create_menu():
    while True:
        print("\n=== TAMBAH MOBIL ===")
        print("1. Tambah data mobil baru")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-2): ")

        if pilihan == '1':
            nama = input("Masukkan nama mobil (primary key): ").title()
            # Cek duplikasi
            for mobil in data_mobil:
                if mobil['nama'] == nama:
                    print("Data sudah ada.\n")
                    break
            else:
                merk = input("Masukkan merk mobil: ").title()
                tahun = int(input("Masukkan tahun pembuatan: "))
                harga = int(input("Masukkan harga sewa per hari: "))

                simpan = input("Simpan data? (y/n): ").lower()
                if simpan == 'y':
                    data_mobil.append({'nama': nama, 'merk': merk, 'tahun': tahun, 'harga': harga})
                    print("Data successfully saved.\n")
                else:
                    print("Data tidak disimpan.\n")
        elif pilihan == '2':
            print("Kembali ke Menu Utama...\n")
            break
        else:
            print("Data yang dimasukkan tidak valid.\n")

# UPDATE MENU
def update_menu():
    while True:
        print("\n=== UPDATE DATA MOBIL ===")
        print("1. Ubah data mobil")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-2): ")

        if pilihan == '1':
            nama = input("Masukkan nama mobil (primary key): ").title()
            mobil_ditemukan = None
            for mobil in data_mobil:
                if mobil['nama'] == nama:
                    mobil_ditemukan = mobil
                    break

            if not mobil_ditemukan:
                print("Data yang dicari tidak ada.\n")
                continue

            print(f"Data ditemukan: {mobil_ditemukan['nama']} | {mobil_ditemukan['merk']} | {mobil_ditemukan['tahun']} | Rp{mobil_ditemukan['harga']}/hari")
            lanjut = input("Lanjutkan update? (y/n): ").lower()
            if lanjut == 'y':
                kolom = input("Masukkan nama kolom yang ingin diubah (nama/merk/tahun/harga): ").lower()

                # Jika user ingin mengubah kolom nama
                if kolom == 'nama':
                    nama_baru = input("Masukkan nama baru: ").title()
                    # Cek apakah nama baru sudah digunakan mobil lain
                    for mobil in data_mobil:
                        if mobil['nama'] == nama_baru and mobil is not mobil_ditemukan:
                            print("Nama tersebut sudah digunakan mobil lain.\n")
                            break
                    else:
                        konfirmasi = input(f"Yakin ubah nama '{mobil_ditemukan['nama']}' menjadi '{nama_baru}'? (y/n): ").lower()
                        if konfirmasi == 'y':
                            mobil_ditemukan['nama'] = nama_baru
                            print("Nama mobil berhasil diperbarui.\n")
                        else:
                            print("Update dibatalkan.\n")

                elif kolom in mobil_ditemukan:
                    nilai_baru = input("Masukkan nilai baru: ")
                    if kolom in ['tahun', 'harga']:
                        nilai_baru = int(nilai_baru)
                    konfirmasi = input("Update data? (y/n): ").lower()
                    if konfirmasi == 'y':
                        mobil_ditemukan[kolom] = nilai_baru
                        print("Data berhasil diupdate.\n")
                    else:
                        print("Update dibatalkan.\n")
                else:
                    print("Kolom tidak ditemukan.\n")
            else:
                print("Update dibatalkan.\n")

        elif pilihan == '2':
            print("Kembali ke Menu Utama...\n")
            break
        else:
            print("Data yang dimasukkan tidak valid.\n")

# DELETE MENU
def delete_menu():
    while True:
        print("\n=== HAPUS MOBIL ===")
        print("1. Hapus data mobil")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-2): ")

        if pilihan == '1':
            nama = input("Masukkan nama mobil (primary key): ").title()
            for mobil in data_mobil:
                if mobil['nama'] == nama:
                    konfirmasi = input(f"Yakin ingin menghapus '{nama}'? (y/n): ").lower()
                    if konfirmasi == 'y':
                        data_mobil.remove(mobil)
                        print("Data berhasil dihapus.\n")
                    else:
                        print("Penghapusan dibatalkan.\n")
                    break
            else:
                print("Data yang dicari tidak ada.\n")

        elif pilihan == '2':
            print("Kembali ke Menu Utama...\n")
            break
        else:
            print("Data yang dimasukkan tidak valid.\n")

# MAIN MENU
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

# EKSEKUSI PROGRAM
main_menu()