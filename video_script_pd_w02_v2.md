# Naskah & Metadata Video Kuliah Minggu 02: Persamaan Diferensial v2.0

### 1. Metadata Siap Unggah YouTube (SEO Optimized)

**Tautan Resmi YouTube:** [https://youtu.be/5GQHKrvaSwg](https://youtu.be/5GQHKrvaSwg)  

**Judul Resmi:** `[Minggu 02] PDB Orde 1: Separabel, Eksak, Faktor Integrasi & Rangkaian RC | Persamaan Diferensial | Teknik Elektro UNIB`

**Deskripsi Siap Unggah:**
```text
Kuliah Daring Minggu 02 - Persamaan Diferensial (Teknik Elektro UNIB)
Topik: Bentuk Diferensial M dx + N dy = 0, Medan Konservatif, Transien Sirkuit RC, Paradoks Efisiensi 50%, Snubber IGBT, dan Julia Tsit5

Dosen Pengampu:
- Ir. Novalio Daratha, S.T., M.Sc., Ph.D.
- Muhammad Arfan, S.T., M.T.
Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika
Fakultas Teknik, Universitas Bengkulu

Akses portal perkuliahan, modul ajar, lembar kerja C1-C6, dan problem set:
https://www.ndaratha.my.id/persamaan-diferensial/

Linimasa Bab (Timestamps):
00:00 - 01. Pembukaan Perkuliahan Minggu 02
00:47 - 02. Sub-CPMK OBE & Taksonomi Bloom
01:46 - 03. Peta Konsep & Taksonomi PDB Orde 1
02:40 - 04. Metode Separabel & Syarat Singularitas
03:24 - 05. Persamaan Eksak & Uji Euler-Clairaut
04:09 - 06. Intuisi Fisika Medan Konservatif
04:55 - 07. Algoritma Rekonstruksi Potensial u(x,y)
05:45 - 08. Penentuan Faktor Pengintegrasi mu
06:35 - 09. Pemodelan Transien Sirkuit RC
07:25 - 10. Dinamika Transien & Paradoks Energi 50%
08:14 - 11. Proteksi RC Snubber pada IGBT
08:57 - 12. Contoh Soal Terhitung Bank Kapasitor
09:54 - 13. Praktikum Komputasi Julia Tsit5
10:45 - 14. Kuis Interaktif & Evaluasi Bloom
12:07 - 15. Rangkuman & Referensi

Buku Referensi Pembelajaran:
1. Erwin Kreyszig, "Advanced Engineering Mathematics", 10th Edition, John Wiley & Sons.
2. Dennis G. Zill, "A First Course in Differential Equations with Modeling Applications", 11th Edition.
3. William H. Hayt & John A. Buck, "Engineering Electromagnetics", 9th Edition, McGraw-Hill.
4. Standar Industri Terkait (IEEE & IEC).

#PersamaanDiferensial #TeknikElektro #UniversitasBengkulu #KalkulusLanjut #DifferentialEquations #JuliaLang
```

---

## 2. Capaian Pembelajaran (Sub-CPMK 2 OBE Taksonomi Bloom)
- **C1 (Mengingat):** Menyatakan bentuk kanonik diferensial M dx + N dy = 0 dan kriteria Euler-Clairaut.
- **C2 (Memahami):** Menghubungkan persamaan eksak dengan medan konservatif skalar elektrostatik.
- **C3 (Menerapkan):** Menghitung faktor pengintegrasi mu(x) atau mu(y) pada PDB non-eksak secara analitik.
- **C4 (Menganalisis):** Memodelkan dinamika pengisian & pengosongan kapasitor (tau = RC).
- **C5 (Mengevaluasi):** Mengkaji paradoks efisiensi 50% disipasi kalor resistor pada sirkuit RC.
- **C6 (Komputasi):** Memprogram solver numerik adaptif Julia DifferentialEquations.jl dengan metode Tsit5().

---

## 3. Naskah Audio Narasi Per Salindia (15 Slide Lengkap)

### Salindia 01: Judul & Pembukaan Kuliah Minggu 02

Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, selamat datang kembali dalam perkuliahan daring Persamaan Diferensial semester genap 2026. Pada pertemuan minggu kedua ini, kita akan membedah secara tuntas tiga metodologi analitik fundamental untuk menyelesaikan Persamaan Diferensial Biasa Orde Satu, yaitu: Metode Separabel atau pemisahan variabel, Persamaan Eksak berbasis medan vektor konservatif, serta teknik penanganan persamaan non-eksak melalui Faktor Pengintegrasi. Selanjutnya, kita akan menerapkan seluruh perangkat matematika ini untuk memodelkan fenomena transien pada sirkuit resistor kapasitor atau sirkuit RC, serta proteksi sakelar daya semikonduktor di industri tenaga listrik. Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan.

### Salindia 02: Capaian Pembelajaran (Sub-CPMK 2) & Taksonomi Bloom

Mari kita cermati Capaian Pembelajaran Sub-CPMK Minggu kedua berbasis Taksonomi Bloom. Pada C1 Mengingat, mahasiswa mampu menyatakan bentuk diferensial M d x ditambah N d y sama dengan nol dan uji Euler-Clairaut. Pada C2 Memahami, mahasiswa mampu mengaitkan persamaan eksak dengan konsep gradien potensial medan elektrostatik. Pada C3 Menerapkan, mahasiswa mampu menghitung faktor pengintegrasi mu x atau mu y pada PDB non-eksak. Pada C4 Menganalisis, mahasiswa mampu memodelkan pengisian kapasitor dan konstanta waktu tau sama dengan R dikali C. Pada C5 Mengevaluasi, mahasiswa mampu membuktikan paradoks efisiensi lima puluh persen pada pengisian kapasitor. Dan pada C6 Komputasi, mahasiswa mampu memprogram solver Tsit lima pada pustaka DifferentialEquations dot j l di Julia.

### Salindia 03: Peta Jalan Kurikulum & Posisi Modul Minggu 2

Bagan alir pada slide ini memperlihatkan sistematika keputusan dalam memilih metode penyelesaian PDB orde satu. Langkah pertama, ubah persamaan ke bentuk diferensial M d x ditambah N d y sama dengan nol. Uji apakah variabel x dan y dapat dipisahkan secara langsung. Jika ya, selesaikan dengan integrasi terpisah. Jika tidak separabel, lakukan uji ke-eksak-an turunan parsial parsial M per parsial y dan parsial N per parsial x. Bila nilainya identik, maka PDB bersifat eksak dan dapat diselesaikan dengan merekonstruksi fungsi potensial skalar u x koma y. Namun bila tidak sama, cari faktor pengintegrasi mu untuk mengubahnya menjadi eksak.

### Salindia 04: Metode Pemisahan Variabel (Separable ODE)

Bentuk umum metode separabel adalah g y d y sama dengan f x d x. Solusi umum diperoleh langsung melalui integrasi kedua ruas, menghasilkan integral g y d y sama dengan integral f x d x ditambah C. Perhatikan peringatan matematis di sebelah kanan: pembagian dengan suku yang memuat variabel harus memeriksa syarat nol. Nilai variabel yang menyebabkan penyebut bernilai nol dapat melahirkan solusi singular yang tidak tercakup dalam konstanta C pada keluarga solusi umum.

### Salindia 05: Persamaan Eksak: Definisi & Kriteria Euler-Clairaut

Suatu diferensial M d x ditambah N d y dikatakan eksak jika merupakan diferensial total dari suatu fungsi skalar u x koma y, yaitu d u sama dengan parsial u per parsial x d x ditambah parsial u per parsial y d y sama dengan nol. Berdasarkan Teorema Euler-Clairaut tentang kesetaraan turunan parsial campuran kedua, syarat perlu dan cukup ke-eksak-an adalah parsial M per parsial y harus sama dengan parsial N per parsial x pada domain terdefinisi. Solusi implisitnya dinyatakan sederhana sebagai fungsi tingkat u x koma y sama dengan konstanta C.

### Salindia 06: Intuisi Fisika: Analogi Medan Vektor Konservatif

Bagi mahasiswa Teknik Elektro, konsep PDB eksak memiliki analogi fisik yang sangat indah dengan medan elektrostatika. Vektor F sama dengan M i topi ditambah N j topi bertindak sebagai medan vektor gaya. Kriteria ke-eksak-an sesungguhnya adalah komponen kurva rotasi atau curl dari vektor F yang bernilai nol. Sesuai Hukum Elektrostatika Gauss dan Faraday untuk medan statik, rotasi medan listrik E sama dengan nol. Ini membuktikan bahwa medan tersebut bersifat konservatif dan dapat diturunkan dari gradien potensial skalar listrik V. Garis-garis solusi PDB eksak tidak lain adalah garis ekuipotensial pada ruang elektrostatika.

### Salindia 07: Prosedur Rekonstruksi Solusi Eksak: Langkah demi Langkah

Untuk menurunkan fungsi solusi u x koma y secara first-principles, kita gunakan algoritma 4 langkah. Langkah 1: integrasikan M terhadap x dengan menganggap y konstan, memunculkan fungsi pengintegrasi k y. Langkah 2: turunkan hasil tersebut secara parsial terhadap y. Langkah 3: samakan hasil turunan tersebut dengan fungsi N x koma y untuk mengisolasi turunan k aksen y. Langkah 4: integrasikan k aksen y terhadap y, lalu gabungkan ke solusi akhir u x koma y sama dengan C.

### Salindia 08: Teknik Faktor Pengintegrasi untuk PDB Non-Eksak

Jika uji ke-eksak-an gagal, kita dapat mengalikan seluruh persamaan dengan fungsi pengali mu x koma y sehingga diferensial baru menjadi eksak. Berdasarkan penurunan parsial, jika ekspresi parsial M per parsial y dikurang parsial N per parsial x dibagi N hanya merupakan fungsi dari x saja, maka faktor pengintegrasi adalah mu x sama dengan eksponensial integral p x d x. Sebaliknya, jika dibagi minus M hanya memuat variabel y, maka mu y adalah eksponensial integral q y d y.

### Salindia 09: Pemodelan Fisis Sirkuit RC dari Prinsip Dasar (KVL)

Sekarang mari kita masuk ke Pilar 1 dan 4, yaitu pemodelan sirkuit RC dari prinsip fisika dasar. Berdasarkan Hukum Tegangan Kirchhoff, tegangan sumber V nol sama dengan jatuh tegangan resistor v R ditambah tegangan kapasitor v C. Karena arus pengisian kapasitor i sama dengan C dikali d v C per d t, kita peroleh PDB linier orde satu: R dikali C dikali d v C per d t ditambah v C sama dengan V nol. Konstanta waktu sirkuit tau didefinisikan sebagai perkalian resistansi R dan kapasitansi C.

### Salindia 10: Dinamika Transien & Paradoks Efisiensi Energi 50%

Solusi analitis tegangan pengisian kapasitor adalah v C t sama dengan V nol dikali kurung satu dikurang e pangkat minus t per tau. Arus transien meluruh eksponensial dari nilai awal V nol per R. Perhatikan tinjauan neraca energi: energi yang disuplai oleh sumber tegangan adalah C dikali V nol kuadrat. Namun energi medan elektrostatik yang tersimpan di dalam dielektrik kapasitor hanyalah setengah C dikali V nol kuadrat. Kemana perginya sisa energi tersebut? Tepat setengah energi diserap dan diubah menjadi panas pada resistor. Hasil ini independen dari nilai resistansi R, bahkan jika R mendekati nol, energi tetap terdisipasi melalui radiasi elektromagnetik.

### Salindia 11: Aplikasi Industri Tenaga Listrik: Proteksi Snubber RC

Di industri tenaga listrik dan elektronika daya, prinsip PDB transien RC diterapkan langsung dalam perancangan rangkaian proteksi atau RC snubber. Ketika sakelar semikonduktor daya seperti IGBT atau MOSFET memutus arus beban yang bersifat induktif, timbul fenomena tegangan transien ekstrem di mana laju lonjakan tegangan d v per d t mendekati tak hingga. Lonjakan d v per d t yang melampaui batas ketahanan semikonduktor dapat merusak struktur dielektrik internal komponen. Berdasarkan standar industri IEEE dan IEC, kapasitor snubber C s dipasang secara paralel untuk menyerap arus transien dan menahan laju kenaikan tegangan sesaat pada t sama dengan nol positif menjadi arus puncak dibagi C s, sehingga sakelar semikonduktor terlindungi secara aman.

### Salindia 12: Contoh Soal Terhitung (Worked Example): Bank Kapasitor

Mari kita cermati contoh soal terhitung pada gardu induk kelistrikan. Suatu bank kapasitor dua ratus mikrofarad dihubungkan ke bus tegangan dua ratus lima puluh volt melalui resistor pembatas lima puluh ohm, dengan tegangan sisa awal kapasitor sebesar lima puluh volt. Langkah satu: kita hitung konstanta waktu transien tau sama dengan R dikali C, yaitu lima puluh ohm dikalikan dua ratus mikrofarad, menghasilkan sepuluh milidetik. Langkah dua: masukkan kondisi awal ke solusi analitik, diperoleh persamaan tegangan v C t sama dengan dua ratus lima puluh dikurang dua ratus dikali e pangkat minus seratus t volt. Langkah tiga: arus pemula transien pada t sama dengan nol positif adalah dua ratus lima puluh dikurang lima puluh dibagi lima puluh, yaitu empat ampere. Pada t sama dengan satu tau atau sepuluh milidetik, tegangan mencapai seratus tujuh puluh enam koma empat volt, dan pada lima tau atau lima puluh milidetik, tegangan telah mencapai dua ratus empat puluh delapan koma tujuh volt atau di atas sembilan puluh sembilan persen dari nilai tunaknya.

### Salindia 13: Praktikum Komputasi Julia: Transien Sirkuit RC

Sekarang kita terapkan Pilar ketiga, yaitu komputasi ilmiah terbuka berbasis Julia. Pada slide ini ditampilkan skrip ringkas menggunakan paket DifferentialEquations dot j l dan Plots dot j l. Kita definisikan parameter rangkaian V nol dua ratus lima puluh volt, R lima puluh ohm, dan C dua ratus mikrofarad. Model PDB dinyatakan dalam fungsi f r c kurung v koma p koma t sama dengan kurung V nol dikurang v dibagi R dikali C. Masalah nilai awal dikemas ke dalam objek O D E Problem dengan kondisi awal lima puluh volt pada rentang waktu simulasi nol hingga enam puluh milidetik, lalu diselesaikan menggunakan solver numerik adaptif Tsit lima. Grafik di sebelah kanan membuktikan bahwa kurva komputasi numerik Julia berwarna biru berimpit secara sempurna dengan solusi analitis garis putus-putus merah, memverifikasi ketepatan analisis matematis kita.

### Salindia 14: Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)

**[Bagian 1 - Pertanyaan Kuis]:**
Saatnya kuis interaktif untuk menguji pemahaman konsep fisika Anda. Tinjau kasus rekayasa berikut: Suatu kapasitor C diisi dari kondisi awal nol volt hingga tegangan V nol melalui resistor R. Jika nilai resistansi R diperkecil menjadi setengahnya, bagaimanakah energi total yang terdisipasi pada resistor E R? Pilihan A: Menjadi setengahnya karena arus lebih cepat berhenti. Pilihan B: Menjadi dua kali lipat karena arus awal lebih besar. Pilihan C: Tetap sama, yaitu setengah C V nol kuadrat, tidak bergantung pada nilai R. Pilihan D: Menjadi nol karena resistansi mendekati konduktor ideal. Silakan analisis dan tentukan jawaban terbaik Anda dalam delapan detik ke depan.

*[Jeda Hening Berpikir: 8 Detik Terprogram]*

**[Bagian 2 - Pembahasan Kuis & Tantangan Bloom]:**
Waktu habis. Jawaban yang tepat adalah C: Tetap sama, yaitu setengah C V nol kuadrat! Sebagaimana telah kita buktikan pada neraca energi, efisiensi pengisian kapasitor selalu tepat lima puluh persen dan sepenuhnya independen dari nilai resistansi R. Pada kolom sebelah kanan, Anda juga ditantang untuk membuktikan daya disipasi puncak V nol kuadrat per R pada level C4, serta merancang kapasitor snubber IGBT pada level C6.

### Salindia 15: Rangkuman Inti Perkuliahan & Referensi

Berikut rangkuman empat poin kunci perkuliahan kita hari ini. Pertama, PDB separabel diselesaikan dengan memisahkan variabel secara aljabar langsung. Kedua, PDB eksak setara dengan medan vektor konservatif berotasi nol dan diselesaikan melalui integrasi fungsi potensial u x koma y. Ketiga, faktor pengintegrasi mu bertindak sebagai transformator yang mengubah PDB non-eksak menjadi eksak. Keempat, dinamika transien RC dicirikan oleh konstanta waktu tau sama dengan R dikali C dengan efisiensi energi tepat lima puluh persen. Untuk pendalaman materi, silakan pelajari buku teks Kreyszig bab satu, buku Zill bab dua, serta kerjakan Lembar Kerja dan Problem Set pada portal web perkuliahan. Sampai jumpa pada Minggu ketiga, terima kasih atas perhatian Anda.

