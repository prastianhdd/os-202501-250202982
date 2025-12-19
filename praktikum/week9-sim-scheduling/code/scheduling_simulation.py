import csv

data = 'dataset.csv'

# 1. Membaca Data 
proses_list = []
try:
    with open (data, 'r') as file:
        reader = csv.DictReader(file)
        for baris in reader:
            proses_list.append({
            'id' : baris['Proses'],
            'at' : int(baris['Arrival Time']),
            'bt' : int(baris['Burst Time']),
            'start' : 0,
            'finish' : 0,
            'tat' : 0,
            'wt' : 0
        })
except FileNotFoundError:
    print(f"File {data} tidak ditemukan")
    exit()

proses_list.sort(key=lambda x: x['at'])

# 2. Simulasi 
print("\nLog Eksekusi - FCFS ")
waktu_sekarang = 0

for p in proses_list:
    if waktu_sekarang < p['at']:
        print(f" Waktu {waktu_sekarang} - {p['at']}: CPU Idle (Menunggu proses datang)")
        waktu_sekarang = p['at']

    p['start'] = waktu_sekarang
    print(f" Waktu {p['start']}: {p['id']} Mulai dieksekusi")
    
    # Proses berjalan... (waktu bertambah sesuai Burst Time)
    waktu_sekarang += p['bt']
    
    p['finish'] = waktu_sekarang
    print(f" Waktu {p['finish']}: {p['id']} Selesai dieksekusi")
    
    p['tat'] = p['finish'] - p['at']
    p['wt'] = p['tat'] - p['bt']

# 3. Output Tabel
print(f"\n\n{'Proses':<6} | {'AT':<4} | {'BT':<4} | {'Mulai':<6} | {'Selesai':<8} | {'TAT':<5} | {'WT':<5}")
print("-" * 55 )

total_tat = 0
total_wt = 0

for p in proses_list:
    print(f"{p['id']:<6} | {p['at']:<4} | {p['bt']:<4} | {p['start']:<6} | {p['finish']:<8} | {p['tat']:<5} | {p['wt']:<5}")
    total_tat += p['tat']
    total_wt += p['wt']

print("-" * 55)
rata_tat = total_tat / len(proses_list)
rata_wt = total_wt / len(proses_list)

print(f"\nRata-rata Turnaround Time : {rata_tat} ms")
print(f"Rata-rata Waiting Time    : {rata_wt} ms\n")