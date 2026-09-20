# Naskah & Metadata Video Kuliah Minggu 09: Persamaan Diferensial v2.0

### 1. Metadata Siap Unggah YouTube (SEO Optimized)

**Tautan Resmi YouTube:** [https://youtu.be/VaRiwphPnaw](https://youtu.be/VaRiwphPnaw)  

**Judul Resmi:** `[Minggu 09] Pengantar PDP & Deret Fourier: Harmonis Sistem Tenaga IEEE 519 | Persamaan Diferensial | Teknik Elektro UNIB`

**Deskripsi Siap Unggah:**
```text
Kuliah Daring Minggu 09 - Persamaan Diferensial (Teknik Elektro UNIB)
Topik: Klasifikasi PDP Linier Orde Dua (Eliptik, Parabolik, Hiperbolik), Teorema Ortogonalitas, Sifat Simetri Gelombang Inverter, Fenomena Gibbs, Total Harmonic Distortion (THD), dan Batas IEEE Std 519-2022

Dosen Pengampu:
- Ir. Novalio Daratha, S.T., M.Sc., Ph.D.
- Muhammad Arfan, S.T., M.T.
Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika
Fakultas Teknik, Universitas Bengkulu

Akses portal perkuliahan, modul ajar, lembar kerja C1-C6, dan problem set:
https://www.ndaratha.my.id/persamaan-diferensial/

Linimasa Bab (Timestamps):
00:00 - 01. Pembukaan Perkuliahan Minggu 09
00:44 - 02. Sub-CPMK 9 & Taksonomi Bloom
01:36 - 03. Peta Kurikulum: Transisi PDP
02:18 - 04. Taksonomi PDP Linier Orde Dua
03:05 - 05. Teorema Ortogonalitas
03:45 - 06. Formulasi Deret Fourier
04:23 - 07. Pemanfaatan Sifat Simetri
05:12 - 08. Dekomposisi Spektrum Inverter
05:50 - 09. Contoh Soal Gelombang Persegi
06:32 - 10. Fenomena Gibbs
07:09 - 11. Analisis Polusi Harmonisa
07:44 - 12. Regulasi IEEE Std 519-2022
08:25 - 13. Praktikum Julia: Rekonstruksi Fourier
09:04 - 14. Kuis Interaktif & Evaluasi Bloom
10:49 - 15. Rangkuman Eksekutif & Penutup

Buku Referensi Pembelajaran:
1. Erwin Kreyszig, "Advanced Engineering Mathematics", 10th Edition, John Wiley & Sons.
2. Dennis G. Zill, "A First Course in Differential Equations with Modeling Applications", 11th Edition.
3. William H. Hayt & John A. Buck, "Engineering Electromagnetics", 9th Edition, McGraw-Hill.
4. Standar Industri Terkait (IEEE & IEC).

#PersamaanDiferensial #TeknikElektro #UniversitasBengkulu #KalkulusLanjut #DifferentialEquations #JuliaLang
```

---

## 2. Capaian Pembelajaran (Sub-CPMK 9 OBE Taksonomi Bloom)
- **C1 (Mengingat):** Menyatakan klasifikasi diskriminan PDP orde 2 (eliptik, parabolik, hiperbolik) dan rumus koefisien Fourier Euler.
- **C2 (Memahami):** Menjelaskan makna fisis ortogonalitas fungsi harmonik dan asal mula lonjakan 9% fenomena Gibbs pada diskontinuitas.
- **C3 (Menerapkan):** Menghitung koefisien deret Fourier a0, an, bn dengan memanfaatkan penyederhanaan simetri ganjil dan setengah gelombang.
- **C4 (Menganalisis):** Menganalisis spektrum frekuensi harmonisa inverter dan menghitung Total Harmonic Distortion (THD) arus/tegangan.
- **C5 (Mengevaluasi):** Mengevaluasi kesesuaian profil distorsi harmonisa beban industri terhadap standar regulasi IEEE Std 519-2022.
- **C6 (Komputasi):** Memprogram sintesis deret Fourier dan visualisasi konvergensi spektral gelombang menggunakan bahasa Julia.

---

## 3. Naskah Audio Narasi Per Salindia (15 Slide Lengkap)

### Salindia 01: Judul & Pembukaan Kuliah Minggu 09

Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, selamat datang kembali dalam perkuliahan daring Persamaan Diferensial semester genap 2026 pasca Ujian Tengah Semester. Pada Minggu kesembilan ini, kita memulai paruh kedua kurikulum dengan melangkah ke ranah yang lebih tinggi: Pengantar Persamaan Diferensial Parsial atau PDP dan Analisis Deret Fourier. Kita akan mempelajari klasifikasi PDP orde dua menjadi tipe eliptik, parabolik, dan hiperbolik, teorema ortogonalitas, dekomposisi harmonisa gelombang inverter, fenomena Gibbs, serta standar industri penanggulangan polusi harmonisa IEEE Std 519-2022. Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan.

### Salindia 02: Sub-CPMK Taksonomi Bloom (Minggu 9)

Berikut adalah Capaian Pembelajaran Sub-CPMK Minggu kesembilan dalam Taksonomi Bloom. Pada C1 Mengingat, mahasiswa mampu menyatakan klasifikasi diskriminan PDP dan formula koefisien deret Fourier. Pada C2 Memahami, mahasiswa mampu menjelaskan konsep ortogonalitas fungsi trigonometri sebagai basis ruang Hilbert tak hingga. Pada C3 Menerapkan, mahasiswa mampu menurunkan deret Fourier gelombang periodik dengan memanfaatkan sifat simetri gelombang. Pada C4 Menganalisis, mahasiswa mampu menghitung indeks distorsi harmonisa total atau THD pada sistem tenaga. Pada C5 Mengevaluasi, mahasiswa mampu menguji kepatuhan kualitas daya listrik industri terhadap standar IEEE 519. Dan pada C6 Komputasi, mahasiswa mampu memprogram sintesis deret Fourier interaktif menggunakan bahasa Julia.

### Salindia 03: Peta Kurikulum: Transisi Parameter Terpusat ke Terdistribusi

Perhatikan lompatan konseptual pada peta kurikulum ini. Sebelum UTS, kita memodelkan sirkuit listrik sebagai sistem parameter terpusat atau lumped-parameter menggunakan PDB, di mana variabel hanya bergantung pada satu variabel bebas yaitu waktu t. Mulai minggu ini, kita memasuki domain Medan Elektromagnetika dan Gelombang sebagai sistem parameter terdistribusi, di mana variabel seperti tegangan, arus, medan listrik, dan temperatur bergantung secara simultan pada ruang spasial x, y, z dan waktu t. Untuk membedah sistem multi-variabel ini, Deret Fourier menjadi jembatan matematika utama yang menguraikan sebarang sinyal spasial atau temporal menjadi jumlahan harmonisa gelombang sinusoidal murni.

### Salindia 04: Taksonomi & Klasifikasi PDP Linier Orde Dua

Persamaan Diferensial Parsial linier orde dua dua variabel memiliki bentuk umum: A dikali u x x ditambah B dikali u x y ditambah C dikali u y y ditambah suku orde lebih rendah sama dengan nol. Sifat fisis persamaan diklasifikasikan berdasarkan tanda diskriminan kuadratik: Delta sama dengan B kuadrat dikurang empat A C. Pertama, tipe Hiperbolik bila diskriminan positif, memodelkan gelombang perambatan dan saluran transmisi. Kedua, tipe Parabolik bila diskriminan nol, memodelkan difusi panas dan fenomena disipasi termal. Dan ketiga, tipe Eliptik bila diskriminan negatif, memodelkan medan potensial elektrostatika kesetimbangan tunak seperti persamaan Laplace. Klasifikasi ini menentukan jenis syarat batas yang menjamin solusi unik dan stabil.

### Salindia 05: Fondasi Matematika: Teorema Ortogonalitas

Fondasi matematika utama dari deret Fourier adalah Teorema Ortogonalitas fungsi-fungsi trigonometri pada interval satu periode minus L hingga L. Integral dari perkalian kosinus m pi x per L dengan kosinus n pi x per L bernilai nol jika m tidak sama dengan n, dan bernilai tepat L jika m sama dengan n. Demikian pula, perkalian sinus m dengan sinus n bernilai nol bila m berbeda dengan n, dan perkalian silang sinus dengan kosinus selalu bernilai nol untuk semua m dan n. Secara fisis dan aljabar linier, fungsi-fungsi harmonik ini membentuk himpunan vektor basis yang saling tegak lurus pada ruang fungsi tak hingga, memungkinkan kita mengekstrak setiap koefisien harmonisa secara independen tanpa saling mengganggu.

### Salindia 06: Formulasi Deret Fourier Trigonometrik

Berdasarkan teorema Fourier, setiap fungsi periodik f t dengan periode T sama dengan dua L dapat dinyatakan sebagai deret tak hingga: f t sama dengan a nol per dua ditambah jumlahan dari n sama dengan satu hingga tak hingga kurung a n kosinus n omega nol t ditambah b n sinus n omega nol t, di mana omega nol adalah frekuensi sudut fundamental dua pi per T. Koefisien a nol per dua merepresentasikan komponen rata-rata DC dari sinyal. Koefisien a n dan b n dihitung menggunakan rumus integral Euler-Fourier yang memanfaatkan sifat ortogonalitas. Deret ini membuktikan bahwa sebarang bentuk gelombang tak beraturan dapat dibentuk dari paduan harmonisa nada dasar dan kelipatannya.

### Salindia 07: Pemanfaatan Sifat Simetri Bentuk Gelombang

Dalam rekayasa sistem tenaga, menghitung integral Fourier dapat disederhanakan secara dramatis dengan mengenali simetri bentuk gelombang. Pertama, Simetri Genap: f minus t sama dengan f t, seluruh koefisien b n otomatis nol, menyisakan deret kosinus murni. Kedua, Simetri Ganjil: f minus t sama dengan minus f t, komponen DC dan seluruh a n otomatis nol, menyisakan deret sinus murni. Ketiga, Simetri Setengah Gelombang atau Half-Wave Symmetry: f t ditambah T per dua sama dengan minus f t, yang mencirikan gelombang inverter AC simetris. Pada simetri ini, seluruh harmonisa genap bernilai nol mutlak! Sinyal hanya memuat harmonisa ganjil: harmonisa ke-tiga, ke-lima, ke-tujuh, dan seterusnya.

### Salindia 08: Diagram Gelombang Kotak Inverter & Dekomposisi Spektrum

Slide ini menampilkan ilustrasi dekomposisi gelombang kotak keluaran inverter jembatan penuh satu fasa. Gelombang kotak bolak-balik memiliki simetri ganjil dan simetri setengah gelombang. Ketika diuraikan ke dalam domain frekuensi, spektrum amplitudonya memperlihatkan bahwa gelombang kotak tersusun dari: gelombang sinusoidal fundamental berfrekuensi lima puluh Hertz dengan amplitudo empat V nol per pi, ditambah harmonisa ketiga pada seratus lima puluh Hertz dengan amplitudo sepertiga, harmonisa kelima pada dua ratus lima puluh Hertz dengan amplitudo seperlima, dan seterusnya. Semakin tinggi orde harmonisa, kontribusi energinya meluruh sebanding dengan satu per n.

### Salindia 09: Contoh Terhitung: Deret Fourier Gelombang Persegi V_0 = 100 V

Mari kita selesaikan contoh perhitungan eksplisit deret Fourier gelombang kotak inverter dengan amplitudo V nol sama dengan seratus Volt. Karena gelombang memiliki simetri ganjil, komponen DC a nol sama dengan nol dan koefisien kosinus a n sama dengan nol. Koefisien b n dihitung melalui integral: diperoleh b n sama dengan empat ratus dibagi n pi untuk n ganjil, dan nol untuk n genap. Persamaan deret fourier akhirnya adalah: v t sama dengan empat ratus per pi dikalikan kurung sinus omega nol t ditambah sepertiga sinus tiga omega nol t ditambah seperlima sinus lima omega nol t ditambah sepertujuh sinus tujuh omega nol t dan seterusnya. Amplitudo komponen fundamental adalah seratus dua puluh tujuh koma tiga Volt.

### Salindia 10: Fenomena Gibbs (Gibbs Phenomenon) pada Tepi Sinyal

Perhatikan perilaku aproksimasi deret Fourier pada titik diskontinuitas lonjakan sinyal yang memunculkan Fenomena Gibbs. Meskipun kita menambah jumlah suku deret Fourier hingga ribuan atau jutaan suku, pada tepi transisi diskontinu selalu muncul lonjakan lewatan atau overshoot sebesar sekitar sembilan persen dari tinggi lonjakan sinyal! Penambahan jumlah suku hanya merapatkan frekuensi osilasi lonjakan ke dekat tepi diskontinuitas, tetapi tidak pernah menghilangkan puncak lewatan sembilan persen tersebut. Secara fisis pada sistem transmisi daya, fenomena Gibbs merepresentasikan osilasi transien frekuensi tinggi saat terjadi pensaklaran pemutus daya atau sambaran petir.

### Salindia 11: Analisis Polusi Harmonisa Sistem Tenaga Listrik

Beban-beban non-linier modern seperti konverter AC-DC, penggerak motor VFD, catu daya komputer, dan inverter PLTS surya menarik arus yang terdistorsi dari jaringan PLN. Distorsi harmonisa ini memicu berbagai masalah serius pada sistem tenaga: pemanasan berlebih dan penuaan dini pada belitan transformator akibat rugi arus eddy yang membesar sebanding kuadrat frekuensi, resonansi paralel pada bank kapasitor koreksi faktor daya, serta gangguan interferensi elektromagnetik pada kabel telekomunikasi. Tingkat polusi gelombang diukur menggunakan parameter Total Harmonic Distortion atau THD.

### Salindia 12: Standar Industri: Regulasi Harmonisa IEEE Std 519-2022

Untuk menjaga stabilitas dan kualitas daya pada jaringan interkoneksi, standar internasional IEEE Standard 519 edisi 2022 menetapkan batasan ketat terhadap distorsi harmonisa pada titik sambung bersama atau Point of Common Coupling PCC. Total Harmonic Distortion tegangan dibatasi maksimum lima persen untuk sistem tegangan rendah dan menengah di bawah enam puluh sembilan kilo Volt, dengan batas harmonisa individu maksimum tiga persen. Batas distorsi arus disesuaikan dengan rasio hubung singkat I SC terhadap arus beban I L. Jika pelanggan industri melanggar batas IEEE 519 ini, mereka diwajibkan memasang filter harmonisa aktif atau pasif sebelum diizinkan terhubung ke jaringan PLN.

### Salindia 13: Praktikum Komputasi Julia: Rekonstruksi Deret Fourier

Pada praktikum komputasi Julia ini, kita memprogram fungsi rekonstruksi deret Fourier dan visualisasi konvergensinya secara interaktif. Dengan memanfaatkan vektorisasi efisien bahasa Julia, kita menghitung aproksimasi deret gelombang kotak untuk N sama dengan satu, tiga, lima, hingga lima puluh harmonisa. Grafik di sebelah kanan memperlihatkan bagaimana gelombang sinusoidal tunggal pada N sama dengan satu perlahan-lahan bertransformasi menjadi gelombang kotak yang tajam seiring bertambahnya jumlah harmonisa, sekaligus memvisualisasikan osilasi fenomena Gibbs pada tepi lonjakan. Simulasi Julia ini memperdalam pemahaman intuitif Anda mengenai konvergensi ruang fungsi.

### Salindia 14: Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)

**[Bagian 1 - Pertanyaan Kuis]:**
Saatnya kuis interaktif untuk menguji pemahaman fisis deret Fourier Anda. Perhatikan studi kasus pada layar: Jika jumlah harmonisa deret Fourier gelombang kotak dinaikkan dari N sama dengan dua puluh lima hingga N sama dengan satu juta suku, apakah lonjakan overshoot di sudut diskontinuitas akan hilang menuju nol persen? Pilihan A: Ya, karena deret Fourier terbukti konvergen sempurna menuju fungsi aslinya. Pilihan B: Tidak, lecutan overshoot tetap bertengger konstan sebesar kira-kira delapan koma sembilan puluh lima persen sesuai Fenomena Gibbs, dan hanya lebarnya yang menyempit menuju nol! Pilihan C: Ya, tetapi membutuhkan penambahan komponen resistor fisik di dunia nyata. Pilihan D: Tidak, lecutan overshoot justru membesar secara tak terkendali menjadi lima puluh persen. Silakan analisis sifat konvergensi ini dan tentukan pilihan jawaban terbaik Anda dalam delapan detik ke depan.

*[Jeda Hening Berpikir: 8 Detik Terprogram]*

**[Bagian 2 - Pembahasan Kuis & Tantangan Bloom]:**
Waktu habis. Jawaban yang tepat adalah B: Tidak hilang, melainkan bertengger konstan pada delapan koma sembilan puluh lima persen! Ini adalah Fenomena Gibbs yang sangat terkenal. Pada titik diskontinuitas lompatan, penambahan harmonisa hingga tak hingga hanya memampatkan energi overshoot ke dalam pita interval spasial yang makin sempit mendekati nol, namun amplitudo puncaknya tetap konstan sekitar sembilan persen. Pada kolom tantangan sebelah kanan, Anda juga ditantang menghitung Total Harmonic Distortion atau THD inverter PLTS sesuai batas IEEE Std 519 di level C4, membuktikan teorema ortogonalitas fungsi trigonometri di level C5, serta merancang filter harmonisa aktif untuk meredam harmonisa ke-tiga dan ke-lima di level C6.

### Salindia 15: Rangkuman Eksekutif & Jembatan ke Minggu 10

Sebagai rangkuman perkuliahan minggu kesembilan: Pertama, transisi menuju sistem parameter terdistribusi diawali dengan klasifikasi PDP linier orde dua. Kedua, teorema ortogonalitas memungkinkan dekomposisi sebarang sinyal periodik menjadi deret Fourier independen. Ketiga, sifat simetri menyederhanakan perhitungan koefisien dan membuktikan ketiadaan harmonisa genap pada inverter simetris. Dan keempat, pembatasan harmonisa berdasarkan IEEE 519 sangat krusial untuk mencegah pemanasan berlebih pada transformator. Silakan pelajari modul ajar dan tuntaskan Lembar Kerja serta Problem Set Minggu kesembilan di portal ndaratha dot my dot id. Pada minggu kesepuluh, kita akan mempelajari metode pemisahan variabel atau separation of variables untuk menyelesaikan PDP difusi termal. Terima kasih dan wassalamualaikum warahmatullahi wabarakatuh.

