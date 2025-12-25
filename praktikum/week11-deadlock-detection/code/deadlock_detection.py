import csv
import time
from colorama import Fore, Back, Style, init

# Inisialisasi colorama untuk pewarnaan terminal
init(autoreset=True)

def baca_data_persimpangan(nama_file):
    """Fungsi untuk membaca data posisi dan tujuan mobil dari file CSV."""
    daftar_kendaraan = []
    try:
        with open(nama_file, mode='r') as file:
            pembaca = csv.DictReader(file)
            for baris in pembaca:
                daftar_kendaraan.append(baris)
    except FileNotFoundError:
        print(Fore.RED + f"Kesalahan: File {nama_file} tidak ditemukan!")
    return daftar_kendaraan

def cek_macet_melingkar(peta_tunggu, mobil_sekarang, sudah_dicek, antrean_pantau):
    """Mencari apakah ada kendaraan yang saling mengunci dalam lingkaran."""
    sudah_dicek.add(mobil_sekarang)
    antrean_pantau.add(mobil_sekarang)

    for mobil_di_depan in peta_tunggu.get(mobil_sekarang, []):
        if mobil_di_depan not in sudah_dicek:
            if cek_macet_melingkar(peta_tunggu, mobil_di_depan, sudah_dicek, antrean_pantau):
                return True
        elif mobil_di_depan in antrean_pantau:
            return True

    antrean_pantau.remove(mobil_sekarang)
    return False

def simulasi_deteksi():
    print(Style.BRIGHT + Fore.CYAN + "\nSISTEM MONITORING PERSIMPANGAN JALAN")
    
    catatan = baca_data_persimpangan('dataset_deadlock.csv')
    if not catatan:
        return

    # Tahap 1: Memetakan siapa yang ada di jalur mana
    # Allocation = Jalur yang sedang ditempati
    posisi_jalan = {baris['Allocation']: baris['Proses'] for baris in catatan}
    
    # Tahap 2: Menganalisis pergerakan dan hambatan
    siapa_menunggu_siapa = {}
    print(Fore.YELLOW + "\n[!] Polisi memantau pergerakan:")
    
    for baris in catatan:
        mobil = baris['Proses']
        jalur_asal = baris['Allocation']
        jalur_tujuan = baris['Request']
        
        # Narasi detail sesuai permintaan: Mobil A di jalur X ingin ke jalur Y
        print(f"   {Fore.WHITE}{mobil} berada di {Fore.GREEN}{jalur_asal} {Fore.WHITE}ingin ke {Fore.BLUE}{jalur_tujuan}")
        
        if jalur_tujuan in posisi_jalan:
            penghalang = posisi_jalan[jalur_tujuan]
            siapa_menunggu_siapa[mobil] = [penghalang]
            print(f"     {Fore.RED}>> Tertahan! {jalur_tujuan} sedang diisi oleh {Fore.MAGENTA}{penghalang}")
        else:
            print(f"     {Fore.GREEN}>> Jalur tujuan kosong.")
        
        time.sleep(0.5)

    # Tahap 3: Deteksi lingkaran (Deadlock)
    print(Fore.YELLOW + "\n[!] Memeriksa potensi macet melingkar...")
    kendaraan_terjebak = []
    semua_mobil = [baris['Proses'] for baris in catatan]

    for mobil in semua_mobil:
        if cek_macet_melingkar(siapa_menunggu_siapa, mobil, set(), set()):
            kendaraan_terjebak.append(mobil)
    
    # Tahap 4: Kesimpulan akhir
    print("\nKESIMPULAN OPERASI:")
    if kendaraan_terjebak:
        print(Back.RED + Fore.WHITE + Style.BRIGHT + " STATUS: TERDETEKSI DEADLOCK ")
        print(f"Kendaraan yang saling mengunci: {Fore.RED}{', '.join(kendaraan_terjebak)}")
        print(Fore.RED + "Tindakan: Diperlukan derek paksa untuk mengurai kemacetan.")
    else:
        print(Back.GREEN + Fore.BLACK + Style.BRIGHT + " STATUS: LALU LINTAS AMAN ")
        print(Fore.GREEN + "Keterangan: Semua kendaraan dapat bergerak lancar.")

if __name__ == "__main__":
    simulasi_deteksi()