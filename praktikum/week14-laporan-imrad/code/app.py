import platform
import time
import os

def check_system():

    print("PROGRAM PENGUJIAN PERFORMA")
    print("(VM vs Docker Study Case)")
    
    # 1. Cek kita sedang dimana (OS-nya apa)
    print(f"[INFO] Sistem Operasi : {platform.system()}")
    print(f"[INFO] Versi Rilis    : {platform.release()}")
    print(f"[INFO] Versi Node     : {platform.node()}")
    
    # 2. Simulasi Proses (Biar ada waktu buat Screenshot)
    print("[STATUS] Program sedang berjalan...")
    print("[ACTION] SILAKAN CEK TASK MANAGER SEKARANG!")
    print("[ACTION] Ambil screenshot RAM usage...")
    
    # Tahan selama 2000 detik
    for i in range(2000, 0, -1):
        print(f"Sisa waktu: {i} detik...", end='\r')
        time.sleep(1)
        
    print("\n[STATUS] Program Selesai.")
    print("="*40)

if __name__ == "__main__":
    check_system()