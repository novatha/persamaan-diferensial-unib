# Naskah & Metadata Video Kuliah Minggu 15: Persamaan Diferensial v2.0

### 1. Metadata Siap Unggah YouTube (SEO Optimized)

**Judul Resmi:** `[Minggu 15] Legendre, 4 Persamaan Maxwell, & Sintesis Kurikulum | Persamaan Diferensial | Teknik Elektro UNIB`

**Deskripsi Siap Unggah:**
```text
Kuliah Daring Minggu 15 - Persamaan Diferensial (Teknik Elektro UNIB)
Topik: Polinomial Legendre Koordinat Bola, Arus Pergeseran Maxwell, Gelombang EM 3D, Vektor Poynting, Paparan Medan SUTET 500 kV, dan Matriks Sintesis Komprehensif Persamaan Diferensial Menuju UAS

Dosen Pengampu:
- Ir. Novalio Daratha, S.T., M.Sc., Ph.D.
- Muhammad Arfan, S.T., M.T.
Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika
Fakultas Teknik, Universitas Bengkulu

Akses portal perkuliahan, modul ajar, lembar kerja C1-C6, dan problem set:
https://www.ndaratha.my.id/persamaan-diferensial/

Linimasa Bab (Timestamps):
00:00 - 01. Pembukaan Perkuliahan Minggu 15
00:42 - 02. Sub-CPMK 15 & Taksonomi Bloom
01:35 - 03. Peta Kurikulum: Sintesis Akhir
02:15 - 04. Koordinat Bola & PDB Legendre
03:00 - 05. Polinomial Legendre & Ortogonalitas
03:42 - 06. Bola Konduktor dalam Medan Seragam
04:22 - 07. Empat Persamaan Maxwell
05:07 - 08. Arus Pergeseran Maxwell
05:47 - 09. Contoh Soal Arus Pergeseran Kapasitor
06:30 - 10. Gelombang Elektromagnetik 3D
07:12 - 11. Vektor Poynting Aliran Daya
07:49 - 12. Paparan Medan SUTET & ICNIRP
08:34 - 13. Praktikum Julia: Polinomial Legendre
09:13 - 14. Kuis Interaktif & Evaluasi Bloom
10:54 - 15. Matriks Sintesis Kurikulum & Penutup

Buku Referensi Pembelajaran:
1. Erwin Kreyszig, "Advanced Engineering Mathematics", 10th Edition, John Wiley & Sons.
2. Dennis G. Zill, "A First Course in Differential Equations with Modeling Applications", 11th Edition.
3. William H. Hayt & John A. Buck, "Engineering Electromagnetics", 9th Edition, McGraw-Hill.
4. Standar Industri Terkait (IEEE & IEC).

#PersamaanDiferensial #TeknikElektro #UniversitasBengkulu #KalkulusLanjut #DifferentialEquations #JuliaLang
```

---

## 2. Capaian Pembelajaran (Sub-CPMK 15 OBE Taksonomi Bloom)
- **C1 (Mengingat):** Menyatakan bentuk kanonik PDB Legendre (1-x^2)y'' - 2xy' + n(n+1)y = 0 dan 4 Persamaan Maxwell bentuk diferensial.
- **C2 (Memahami):** Menjelaskan konsep fisis Arus Pergeseran Maxwell J_d = dD/dt yang menyempurnakan Hukum Ampere dan kontinuitas muatan.
- **C3 (Menerapkan):** Menurunkan persamaan gelombang elektromagnetik 3D dari Persamaan Maxwell pada medium ruang bebas.
- **C4 (Menganalisis):** Menganalisis kerapatan fluks aliran daya gelombang elektromagnetik menggunakan Vektor Poynting S = E x H.
- **C5 (Mengevaluasi):** Mengevaluasi keselamatan batas paparan radiasi medan elektromagnetik di bawah koridor SUTET 500 kV sesuai standar ICNIRP.
- **C6 (Komputasi):** Memprogram visualisasi permukaan fungsi Polinomial Legendre dan gelombang 3D menggunakan bahasa Julia.

---

## 3. Naskah Audio Narasi Per Salindia (15 Slide Lengkap)

### Salindia 01: Judul & Pembukaan Kuliah Minggu 15

Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, selamat datang dalam perkuliahan daring puncak penutup semester genap 2026: Minggu kelima belas Persamaan Diferensial. Pada pertemuan pamungkas ini, kita mengintegrasikan seluruh perangkat matematika yang telah kita bangun menuju mahakarya fisika rekayasa terbesar abad kesembilan belas: Polinomial Legendre pada Koordinat Bola, Empat Persamaan Maxwell dalam Bentuk Diferensial, penurunan persamaan gelombang elektromagnetik tiga dimensi, aliran daya Vektor Poynting, serta sintesis komprehensif seluruh kurikulum perkuliahan kita sebagai persiapan menghadapi Ujian Akhir Semester. Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan.

### Salindia 02: Capaian Pembelajaran Modul (Sub-CPMK 15 -- OBE)

Berikut adalah Capaian Pembelajaran Sub-CPMK Minggu kelima belas berbasis Taksonomi Bloom. Pada C1 Mengingat, mahasiswa mampu menyatakan empat persamaan Maxwell diferensial dan formula Rodrigues polinomial Legendre. Pada C2 Memahami, mahasiswa mampu menjelaskan konsep fisis Arus Pergeseran Maxwell yang menyatukan kelistrikan dan kemagnetan. Pada C3 Menerapkan, mahasiswa mampu menurunkan perambatan gelombang medan elektromagnetik 3D dari hukum Faraday dan Ampere. Pada C4 Menganalisis, mahasiswa mampu menghitung laju kerapatan daya yang diradiasikan menggunakan Vektor Poynting S. Pada C5 Mengevaluasi, mahasiswa mampu mengkaji ambang batas paparan medan EM di bawah jalur transmisi SUTET 500 kV standar ICNIRP. Dan pada C6 Komputasi, mahasiswa mampu memprogram visualisasi ortogonalitas Legendre dengan bahasa Julia.

### Salindia 03: Peta Kurikulum: Dari Parameter Terpusat ke Terdistribusi

Perhatikan kilas balik perjalanan intelektual kita sepanjang enam belas pekan pada peta kurikulum ini. Kita mengawali perjalanan dari sirkuit parameter terpusat PDB orde satu RC dan RL, berkembang ke osilator RLC orde dua homogen dan non-homogen, beralih ke ranah domain frekuensi kompleks s melalui Transformasi Laplace, menjelajahi spektrum harmonisa deret Fourier, menembus Persamaan Diferensial Parsial difusi termal kabel dan gelombang telegrafer saluran transmisi, hingga akhirnya tiba pada puncak sintesis tertinggi: Empat Persamaan Maxwell. Setiap persamaan diferensial yang Anda pelajari bukanlah rumus hafalan abstrak, melainkan bahasa universal yang melukiskan hukum kekekalan energi di alam semesta.

### Salindia 04: Persamaan Laplace Koordinat Bola & Persamaan Legendre

Ketika memodelkan medan potensial di sekitar bola konduktor, antena isotropis, atau kubah tegangan tinggi, kita menggunakan sistem Koordinat Bola r, theta, phi. Melalui metode pemisahan variabel pada Persamaan Laplace dengan simetri azimut, suku sudut polar theta tereduksi menjadi Persamaan Diferensial Legendre: kurung satu dikurang x kuadrat d kuadrat y per d x kuadrat dikurang dua x d y per d x ditambah n kurung n ditambah satu dikalikan y sama dengan nol, dengan substitusi x sama dengan kosinus theta. Agar solusi fisis tidak meledak di kutub bola x sama dengan plus minus satu, parameter n wajib berupa bilangan bulat non-negatif nol, satu, dua, dan seterusnya. Solusi yang dihasilkan dinamakan Polinomial Legendre P n x.

### Salindia 05: Polinomial Legendre P_n(cos theta) & Sifat Ortogonalitas

Polinomial Legendre dapat dihitung secara sistematis menggunakan Rumus Rodrigues: P nol x sama dengan satu. P satu x sama dengan x atau kosinus theta. P dua x sama dengan setengah kurung tiga x kuadrat dikurang satu. P tiga x sama dengan setengah kurung lima x pangkat tiga dikurang tiga x. Sebagaimana fungsi sinus dan kosinus pada deret Fourier, Polinomial Legendre memiliki Sifat Ortogonalitas pada interval minus satu hingga satu: integral dari P m x dikalikan P n x d x bernilai nol jika m tidak sama dengan n, dan bernilai dua dibagi kurung dua n ditambah satu jika m sama dengan n. Sifat ortogonalitas ini memungkinkan kita mengekspansikan sebarang distribusi potensial pada permukaan bola.

### Salindia 06: Aplikasi: Bola Konduktor dalam Medan Seragam E_0 a_z

Slide ini menampilkan kasus klasik bola konduktor logam berjejari R yang diletakkan di dalam medan listrik seragam E nol searah sumbu z. Muatan bebas di dalam konduktor mengalami induksi dan berpolarisasi, membentuk muatan positif di kutub atas dan muatan negatif di kutub bawah. Solusi potensial di luar bola diturunkan sebagai: V r koma theta sama dengan minus E nol dikalikan kurung r dikurang R pangkat tiga per r kuadrat dikalikan kosinus theta. Perhatikan bahwa suku kosinus theta adalah tepat Polinomial Legendre orde satu P satu! Medan listrik terdistorsi melengkung masuk secara tegak lurus ke permukaan bola konduktor, membuktikan bahwa bola logam bertindak sebagai pelindung ekuipotensial sempurna.

### Salindia 07: Empat Persamaan Diferensial Maxwell

Kini kita masuki puncak sintesis elektromagnetika: Empat Persamaan Maxwell dalam bentuk diferensial parsial. Pertama, Hukum Gauss Elektrostatika: divergensi D sama dengan rapat muatan volume rho v, menyatakan muatan listrik sebagai sumber medan listrik. Kedua, Hukum Gauss Magnetika: divergensi B sama dengan nol, menyatakan tidak adanya monopol magnet di alam semesta; garis medan magnet selalu membentuk kurva tertutup. Ketiga, Hukum Induksi Faraday: curl E sama dengan minus parsial B per parsial t, menyatakan perubahan medan magnetik terhadap waktu melahirkan medan listrik berputar. Dan keempat, Hukum Ampere-Maxwell: curl H sama dengan rapat arus konduksi J ditambah rapat arus pergeseran parsial D per parsial t.

### Salindia 08: Arus Pergeseran Maxwell (Displacement Current)

Kontribusi orisinal terbesar James Clerk Maxwell adalah menambahkan suku Arus Pergeseran parsial D per parsial t pada Hukum Ampere. Hukum Ampere klasik sebelumnya curl H sama dengan J melanggar hukum kekekalan kontinuitas muatan pada celah kapasitor AC. Di antara kedua pelat kapasitor hampa udara, tidak ada muatan elektron riil yang melintas konduksi J sama dengan nol. Maxwell berhipotesis bahwa laju perubahan medan listrik terhadap waktu parsial D per parsial t bertindak persis seperti arus listrik sejati yang membangkitkan medan magnet sirkular! Penambahan suku arus pergeseran ini melengkapi simetri elektromagnetik dan memprediksi keberadaan gelombang elektromagnetik mandiri yang merambat di ruang hampa.

### Salindia 09: Contoh Terhitung: Kesamaan I_c & I_d pada Kapasitor

Mari kita buktikan kesetaraan arus pergeseran melalui contoh perhitungan kapasitor keping sejajar berpelat lingkaran berjejari lima sentimeter dengan celah satu milimeter, dihubungkan ke sumber tegangan AC seratus Volt puncak frekuensi satu Mega Hertz. Arus konduksi riil pada kawat adalah i c sama dengan C dikali d v per d t, bernilai maksimum nol koma empat puluh empat Ampere. Di dalam celah udara hampa, medan listrik berubah seirama tegangan sumber. Menghitung integral arus pergeseran i d sama dengan integral epsilon nol dikalikan d E per d t melintasi luas pelat kapasitor menghasilkan nilai yang persis sama: i d sama dengan nol koma empat puluh empat Ampere! Arus pergeseran menjamin kontinuitas total arus listrik melintasi rangkaian tanpa ada keterputusan sedikit pun.

### Salindia 10: Penurunan Persamaan Gelombang Elektromagnetik 3D

Dengan memanfaatkan identitas vektor kalkulus: curl dari curl vektor sama dengan gradien divergensi dikurang Laplacian vektor, kita turunkan perambatan medan pada ruang hampa bebas muatan dan arus: curl dari curl E sama dengan minus parsial per parsial t dari curl B. Karena divergensi E nol dan curl B sama dengan mu nol epsilon nol parsial E per parsial t, kita peroleh Persamaan Gelombang Elektromagnetik Tiga Dimensi: nabla kuadrat E sama dengan mu nol dikalikan epsilon nol dikalikan parsial kuadrat E per parsial t kuadrat! Kecepatan rambat gelombang dihitung dari konstanta fundamental alam: c sama dengan satu dibagi akar mu nol kali epsilon nol, menghasilkan tepat dua ratus sembilan puluh sembilan ribu tujuh ratus sembilan puluh dua kilometer per detik: kecepatan cahaya!

### Salindia 11: Aliran Energi Gelombang & Vektor Poynting

Gelombang elektromagnetik yang merambat membawa energi dan momentum melintasi ruang angkasa. Laju aliran kerapatan daya per satuan luas dinyatakan oleh Vektor Poynting S: vektor S sama dengan perkalian silang medan listrik E terhadap medan magnet H dalam satuan Watt per meter persegi. Arah vektor Poynting menunjukkan arah perambatan energi gelombang. Untuk gelombang bidang terpolarisasi linier yang merambat ke arah sumbu z, nilai rata-rata waktu vektor Poynting adalah setengah real dari perkalian fasor E silang H konjugat, atau setengah E m kuadrat dibagi impedansi intrinsik ruang hampa eta nol yang bernilai tiga ratus tujuh puluh tujuh Ohm atau seratus dua puluh pi Ohm.

### Salindia 12: Standar Industri: Paparan Medan EM SUTET 500 kV

Sebagai insinyur teknik elektro, pemahaman Persamaan Maxwell sangat krusial dalam menjamin keselamatan publik di bawah jalur transmisi tegangan ekstra tinggi. Saluran Udara Tegangan Ekstra Tinggi SUTET 500 kV PLN membangkitkan medan listrik dan medan magnet frekuensi rendah lima puluh Hertz di ruang bebas sekitarnya. Komisi Internasional Perlindungan Radiasi Non-Ionisasi ICNIRP dan standar Peraturan Menteri ESDM menetapkan batas aman paparan masyarakat umum: intensitas medan listrik maksimum lima kilo Volt per meter, dan kerapatan fluks medan magnet maksimum seratus mikro Tesla atau nol koma satu mili Tesla. Melalui perhitungan Persamaan Laplace dan Biot-Savart, insinyur PLN merancang tinggi bebas minimum menara konduktor agar paparan medan di permukaan tanah selalu berada jauh di bawah ambang batas aman kesehatan internasional.

### Salindia 13: Praktikum Komputasi Julia: Polinomial Legendre Koordinat Bola

Pada praktikum komputasi Julia penutup ini, kita mengevaluasi keluarga fungsi Polinomial Legendre P n x dan memvisualisasikan medan potensial bola konduktor secara tiga dimensi. Dengan memanfaatkan paket SpecialFunctions dot j l dan Plots dot j l, kita gambarkan kurva ortogonalitas P nol hingga P empat pada selang minus satu hingga satu. Plot kontur permukaan di sebelah kanan memperlihatkan kelengkungan garis-garis medan listrik E yang membelok mulus menabrak permukaan bola konduktor secara tegak lurus sempurna, mengonfirmasi kebenaran analitis solusi koordinat bola. Skrip komputasi Julia ini mengintegrasikan pemodelan matematika dengan visualisasi rekayasa modern berkecepatan tinggi.

### Salindia 14: Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)

**[Bagian 1 - Pertanyaan Kuis]:**
Saatnya kuis interaktif puncak untuk menguji pemahaman Persamaan Maxwell Anda. Perhatikan studi kasus pada layar: Maxwell menambahkan suku arus pergeseran J d sama dengan parsial D per parsial t pada Hukum Ampere. Jika suku arus pergeseran ini diabaikan, hukum fisika fundamental manakah yang langsung dilanggar pada celah kapasitor AC? Pilihan A: Hukum Pertama Termodinamika. Pilihan B: Hukum Kekekalan Muatan Listrik atau Persamaan Kontinuitas divergensi J ditambah parsial rho v per parsial t sama dengan nol! Pilihan C: Hukum Gravitasi Universal Newton. Pilihan D: Hukum Pemantulan Gelombang Optik Snellius. Silakan analisis implikasi fisis kontinuitas muatan ini dan tentukan pilihan terbaik Anda dalam delapan detik ke depan.

*[Jeda Hening Berpikir: 8 Detik Terprogram]*

**[Bagian 2 - Pembahasan Kuis & Tantangan Bloom]:**
Waktu habis. Jawaban yang tepat adalah B: Hukum Kekekalan Muatan Listrik atau Persamaan Kontinuitas! Karena divergensi dari kurva rotasi selalu identik dengan nol, tanpa suku arus pergeseran Maxwell, Hukum Ampere lama memaksa divergensi rapat arus konduksi J harus selalu sama dengan nol. Ini berarti muatan tidak boleh menumpuk di pelat kapasitor, yang secara fatal melanggar kekekalan muatan. Penambahan parsial D per parsial t melengkapi persamaan kontinuitas secara sempurna. Pada kolom tantangan sebelah kanan, Anda juga ditantang menurunkan persamaan gelombang tiga dimensi medan listrik di level C4, mengevaluasi vektor Poynting SUTET lima ratus kilo Volt sesuai standar IEEE C95.1 di level C5, serta merancang susunan fasa ganda mitigasi medan bocor di level C6.

### Salindia 15: Matriks Sintesis Akhir Kurikulum Persamaan Diferensial

Sebagai penutup seluruh perkuliahan kita: Matriks Sintesis pada slide ini merangkum keterpaduan utuh kurikulum Persamaan Diferensial. Anda telah menguasai empat pilar pedagogis: dari intuisi fisika, derivasi analitik eksak, simulasi komputasi numerik terbuka berbasis Julia, hingga standar industri internasional PLN, IEEE, dan IEC. Seluruh metode yang Anda kuasai ini adalah fondasi kokoh untuk melangkah ke mata kuliah lanjutan: Medan Elektromagnetika, Analisis Sistem Tenaga, Teknik Tegangan Tinggi, dan Sistem Kendali. Saya, Insinyur Novalio Daratha, bersama Bapak Muhammad Arfan, mengucapkan selamat atas kerja keras, ketekunan, dan dedikasi Anda sepanjang semester ini. Persiapkan diri Anda sebaik mungkin menghadapi Ujian Akhir Semester dengan mempelajari seluruh modul, lembar kerja, dan problem set di portal ndaratha dot my dot id. Semoga ilmu ini menjadi lentera keberkahan bagi karier keteknikan Anda di masa depan. Sukses selalu, terima kasih, dan wassalamu'alaikum warahmatullahi wabarakatuh.

