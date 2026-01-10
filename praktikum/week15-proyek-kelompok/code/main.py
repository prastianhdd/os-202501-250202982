import os
import sys

# Import fungsi yang baru kita buat
from cpu_scheduling import load_download_data, simulasi_download_fcfs
from page_replacement import load_ram_data, simulasi_ram_hp

def main():
    while True:
        print("=== SIMULASI OS SEDERHANA ===")
        print("1. Simulasi Download Manager (FCFS)")
        print("2. Simulasi RAM HP (Multitasking)")
        print("3. Keluar")
        
        choice = input("Pilih menu: ")

        if choice == '1':
            filename = 'data/processes.csv'
            print("Memuat antrean download dari " + filename + "...")
            # Pastikan isi CSV nanti sesuai (Nama, Waktu, Durasi)
            data = load_download_data(filename)
            if len(data) > 0:
                simulasi_download_fcfs(data)
                
        elif choice == '2':
            filename = 'data/pages.txt'
            print("Memuat riwayat aplikasi dari " + filename + "...")
            data = load_ram_data(filename)
            
            if len(data) > 0:
                cap_str = input("Masukkan kapasitas RAM (Berapa aplikasi bisa jalan bersamaan?): ")
                if cap_str.isdigit():
                    simulasi_ram_hp(data, int(cap_str))
                else:
                    print("Input harus angka.")

        elif choice == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()