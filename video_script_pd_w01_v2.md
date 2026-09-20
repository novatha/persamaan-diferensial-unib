# Naskah & Metadata Video Kuliah Minggu 01: Persamaan Diferensial v2.0

### 1. Metadata Siap Unggah YouTube (SEO Optimized)

**Judul Resmi:** `[Minggu 01] Klasifikasi PDB/PDP, Masalah Nilai Awal, & Pemodelan Rangkaian RL | Persamaan Diferensial | Teknik Elektro UNIB`

**Deskripsi Siap Unggah:**
```text
Kuliah Daring Minggu 01 - Persamaan Diferensial (Teknik Elektro UNIB)
Topik: Klasifikasi Orde, Derajat, Linieritas, Solusi Umum & Khusus IVP, Transien RL, Arus Inrush Trafo PLN, dan Julia DifferentialEquations.jl

Dosen Pengampu:
- Ir. Novalio Daratha, S.T., M.Sc., Ph.D.
- Muhammad Arfan, S.T., M.T.
Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika
Fakultas Teknik, Universitas Bengkulu

Akses portal perkuliahan, modul ajar, lembar kerja C1-C6, dan problem set:
https://www.ndaratha.my.id/persamaan-diferensial/

Linimasa Bab (Timestamps):
00:00 - 01. Pembukaan Perkuliahan Persamaan Diferensial
00:41 - 02. Capaian Pembelajaran Sub-CPMK 1
01:36 - 03. Peta Konsep & Filosofi Dinamika Sistem
02:17 - 04. Taksonomi PDB vs PDP
02:58 - 05. Klasifikasi Orde, Derajat, & Linieritas
03:38 - 06. Pemodelan First-Principles Rangkaian RL
04:15 - 07. Solusi Umum & Masalah Nilai Awal
04:49 - 08. Penurunan Solusi Analitik Rangkaian RL
05:24 - 09. Dinamika Transien & Skala Waktu tau
05:57 - 10. Studi Kasus Arus Inrush Trafo Gardu Induk
06:38 - 11. Contoh Soal Terhitung Solenoida PMT
07:28 - 12. Praktikum Komputasi Julia DifferentialEquations
08:08 - 13. Verifikasi Simulasi Julia vs Solusi Eksak
08:39 - 14. Kuis Interaktif & Evaluasi Bloom
10:08 - 15. Rangkuman Perkuliahan & Penutup

Buku Referensi Pembelajaran:
1. Erwin Kreyszig, "Advanced Engineering Mathematics", 10th Edition, John Wiley & Sons.
2. Dennis G. Zill, "A First Course in Differential Equations with Modeling Applications", 11th Edition.
3. William H. Hayt & John A. Buck, "Engineering Electromagnetics", 9th Edition, McGraw-Hill.
4. Standar Industri Terkait (IEEE & IEC).

#PersamaanDiferensial #TeknikElektro #UniversitasBengkulu #KalkulusLanjut #DifferentialEquations #JuliaLang
```

---

## 2. Capaian Pembelajaran (Sub-CPMK 1 OBE Taksonomi Bloom)
- **C1 (Mengingat):** Mendefinisikan PDB dan PDP serta membedakan konsep orde, derajat, dan linieritas.
- **C2 (Memahami):** Menjelaskan makna fisis konstanta integrasi dan kontinuitas energi medan magnet induktor.
- **C3 (Menerapkan):** Menurunkan dan menyelesaikan PDB orde satu sirkuit RL dari Hukum Tegangan Kirchhoff.
- **C4 (Menganalisis):** Menganalisis profil transien peluruhan dan pengisian arus terhadap variasi konstanta waktu tau.
- **C5 (Mengevaluasi):** Mengevaluasi fenomena arus inrush transformator gardu induk PLN berbasis batas kejenuhan inti.
- **C6 (Komputasi):** Mengembangkan simulasi komputasi numerik transien RL menggunakan bahasa pemrograman Julia.

---

## 3. Naskah Audio Narasi Per Salindia (15 Slide Lengkap)

### Salindia 01: Judul & Pembukaan Kuliah Minggu 01

Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, selamat datang dalam perkuliahan daring Persamaan Diferensial semester genap 2026. Mata kuliah ini dirancang khusus untuk membangun fondasi analisis matematika yang kokoh dalam memodelkan fenomena fisis kelistrikan dan elektromagnetika. Pada pertemuan perdana minggu pertama ini, kita akan membahas: Klasifikasi PDB dan PDP, Konsep Orde dan Derajat, Syarat Linieritas, Solusi Umum versus Solusi Khusus, Masalah Nilai Awal atau Initial Value Problem, serta Pemodelan Fisis Rangkaian Listrik berbasis Hukum Kirchhoff. Kuliah ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan.

### Salindia 02: Capaian Pembelajaran (Sub-CPMK) & Taksonomi Bloom

Sebelum melangkah lebih jauh, mari kita pahami Capaian Pembelajaran Mata Kuliah minggu ini berbasis Taksonomi Bloom. Pada level C1 Mengingat, mahasiswa mampu mendefinisikan PDB dan PDP serta membedakan konsep orde, derajat, dan linieritas. Pada level C2 Memahami, mahasiswa mampu menjelaskan makna fisis konstanta integrasi dan kondisi awal pada rangkaian listrik. Pada level C3 Menerapkan, mahasiswa mampu menurunkan dan menyelesaikan PDB orde satu dari rangkaian RL menggunakan Hukum Tegangan Kirchhoff. Pada level C4 Menganalisis, mahasiswa mampu menganalisis sifat transien eksponensial dan mengidentifikasi konstanta waktu tau. Pada level C5 Mengevaluasi, mahasiswa mampu mengevaluasi dampak arus inrush trafo terhadap koordinasi relai pengaman. Dan pada level C6 Komputasi, mahasiswa mampu memprogram simulasi numerik respon transien rangkaian di Julia.

### Salindia 03: Peta Jalan Kurikulum & Filosofi Dinamika Elektro

Perhatikan diagram alir kurikulum pada slide ini. Mata kuliah Persamaan Diferensial menjadi jembatan antara sains dasar fisika kalkulus dengan rekayasa terapan seperti Analisis Rangkaian Listrik, Medan Elektromagnetika, dan Sistem Tenaga Listrik. Mengapa insinyur elektro harus menguasai persamaan diferensial? Karena energi di alam semesta tidak dapat berubah seketika. Hubungan antara tegangan, arus, muatan, dan fluks magnetik selalu melibatkan laju perubahan terhadap waktu d per d t, maupun gradien spasial laplacian pada ruang tiga dimensi. Memahami persamaan diferensial berarti memahami bahasa alami alam semesta dalam mengalirkan energi.

### Salindia 04: Taksonomi Persamaan Diferensial: PDB vs PDP

Mari kita klasifikasikan persamaan diferensial ke dalam dua keluarga besar. Pertama, Persamaan Diferensial Biasa atau PDB, yaitu persamaan yang hanya memuat turunan terhadap satu variabel bebas tunggal, seperti waktu t. PDB digunakan untuk memodelkan sistem elemen terpusat, misalnya pengosongan kapasitor RC atau dinamika mesin sinkron. Kedua, Persamaan Diferensial Parsial atau PDP, yang memuat turunan parsial terhadap dua atau lebih variabel bebas, seperti ruang spasial x, y, z dan waktu t. PDP memodelkan fenomena medan terdistribusi, seperti Persamaan Gelombang saluran transmisi tegangan tinggi, Persamaan Laplace potensial elektrostatika, serta difusi panas trafo daya.

### Salindia 05: Klasifikasi Formal: Orde, Derajat, & Linieritas

Ada tiga atribut utama untuk mengklasifikasikan persamaan diferensial secara formal. Pertama, Orde, yaitu tingkat turunan tertinggi yang muncul di dalam persamaan. Kedua, Derajat, yaitu pangkat aljabar dari turunan tertinggi setelah persamaan dibebaskan dari bentuk pecahan atau akar. Ketiga, Linieritas. Suatu persamaan diferensial dikatakan linier jika memenuhi tiga kriteria ketat: variabel tak bebas y dan seluruh turunannya hanya berpangkat satu, tidak ada suku perkalian silang antar turunan, serta tidak ada fungsi non-linier transendental seperti sinus, eksponensial, atau logaritma yang memuat variabel terikat y.

### Salindia 06: Pemodelan Fisis: Sirkuit Pengisian RL

Sekarang kita masuki Pilar 1: pemodelan fisis dari hukum dasar rangkaian. Tinjau sirkuit RL seri yang dihubungkan ke sumber tegangan searah V nol saat sakelar ditutup pada t sama dengan nol. Berdasarkan Hukum Tegangan Kirchhoff, jumlah tegangan dalam loop tertutup sama dengan nol: tegangan sumber V nol sama dengan jatuh tegangan resistor v R ditambah tegangan induktor v L. Karena tegangan resistor adalah R dikali i, dan tegangan induktor menurut Hukum Faraday-Lenz adalah L dikali d i per d t, maka kita peroleh PDB linier orde satu koefisien konstan: L d i per d t ditambah R i sama dengan V nol.

### Salindia 07: Solusi Umum vs Solusi Khusus (IVP)

Dalam matematika, mengintegrasikan PDB orde satu akan selalu memunculkan satu konstanta integrasi sembarang C. Ekspresi yang masih memuat konstanta C sembarang disebut Solusi Umum, yang secara geometris merepresentasikan keluarga kurva tak berhingga banyaknya. Namun di laboratorium teknik elektro nyata, respons arus rangkaian pada saat sakelar ditutup hanya memiliki satu kurva riil yang unik. Untuk menentukan nilai spesifik konstanta C, kita memerlukan Masalah Nilai Awal atau Initial Value Problem, yaitu kondisi nilai variabel keadaan pada saat awal t sama dengan nol, i nol sama dengan nol.

### Salindia 08: Derivasi Analitik Solusi Khusus Rangkaian RL

Mari kita turunkan solusi khususnya langkah demi langkah menggunakan metode separabel. Dari L d i per d t sama dengan V nol dikurang R i, kita pisahkan variabel arus ke ruas kiri dan waktu ke ruas kanan: d i dibagi kurung V nol per R dikurang i sama dengan R per L d t. Integrasikan kedua ruas menghasilkan minus logaritma natural kurung V nol per R dikurang i sama dengan R per L t ditambah konstanta. Dengan mengeksponensialkan kedua ruas dan mensubstitusikan syarat batas arus awal nol pada t sama dengan nol, kita peroleh solusi khusus eksak: i t sama dengan V nol per R dikali kurung satu dikurang e pangkat minus t per tau.

### Salindia 09: Karakteristik Dinamika Transien & Konstanta Waktu tau

Parameter tau didefinisikan sebagai L per R dan dinamakan konstanta waktu sirkuit dengan satuan detik. Konstanta waktu mengukur kelembaman sistem induktif dalam merespons perubahan energi magnetik. Pada saat t sama dengan satu tau, arus pengisian mencapai enam puluh tiga koma dua persen dari arus kondisi mantap. Pada tiga tau, arus telah mencapai sembilan puluh lima persen. Dan pada lima tau atau 5 tau, arus telah mencapai sembilan puluh sembilan koma tiga persen, sehingga secara praktis rekayasa dianggap telah mencapai keadaan tunak atau steady-state.

### Salindia 10: Studi Kasus Rekayasa: Arus Inrush Trafo Gardu Induk PLN

Mari kita lihat aplikasi nyata di industri kelistrikan PLN. Ketika transformator daya gardu induk dihubungkan ke grid pada saat gelombang tegangan berada di titik nol derajat, fluks magnetik inti trafo harus berlipat ganda menjadi dua kali fluks nominal demi memenuhi hukum Faraday. Akibatnya, inti besi trafo mengalami saturasi magnetik hebat, menyebabkan induktansi efektif L anjlok drastis ke nilai induktansi udara. Penurunan drastis nilai L ini memicu lonjakan arus yang disebut arus inrush hingga delapan sampai dua belas kali lipat arus nominal. Pemodelan transien PDB memungkinkan para insinyur merancang kurva koordinasi relai diferensial agar tidak memutus pemutus tenaga secara keliru saat pensaklaran.

### Salindia 11: Contoh Soal Terhitung (Worked Example): Solenoida PMT

Mari kita selesaikan contoh soal numerik perancangan koil solenoida pemutus tenaga atau PMT. Koil memiliki induktansi L sama dengan dua koma lima Henry dan resistansi R sama dengan lima puluh ohm, dihubungkan ke sumber DC seratus volt. Pertama, kita hitung konstanta waktu tau sama dengan L per R, yaitu dua koma lima dibagi lima puluh, menghasilkan nol koma nol lima detik atau lima puluh milidetik. Kedua, arus tunak adalah V nol per R sama dengan seratus dibagi lima puluh, yaitu dua Ampere. Ketiga, arus pada t sama dengan tiga puluh milidetik dihitung dari rumus analitik, menghasilkan nol koma sembilan nol dua Ampere. Keempat, waktu yang dibutuhkan untuk mencapai satu koma delapan Ampere atau sembilan puluh persen arus maksimum adalah minus tau dikali logaritma natural nol koma satu, menghasilkan seratus lima belas milidetik.

### Salindia 12: Praktikum Komputasi Numerik Terbuka Berbasis Julia

Sekarang kita masuk ke Pilar 3, yaitu komputasi ilmiah modern berbasis bahasa pemrograman berkecepatan tinggi: Julia. Pada salindia ini ditampilkan kode ringkas menggunakan pustaka terdepan dunia, DifferentialEquations dot j l dan Plots dot j l. Kita definisikan fungsi dinamika sirkuit RL f r l kurung i koma p koma t sama dengan kurung V nol dikurang R dikali i dibagi L. Selanjutnya kita inisialisasi masalah nilai awal menggunakan konstruktor O D E Problem dengan kondisi awal arus nol, lalu menyelesaikannya menggunakan solver numerik adaptif Tsit lima. Julia mengeksekusi kode ini dengan kompilasi JIT mendekati kecepatan bahasa C.

### Salindia 13: Verifikasi Hasil Komputasi Julia & Dinamika Transien

Pada salindia ini kita bandingkan kurva respon hasil solver Julia dengan garis analitis eksak. Perhatikan bahwa titik-titik diskret komputasi Tsit lima berimpit secara sempurna tanpa deviasi sedikit pun pada solusi eksak. Grafik di sebelah kanan juga memvisualisasikan bagaimana laju perubahan arus d i per d t mencapai nilai maksimum pada t sama dengan nol dan meluruh secara mulus menuju nol saat kondisi mantap tercapai. Ini membuktikan bahwa pustaka numerik terbuka memberikan akurasi yang sangat tinggi untuk analisis dinamika sistem keteknikan.

### Salindia 14: Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)

**[Bagian 1 - Pertanyaan Kuis]:**
Saatnya kuis interaktif untuk menguji intuisi fisika Anda. Tinjau kasus rekayasa berikut: Sakelar rangkaian RL dihubungkan ke sumber tegangan DC V nol. Saat sakelar ditutup pada t sama dengan nol, mengapa arus awal i nol positif bernilai tepat nol, padahal tegangan sumber V nol sudah aktif penuh? Pilihan A: Resistor R memblokir aliran arus pada awal transien. Pilihan B: Induktor menginduksi gaya gerak listrik lawan v L sama dengan minus L d i per d t yang menentang lonjakan arus demi kekekalan fluks! Pilihan C: Baterai memerlukan jeda waktu untuk melepaskan muatan listrik. Pilihan D: Energi medan magnetik membutuhkan hambatan luar untuk stabil. Silakan pikirkan dan tentukan pilihan jawaban Anda dalam delapan detik ke depan.

*[Jeda Hening Berpikir: 8 Detik Terprogram]*

**[Bagian 2 - Pembahasan Kuis & Tantangan Bloom]:**
Waktu habis. Jawaban yang tepat adalah B: Induktor menginduksi gaya gerak listrik lawan v L sama dengan minus L d i per d t! Sesuai Hukum Faraday-Lenz dan prinsip kekekalan energi medan magnetik setengah L i kuadrat, energi tidak dapat berubah diskontinu. Oleh karena itu arus induktor harus kontinu, memaksa arus bernilai nol tepat pada saat sakelar ditutup. Pada panel sebelah kanan, Anda juga ditantang untuk menganalisis disipasi energi kalor resistor pada C4, mengevaluasi respons relai proteksi pada C5, serta merancang sirkuit snubber pada level C6.

### Salindia 15: Rangkuman Inti Perkuliahan & Referensi

Sebagai penutup pertemuan perdana, mari kita rangkum tiga pilar utama materi hari ini. Pertama, dinamika sistem tenaga dan rangkaian elektrik dimodelkan oleh persamaan diferensial melalui Hukum Kirchhoff dan prinsip kontinuitas energi medan. Kedua, solusi umum memuat konstanta integrasi sembarang, sedangkan solusi khusus ditentukan secara tunggal oleh Masalah Nilai Awal atau IVP. Ketiga, konstanta waktu tau sama dengan L per R menjadi penentu kecepatan respons transien. Untuk memperdalam pemahaman, silakan kerjakan Lembar Kerja Mahasiswa dan Problem Set C1 sampai C6 pada portal web perkuliahan. Terima kasih atas perhatian Anda, sampai jumpa pada perkuliahan minggu kedua.

