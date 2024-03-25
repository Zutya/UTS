import datetime

def main():
    hari_ini = datetime.date.today()
    
    tanggal = hari_ini.day
    
    hasil_perkalian = 1
    for i in range(1, tanggal + 1):
        hasil_perkalian *= i
    
        print("Hasil yg didapat dari pengalian yg dimulai dari 1 hingga tanggal hari ini ({}) adalah:".format(tanggal), hasil_perkalian)

if __name__ == "__main__":
    main()
