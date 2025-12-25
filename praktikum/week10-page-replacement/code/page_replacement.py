import os

# --- KONFIGURASI ---
nama_file = 'reference_string.txt'
jumlah_frame = 3

# --- FUNGSI BANTUAN (Untuk print tabel rapi) ---
def cetak_langkah(step, page, status, frames):
    # Mengubah list frame menjadi string format "[ 7 0 1 ]"
    frame_str = " ".join(str(x) for x in frames)
    # Jika frame masih kosong, isi spasi agar rapi
    if len(frames) < jumlah_frame:
        sisa = jumlah_frame - len(frames)
        frame_str += " -" * sisa
        
    print(f"| {step:<3} |  {page:<4} | {status:<10} | [ {frame_str} ]")

# --- LOAD DATASET ---
pages = []
try:
    with open(nama_file, 'r') as f:
        content = f.read().strip()
        # Mengubah string "7, 0, 1" menjadi list integer [7, 0, 1]
        pages = [int(x.strip()) for x in content.split(',')]
except FileNotFoundError:
    print(f"File {nama_file} tidak ditemukan di folder code/!")
    exit()

print(f"\nDataset Loaded: {pages}")
print(f"Jumlah Frame  : {jumlah_frame}")


# ==========================================
# SIMULASI 1: FIFO (First-In First-Out)
# ==========================================
print("\n" + "="*50)
print(f"{'SIMULASI FIFO (First-In First-Out)':^50}")
print("="*50)
print(f"| {'No':<3} | {'Page':<4} | {'Status':<10} | {'Isi Frame (Memori)':<15}")
print("-" * 50)

frames_fifo = []
fifo_faults = 0
pointer = 0  # Penunjuk indeks mana yang akan diganti (0, 1, atau 2)

# Karena kita ingin simulasi fisik frame yang tetap, kita inisialisasi dengan -1 (kosong)
# tapi untuk visualisasi list python, kita main append/replace saja agar mudah.
# Di sini saya pakai pendekatan list sederhana.

frames_fifo = [] 

for i, page in enumerate(pages):
    status = ""
    
    # Cek apakah page sudah ada di frame (HIT)
    if page in frames_fifo:
        status = "HIT"
    else:
        status = "MISS"
        fifo_faults += 1
        
        # Jika frame belum penuh, masukkan saja
        if len(frames_fifo) < jumlah_frame:
            frames_fifo.append(page)
        else:
            # Jika penuh, ganti halaman yang ditunjuk pointer
            frames_fifo[pointer] = page
            # Geser pointer secara memutar (0 -> 1 -> 2 -> 0 -> ...)
            pointer = (pointer + 1) % jumlah_frame
            
    cetak_langkah(i+1, page, status, frames_fifo)

print("-" * 50)
print(f"Total Page Fault FIFO: {fifo_faults}")


# ==========================================
# SIMULASI 2: LRU (Least Recently Used)
# ==========================================
print("\n" + "="*50)
print(f"{'SIMULASI LRU (Least Recently Used)':^50}")
print("="*50)
print(f"| {'No':<3} | {'Page':<4} | {'Status':<10} | {'Isi Frame (Stack Visual)'}")
print("-" * 50)
# Catatan: Untuk LRU, urutan list di bawah menggambarkan urutan penggunaan.
# Paling KIRI (indeks 0) = Paling Jarang Dipakai (Least Recent) -> Siap diganti
# Paling KANAN (indeks akhir) = Baru Saja Dipakai (Most Recent)

frames_lru = []
lru_faults = 0

for i, page in enumerate(pages):
    status = ""
    
    if page in frames_lru:
        status = "HIT"
        # Logika LRU: Jika terpakai, pindahkan ke posisi paling kanan (Most Recent)
        frames_lru.remove(page)
        frames_lru.append(page)
    else:
        status = "MISS"
        lru_faults += 1
        
        if len(frames_lru) < jumlah_frame:
            frames_lru.append(page)
        else:
            # Jika penuh, hapus yang paling kiri (paling lama tak dipakai)
            frames_lru.pop(0)
            frames_lru.append(page)
            
    cetak_langkah(i+1, page, status, frames_lru)

print("-" * 50)
print(f"Total Page Fault LRU : {lru_faults}")


# ==========================================
# KESIMPULAN
# ==========================================
print("\n=== PERBANDINGAN ===")
print(f"FIFO Page Faults: {fifo_faults}")
print(f"LRU Page Faults : {lru_faults}")

if lru_faults < fifo_faults:
    print(">> Algoritma LRU lebih efisien pada dataset ini.")
elif fifo_faults < lru_faults:
    print(">> Algoritma FIFO lebih efisien pada dataset ini.")
else:
    print(">> Kedua algoritma memiliki performa sama.")