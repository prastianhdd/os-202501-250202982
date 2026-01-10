def load_download_data(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    downloads = []
    
    for i in range(1, len(lines)):
        line = lines[i].strip()
        parts = line.split(",")
        # Format: [NamaFile, WaktuKlik, LamaDownload]
        d = [parts[0], int(parts[1]), int(parts[2])]
        downloads.append(d)
        
    return downloads

def simulasi_download_fcfs(downloads):
    n = len(downloads)
    
    # 1. Bubble Sort (Urutkan berdasarkan Waktu Klik)
    for i in range(n):
        for j in range(0, n - i - 1):
            if downloads[j][1] > downloads[j+1][1]:
                temp = downloads[j]
                downloads[j] = downloads[j+1]
                downloads[j+1] = temp

    print("\n" + "="*60)
    print("           SIMULASI ANTREAN DOWNLOAD (FCFS)")
    print("="*60)
    
    # Header Tabel dengan jarak yang pas
    # :<20 artinya rata kiri dengan lebar 20 karakter
    print(f"{'File Name':<25} | {'Waktu':<8} | {'Durasi':<8} | {'Status'}")
    print("-" * 80)

    current_time = 0
    total_wait = 0

    for i in range(n):
        name = downloads[i][0]
        arrival = downloads[i][1]
        burst = downloads[i][2]

        # Jika internet idle
        if current_time < arrival:
            current_time = arrival

        wait = current_time - arrival
        total_wait = total_wait + wait
        
        # Format baris data agar lurus dengan header
        status_msg = f"Sedang download... (Tunggu: {wait}s)"
        print(f"{name:<25} | {arrival:<8} | {str(burst)+'s':<8} | {status_msg}")
        
        current_time = current_time + burst
        
    print("-" * 80)
    print(f"Semua file selesai! Total Waktu : {current_time} detik")
    print(f"Rata-rata Menunggu              : {total_wait / n} detik")
    print("\n")# cpu_schedulling.py