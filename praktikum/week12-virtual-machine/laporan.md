
# Tugas Praktikum Minggu 12  
Topik: Virtualisasi Menggunakan Virtual Machine  

---

## Identitas
- **Nama**  : Prastian Hidayat  
- **NIM**   : 250202982
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).  
2. Membuat dan menjalankan sistem operasi guest di dalam VM.  
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).  
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.  
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori

1.  **Virtualisasi (Virtualization)**
   
    Virtualisasi adalah teknologi yang memungkinkan satu komputer fisik (Host) untuk menjalankan beberapa sistem operasi (Guest) secara bersamaan dengan membagi sumber daya *hardware* secara efisien. Ini menciptakan lapisan abstraksi antara *hardware* fisik dan sistem operasi.

2.  **VirtualBox**
   
    VirtualBox adalah perangkat lunak virtualisasi yang memungkinkan pengguna menciptakan mesin virtual untuk menjalankan satu atau lebih sistem operasi tambahan secara bersamaan di dalam satu komputer fisik. Fungsi utamanya adalah menyediakan lingkungan terisolasi untuk menguji perangkat lunak, mempelajari instalasi sistem operasi yang berbeda (seperti Linux di dalam Windows), serta memfasilitasi pengembangan aplikasi lintas platform tanpa risiko merusak sistem operasi utama.

3.  **Host OS vs Guest OS**
    * **Host OS:** Sistem operasi fisik yang menjalankan komputer (Windows 11).
    * **Guest OS:** Sistem operasi virtual yang berjalan di dalam *container* virtual (Ubuntu Linux).

4.  **Isolasi Resource & Sandboxing**
   
    Virtualisasi menyediakan mekanisme keamanan di mana kerusakan pada Guest OS (misalnya terkena virus atau *crash*) tidak akan memengaruhi Host OS. Setiap VM berjalan dalam lingkungan terisolasi (*sandbox*) yang memiliki jatah CPU dan RAM sendiri.

---

## Langkah Praktikum

Saya memilih untuk menjalankan Virtual OS Linux Ubuntu 24.04 LTS Dekstop, maka dari itu langkah praktikum sebagai berikut :

### A. Persiapan & Instalasi
1.  Mengunduh file ISO **Ubuntu 24.04 Desktop** dan aplikasi **Oracle VirtualBox**.
    -  **Ubuntu 24.04 Desktop** : https://ubuntu.com/download/desktop
    -  **Oracle VirtualBox** : https://download.virtualbox.org/virtualbox/7.2.4/VirtualBox-7.2.4-170995-Win.exe
2.  Menginstal VirtualBox pada Dekstop (Host OS).

### B. Konfigurasi Awal (High Resource)
1.  Membuat Virtual Machine baru dengan nama `Linux-Ubuntu`.
2.  Mengatur spesifikasi awal VM:
    * **RAM:** 4096 MB (4 GB).
    * **CPU:** 2 Core.
3.  Menjalankan VM dan menunggu proses instalasi Ubuntu selesai hingga masuk ke desktop.

### C. Eksperimen VM Linux Ubuntu 24.04 LTS
1.  Setelah Konfigurasi selesai, klik open untuk membuka Virtual Machine
2.  Membuka **Terminal** dan menjalankan perintah dasar untuk mengecek spesifikasi sistem.
3.  Membuka aplikasi **Firefox** dan memutar video YouTube serta membuka 5 tab sekaligus untuk memberikan beban kerja (*stress test*).
4.  Membuka **System Monitor** untuk memantau grafik penggunaan RAM dan CPU saat beban tinggi.

### D. Eksperimen VM Mengurangi Resource
1.  Mematikan VM (*Shutdown*).
2.  Masuk ke menu **Settings > System** di VirtualBox.
3.  Menurunkan alokasi resource menjadi:
    * **RAM:** 2048 MB (2 GB).
    * **CPU:** 1 Core.
4.  Menyalakan kembali VM dan mengulangi pengujian dengan membuka Firefox.
5.  Mengamati terjadinya penurunan performa (*lag*) dan peningkatan penggunaan memori hingga mendekati batas maksimal.

### D. Analisis dan Dokumentasi
1. Mencatat proses praktikum dari awal persiapan hingga akhir.
2. Screenshot hasil instalasi virtual box kemudian simpan di `screenshors/instalasi_vm.png`
3. Screenshot hasil konfigurasi Virtual Machine Linux Ubuntu 24.04 LTS dan simpan di `screenshots/konfigurasi_resource.png`
4. Screenshot hasil eksperimen di OS Guest dan simpan di `screenshots/os_guest_running.png`
5. Mencatat konfigurasi Spesifikasi Host OS dan Spefisikasi Guest OS kemudian simpan di code/`catatan_konfigurasi`

### E. Commit & Push
   ```bash
   git add .
   git commit -m "Minggu 12 - Virtual Machine"
   git push origin main
   ```

---


## Kode / Perintah
Berikut adalah perintah terminal yang dijalankan untuk verifikasi sistem di dalam Ubuntu:

```bash
# Mengecek user yang sedang aktif
whoami

# Menampilkan informasi detail kernel dan arsitektur sistem
uname -a

# Menampilkan daftar file di direktori saat ini
ls

# Mengecek penggunaan Memori (RAM) 
free -h
```

## Hasil Eksekusi

Berikut adalah dokumentasi bukti keberhasilan instalasi dan pengujian resource pada Virtual Machine.

### 1. Persiapan dan Instalasi
Proses menginstall Oracle Virtual Box untuk persiapan dalam pembuatan Virtual Machine.

<p align="center">
  <img src="./screenshots/instalasi_vm.png" alt="Instalasi VirtualBox" width="550"/>
</p>

### 2. Konfigurasi & Instalasi VM
Proses pembuatan mesin virtual menggunakan fitur *Unattended Install* di VirtualBox untuk otomatisasi instalasi Ubuntu.
<p align="center">
  <img src="./screenshots/konfigurasi_resource.png" alt="Konfigurasi VM" width="550"/>
</p>

### 2. Eksperimen VM Linux Ubuntu 24.04 LTS
Pengecekan spesifikasi menggunakan perintah `uname -a` (cek kernel) dan `free -h` (cek RAM).

Terlihat total RAM yang terbaca adalah 3.8Gi (4GB).

Pengujian beban kerja dengan membuka 5 tab Firefox (YouTube dan GitHub).
- **Hasil:** RAM terpakai mencapai **92.2% (3.8 GB)**.
- **Kondisi:** Sistem masih berjalan responsif dan lancar meskipun penggunaan memori hampir penuh.

<p align="center">
  <img src="./screenshots/os_guest_running.png" alt="OS Guest Running" width="550"/>
</p>

### 3. Stress Test (Skenario Low Resource : RAM 2 GB)
Setelah proses mengurangi Resource , kemudian membuka lagi VM dan membuka system manager, terlihat belum menjalankan aplikasi lain sudah memakan RAM 1.4 GB ( 62% ).
<p align="center">
  <img src="./screenshots/vm_resource.jpg" alt="Mengurangi Resource" width="500"/>
</p>

Saat menggunakan RAM 4GB, membuka 5 tab berjalan lancar meski RAM terpakai 90%. Namun, saat RAM diturunkan menjadi 2GB, sistem menjadi sangat lambat (lag) dan Firefox sering not responding karena kehabisan memori.
<p align="center">
  <img src="./screenshots/firefox.jpg" alt="Firefox" width="500"/>
</p>

### 4. Catatan Konfigurasi
   ```text
   A. SPESIFIKASI HOST (KOMPUTER ASLI)
   -----------------------------------------------------
   OS Host         : Windows 11
   RAM Host        : 64 GB
   Software VM     : Oracle VirtualBox 7.2.4
   File ISO        : Ubuntu 24.04 Desktop AMD64

   B. IDENTITAS GUEST OS
   -----------------------------------------------------
   Nama VM         : Linux-Ubuntu
   OS Guest        : Ubuntu 24.04 LTS
   Username        : vboxuser
   Password        : 1234
   Hostname        : Linux-Ubuntu

   C. SKENARIO PENGUJIAN RESOURCE
   -----------------------------------------------------
   Skenario 1: Konfigurasi Normal (High Performance)
   - Base Memory (RAM) : 4096 MB (4 GB)
   - Processor (CPU)   : 2 Core
   - Base Disk Memory  : 25 GB
   - Video Memory      : 128 MB
   - Hasil Test        : Lancar membuka 5 tab Firefox.

   Skenario 2: Konfigurasi Rendah (Low Performance)
   - Base Memory (RAM) : 2048 MB (2 GB)
   - Processor (CPU)   : 1 Core
   - Base Disk Memory  : 25 GB
   - Hasil Test        : Terjadi lag signifikan, Firefox lambat merespons.
   ```
---

## Analisis

Berdasarkan percobaan instalasi dan pengujian *stress test* pada Virtual Machine Ubuntu 24.04, berikut adalah analisis mengenai perilaku sistem operasi dalam lingkungan virtual:

### 1. Analisis Manajemen Memori (Memory Management)
Dari pengujian menggunakan Firefox dengan 5 tab aktif (YouTube video playback & Web browsing), terlihat adanya perbedaan signifikan pada manajemen memori:

* **Pemanfaatan RAM Fisik (Physical RAM Usage):**
    Pada konfigurasi 4GB (4096 MB), System Monitor menunjukkan penggunaan memori mencapai **92.2% (sekitar 3.5 GB terpakai)**. Meskipun angka ini terlihat kritis, sistem masih berjalan lancar (*smooth*). Hal ini menunjukkan bahwa kernel Linux Ubuntu mampu memprioritaskan proses aktif (Firefox) di memori utama.
    
* **Peran Virtual Memory (Swap Space):**
    Ketika percobaan dilakukan pada resource rendah (2GB RAM - *berdasarkan skenario pembanding*), terjadi fenomena **Bottleneck**. Karena RAM fisik penuh, Kernel Linux terpaksa memindahkan data dari aplikasi yang tidak aktif ke *Swap Space* (partisi di harddisk). Proses perpindahan data dari RAM (kecepatan tinggi) ke Disk (kecepatan rendah) inilah yang menyebabkan sistem terasa lambat (*lagging*) atau macet. Peristiwa ini dalam teori Sistem Operasi dikenal sebagai **Thrashing**, di mana OS sibuk melakukan *paging* data daripada mengeksekusi instruksi CPU.

### 2. Analisis Processor & Scheduling
Penggunaan konfigurasi **2 Core CPU** pada percobaan utama memberikan dampak signifikan pada kemampuan multitasking:

* **Multithreading:**
    Firefox modern adalah aplikasi *multi-process*. Dengan dialokasikannya 2 Core, *CPU Scheduler* pada Ubuntu dapat membagi beban *render* video YouTube ke satu core, dan proses sistem background ke core lainnya secara paralel.
* **Context Switching:**
    Jika dibandingkan dengan konfigurasi 1 Core, sistem dengan 2 Core memiliki *overhead* yang lebih rendah saat melakukan *context switching*. Pada 1 Core, CPU harus berpindah-pindah tugas dengan sangat cepat antara melayani Firefox dan melayani kernel OS, yang mengakibatkan latensi input (mouse patah-patah) saat beban kerja tinggi.

### 3. Analisis Mekanisme Virtualisasi (Hypervisor Role)
Hasil perintah terminal `uname -a` dan `free -h` membuktikan cara kerja **Type-2 Hypervisor** (VirtualBox):

* **Abstraksi Hardware:**
    Guest OS (Ubuntu) mendeteksi bahwa ia memiliki akses eksklusif ke RAM 4GB dan CPU tertentu. Padahal secara fisik, hardware tersebut adalah milik Host OS (Windows 11). VirtualBox bertindak sebagai perantara yang menipu Guest OS agar merasa berjalan di atas hardware fisik ("Bare Metal"), padahal ia berjalan di atas software.
* **Isolasi Kegagalan (Fault Isolation):**
    Saat Ubuntu mengalami beban puncak (High Load), Task Manager di Windows (Host) memang akan menunjukkan kenaikan penggunaan RAM. Namun, jika Ubuntu mengalami *Crash* atau *Hang*, Windows tidak akan ikut error (BSOD). Ini membuktikan bahwa memori yang dialokasikan untuk VM benar-benar terisolasi dalam *sandbox* yang aman.

---

## Kesimpulan
Berdasarkan percobaan di atas, dapat disimpulkan bahwa:
 
1. **Pengaruh RAM pada Performa:** Pada konfigurasi 4GB RAM, Ubuntu berjalan lancar meskipun penggunaan memori tinggi (90%+) saat multitasking. Namun, saat resource diturunkan menjadi 2GB , sistem operasi mengalami bottleneck. Aplikasi Firefox menjadi sangat lambat dibuka dan sering mengalami not responding karena sistem kehabisan memori fisik.

2. **Peran Hypervisor:** VirtualBox berhasil membagi resource CPU fisik saya. Terbukti saat saya memberikan 2 Core ke VM, Ubuntu hanya mendeteksi 2 CPU, meskipun laptop asli saya memiliki lebih dari itu. Ini membuktikan fungsi abstraksi hardware berjalan dengan baik.

3. **Isolasi Sistem:** Aktivitas berat yang dilakukan di dalam Guest OS (Ubuntu) memang memakan resource RAM laptop asli, namun file sistem antara Windows dan Ubuntu tetap terpisah total.

---

## Quiz

1. **Apa perbedaan antara host OS dan guest OS?**
   
   **Jawaban:**

   * **Host OS:** Sistem operasi utama yang berjalan langsung di fisik laptop/komputer (contoh: Windows 11 saya).
   * **Guest OS:** Sistem operasi virtual yang berjalan "menumpang" di dalam aplikasi VirtualBox (contoh: Ubuntu).

2. **Apa peran hypervisor dalam virtualisasi?**
   
   **Jawaban:**

   Hypervisor (seperti VirtualBox) berperan sebagai **pengelola**. Tugas utamanya adalah membagi sumber daya fisik (seperti RAM dan CPU) dari komputer asli agar bisa digunakan oleh mesin virtual.

3. **Mengapa virtualisasi meningkatkan keamanan sistem?**
   
   **Jawaban:**

   Karena virtualisasi menerapkan konsep **Isolasi (Sandboxing)**. Segala aktivitas di dalam mesin virtual terkurung di lingkungannya sendiri. Jadi, jika Guest OS terkena virus atau rusak, komputer utama (Host) tetap aman dan tidak ikut rusak.

---

## Refleksi Diri
Tuliskan secara singkat:
- **Apa bagian yang paling menantang minggu ini?**
  
  Tidak ada, tetapi lumayan memakan waktu karena mendownload ISO Linux 24.04 ukuran 6 GB.
- **Bagaimana cara Anda mengatasinya?**  

-----

**Credit:** *Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa*