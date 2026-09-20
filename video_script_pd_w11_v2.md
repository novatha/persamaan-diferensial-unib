# Naskah & Metadata Video Kuliah Minggu 11: Persamaan Diferensial v2.0

### 1. Metadata Siap Unggah YouTube (SEO Optimized)

**Tautan Resmi YouTube:** [https://youtu.be/RxoN7UaK3OI](https://youtu.be/RxoN7UaK3OI)  

**Judul Resmi:** `[Minggu 11] Persamaan Gelombang 1D: Telegrafer Saluran Transmisi & Surja IEC 60071 | Persamaan Diferensial | Teknik Elektro UNIB`

**Deskripsi Siap Unggah:**
```text
Kuliah Daring Minggu 11 - Persamaan Diferensial (Teknik Elektro UNIB)
Topik: Persamaan Telegrafer Elemen Mikro Delta x, Solusi Gelombang Berjalan d'Alembert, Impedansi Karakteristik Z0, Koefisien Refleksi Beban Gamma, Standing Wave Ratio (VSWR), dan Surja Petir Gardu Induk IEC 60071

Dosen Pengampu:
- Ir. Novalio Daratha, S.T., M.Sc., Ph.D.
- Muhammad Arfan, S.T., M.T.
Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika
Fakultas Teknik, Universitas Bengkulu

Akses portal perkuliahan, modul ajar, lembar kerja C1-C6, dan problem set:
https://www.ndaratha.my.id/persamaan-diferensial/

Linimasa Bab (Timestamps):
00:00 - 01. Pembukaan Perkuliahan Minggu 11
00:45 - 02. Sub-CPMK 11 & Taksonomi Bloom
01:36 - 03. Peta Kurikulum: Terpusat vs Terdistribusi
02:19 - 04. Penurunan Model Elemen Mikro
02:59 - 05. Eliminasi ke Persamaan Gelombang
03:41 - 06. Solusi d'Alembert
04:18 - 07. Impedansi Karakteristik Z0
04:54 - 08. Skematik Antarmuka Saluran
05:28 - 09. Contoh Soal Solusi d'Alembert
06:05 - 10. Refleksi Gelombang Beban
06:47 - 11. Gelombang Berdiri & VSWR
07:27 - 12. Surja Petir & IEC 60071
08:08 - 13. Praktikum Julia: Gelombang Telegrafer
08:41 - 14. Kuis Interaktif & Evaluasi Bloom
10:22 - 15. Rangkuman Eksekutif & Penutup

Buku Referensi Pembelajaran:
1. Erwin Kreyszig, "Advanced Engineering Mathematics", 10th Edition, John Wiley & Sons.
2. Dennis G. Zill, "A First Course in Differential Equations with Modeling Applications", 11th Edition.
3. William H. Hayt & John A. Buck, "Engineering Electromagnetics", 9th Edition, McGraw-Hill.
4. Standar Industri Terkait (IEEE & IEC).

#PersamaanDiferensial #TeknikElektro #UniversitasBengkulu #KalkulusLanjut #DifferentialEquations #JuliaLang
```

---

## 2. Capaian Pembelajaran (Sub-CPMK 11 OBE Taksonomi Bloom)
- **C1 (Mengingat):** Menyatakan bentuk kanonik Persamaan Telegrafer dan Persamaan Gelombang 1D hiperbolik.
- **C2 (Memahami):** Menjelaskan batas fisik kapan saluran transmisi harus diperlakukan sebagai parameter terdistribusi (panjang gelombang lambda).
- **C3 (Menerapkan):** Menghitung kecepatan rambat v, impedansi karakteristik Z0, dan koefisien refleksi tegangan/arus Gamma.
- **C4 (Menganalisis):** Menganalisis pembentukan gelombang berdiri atau standing waves dan Voltage Standing Wave Ratio (VSWR).
- **C5 (Mengevaluasi):** Mengevaluasi fenomena pelipatan tegangan surja petir pada ujung saluran transmisi terbuka sesuai IEC 60071.
- **C6 (Komputasi):** Memprogram simulasi animasi perambatan gelombang maju dan pantul pada saluran transmisi dengan Julia.

---

## 3. Naskah Audio Narasi Per Salindia (15 Slide Lengkap)

### Salindia 01: Judul & Pembukaan Kuliah Minggu 11

Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, selamat datang kembali dalam perkuliahan daring Persamaan Diferensial semester genap 2026. Pada Minggu kesebelas ini, kita membedah fenomena perambatan gelombang elektromagnetik: Persamaan Gelombang Satu Dimensi dan Persamaan Telegrafer Saluran Transmisi Daya. Kita akan mempelajari penurunan model mikroskopis elemen saluran delta x, solusi gelombang berjalan d'Alembert, impedansi karakteristik Z nol, fenomena pantulan gelombang pada beban terminasi, rasio gelombang berdiri atau VSWR, serta mitigasi surja petir gardu induk berbasis standar koordinasi isolasi IEC 60071. Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan.

### Salindia 02: Sub-CPMK Taksonomi Bloom (Minggu 11)

Berikut adalah Capaian Pembelajaran Sub-CPMK Minggu kesebelas berbasis Taksonomi Bloom. Pada C1 Mengingat, mahasiswa mampu menyatakan bentuk matematis Persamaan Telegrafer dan persamaan gelombang hiperbolik. Pada C2 Memahami, mahasiswa mampu menjelaskan kriteria rasio panjang fisik saluran terhadap panjang gelombang lambda. Pada C3 Menerapkan, mahasiswa mampu menghitung koefisien refleksi Gamma L dan impedansi karakteristik saluran. Pada C4 Menganalisis, mahasiswa mampu membedakan gelombang berjalan murni versus gelombang berdiri penuh. Pada C5 Mengevaluasi, mahasiswa mampu membuktikan penggandaan tegangan surja dua kali lipat pada saluran terbuka IEC 60071. Dan pada C6 Komputasi, mahasiswa mampu memprogram visualisasi perambatan gelombang menggunakan bahasa Julia.

### Salindia 03: Peta Kurikulum: Batas Rangkaian Terpusat vs Terdistribusi

Perhatikan kriteria fundamental pada slide ini yang membedakan teori sirkuit terpusat dengan teori saluran transmisi. Kapan suatu kawat penghubung dapat dianggap sebagai simpul rangkaian biasa dengan tegangan seragam, dan kapan ia wajib dianalisis sebagai saluran transmisi terdistribusi? Jawabannya ditentukan oleh perbandingan panjang fisik kawat d terhadap panjang gelombang sinyal lambda. Jika panjang kawat d jauh lebih kecil daripada sepersepuluh lambda, waktu tempuh gelombang dapat diabaikan. Namun jika panjang kawat sebanding atau lebih besar dari nol koma satu lambda, seperti pada saluran transmisi daya lima puluh Hertz sepanjang ratusan kilometer atau kabel sinyal frekuensi radio giga Hertz, efek perambatan gelombang dan jeda waktu propagasi mutlak wajib diperhitungkan.

### Salindia 04: Penurunan Model Elemen Mikro Delta x Saluran Transmisi

Mari kita turunkan model mikroskopis saluran transmisi dua kawat secara first-principles. Tinjau potongan kecil saluran sepanjang delta x. Elemen mikro ini dimodelkan oleh empat parameter per satuan panjang: resistansi kawat R dalam Ohm per meter, induktansi loop L dalam Henry per meter, konduktansi kebocoran dielektrik G dalam Siemens per meter, dan kapasitansi antar-konduktor C dalam Farad per meter. Menerapkan KVL pada loop mikro dan KCL pada simpul paralel, kita peroleh sepasang Persamaan Telegrafer berpasangan: parsial v per parsial x sama dengan minus R i dikurang L dikali parsial i per parsial t, dan parsial i per parsial x sama dengan minus G v dikurang C dikali parsial v per parsial t.

### Salindia 05: Eliminasi Silang Menuju Persamaan Gelombang 1D

Untuk saluran transmisi tanpa rugi-rugi di mana resistansi R dan konduktansi G bernilai nol, kita lakukan eliminasi silang: turunkan persamaan tegangan terhadap x dan substitusikan turunan arus terhadap t. Hasilnya adalah Persamaan Gelombang Satu Dimensi murni: parsial kuadrat v per parsial x kuadrat sama dengan L dikalikan C dikalikan parsial kuadrat v per parsial t kuadrat. Persamaan ini identik dengan bentuk kanonik: parsial kuadrat v per parsial x kuadrat sama dengan satu per v kuadrat dikalikan parsial kuadrat v per parsial t kuadrat. Kecepatan rambat gelombang elektromagnetik pada saluran adalah v sama dengan satu per akar L C, yang pada kabel udara sama persis dengan kecepatan cahaya tiga ratus ribu kilometer per detik.

### Salindia 06: Solusi Perjalanan Gelombang d'Alembert

Jean le Rond d'Alembert membuktikan bahwa solusi umum dari persamaan gelombang satu dimensi selalu dapat diuraikan menjadi superposisi dua gelombang berjalan sembarang: v x koma t sama dengan f satu kurung x dikurang v t ditambah f dua kurung x ditambah v t. Fungsi f satu kurung x dikurang v t merepresentasikan Gelombang Maju yang merambat ke arah sumbu x positif dengan profil bentuk gelombang tetap. Sedangkan fungsi f dua kurung x ditambah v t merepresentasikan Gelombang Pantul yang merambat ke arah sumbu x negatif. Bentuk fungsi f satu dan f dua sepenuhnya ditentukan oleh kondisi awal distribusi spasial tegangan dan laju perubahan mula-mula.

### Salindia 07: Impedansi Karakteristik Z_0 & Rasio Gelombang Arus

Pada gelombang berjalan murni, perbandingan antara gelombang tegangan dan gelombang arus di setiap titik dan saat adalah konstan, didefinisikan sebagai Impedansi Karakteristik Saluran: Z nol sama dengan akar L dibagi C dalam satuan Ohm. Sangat penting dicatat bahwa Z nol bukanlah hambatan disipatif yang memanaskan kawat, melainkan rasio antara medan listrik terhadap medan magnet gelombang yang merambat. Untuk saluran udara transmisi PLN, nilai Z nol tipikal berkisar antara tiga ratus hingga empat ratus Ohm. Sedangkan untuk kabel koaksial dan kabel tanah bawah laut, nilai Z nol tipikal adalah lima puluh atau tujuh puluh lima Ohm.

### Salindia 08: Skematik Rangkaian Terdistribusi & Antarmuka Saluran

Slide ini menampilkan diagram antarmuka saluran transmisi yang menghubungkan generator pengirim dengan impedansi sumber Z S di ujung kirim, membentang sepanjang jarak L dengan impedansi karakteristik Z nol, menuju beban penerima dengan impedansi Z L di ujung terima. Ketika gelombang surja tiba di ujung saluran, terjadi interaksi gelombang pada diskontinuitas impedansi. Jika impedansi beban Z L sama persis dengan Z nol, seluruh energi gelombang diserap sempurna oleh beban tanpa ada pantulan sama sekali. Kondisi ini dinamakan Saluran Tersesuai Sempurna atau Matched Line.

### Salindia 09: Contoh Terhitung: Solusi d'Alembert Impuls Awal

Mari kita selesaikan contoh soal analitis perambatan pulsa segitiga awal pada saluran transmisi tanpa rugi-rugi. Tegangan awal pada t sama dengan nol memiliki profil pulsa segitiga setinggi seratus kilo Volt di tengah bentang saluran, dengan laju awal nol. Berdasarkan formula d'Alembert, pulsa awal tersebut terbelah secara simetris menjadi dua pulsa identik: satu pulsa gelombang maju setinggi lima puluh kilo Volt yang merambat ke kanan dengan kecepatan v, dan satu pulsa gelombang mundur setinggi lima puluh kilo Volt yang merambat ke kiri dengan kecepatan v. Kedua pulsa bergerak saling menjauh dengan menjaga bentuk geometrisnya secara sempurna tanpa distorsi.

### Salindia 10: Refleksi Gelombang pada Terminasi Beban Z_L

Bila impedansi beban Z L tidak sama dengan Z nol, sebagian energi gelombang akan dipantulkan kembali menuju generator. Tingkat pantulan diukur oleh Koefisien Refleksi Tegangan Gamma L: Gamma L sama dengan Z L dikurang Z nol dibagi Z L ditambah Z nol. Perhatikan tiga kasus ekstrem: Kasus satu, Beban Hubung Singkat Z L sama dengan nol: Gamma L sama dengan minus satu, gelombang tegangan dipantulkan berbalik fasa seratus delapan puluh derajat sehingga tegangan total di ujung beban nol. Kasus dua, Beban Rangkaian Terbuka Z L tak hingga: Gamma L sama dengan plus satu, gelombang pantul sefasa penuh! Tegangan total di ujung terbuka melonjak menjadi dua kali lipat tegangan datang!

### Salindia 11: Gelombang Berdiri (Standing Waves) & VSWR

Superposisi kontinu antara gelombang datang dan gelombang pantul menghasilkan pola interferensi stasioner yang disebut Gelombang Berdiri atau Standing Waves. Pada titik-titik tertentu terjadi interferensi konstruktif yang membentuk titik perut tegangan maksimum V max, sedangkan pada titik lain terjadi interferensi destruktif yang membentuk titik simpul tegangan minimum V min. Kualitas penyesuaian impedansi diukur oleh Voltage Standing Wave Ratio atau VSWR, yaitu rasio V max terhadap V min, atau satu ditambah mutlak Gamma dibagi satu dikurang mutlak Gamma. Nilai VSWR ideal adalah satu koma nol. Semakin besar VSWR, semakin banyak energi yang terpantul sia-sia.

### Salindia 12: Standar Industri: Surja Petir & Koordinasi Isolasi IEC 60071

Penerapan paling kritis dari teori pantulan gelombang adalah perlindungan gardu induk terhadap sambaran petir. Ketika sambaran petir menghantam kawat fasa SUTT, gelombang surja tegangan tinggi merambat menuju transformator gardu induk. Karena belitan transformator memiliki impedansi surja yang sangat besar dibandingkan saluran udara, terminal transformator bertindak mendekati rangkaian terbuka dengan koefisien pantul Gamma L mendekati plus satu! Tegangan surja petir melonjak dua kali lipat di terminal transformator. Berdasarkan standar IEC 60071, Lightning Arrester atau penangkap petir MOV wajib dipasang sedekat mungkin dengan bushing transformator untuk memotong gelombang pantul sebelum merusak isolasi belitan trafo.

### Salindia 13: Praktikum Komputasi Julia: Gelombang Telegrafer Transmisi

Pada praktikum komputasi Julia ini, kita memprogram solver numerik metode beda hingga FDM berbasis skema Lax-Wendroff untuk menyimulasikan perambatan gelombang surja pada saluran transmisi sepanjang seratus kilometer. Grafik animasi di sebelah kanan memperlihatkan gelombang pulsa surja petir yang bergerak melintasi saluran, mencapai ujung terbuka pada kilometer seratus, dan seketika mengalami pelipatan amplitudo menjadi dua ratus persen sebelum terpantul kembali menuju sumber. Simulasi Julia interaktif ini memberikan visualisasi dinamis yang memperkuat pemahaman matematis Anda mengenai solusi d'Alembert.

### Salindia 14: Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)

**[Bagian 1 - Pertanyaan Kuis]:**
Saatnya kuis interaktif untuk menguji intuisi gelombang saluran transmisi Anda. Perhatikan studi kasus pada layar: Saluran transmisi seratus lima puluh kilo Volt memiliki ujung terbuka atau open circuit dengan Z L menuju tak hingga. Ketika gelombang surja petir V plus menabrak ujung saluran tersebut, berapakah tegangan sesaat yang dialami isolator ujung saluran? Pilihan A: Nol Volt karena arus listrik tidak dapat mengalir ke luar kawat. Pilihan B: Dua kali lipat atau dua V plus akibat pemantulan sefasa penuh dengan koefisien refleksi Gamma L sama dengan plus satu! Pilihan C: Setengahnya atau V plus per dua karena fenomena pembagian tegangan. Pilihan D: Berkurang drastis karena energi terserap langsung ke udara bebas. Silakan analisis mekanisme pantulan surja ini dan tentukan pilihan terbaik Anda dalam delapan detik ke depan.

*[Jeda Hening Berpikir: 8 Detik Terprogram]*

**[Bagian 2 - Pembahasan Kuis & Tantangan Bloom]:**
Waktu habis. Jawaban yang tepat adalah B: Dua kali lipat atau dua V plus akibat pemantulan sefasa penuh! Pada ujung terbuka, arus harus bernilai nol sehingga gelombang pantul arus berlawanan fasa minus I plus. Sebaliknya, gelombang pantul tegangan sefasa penuh plus V plus dengan Gamma L sama dengan plus satu. Superposisi gelombang datang dan gelombang pantul melipatgandakan tegangan menjadi tepat dua kali lipat, mengancam ketahanan isolator. Pada kolom tantangan sebelah kanan, Anda juga ditantang menyusun diagram kisi Bewley di level C4, mengevaluasi rasio gelombang berdiri atau VSWR di level C5, serta merancang koordinasi isolasi lightning arrester standar IEC 60071 di level C6.

### Salindia 15: Rangkuman Eksekutif & Jembatan ke Minggu 12

Sebagai rangkuman perkuliahan minggu kesebelas: Pertama, saluran transmisi wajib diperlakukan sebagai sistem parameter terdistribusi jika panjang kawat sebanding dengan panjang gelombang. Kedua, Persamaan Telegrafer tanpa rugi-rugi tereduksi menjadi Persamaan Gelombang hiperbolik dengan kecepatan perambatan satu per akar L C. Ketiga, solusi d'Alembert membagi gelombang menjadi komponen maju dan mundur yang berinteraksi di titik batas beban. Dan keempat, pantulan pada ujung terbuka melipatgandakan tegangan surja dua kali lipat sesuai standar IEC 60071. Silakan pelajari modul ajar dan tuntaskan Lembar Kerja serta Problem Set Minggu kesebelas di portal ndaratha dot my dot id. Pada minggu kedua belas, kita akan mempelajari Persamaan Panas 1D dan manajemen termal kabel bawah tanah. Terima kasih dan wassalamualaikum warahmatullahi wabarakatuh.

