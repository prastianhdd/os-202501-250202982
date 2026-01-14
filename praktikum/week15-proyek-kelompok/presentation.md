# PRESENTASI PROYEK KELOMPOK: MINI SIMULASI OS
**Topik:** CPU Scheduling (FCFS) & Memory Management (FIFO)

**Minggu:** 15

---

## Nama Anggota Kelompok 
- Prastian Hidayat (250202982)
- Gradyan Alannahda Shofari (250202940)
- Awwab Maftuhi (250202920)
- Fatkhurrohman Gilang Ramadhan (250202985)

---
  
## 1. PENDAHULUAN
### Latar Belakang
* Konsep OS (CPU Scheduling & Memory) seringkali abstrak dan sulit dibayangkan.
* Kami membuat aplikasi **Mini Simulasi** dengan analogi sehari-hari agar lebih konkret.

### Studi Kasus
1.  **Simulasi Download Manager**, yang merepresentasikan algoritma *CPU Scheduling* tipe *First-Come First-Served* (FCFS). 
  * Dalam simulasi ini, berkas yang diklik pertama kali akan diproses (diunduh) hingga selesai sebelum sistem beralih ke berkas berikutnya.
2.  **Simulasi RAM HP**, yang memodelkan algoritma *Page Replacement* tipe FIFO (*First-In First-Out*). 
  * Simulasi ini menggambarkan manajemen memori pada ponsel pintar, di mana aplikasi yang paling lama dibuka akan ditutup secara otomatis oleh sistem ketika kapasitas memori (RAM) telah penuh dan pengguna membuka aplikasi baru.

---

## 2. ARSITEKTUR APLIKASI
### Tech Stack
* **Bahasa:** Python (Berbasis CLI/Terminal).
* **Environment:** Docker (Untuk konsistensi / *reproducible*).
* **Version Control:** Git (Branching per fitur).

### Desain Modular
Secara garis besar, arsitektur aplikasi terdiri dari tiga komponen utama:
1.  **Controller Utama (`main.py`):** Bertindak sebagai pintu masuk (*entry point*) aplikasi yang menangani interaksi pengguna, menampilkan menu pilihan, dan memanggil fungsi dari modul yang relevan.
2.  **Modul Logika (*Logic Modules*):** Berkas terpisah yang berisi implementasi algoritma sistem operasi, yaitu `cpu_scheduling.py` untuk penjadwalan CPU dan `page_replacement.py` untuk manajemen memori.
3.  **Manajemen Data (*Data Layer*):** Penyimpanan data input statis dalam bentuk berkas teks (`.csv` dan `.txt`) yang terletak di direktori `data/` untuk dibaca oleh modul logika.

---

## 3. LIVE DEMO

**Skenario Demo:**
1.  **Jalankan Docker:**
    `docker run -it --rm week15-proyek-kelompok`
2.  **Simulasi 1: Download Manager (FCFS)**
    * Input: `processes.csv`
    * Amati: Urutan proses dan waktu tunggu.
3.  **Simulasi 2: RAM HP (FIFO)**
    * Input: `pages.txt`
    * Set Kapasitas RAM: **3 Aplikasi**.
    * Amati: Aplikasi mana yang terkena *Kill/Page Fault*.

---

## 4. HASIL & ANALISIS: CPU SCHEDULING (FCFS)

**Data Uji:**
* MobileLegend (50s), TugasKuliah (10s), Lagu (3s), Film (20s).

**Hasil:**
* **Total Waktu:** 83 detik.
* **Rata-rata Menunggu:** 41.75 detik.

**Analisis:**
* Terjadi fenomena **Convoy Effect**. yang dimana BT Pendek menunggu AT lebih dulu.
* File kecil (`Lagu.mp3`, 3s) terpaksa menunggu sangat lama (58s) karena terhalang file besar (`MobileLegend`) yang datang duluan.
* **Kesimpulan:** FCFS adil secara urutan, tapi tidak efisien untuk *waiting time* jika ada proses besar di awal.

---

## 5. HASIL & ANALISIS: MEMORY (FIFO)

**Data Uji:**
* Urutan Buka: WA, Discord, YT, ML, WA, Discord, IG, YT.
* Kapasitas RAM: 3 Frame.

**Hasil:**
* **Total Page Fault:** 8 kali.

**Analisis:**
* Algoritma FIFO murni melihat waktu masuk.
* Aplikasi yang sering dipakai (`WhatsApp`) tetap dihapus saat RAM penuh hanya karena ia "paling tua" di memori.
* Akibatnya, saat `WhatsApp` dibuka lagi, harus *loading ulang* (Page Fault).
* **Kesimpulan:** FIFO mudah diimplementasi, tapi kurang optimal untuk pola penggunaan aplikasi yang repetitif.

---

## 6. TIM & KONTRIBUSI

Proyek dikerjakan menggunakan Git Flow dengan pembagian peran:

| Nama Anggota | Peran Utama | Deskripsi Kontribusi |
| :--- | :--- | :--- |
| **Prastian Hidayat** | *Project Lead & Integrator* | • Merancang struktur awal proyek dan `main.py`.<br>• Mengelola repositori Git (merge PR, resolve conflict).<br>• Membuat konfigurasi `Dockerfile` agar aplikasi berjalan di container.<br>• Melakukan pengujian fungsional seluruh modul.<br>• Mengumpulkan *screenshot* bukti demo.|
| **Awwab Maftuhi** | *Developer (Modul Scheduling)* | • Mengimplementasikan algoritma FCFS pada `cpu_scheduling.py`.<br>• Menyusun logika *sorting* data berdasarkan waktu kedatangan.<br>• Membuat dataset `processes.csv`. |
| **Fatkhurrohman Gilang Ramadhan** | *Developer (Modul Memory)* | • Mengimplementasikan algoritma FIFO pada `page_replacement.py`.<br>• Membuat visualisasi tabel isi RAM.<br>• Menyusun dataset `pages.txt` dan skenario uji *page fault*. |
| **Gradyan Alannahda Shofari** | *Documentation & QA* | • Menyusun file `README.md` dan dokumentasi cara penggunaan.<br>• Menyusun file dokumen akhir `laporan.md` |

![Kontribusi Kelompok](./screenshots/commits-kelompok.png)

---
**Terima Kasih**
*Ada Pertanyaan?*
