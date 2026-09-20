# Naskah & Metadata Video Kuliah Minggu 04: Persamaan Diferensial v2.0

### 1. Metadata Siap Unggah YouTube (SEO Optimized)

**Judul Resmi:** `[Minggu 04] PDB Orde 2 Homogen: Karakteristik Akar & Tiga Ragam Redaman RLC | Persamaan Diferensial | Teknik Elektro UNIB`

**Deskripsi Siap Unggah:**
```text
Kuliah Daring Minggu 04 - Persamaan Diferensial (Teknik Elektro UNIB)
Topik: Persamaan Karakteristik, Determinan Wronskian, Respon RLC Bebas Sumber (Overdamped, Critically Damped, Underdamped), dan Analisis Ruang Fasa

Dosen Pengampu:
- Ir. Novalio Daratha, S.T., M.Sc., Ph.D.
- Muhammad Arfan, S.T., M.T.
Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika
Fakultas Teknik, Universitas Bengkulu

Akses portal perkuliahan, modul ajar, lembar kerja C1-C6, dan problem set:
https://www.ndaratha.my.id/persamaan-diferensial/

Linimasa Bab (Timestamps):
00:00 - 01. Pembukaan Perkuliahan Minggu 04
00:39 - 02. Sub-CPMK 3 & Taksonomi Bloom
01:28 - 03. Peta Konsep: Lompatan ke Orde 2
02:06 - 04. Bentuk Standar & Karakteristik
02:41 - 05. Superposisi & Determinan Wronskian
03:19 - 06. Pemodelan Sirkuit RLC Seri
03:58 - 07. Parameter Standar Karakteristik RLC
04:38 - 08. Ragam 1: Overdamped
05:17 - 09. Ragam 2: Critically Damped
05:59 - 10. Ragam 3: Underdamped
06:40 - 11. Tangki LC & Ruang Fasa
07:20 - 12. Contoh Soal Terhitung RLC
08:09 - 13. Praktikum Julia: Tiga Ragam Redaman
08:47 - 14. Kuis Interaktif & Evaluasi Bloom
10:24 - 15. Rangkuman Perkuliahan & Penutup

Buku Referensi Pembelajaran:
1. Erwin Kreyszig, "Advanced Engineering Mathematics", 10th Edition, John Wiley & Sons.
2. Dennis G. Zill, "A First Course in Differential Equations with Modeling Applications", 11th Edition.
3. William H. Hayt & John A. Buck, "Engineering Electromagnetics", 9th Edition, McGraw-Hill.
4. Standar Industri Terkait (IEEE & IEC).

#PersamaanDiferensial #TeknikElektro #UniversitasBengkulu #KalkulusLanjut #DifferentialEquations #JuliaLang
```

---

## 2. Capaian Pembelajaran (Sub-CPMK 4 OBE Taksonomi Bloom)
- **C1 (Mengingat):** Menyatakan bentuk baku PDB orde 2 homogen koefisien konstan dan persamaan karakteristik kuadrat.
- **C2 (Memahami):** Menjelaskan makna fisis parameter atenuasi alpha, frekuensi resonansi alami omega nol, dan rasio redaman zeta.
- **C3 (Menerapkan):** Menurunkan solusi khusus IVP untuk ketiga ragam redaman dengan determinan Wronskian.
- **C4 (Menganalisis):** Membandingkan dinamika respon waktu dan lintasan ruang fasa antara kondisi overdamped, kritis, dan underdamped.
- **C5 (Mengevaluasi):** Mengevaluasi perancangan resistor peredam lonjakan arus inrush pemutus daya sesuai standar IEEE.
- **C6 (Komputasi):** Memprogram simulasi numerik ketiga ragam redaman RLC menggunakan paket Julia DifferentialEquations.jl.

---

## 3. Naskah Audio Narasi Per Salindia (15 Slide Lengkap)

### Salindia 01: Judul & Pembukaan Kuliah Minggu 04

Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, selamat datang dalam perkuliahan daring Persamaan Diferensial semester genap 2026. Pada Minggu keempat ini, kita melompat ke tingkat kompleksitas baru yang sangat fundamental dalam analisis sistem fisik: Persamaan Diferensial Biasa Orde Dua Homogen dengan Koefisien Konstan. Kita akan membedah penurunan persamaan karakteristik, determinan Wronskian, serta dinamika rangkaian RLC bebas sumber yang melahirkan tiga ragam redaman klasik: overdamped, critically damped, dan underdamped. Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan.

### Salindia 02: Capaian Pembelajaran (Sub-CPMK 3) & Taksonomi Bloom

Capaian pembelajaran minggu ini mencakup enam tingkatan Taksonomi Bloom. Pada C1 Mengingat, mahasiswa mampu menyatakan bentuk baku PDB orde dua homogen dan persamaan karakteristiknya. Pada C2 Memahami, mahasiswa mampu mengaitkan diskriminan aljabar dengan redaman energi pada osilator listrik. Pada C3 Menerapkan, mahasiswa mampu menurunkan solusi analitik eksak untuk berbagai kondisi nilai awal. Pada C4 Menganalisis, mahasiswa mampu membedakan waktu naik, lewatan maksimum atau overshoot, dan frekuensi teredam. Pada C5 Mengevaluasi, mahasiswa mampu menguji kriteria kestabilan osilasi pada tangki LC dan pemutus daya industri. Dan pada C6 Komputasi, mahasiswa mampu menyimulasikan dinamika redaman menggunakan Julia Tsit5.

### Salindia 03: Peta Konsep: Lompatan dari Orde 1 Menuju Orde 2

Perhatikan diagram transisi pada slide ini. Pada sistem orde satu yang kita pelajari pada minggu sebelumnya, hanya terdapat satu elemen penyimpan energi, sehingga respon transien selalu bersifat monoton eksponensial tanpa osilasi. Namun pada sistem orde dua, terdapat dua elemen penyimpan energi yang saling berinteraksi: induktor yang menyimpan medan magnet dan kapasitor yang menyimpan medan listrik. Pertukaran energi kinetik dan potensial bolak-balik antara kedua elemen ini melahirkan fenomena osilasi gelombang. Struktur matematisnya berubah dari persamaan linier sederhana menjadi persamaan kuadrat yang menghasilkan dua akar karakteristik independen.

### Salindia 04: Bentuk Standar PDB Orde 2 Homogen & Persamaan Karakteristik

Bentuk umum PDB orde dua linier homogen koefisien konstan dinyatakan sebagai: a dikali d kuadrat y per d t kuadrat ditambah b dikali d y per d t ditambah c dikali y sama dengan nol. Dengan menggunakan postulat solusi eksponensial y t sama dengan e pangkat s dikali t, kita turunkan Persamaan Karakteristik: a dikali s kuadrat ditambah b dikali s ditambah c sama dengan nol. Akar-akar persamaan kuadrat ini adalah s satu dan s dua sama dengan minus b plus minus akar b kuadrat dikurang empat a c seluruhnya dibagi dua a. Sifat fisis dari solusi gerak sistem sepenuhnya ditentukan oleh tanda diskriminan kuadratik tersebut.

### Salindia 05: Teorema Superposisi & Determinan Wronskian

Berdasarkan Prinsip Superposisi Linier, jika y satu dan y dua adalah dua solusi khusus independen dari PDB homogen, maka kombinasi linier y sama dengan c satu y satu ditambah c dua y dua juga merupakan solusi umum lengkap. Untuk membuktikan kebebasan linier kedua solusi tersebut, kita menggunakan alat matematika yang disebut Determinan Wronskian W. Wronskian dari y satu dan y dua adalah determinan matriks dua kali dua yang memuat kedua fungsi pada baris pertama dan turunan pertamanya pada baris kedua. Teorema Abel menyatakan bahwa jika Wronskian tidak bernilai nol pada suatu interval, maka kedua fungsi dijamin bebas linier dan membentuk basis himpunan solusi fundamental.

### Salindia 06: Pemodelan Fisis: Rangkaian RLC Seri Bebas Sumber

Mari kita turunkan model fisis rangkaian RLC seri bebas sumber secara first-principles. Berdasarkan Hukum Tegangan Kirchhoff pada loop tertutup: tegangan resistor v R ditambah tegangan induktor v L ditambah tegangan kapasitor v C sama dengan nol. Dengan menyatakan arus i t sebagai C dikalikan d v C per d t, tegangan resistor adalah R C d v C per d t, dan tegangan induktor adalah L C d kuadrat v C per d t kuadrat. Dengan membagi seluruh persamaan dengan L C, kita peroleh bentuk kanonik rekayasa elektro: d kuadrat v C per d t kuadrat ditambah R per L dikali d v C per d t ditambah satu per L C dikali v C sama dengan nol.

### Salindia 07: Parameter Standar Karakteristik RLC

Dalam literatur teknik elektro dan teori kendali standar industri, bentuk kanonik orde dua dinyatakan dengan parameter baku: d kuadrat y per d t kuadrat ditambah dua alpha dikali d y per d t ditambah omega nol kuadrat dikali y sama dengan nol. Di sini, alpha sama dengan R dibagi dua L dinamakan koefisien atenuasi atau frekuensi Neper dalam satuan Neper per detik. omega nol sama dengan satu dibagi akar L C dinamakan frekuensi sudut resonansi alami tanpa redaman dalam radian per detik. Sedangkan rasio redaman tanpa dimensi zeta didefinisikan sebagai perbandingan alpha terhadap omega nol. Ketiga parameter ini membagi perilaku sistem ke dalam tiga ragam redaman yang berbeda.

### Salindia 08: Ragam 1: Teredam Lebih (Overdamped, alpha > omega_0 atau zeta > 1)

Ragam pertama adalah Teredam Lebih atau Overdamped, yang terjadi bila resistansi R cukup besar sehingga alpha lebih besar dari omega nol atau rasio redaman zeta lebih besar dari satu. Diskriminan persamaan kuadrat bernilai positif, menghasilkan dua akar real berbeda negatif: s satu dan s dua sama dengan minus alpha plus minus akar alpha kuadrat dikurang omega nol kuadrat. Solusi umumnya adalah penjumlahan dua fungsi peluruhan eksponensial murni: A satu e pangkat s satu t ditambah A dua e pangkat s dua t. Respon sistem sangat lambat kembali ke titik kesetimbangan tanpa mengalami osilasi sama sekali, karena disipasi energi kalor pada resistor sangat dominan dibandingkan laju pertukaran energi medan.

### Salindia 09: Ragam 2: Teredam Kritis (Critically Damped, alpha = omega_0 atau zeta = 1)

Ragam kedua adalah Teredam Kritis atau Critically Damped, yang terjadi saat resistansi bernilai tepat R kritis sama dengan dua kali akar L per C, sehingga alpha persis sama dengan omega nol atau zeta sama dengan satu. Diskriminan bernilai nol, menghasilkan satu akar kembar real negatif s sama dengan minus alpha. Agar diperoleh dua solusi yang bebas linier, solusi kedua dikalikan dengan variabel waktu t, menghasilkan: y t sama dengan kurung A satu ditambah A dua dikali t seluruhnya dikalikan e pangkat minus alpha t. Keistimewaan ragam kritis adalah sistem kembali ke kondisi tunak dalam waktu tercepat tanpa pernah mengalami lewatan atau overshoot sedikit pun. Ragam ini menjadi acuan desain jarum instrumen analog dan peredam kejut mekanis.

### Salindia 10: Ragam 3: Teredam Kurang (Underdamped, alpha < omega_0 atau zeta < 1)

Ragam ketiga adalah Teredam Kurang atau Underdamped, yang terjadi bila resistansi kecil sehingga alpha lebih kecil dari omega nol atau zeta kurang dari satu. Diskriminan bernilai negatif, menghasilkan sepasang akar kompleks konjugat: s satu dan s dua sama dengan minus alpha plus minus j dikali omega d, di mana omega d sama dengan akar omega nol kuadrat dikurang alpha kuadrat adalah frekuensi osilasi alami teredam. Menggunakan rumus Euler, solusi berubah menjadi gelombang sinusoidal yang terbungkus selubung peluruhan eksponensial: e pangkat minus alpha t dikalikan kurung B satu kosinus omega d t ditambah B dua sinus omega d t. Sistem berosilasi bolak-balik dengan amplitudo yang menyusut perlahan menuju nol.

### Salindia 11: Kasus Khusus Tangki LC Murni & Analisis Ruang Fasa

Jika resistansi R bernilai nol ohm, kita memperoleh sirkuit LC ideal tanpa disipasi. Akar karakteristik menjadi imajiner murni plus minus j omega nol, menghasilkan osilasi harmonik abadi dengan frekuensi sudut tetap. Analisis Ruang Fasa atau phase-plane menghubungkan variabel keadaan arus terhadap tegangan. Pada tangki LC murni, lintasan di ruang fasa membentuk kurva elips tertutup yang merepresentasikan hukum kekekalan energi elektromagnetik total. Pada sistem teredam kurang, lintasan ruang fasa berputar spiral ke dalam menuju titik pusat stabil. Sedangkan pada sistem teredam lebih, lintasan melengkung langsung menuju titik asal tanpa putaran.

### Salindia 12: Contoh Soal Terhitung (Worked Example): RLC Seri Industri

Mari kita selesaikan contoh soal terhitung rangkaian RLC industri: L sama dengan sepuluh mili Henry, C sama dengan satu mikrofarad, dengan tegangan awal kapasitor seratus Volt dan arus awal induktor nol. Langkah satu: kita hitung omega nol sama dengan satu dibagi akar sepuluh mili Henry kali satu mikrofarad, yaitu sepuluh ribu radian per detik. Resistansi kritisnya adalah dua ratus Ohm. Jika R dipilih empat puluh Ohm, maka alpha adalah dua ribu Neper per detik. Karena alpha lebih kecil dari omega nol, sistem berada pada ragam underdamped dengan frekuensi teredam sembilan ribu tujuh ratus sembilan puluh delapan radian per detik. Solusi analitisnya adalah v C t sama dengan e pangkat minus dua ribu t dikalikan kurung seratus kosinus sembilan ribu tujuh ratus sembilan puluh delapan t ditambah dua puluh koma empat sinus sembilan ribu tujuh ratus sembilan puluh delapan t Volt.

### Salindia 13: Praktikum Komputasi Julia: Tiga Ragam Redaman RLC

Pada demonstrasi komputasi Julia ini, kita membuat simulasi interaktif yang membandingkan ketiga ragam redaman secara langsung. Dengan mendefinisikan sistem persamaan diferensial orde dua sebagai sistem dua PDB orde satu dalam bentuk state-space, kita panggil solver adaptif Tsit5 dari paket DifferentialEquations dot j l. Grafik kurva merah memperlihatkan ragam underdamped yang berosilasi dengan lewatan puncak, kurva hijau menunjukkan respon tercepat ragam critically damped yang mencapai nilai tunak tanpa overshoot, dan kurva biru memperlihatkan respon lambat ragam overdamped. Visualisasi komputasi ini mempertegas intuisi rekayasa Anda dalam memilih parameter sirkuit yang tepat.

### Salindia 14: Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)

**[Bagian 1 - Pertanyaan Kuis]:**
Saatnya kuis interaktif untuk menguji intuisi rekayasa Anda. Perhatikan kasus rekayasa pada layar: Mengapa aktuator mekanik penutup pemutus tenaga atau PMT gardu induk dan jarum ukur analog selalu dirancang tepat pada kondisi redaman kritis dengan zeta sama dengan satu? Pilihan A: Mengurangi konsumsi daya listrik baterai DC gardu induk. Pilihan B: Mencapai posisi tunak dalam waktu tersingkat tanpa mengalami lenting atau osilasi lewatan overshoot! Pilihan C: Menghasilkan tegangan transien paling besar. Pilihan D: Mencegah panas pada kumparan elektromagnet aktuator. Silakan analisis konsep redaman fisis ini dan tentukan pilihan jawaban terbaik Anda dalam delapan detik ke depan.

*[Jeda Hening Berpikir: 8 Detik Terprogram]*

**[Bagian 2 - Pembahasan Kuis & Tantangan Bloom]:**
Waktu habis. Jawaban yang tepat adalah B: Mencapai posisi tunak dalam waktu tersingkat tanpa mengalami lenting atau osilasi overshoot! Jika dirancang underdamped, kontak PMT akan memantul bolak-balik atau mengalami contact bounce yang memicu busur api listrik fatal dan merusak kontak logam. Sebaliknya jika dirancang overdamped, penutupan kontak akan berlangsung terlalu lambat sehingga membahayakan pemutusan arus gangguan. Kondisi redaman kritis zeta sama dengan satu menjamin transisi tercepat menuju posisi kontak rapat tanpa getaran sedikit pun. Pada kolom tantangan sebelah kanan, Anda juga ditantang membuktikan kebebasan linier determinan Wronskian pada level C4, mengevaluasi radiasi tangki LC pada level C5, serta merancang parameter resistansi filter osilasi tiga ratus empat belas radian per detik pada level C6.

### Salindia 15: Rangkuman Inti Perkuliahan & Referensi

Sebagai rangkuman perkuliahan minggu keempat: Pertama, PDB orde dua homogen memiliki persamaan karakteristik kuadrat yang menentukan jenis akar real berbeda, kembar, atau kompleks konjugat. Kedua, interaksi dinamis antara L dan C melahirkan tiga ragam redaman fisis: overdamped, critically damped, dan underdamped. Ketiga, determinan Wronskian membuktikan kebebasan linier basis solusi fundamental. Dan keempat, simulasi numerik Julia memvalidasi ketepatan analisis analitis. Silakan unduh materi modul dan selesaikan Lembar Kerja serta Problem Set Minggu keempat di portal ndaratha dot my dot id. Pada minggu kelima, kita akan membedah PDB orde dua non-homogen, metode koefisien tak tentu, dan fenomena resonansi. Terima kasih dan wassalamualaikum warahmatullahi wabarakatuh.

