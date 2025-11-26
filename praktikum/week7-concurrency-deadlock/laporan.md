# Laporan Praktikum Minggu 7
## Topik: Sinkronisasi Proses dan Masalah Deadlock

---

## Identitas Kelompok
**Nama**  :  
1. Prastian Hidayat (250202982) - (Ketua) - Bagian Implementasi
2. Gradyan Alannahda Shofari(250202940) - Bagian Dokumentasi
3. Awwab Maftuhi(250202920) - Bagian Analisis

**Kelas** : 1IKRB

---

## Tujuan

 - Memahami konsep sinkronisasi proses
Mahasiswa belajar bagaimana proses yang berjalan bersamaan dapat diatur agar tidak saling mengganggu, terutama saat mengakses critical section.
- Mengidentifikasi dan menganalisis masalah deadlock
Praktikum membantu mahasiswa mengenali kondisi yang menyebabkan deadlock (mutual exclusion, hold and wait, no preemption, circular wait) serta dampaknya pada sistem.
- Melatih penerapan mekanisme sinkronisasi
Mahasiswa mencoba menggunakan alat seperti semaphore, mutex, dan monitor untuk mengatur eksekusi proses secara aman.
- Mengembangkan keterampilan pemecahan masalah
Praktikum memberi pengalaman langsung dalam merancang solusi untuk mencegah atau mengatasi deadlock, misalnya dengan algoritma pencegahan atau deteksi.
- Menghubungkan teori dengan praktik nyata
Mahasiswa tidak hanya memahami konsep dari buku, tetapi juga melihat bagaimana sinkronisasi dan deadlock terjadi dalam simulasi atau program nyata.

---

## Dasar Teori
Dalam sistem operasi modern, banyak proses dapat berjalan secara bersamaan untuk memanfaatkan sumber daya komputer secara efisien. Namun, eksekusi paralel ini menimbulkan tantangan berupa potensi konflik ketika beberapa proses mencoba mengakses sumber daya yang sama. Oleh karena itu, konsep sinkronisasi proses menjadi sangat penting. Sinkronisasi adalah mekanisme yang digunakan untuk mengatur interaksi antar proses agar tidak saling mengganggu, terutama ketika mereka memasuki critical section, yaitu bagian kode yang menggunakan sumber daya bersama. Tanpa sinkronisasi, dapat terjadi race condition, yaitu kondisi di mana hasil eksekusi bergantung pada urutan akses proses, sehingga data bisa menjadi tidak konsisten.
Tujuan utama sinkronisasi adalah menjaga konsistensi data, mencegah konflik, dan memastikan eksekusi proses berlangsung secara teratur. Beberapa mekanisme sinkronisasi yang umum digunakan antara lain semaphore, mutex, dan monitor. Semaphore adalah variabel khusus dengan operasi wait dan signal untuk mengatur giliran proses. Mutex berfungsi sebagai kunci eksklusif agar hanya satu proses dapat masuk ke critical section pada satu waktu. Monitor merupakan abstraksi tingkat tinggi yang secara otomatis melindungi critical section dengan prosedur sinkronisasi, sehingga lebih aman dan mudah digunakan.

Selain sinkronisasi, sistem operasi juga menghadapi masalah deadlock. Deadlock adalah kondisi di mana sekumpulan proses tidak dapat melanjutkan eksekusi karena saling menunggu sumber daya yang tidak pernah dilepaskan. Deadlock hanya terjadi jika empat kondisi berikut terpenuhi secara bersamaan:

- Mutual Exclusion – sumber daya hanya dapat digunakan oleh satu proses pada satu waktu.
- Hold and Wait – proses menahan satu sumber daya sambil menunggu sumber daya lain.
- No Preemption – sumber daya tidak dapat diambil paksa dari proses.
- Circular Wait – terdapat rantai proses yang saling menunggu dalam lingkaran.

Dampak deadlock sangat serius karena sistem dapat macet, proses tidak bisa selesai, dan sumber daya menjadi tidak efisien. Untuk mengatasinya, sistem operasi menerapkan strategi seperti pencegahan (menghindari salah satu kondisi penyebab deadlock), deteksi (menggunakan algoritma untuk memeriksa status sistem), dan pemulihan (menghentikan proses atau memaksa pelepasan sumber daya).
Secara keseluruhan, sinkronisasi proses dan penanganan deadlock merupakan dua aspek fundamental dalam sistem operasi. Sinkronisasi memastikan proses paralel berjalan aman dan konsisten, sedangkan pemahaman tentang deadlock membantu mencegah kebuntuan yang dapat mengganggu kinerja sistem. Praktikum mengenai topik ini memberikan kesempatan bagi mahasiswa untuk menghubungkan teori dengan praktik nyata, sehingga mereka dapat memahami dan mengatasi permasalahan yang muncul dalam lingkungan komputasi paralel.


---

## Langkah Praktikum

1. **Persiapan Tim**
   - Bentuk kelompok beranggotakan 3–4 orang.  
   - Tentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).

2. **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**
   - Implementasikan versi sederhana dari masalah *Dining Philosophers* tanpa mekanisme pencegahan deadlock.  
   - Contoh pseudocode:
     ```text
     while true:
       think()
       pick_left_fork()
       pick_right_fork()
       eat()
       put_left_fork()
       put_right_fork()
     ```
   - Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).
   - Identifikasi kapan dan mengapa deadlock terjadi.

3. **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**
   - Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
     - Menggunakan *semaphore (mutex)* untuk mengontrol akses.
     - Membatasi jumlah filosof yang dapat makan bersamaan (max 4).  
     - Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).  
   - Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

4. **Eksperimen 3 – Analisis Deadlock**
   - Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.  
   - Sajikan hasil analisis dalam tabel seperti contoh berikut:

     | Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
     |------------------|---------------------------|------------------------|
     | Mutual Exclusion | Ya (satu garpu hanya satu proses) | Gunakan semaphore untuk kontrol akses |
     | Hold and Wait | Ya | Hindari proses menahan lebih dari satu sumber daya |
     | No Preemption | Ya | Tidak ada mekanisme pelepasan paksa |
     | Circular Wait | Ya | Ubah urutan pengambilan sumber daya |

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua diagram, screenshot simulasi, dan hasil diskusi di:
     ```
     praktikum/week7-concurrency-deadlock/screenshots/
     ```
   - Tuliskan laporan kelompok di `laporan.md` (format IMRaD singkat: *Pendahuluan, Metode, Hasil, Analisis, Diskusi*).

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 7 - Sinkronisasi Proses & Deadlock"
   git push origin main
   ```

---

## Hasil Eksekusi dan Analisis
### Eksperimen 1
![alt text](<screenshots/dining-philosopher.png>)
```
START 

# Preparation
- garpu 5 
- piring 1

# Proses
1. Think
2. Ready 
3. P1 - P5 take left fork 
4. P1 - P5 take right fork # deadlock terjadi
5. P1 - P5 eat # ini tidak terjadi karena deadlock
6. P1 - P5 put left fork
7. P1 - P5 put right fork
8. Repeat from step 1

FINISH
```

Deadlock terjadi karena setiap filosofi memegang satu garpu dan menunggu garpu lainnya yang sedang dipegang oleh filosofi lain. 
Untuk mengatasi deadlock, beberapa strategi dapat diterapkan, seperti:
1. Membatasi jumlah filosofi yang dapat duduk di meja pada satu waktu (misalnya, hanya 4 dari 5 filosofi yang diizinkan duduk).
2. Memaksa filosofi untuk mengambil kedua garpu sekaligus atau tidak sama sekali. 

### Eksperimen 2
```
START 

# Preparation
- garpu 5 
- piring 1

# Proses
1. Think
2. Ready 
3. Session 1
    P1 take left fork and right fork
    P2 hold and wait
    P3 take left fork and right fork 
    P4 take left fork
    P5 hold and wait
    
4. Session 2
    P1 put left fork and right fork
    P2 take left fork and right fork
    P3 put left fork and right fork
    P4 take right fork
    P5 take left fork

5. Session 3
    P2 put left fork and right fork
    P4 put left fork and right fork
    P5 take right fork

6. Session 4
    P5 put left fork and right fork

FINISH
```
- Analisis hasil modifikasi pseudococde dan buktikan bahwa deadlock telah dihindari.

    *   Skenario ini menunjukkan implementasi protokol yang berhasil mencegah deadlock. Meskipun sumber daya terbatas (5 filosof dan 5 garpu), urutan eksekusi yang ditetapkan memastikan semua proses (filosof) pada akhirnya dapat mengakses sumber daya yang dibutuhkan:

         Akses Bersamaan (Session 1): Tiga filosof (P1, P3, P4) dapat langsung menyelesaikan proses mereka karena ada cukup garpu untuk tiga pasangan (mengingat P1, P3, dan P4 tidak bersebelahan semua).
          Pembebasan Sumber Daya: Segera setelah P1, P3, dan P4 selesai (Session 2 & 3), mereka melepaskan garpu.

         Akses Bertahap: Filosof yang menunggu (P2 dan P5) kemudian dapat mengambil garpu yang telah dibebaskan tersebut. P2 berhasil di Session 2, dan P5 berhasil di Session 3.

         Model protokol ini secara implisit mengatur agar tidak semua filosof mencoba mengambil garpu kiri secara bersamaan, yang merupakan penyebab utama deadlock pada masalah standar. Urutan eksekusi yang terstruktur (Session 1 -> Session 2 -> Session 3) menjamin progress (kemajuan) dan fairness (keadilan akses) dalam jangka waktu tertentu.* 
### Eksperimen 3
   - Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed
      
      * Masalah klasik Lima Filosof Makan mencerminkan empat kondisi Coffman yang harus terpenuhi agar terjadi kebuntuan (deadlock) dalam sistem komputasi. Mengeliminasi setidaknya satu kondisi adalah kunci untuk solusi.

          1. Mutual Exclusion (Saling Pengecualian):

         Terjadi: Setiap garpu adalah sumber daya eksklusif dan hanya dapat dipegang oleh satu filosof. Kondisi ini harus dipertahankan karena merupakan sifat alami sumber daya.

         2. Hold and Wait (Menahan dan Menunggu):

         Terjadi: Filosof menahan garpu yang sudah diperoleh sambil menunggu garpu kedua dari tetangganya.

         Solusi: Terapkan prinsip alokasi all or nothing. Filosof hanya diizinkan mengambil kedua garpu secara bersamaan. Jika tidak bisa, ia harus melepaskan garpu yang sudah dipegang dan mencoba kembali.

         3. No Preemption (Tanpa Perebutan):

         Terjadi: Garpu tidak dapat diambil paksa (direbut) dari filosof yang sedang memegangnya.

         Solusi: Tambahkan mekanisme pelepasan paksa (preemption). Jika filosof menunggu terlalu lama, sistem dapat memaksa ia melepaskan garpu yang dipegangnya (time-out) untuk menghindari starvation (kelaparan) atau deadlock.

         4. Circular Wait (Menunggu Melingkar):

         Terjadi: Semua filosof secara serentak memegang garpu kiri mereka dan menunggu garpu kanan, membentuk rantai tertutup di mana P1 menunggu P2, P2 menunggu P3, dan seterusnya, hingga P5 menunggu P1.

         Solusi: Tetapkan pengurutan sumber daya (resource ordering) yang ketat. Misalnya, semua filosof harus mengambil garpu dengan nomor indeks terkecil terlebih dahulu. Ini memecah rantai sirkular, menghilangkan kemungkinan deadlock.

   - Sajikan hasil analisis dalam tabel 

      | No. | Kondisi Deadlock | Terjadi di Versi Deadlock (Filosof Makan) | Solusi Utama di Versi Fixed |
      | :--- | :--- | :--- | :--- |
      | 1. | **Mutual Exclusion** (Saling Pengecualian) | Ya. Satu garpu hanya dapat dipegang oleh satu filosof pada satu waktu. | **Dipertahankan (Non-Eliminable).** Kondisi ini tidak dapat dihilangkan karena garpu (sumber daya) adalah entitas yang tidak dapat dibagi (*non-shareable*). Solusi berfokus pada kondisi lain. |
      | 2. | **Hold and Wait** (Menahan dan Menunggu) | Ya. Filosof menahan garpu yang sudah didapat sambil menunggu garpu kedua (kiri atau kanan). | **Alokasi 'All or Nothing'.** Filosof hanya diizinkan mengambil garpu **hanya jika kedua garpu tersedia** secara serentak. Jika tidak, ia harus melepaskan semua garpu yang dipegang. |
      | 3. | **No Preemption** (Tanpa Perebutan) | Ya. Garpu tidak dapat diambil secara paksa dari filosof lain yang memegangnya. | **Preemption (Pelepasan Paksa).** Jika filosof menunggu terlalu lama untuk garpu kedua, sistem dapat memaksanya melepaskan garpu yang sudah dipegangnya (melalui mekanisme *time-out*) untuk mencegah *deadlock*. |
      | 4. | **Circular Wait** (Menunggu Melingkar) | Ya. Semua filosof memegang garpu kiri mereka dan menunggu garpu kanan mereka, membentuk rantai tunggu tertutup. | **Pengurutan Sumber Daya (Resource Ordering).** Tetapkan urutan pengambilan yang ketat (misalnya, selalu ambil garpu dengan nomor indeks **terkecil** terlebih dahulu) untuk memutus rantai ketergantungan sirkular. |



---

## Kesimpulan
- Sinkronisasi proses sangat penting untuk menjaga konsistensi data dan mencegah race condition ketika beberapa proses berjalan bersamaan dan mengakses sumber daya yang sama.
- Deadlock terjadi jika empat kondisi utama terpenuhi (mutual exclusion, hold and wait, no preemption, circular wait), sehingga pemahaman dan penerapan strategi pencegahan, deteksi, serta pemulihan menjadi krusial dalam sistem operasi.
- Praktikum memberikan pengalaman nyata bagi mahasiswa dalam menerapkan mekanisme sinkronisasi (semaphore, mutex, monitor) dan memahami cara mengatasi deadlock, sehingga teori dapat terhubung langsung dengan praktik pemrograman paralel.

---

## Quiz
1. Sebutkan empat kondisi utama penyebab deadlock. 

- Mutual Exclusion (Eksklusi Saling): Sumber daya hanya dapat digunakan oleh satu proses pada satu waktu.
- Hold and Wait (Menahan dan Menunggu): Proses yang sudah memegang sumber daya tetap menahannya sambil menunggu sumber daya lain.
- No Preemption (Tidak Ada Pengambilalihan): Sumber daya yang sudah diberikan tidak bisa diambil paksa dari proses, hanya bisa dilepas secara sukarela.
- Circular Wait (Menunggu Melingkar): Terdapat rantai proses yang saling menunggu sumber daya dari proses lain dalam lingkaran.
 
2. Mengapa sinkronisasi diperlukan dalam sistem operasi?  

Sinkronisasi diperlukan dalam sistem operasi untuk mencegah race condition dan menjaga konsistensi data ketika banyak proses berjalan secara bersamaan. Tanpa sinkronisasi, proses dapat saling mengganggu saat mengakses sumber daya bersama, sehingga hasil eksekusi menjadi tidak dapat diprediksi.
  
3. Jelaskan perbedaan antara semaphore dan monitor.  

- Semaphore → Mekanisme sinkronisasi tingkat rendah berupa variabel dengan operasi wait dan signal. Fleksibel, tapi rawan kesalahan jika tidak hati-hati.
- Monitor → Abstraksi tingkat tinggi yang otomatis melindungi critical section dengan prosedur dan condition variables. Lebih aman dan mudah digunakan.
  
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
