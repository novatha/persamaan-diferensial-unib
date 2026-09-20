# Naskah & Metadata Video Kuliah Minggu 06: Persamaan Diferensial v2.0

### 1. Metadata Siap Unggah YouTube (SEO Optimized)

**Tautan Resmi YouTube:** [https://youtu.be/iIYM-WRaTiU](https://youtu.be/iIYM-WRaTiU)  

**Judul Resmi:** `[Minggu 06] Transformasi Laplace Dasar: Domain-s & Teorema Pergeseran | Persamaan Diferensial | Teknik Elektro UNIB`

**Deskripsi Siap Unggah:**
```text
Kuliah Daring Minggu 06 - Persamaan Diferensial (Teknik Elektro UNIB)
Topik: Definisi Formal Integral Laplace, Sifat Linieritas, Operator Turunan & Kondisi Awal, Fungsi Heaviside & Dirac, Teorema Pergeseran Frekuensi/Waktu, dan Surja Petir IEC 60060-1

Dosen Pengampu:
- Ir. Novalio Daratha, S.T., M.Sc., Ph.D.
- Muhammad Arfan, S.T., M.T.
Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika
Fakultas Teknik, Universitas Bengkulu

Akses portal perkuliahan, modul ajar, lembar kerja C1-C6, dan problem set:
https://www.ndaratha.my.id/persamaan-diferensial/

Linimasa Bab (Timestamps):
00:00 - 01. Pembukaan Perkuliahan Minggu 06
00:43 - 02. Sub-CPMK 4 & Taksonomi Bloom
01:32 - 03. Peta Konsep: Mengapa Domain-s?
02:16 - 04. Definisi Formal Integral Laplace
03:00 - 05. Pasangan Transformasi Baku
03:39 - 06. Linieritas & Transformasi Turunan
04:18 - 07. Fungsi Tangga Satuan Heaviside
04:54 - 08. Fungsi Impuls Dirac
05:32 - 09. Teorema Pergeseran Pertama
06:07 - 10. Teorema Pergeseran Kedua
06:43 - 11. Surja Petir IEC 60060-1
07:27 - 12. Contoh Soal Konversi IVP ke Domain-s
08:15 - 13. Praktikum Julia: Surja Petir IEC
08:54 - 14. Kuis Interaktif & Evaluasi Bloom
10:31 - 15. Rangkuman Perkuliahan & Penutup

Buku Referensi Pembelajaran:
1. Erwin Kreyszig, "Advanced Engineering Mathematics", 10th Edition, John Wiley & Sons.
2. Dennis G. Zill, "A First Course in Differential Equations with Modeling Applications", 11th Edition.
3. William H. Hayt & John A. Buck, "Engineering Electromagnetics", 9th Edition, McGraw-Hill.
4. Standar Industri Terkait (IEEE & IEC).

#PersamaanDiferensial #TeknikElektro #UniversitasBengkulu #KalkulusLanjut #DifferentialEquations #JuliaLang
```

---

## 2. Capaian Pembelajaran (Sub-CPMK 6 OBE Taksonomi Bloom)
- **C1 (Mengingat):** Menyatakan definisi integral satu sisi Transformasi Laplace dan syarat keberadaan orde eksponensial.
- **C2 (Memahami):** Menjelaskan keuntungan aljabar transformasi turunan d^n y / dt^n yang menyertakan kondisi awal secara otomatis.
- **C3 (Menerapkan):** Menerapkan pasangan transformasi baku dan teorema pergeseran pertama/kedua pada fungsi waktu.
- **C4 (Menganalisis):** Memodelkan sinyal diskontinu pensaklaran tangga Heaviside dan surja petir Dirac impulsif.
- **C5 (Mengevaluasi):** Mengevaluasi bentuk gelombang surja petir standar gardu induk 1.2/50 mikrodetik IEC 60060-1.
- **C6 (Komputasi):** Memprogram sintesis kurva tegangan surja petir dan transformasi Laplace numerik dengan Julia.

---

## 3. Naskah Audio Narasi Per Salindia (15 Slide Lengkap)

### Salindia 01: Judul & Pembukaan Kuliah Minggu 06

Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, selamat datang kembali dalam perkuliahan daring Persamaan Diferensial semester genap 2026. Pada Minggu keenam ini, kita membuka pintu gerbang metode operasional paling berdaya guna dalam rekayasa elektro: Transformasi Laplace dan Teorema Pergeseran pada Domain Frekuensi Kompleks s. Kita akan mempelajari bagaimana transformasi integral mengubah kalkulus diferensial yang rumit menjadi aljabar linier biasa, menangani fungsi khusus tak kontinu seperti Tangga Heaviside dan Impuls Dirac, serta memodelkan gelombang surja petir standar gardu induk IEC 60060-1. Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan.

### Salindia 02: Capaian Pembelajaran (Sub-CPMK 4) & Taksonomi Bloom

Berikut adalah Capaian Pembelajaran Sub-CPMK Minggu keenam berbasis Taksonomi Bloom. Pada C1 Mengingat, mahasiswa mampu menyatakan definisi integral Transformasi Laplace dan wilayah konvergensi ROC. Pada C2 Memahami, mahasiswa mampu menjelaskan keunggulan domain s dalam menggabungkan kondisi awal secara langsung. Pada C3 Menerapkan, mahasiswa mampu menghitung transformasi fungsi elementer dan menerapkan teorema translasi. Pada C4 Menganalisis, mahasiswa mampu memodelkan sinyal pulsa sepotong-sepotong menggunakan fungsi Heaviside. Pada C5 Mengevaluasi, mahasiswa mampu mengkaji parameter waktu muka dan ekor gelombang surja petir IEC. Dan pada C6 Komputasi, mahasiswa mampu memvisualisasikan sinyal surja transien dengan bahasa Julia.

### Salindia 03: Peta Konsep: Mengapa Beralih ke Domain Kompleks s?

Perhatikan diagram alir paradigma operasional Laplace pada slide ini. Dalam domain waktu riil t, menyelesaikan Masalah Nilai Awal PDB membutuhkan proses integrasi, pencarian akar karakteristik, dan penyusunan sistem persamaan aljabar untuk konstanta C satu dan C dua. Transformasi Laplace menawarkan jembatan transformasi: PDB di domain waktu diubah menjadi persamaan aljabar linier di domain frekuensi s. Di domain s, kita hanya melakukan manipulasi aljabar pecahan sederhana untuk mengisolasi variabel Y s. Setelah itu, melalui invers transformasi Laplace, kita langsung memperoleh solusi waktu lengkap yang sudah otomatis memuat seluruh kondisi awal. Metode ini menghilangkan kebutuhan mencari solusi homogen dan partikular secara terpisah.

### Salindia 04: Definisi Formal & Syarat Keberadaan Transformasi Laplace

Secara formal, Transformasi Laplace satu sisi dari fungsi waktu f t didefinisikan sebagai integral tak wajar: L kurung f t sama dengan F s sama dengan integral dari nol hingga tak hingga f t dikalikan e pangkat minus s t d t. Variabel s adalah frekuensi kompleks s sama dengan sigma ditambah j omega. Teorema Keberadaan menjamin bahwa F s pasti ada dan konvergen pada setengah bidang kanan riil s lebih besar dari gamma, asalkan f t memenuhi dua syarat: Pertama, f t kontinu sepotong-sepotong pada setiap interval berhingga. Kedua, f t berorde eksponensial, yaitu nilai mutlak f t tidak tumbuh lebih cepat daripada M dikalikan e pangkat gamma t saat t menuju tak hingga. Seluruh sinyal fisik rekayasa elektro selalu memenuhi kriteria ini.

### Salindia 05: Pasangan Transformasi Laplace Baku Fungsi Elementer

Melalui evaluasi integral definisi, kita memperoleh tabel pasangan transformasi baku fungsi-fungsi elementer. Fungsi konstan satu bertransformasi menjadi satu per s. Fungsi waktu polinomial t pangkat n bertransformasi menjadi n faktorial dibagi s pangkat n ditambah satu. Fungsi peluruhan eksponensial e pangkat a t bertransformasi menjadi satu dibagi s dikurang a. Fungsi sinusoidal kosinus omega t bertransformasi menjadi s dibagi s kuadrat ditambah omega kuadrat, sedangkan sinus omega t bertransformasi menjadi omega dibagi s kuadrat ditambah omega kuadrat. Tabel baku ini menjadi kamus operasional utama Anda dalam menyelesaikan analisis rangkaian listrik.

### Salindia 06: Sifat Linieritas & Transformasi Operator Turunan

Transformasi Laplace memiliki sifat linieritas sempurna: transformasi dari kombinasi linier fungsi sama dengan kombinasi linier transformasinya. Namun keunggulan paling revolusioner terletak pada Teorema Diferensiasi: transformasi Laplace dari turunan pertama d f per d t adalah s dikalikan F s dikurang kondisi awal f nol. Sedangkan turunan kedua d kuadrat f per d t kuadrat bertransformasi menjadi s kuadrat F s dikurang s f nol dikurang f prima nol. Perhatikan bahwa operator kalkulus d per d t berganti menjadi perkalian dengan variabel aljabar s, dan kondisi awal f nol serta laju f prima nol secara otomatis langsung terintegrasi ke dalam persamaan aljabar.

### Salindia 07: Fungsi Khusus 1: Tangga Satuan Heaviside u(t - a)

Dalam teknik pensaklaran listrik, kita sering menghadapi sinyal yang dinyalakan atau dimatikan secara mendadak pada waktu t sama dengan a. Oliver Heaviside memperkenalkan Fungsi Tangga Satuan u kurung t dikurang a, yang bernilai nol untuk t kurang dari a, dan bernilai satu untuk t lebih besar dari atau sama dengan a. Transformasi Laplace dari fungsi tangga satuan u kurung t dikurang a adalah e pangkat minus a s dibagi s. Fungsi Heaviside berfungsi sebagai sakelar aljabar yang sangat efektif untuk menyusun sinyal gelombang pulsa, segitiga, dan gelombang sepotong-sepotong tanpa perlu membagi interval integrasi secara manual.

### Salindia 08: Fungsi Khusus 2: Impuls Satuan Dirac delta(t - a)

Untuk memodelkan fenomena kejutan instan seperti sambaran petir, lonjakan elektrostatik ESD, atau ketukan mekanis sesaat, Paul Dirac merumuskan Fungsi Impuls delta kurung t dikurang a. Fungsi delta bernilai nol di semua titik kecuali pada t sama dengan a di mana nilainya menuju tak hingga, dengan luas integral total tepat sama dengan satu satuan. Sifat penyaring atau sifting property menyatakan bahwa integral f t dikali delta t dikurang a menghasilkan nilai f di titik a. Transformasi Laplace dari impuls satuan Dirac delta t dikurang a adalah fungsi eksponensial murni e pangkat minus a s. Bila impuls terjadi pada t sama dengan nol, transformasinya bernilai tepat satu.

### Salindia 09: Teorema Pergeseran Pertama (Translasi Frekuensi Sumbu-s)

Teorema Pergeseran Pertama atau Translasi Frekuensi menyatakan: jika transformasi dari f t adalah F s, maka perkalian f t dengan fungsi eksponensial e pangkat a t menggeser variabel kompleks s menjadi F kurung s dikurang a. Teorema ini sangat ampuh untuk mentransformasikan gelombang sinusoidal teredam yang muncul pada rangkaian underdamped. Sebagai contoh, fungsi e pangkat minus alpha t dikalikan kosinus omega t langsung bertransformasi menjadi s ditambah alpha dibagi kurung s ditambah alpha kuadrat ditambah omega kuadrat. Peredaman waktu di domain t berkorespondensi langsung dengan pergeseran kutub ke kiri pada bidang s.

### Salindia 10: Teorema Pergeseran Kedua (Translasi Waktu Sumbu-t)

Teorema Pergeseran Kedua atau Translasi Waktu adalah pasangan simetris dari teorema pertama: jika suatu sinyal f t mengalami penundaan waktu sebesar a detik menjadi f kurung t dikurang a dikalikan tangga u t dikurang a, maka hasil transformasinya di domain s adalah F s dikalikan faktor modulasi fasa e pangkat minus a s. Teorema ini menjadi tulang punggung analisis saluran transmisi daya, saluran tunda komunikasi, dan sistem kendali berbasis mikrokontroler dengan jeda waktu transportasi atau dead-time. Penundaan waktu murni tidak mengubah spektrum frekuensi F s selain memberikan pergeseran fasa linier.

### Salindia 11: Aplikasi Industri: Surja Petir Standar IEC 60060-1 / IEEE Std 4

Aplikasi industri bertegangan tinggi yang sangat vital adalah pengujian koordinasi isolasi transformator dan kabel terhadap surja petir. Standar internasional IEC 60060-1 dan IEEE Standard 4 mendefinisikan bentuk gelombang impuls petir standar satu koma dua per lima puluh mikrodetik. Secara matematis, impuls petir ini dibentuk oleh selisih dua fungsi eksponensial: v t sama dengan V nol dikalikan kurung e pangkat minus alpha t dikurang e pangkat minus beta t dikalikan u t. Parameter beta yang besar mengatur waktu muka gelombang yang sangat curam satu koma dua mikrodetik, sedangkan alpha mengatur waktu paruh ekor gelombang lima puluh mikrodetik. Melalui Transformasi Laplace, respon tegangan tembus pada peralatan gardu induk dapat dianalisis secara analitik eksak.

### Salindia 12: Contoh Soal Terhitung (Worked Example): Konversi IVP ke Domain-s

Mari kita bedah contoh soal terhitung konversi Masalah Nilai Awal ke domain s. Diberikan PDB rangkaian: d kuadrat y per d t kuadrat ditambah empat d y per d t ditambah tiga belas y sama dengan nol, dengan syarat awal y nol sama dengan dua dan y prima nol sama dengan minus dua. Langkah satu: kita terapkan transformasi Laplace pada setiap suku. Turunan kedua menjadi s kuadrat Y s dikurang dua s ditambah dua. Turunan pertama menjadi empat dikali s Y s dikurang dua. Suku ketiga menjadi tiga belas Y s. Langkah dua: kumpulkan suku Y s di ruas kiri: kurung s kuadrat ditambah empat s ditambah tiga belas dikali Y s sama dengan dua s ditambah enam. Solusi aljabar di domain s adalah Y s sama dengan dua s ditambah enam dibagi s kuadrat tambah empat s tambah tiga belas.

### Salindia 13: Praktikum Komputasi Julia: Surja Petir IEC 60060-1

Pada praktikum komputasi Julia ini, kita memprogram perumusan analitik impuls petir standar IEC 60060-1 dan mengevaluasi respon transiennya. Kita definisikan konstanta V nol satu koma nol tiga delapan mega Volt, alpha empat belas koma enam ribu detik minus satu, dan beta dua koma empat ratus enam puluh ribu detik minus satu. Grafik di sebelah kanan menunjukkan kurva gelombang surja petir yang melonjak tajam ke puncak satu mega Volt dalam satu koma dua mikrodetik, lalu meluruh perlahan hingga separuh tegangan puncak tepat pada lima puluh mikrodetik. Simulasi numerik Julia ini memungkinkan insinyur menguji margin ketahanan isolator polimer dan transformator transmisi sebelum diproduksi di pabrik.

### Salindia 14: Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)

**[Bagian 1 - Pertanyaan Kuis]:**
Saatnya kuis interaktif untuk menguji pemahaman konsep Laplace Anda. Perhatikan studi kasus pada layar: Mengapa metode Transformasi Laplace jauh lebih unggul daripada metode PDB klasik dalam menganalisis fenomena surja pensaklaran atau switching di gardu induk? Pilihan A: Transformasi Laplace tidak lagi memerlukan penerapan Hukum Tegangan Kirchhoff. Pilihan B: Transformasi Laplace secara otomatis mengonversi fungsi diskontinu seperti fungsi undak Heaviside dan impuls Dirac serta turunan waktu menjadi aljabar rasional domain-s dengan kondisi awal terintegrasi langsung! Pilihan C: Transformasi Laplace hanya dapat diaplikasikan jika frekuensi sistem bernilai tepat nol Hertz. Pilihan D: Transformasi Laplace meniadakan kebutuhan nilai induktansi reaktif komponen. Silakan pertimbangkan dan tentukan jawaban terbaik Anda dalam delapan detik ke depan.

*[Jeda Hening Berpikir: 8 Detik Terprogram]*

**[Bagian 2 - Pembahasan Kuis & Tantangan Bloom]:**
Waktu habis. Jawaban yang tepat adalah B: Mengubah fungsi diskontinu dan turunan menjadi aljabar domain-s dengan kondisi awal otomatis! Metode klasik sangat kesulitan saat menghadapi fungsi masukan terpotong-potong atau diskontinu seperti sambaran petir dan pensaklaran PMT. Dengan Transformasi Laplace, kalkulus diferensial diubah menjadi manipulasi aljabar pecahan parsial sederhana. Pada kolom tantangan sebelah kanan, Anda juga ditantang menentukan tegangan transien dengan teorema pergeseran waktu pada level C4, membuktikan Teorema Nilai Akhir pada level C5, serta merancang rangkaian pembangkit impuls Marx Generator laboratorium tegangan tinggi pada level C6.

### Salindia 15: Rangkuman Inti Perkuliahan & Referensi

Sebagai rangkuman perkuliahan minggu keenam: Pertama, Transformasi Laplace mengonversi kalkulus diferensial menjadi aljabar linier pada domain kompleks s. Kedua, transformasi operator turunan secara otomatis menyertakan kondisi awal tanpa perlu proses terpisah. Ketiga, fungsi khusus Heaviside dan Dirac memungkinkan representasi sinyal pensaklaran dan surja petir secara elegan. Dan keempat, teorema translasi waktu dan frekuensi mempermudah analisis transien kompleks. Silakan pelajari modul ajar dan tuntaskan Lembar Kerja serta Problem Set Minggu keenam di portal ndaratha dot my dot id. Pada minggu ketujuh, kita akan mendalami Invers Transformasi Laplace, metode pecahan parsial, dan analisis sirkuit domain s. Terima kasih dan wassalamualaikum warahmatullahi wabarakatuh.

