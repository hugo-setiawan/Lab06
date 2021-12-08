# Definisikan konstanta-konstanta
MENIT_DALAM_JAM = 60
MENIT_DALAM_HARI = 60 * 24

HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]
MATKUL_TERSEDIA = [
    ["ddp 1 a",     HARI[0] + JAM[8] + 0,    HARI[0] +  JAM[9] + 40],
    ["ddp 1 a",     HARI[2] + JAM[8] + 0,    HARI[2] +  JAM[9] + 40],
    ["ddp 1 b",     HARI[1] + JAM[8] + 0,    HARI[1] +  JAM[9] + 40],
    ["manbis",      HARI[0] + JAM[9] + 0,    HARI[0] + JAM[10] + 40],
    ["matdis 1 a",  HARI[2] + JAM[9] + 0,    HARI[2] + JAM[10] + 40],
    ["matdis 1 b",  HARI[2] + JAM[9] + 0,    HARI[2] + JAM[10] + 40]
]

NAMA_HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

# Buat list matkul_diambil kosong untuk nanti ditambahkan isinya
# Untuk memudahkan, list matkul_diambil selalu dalam keadaan tersortir ascending berdasarkan start_time dan alfabetis
matkul_diambil = []

# Loop utama program
while True:
    print()
    print("=========== SUSUN JADWAL ===========")
    print("1  Add matkul")
    print("2  Drop matkul")
    print("3  Cek ringkasan")
    print("4  Lihat daftar matkul")
    print("5  Selesai")
    print("====================================")
    print()
    # Terima input operasi dan hilangkan trailing & leading spaces
    operasi = input("Masukkan pilihan: ").lower().strip()
    # Validasi input operasi
    if not operasi.isdigit() or int(operasi) not in range(1, 6):
        print("Maaf, pilihan tidak tersedia")
    else:
        operasi_int = int(operasi)

        # Add matkul
        if operasi_int == 1:
            # Terima input, jadikan lowercase agar case insensitive, dan hilangkan trailing & leading spaces
            matkul_nama = input("Masukkan nama matkul: ").lower().strip()
            # Asumsikan matkul yang diinput tidak tersedia
            matkul_is_tersedia = False
            for member in MATKUL_TERSEDIA:
                # matkul_is_tersedia bernilai True jika ada matkul dengan nama matkul_nama
                if matkul_nama == member[0]:
                    matkul_is_tersedia = True
                    break

            if matkul_is_tersedia:
                # Buatlah list yang berisi tiap list detail pertemuan dari MATKUL_TERSEDIA untuk matkul bernama matkul_nama
                matkul_ditambah = [member for member in MATKUL_TERSEDIA if member[0] == matkul_nama]
                # Tambahkan setiap list detail pertemuan ke dalam list matkul_diambil
                matkul_diambil.extend(matkul_ditambah)
                # Sort matkul_diambil berdasarkan start_time, jika ada yang sama sortir dr nama scr alfabetis
                matkul_diambil.sort(key=lambda x: (x[1],x[0]))
            else:
                print("Matkul tidak ditemukan")

        # Drop matkul
        elif operasi_int == 2:
            # Terima input, jadikan lowercase agar case insensitive, dan hilangkan trailing & leading spaces
            matkul_nama = input("Masukkan nama matkul: ").lower().strip()
            # Asumsikan matkul yang diinput tidak diambil
            matkul_is_diambil = False
            for member in matkul_diambil:
                # matkul_is_diambil bernilai True jika ada matkul diambil dengan nama matkul_nama
                if matkul_nama == member[0]:
                    matkul_is_diambil = True
                    break

            if matkul_is_diambil:
                # Menghapus matkul dengan membuat list baru yang berisikan matkul yang tidak dihapus
                matkul_diambil = [member for member in matkul_diambil if member[0] != matkul_nama]
                # Sort matkul_diambil berdasarkan start_time, jika ada yang sama sortir dr nama scr alfabetis
                matkul_diambil.sort(key=lambda x: (x[1],x[0]))
            else:
                print("Matkul tidak ditemukan")

        # Cek ringkasan (cek bentrok)
        elif operasi_int == 3:
            # Asumsikan tidak ada matkul bentrok
            matkul_is_bentrok = False
            for i in range(len(matkul_diambil)):
                for j in range(len(matkul_diambil)):
                    # Jadwal matkul bentrok jika matkul pertama belum selesai ketika matkul kedua dimulai (end_time > start_time selanjutnya)
                    # Pengecekan dilakukan terhadap semua matkul dgn nama berbeda yang mulai setelah matkul yg dicek (i < j; matkul_diambil sudah terurut ascending berdasarkan start_time)
                    if i < j and matkul_diambil[i][0] != matkul_diambil[j][0] and matkul_diambil[i][2] >= matkul_diambil[j][1]:
                        matkul_is_bentrok = True
                        print(f"    {matkul_diambil[i][0]} bentrok dengan {matkul_diambil[j][0]}")

            if not matkul_is_bentrok:
                print("Tidak ada matkul yang bermasalah")

        # Liat daftar (jadwal) matkul
        elif operasi_int == 4:
            if matkul_diambil == []:
                print("Tidak ada matkul yang diambil")
            else:
                print("daftar matkul:")
                # Karena matkul_diambil sudah terurut ascending berdasar start_time, cukup print tiap elemen
                for member in matkul_diambil:
                    # Hitung human-readable hari, jam, dan menit dari start_time dan end_time
                    start_hari = member[1] // 1440
                    start_hari_name = NAMA_HARI[start_hari] + ","
                    start_jam = member[1] % 1440 // 60
                    start_menit = member[1] % 60
                    end_hari = member[2] // 1440
                    end_hari_name = NAMA_HARI[end_hari] + ","
                    end_jam = member[2] % 1440 // 60
                    end_menit = member[2] % 60
                    print(f"    {member[0].upper():<13} {start_hari_name:<7} {start_jam:02d}.{start_menit:02d}   s/d {end_hari_name:<7} {end_jam:02d}.{end_menit:02d}")

        # Selesai
        elif operasi_int == 5:
            print("Terima kasih!")
            # Break untuk keluar dari loop utama program
            break

# References (in no particular order):
# Slides DDP 1-B
# https://realpython.com/list-comprehension-python/
# https://docs.python.org/3/library/stdtypes.html
# https://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value
# https://stackoverflow.com/questions/18563680/sorting-2d-list-python
# https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes/4233482