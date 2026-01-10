# page_replacement.py
def load_ram_data(filename):
    file = open(filename, "r")
    content = file.read().strip()
    file.close()

    apps_raw = content.split(",")
    apps = []
    for app in apps_raw:
        apps.append(app.strip())
        
    return apps

def simulasi_ram_hp(apps, capacity):
    print("\n" + "="*70)
    print(f"       SIMULASI RAM HP (Kapasitas: {capacity} Aplikasi)")
    print("="*70)
    
    ram = []
    force_close_count = 0
    
    # Kolom Isi RAM 
    print(f"{'Aplikasi Buka':<15} | {'Isi RAM (Background)':<50} | {'Keterangan'}")
    print("-" * 85)
    
    for app in apps:
        status = "Buka (Lancar)"
        
        found = False
        for installed in ram:
            if installed == app:
                found = True
        
        if found == False:
            if len(ram) < capacity:
                ram.append(app)
                status = "Loading Baru..."
            else:
                korban = ram.pop(0)
                ram.append(app)
                status = f"PENUH! Tutup {korban}"
                force_close_count = force_close_count + 1
        else:
            status = "Sudah di RAM (Cepat)"
        
        # Tampilkan list RAM 
        ram_display = str(ram)
        print(f"{app:<15} | {ram_display:<50} | {status}")
    
    print("-" * 85)
    print(f"Total Aplikasi Ditutup Paksa (Page Fault): {force_close_count}")
    print("\n")