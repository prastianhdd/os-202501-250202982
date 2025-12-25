import csv
import time
from colorama import Fore, Back, Style, init

# Inisialisasi colorama
init(autoreset=True)

def baca_data_persimpangan(nama_file):
    daftar_kendaraan = []
    try:
        with open(nama_file, mode='r') as file:
            pembaca = csv.DictReader(file)
            for baris in pembaca:
                daftar_kendaraan.append(baris)
    except FileNotFoundError:
        print(Fore.RED + f"Kesalahan: File {nama_file} tidak ditemukan!")
    return daftar_kendaraan

def cari_siklus(peta_tunggu, mobil_sekarang, sudah_dicek, antrean_pantau):
    sudah_dicek.add(mobil_sekarang)
    antrean_pantau.add(mobil_sekarang)

    for mobil_di_depan in peta_tunggu.get(mobil_sekarang, []):
        if mobil_di_depan not in sudah_dicek:
            if cari_siklus(peta_tunggu, mobil_di_depan, sudah_dicek, antrean_pantau):
                return True
        elif mobil_di_depan in antrean_pantau:
            return True

    antrean_pantau.remove(mobil_sekarang)
    return False

def solusi_kemacetan():
    print(Style.BRIGHT + Fore.CYAN + "\nSISTEM PEMULIHAN KEMACETAN (DEADLOCK RECOVERY)")
    
    catatan = baca_data_persimpangan('dataset_deadlock.csv')
    if not catatan:
        return

    # 1. Deteksi Awal
    posisi_jalan = {baris['Allocation']: baris['Proses'] for baris in catatan}
    siapa_menunggu_siapa = {}
    for baris in catatan:
        mobil = baris['Proses']
        tujuan = baris['Request']
        if tujuan in posisi_jalan:
            siapa_menunggu_siapa[mobil] = [posisi_jalan[tujuan]]

    # Mencari mobil yang terjebak
    terjebak = []
    for mobil in [b['Proses'] for b in catatan]:
        if cari_siklus(siapa_menunggu_siapa, mobil, set(), set()):
            terjebak.append(mobil)

    if not terjebak:
        print(Fore.GREEN + "\n[!] Tidak ada kemacetan yang perlu diatasi.")
        return

    print(Fore.RED + f"\n[!] Terdeteksi kemacetan melingkar pada: {', '.join(terjebak)}")
    time.sleep(1)

    # 2. EKSEKUSI SOLUSI: Memilih Korban (Victim Selection)
    # Kita pilih mobil pertama dalam daftar untuk diderek (Terminasi)
    korban = terjebak[0]
    print(Fore.YELLOW + f"\n[PROSES PEMULIHAN] Memilih {korban} untuk diderek keluar dari persimpangan...")
    time.sleep(1.5)
    
    print(Back.WHITE + Fore.BLACK + f" INFO: {korban} telah diderek keluar. Jalur sekarang terbuka! ")
    time.sleep(1)

    # 3. SIMULASI PERGERAKAN SETELAH SOLUSI
    print(Fore.GREEN + "\n[!] Mencoba menjalankan kembali kendaraan yang tersisa:")
    
    # Mobil yang tersisa (tanpa si korban)
    sisa_mobil = [b for b in catatan if b['Proses'] != korban]
    
    for baris in sisa_mobil:
        mobil = baris['Proses']
        asal = baris['Allocation']
        tujuan = baris['Request']
        
        # Cek apakah jalur tujuan sudah kosong karena si korban sudah pergi
        if tujuan not in [b['Allocation'] for b in sisa_mobil]:
            print(f"   {Fore.WHITE}{mobil} (di {asal}) -> {Fore.GREEN}BERHASIL MAJU {Fore.WHITE}ke {tujuan}")
        else:
            # Jika masih menunggu mobil lain yang belum bergerak
            print(f"   {Fore.WHITE}{mobil} (di {asal}) -> {Fore.YELLOW}Menunggu giliran...")
        time.sleep(0.5)

    print("\nKESIMPULAN SOLUSI:")
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + " STATUS: KEMACETAN BERHASIL DIURAI ")
    print(Fore.CYAN + f"Keterangan: Dengan menghentikan {korban}, kendaraan lain dapat melanjutkan tugasnya.")

if __name__ == "__main__":
    solusi_kemacetan()