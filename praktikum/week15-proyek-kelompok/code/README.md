# README.md
# Mini Simulasi Sistem Operasi

Aplikasi berbasis terminal (CLI) ini dibuat untuk mensimulasikan dua konsep inti Sistem Operasi: **CPU Scheduling** dan **Memory Management**. Proyek ini dikembangkan sebagai Tugas Praktikum Minggu 15.

## Fitur Utama

1.  **Simulasi Download Manager (CPU Scheduling)**
    * **Algoritma:** *First-Come First-Served* (FCFS).
    * **Analogi:** Antrean unduhan file, di mana file yang diklik pertama kali akan diunduh hingga selesai (non-preemptive) sebelum memproses file berikutnya.
    * **Output:** Tabel status unduhan, waktu tunggu (*waiting time*), dan rata-rata waktu tunggu.

2.  **Simulasi RAM HP (Page Replacement)**
    * **Algoritma:** *First-In First-Out* (FIFO).
    * **Analogi:** Manajemen memori pada ponsel. Aplikasi yang dibuka disimpan di RAM. Jika RAM penuh, aplikasi yang paling lama dibuka akan ditutup paksa (*force close*) untuk memberi ruang bagi aplikasi baru.
    * **Output:** Visualisasi isi RAM real-time dan total *page fault*.

---

## Struktur Folder

```text
code/
├── main.py              # Entry point aplikasi (Menu Utama)
├── cpu_scheduling.py    # Modul logika FCFS
├── page_replacement.py  # Modul logika FIFO
├── Dockerfile           # Konfigurasi container Docker
├── README.md            # Dokumentasi ini
└── data/                # Dataset simulasi
    ├── processes.csv    # Data untuk antrean download
    └── pages.txt        # Data riwayat aplikasi
```

---

## Cara Menjalankan
Anda dapat menjalankan aplikasi ini menggunakan dua cara: via Docker (disarankan) atau secara Manual (Python Lokal).

### Cara 1: Menggunakan Docker (Disarankan)
Pastikan Docker Desktop / Docker Engine sudah terinstal dan berjalan.

1. Build Image Buka terminal di dalam folder code/, lalu jalankan:

    ```Bash
    docker build -t week15-proyek-kelompok .
    ```

2. Jalankan Container Gunakan flag -it agar bisa berinteraksi dengan menu aplikasi:

    ```Bash
    docker run -it --rm week15-proyek-kelompok
    ```

### Cara 2: Menjalankan Secara Manual (Local Host)
Pastikan Python 3.x sudah terinstal di komputer Anda.

1. Buka Terminal Arahkan terminal ke direktori code/.

2. Jalankan Script

    ```Bash

    python main.py
    ```
---

## Konfigurasi Dataset
Anda dapat mengubah data simulasi dengan mengedit file di folder data/.

1. data/processes.csv (Untuk Scheduling) 
   - Format: NamaFile,WaktuKlik,LamaDownload

   - Penting: Jangan hapus baris header pertama.

    Contoh Isi File:

    ```
    Process,ArrivalTime,BurstTime
    MobileLegends.apk,0,50
    TugasKuliah.pdf,1,10
    Lagu.mp3,2,3
    Film.mp4,3,20
    ```

1. data/pages.txt (Untuk Memory) 
   - Format: Nama aplikasi dipisahkan koma (tanpa spasi setelah koma disarankan).

    Contoh:

    ```
    WhatsApp,Instagram,TikTok,WhatsApp,YouTube
    ```

    Catatan: Tekan Ctrl+C atau pilih menu Keluar untuk menghentikan aplikasi.