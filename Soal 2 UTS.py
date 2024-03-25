import datetime

def main():
    jumlah_hari = int(input("Masukkan jumlah hari dari hari ini: "))

    hari_ini = datetime.date.today()

    tanggal_hasil = hari_ini + datetime.timedelta(days=jumlah_hari)

    nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

    nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
                  "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

    hari = nama_hari[tanggal_hasil.weekday()]
    tanggal = tanggal_hasil.day
    bulan = nama_bulan[tanggal_hasil.month - 1]
    tahun = tanggal_hasil.year

    print(f"Pada tanggal {tanggal} {bulan} {tahun} jatuh pada hari {hari}.")

if __name__ == "__main__":
    main()
