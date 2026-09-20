# Naskah & Metadata Video Kuliah Minggu 14: Persamaan Diferensial v2.0

### 1. Metadata Siap Unggah YouTube (SEO Optimized)

**Tautan Resmi YouTube:** [https://youtu.be/VidTzwMhRDo](https://youtu.be/VidTzwMhRDo)  

**Judul Resmi:** `[Minggu 14] Fungsi Bessel: Koordinat Silinder & Efek Kulit Konduktor ACSR | Persamaan Diferensial | Teknik Elektro UNIB`

**Deskripsi Siap Unggah:**
```text
Kuliah Daring Minggu 14 - Persamaan Diferensial (Teknik Elektro UNIB)
Topik: Metode Deret Frobenius, Titik Singular Reguler, Fungsi Bessel J_nu & Y_nu, Frekuensi Pancung Pandu Gelombang TM01, Mekanisme Fisis Skin Effect, Kedalaman Penetrasi Delta, dan Konduktor ACSR IEC 61089

Dosen Pengampu:
- Ir. Novalio Daratha, S.T., M.Sc., Ph.D.
- Muhammad Arfan, S.T., M.T.
Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika
Fakultas Teknik, Universitas Bengkulu

Akses portal perkuliahan, modul ajar, lembar kerja C1-C6, dan problem set:
https://www.ndaratha.my.id/persamaan-diferensial/

Linimasa Bab (Timestamps):
00:00 - 01. Pembukaan Perkuliahan Minggu 14
00:49 - 02. Sub-CPMK 14 & Taksonomi Bloom
01:42 - 03. Peta Kurikulum: Geometri Melingkar
02:22 - 04. Penurunan PDB Bessel
02:56 - 05. Metode Deret Frobenius
03:33 - 06. Fungsi Bessel J_nu & Y_nu
04:16 - 07. Akar Nol Bessel & Frekuensi Pancung
04:57 - 08. Mekanisme Fisis Skin Effect
05:41 - 09. Contoh Soal Pandu Gelombang
06:25 - 10. Contoh Soal Kedalaman Kulit
07:07 - 11. Peningkatan Resistansi AC/DC
07:42 - 12. Konduktor ACSR & Standar IEC 61089
08:26 - 13. Praktikum Julia: Bessel & Skin Effect
09:09 - 14. Kuis Interaktif & Evaluasi Bloom
10:51 - 15. Rangkuman Eksekutif & Penutup

Buku Referensi Pembelajaran:
1. Erwin Kreyszig, "Advanced Engineering Mathematics", 10th Edition, John Wiley & Sons.
2. Dennis G. Zill, "A First Course in Differential Equations with Modeling Applications", 11th Edition.
3. William H. Hayt & John A. Buck, "Engineering Electromagnetics", 9th Edition, McGraw-Hill.
4. Standar Industri Terkait (IEEE & IEC).

#PersamaanDiferensial #TeknikElektro #UniversitasBengkulu #KalkulusLanjut #DifferentialEquations #JuliaLang
```

---

## 2. Capaian Pembelajaran (Sub-CPMK 14 OBE Taksonomi Bloom)
- **C1 (Mengingat):** Menyatakan bentuk kanonik Persamaan Diferensial Bessel x^2 y'' + x y' + (x^2 - nu^2)y = 0 dan deret Frobenius.
- **C2 (Memahami):** Menjelaskan perilaku asimtotik fungsi Bessel jenis pertama J_nu (terhingga) dan jenis kedua Y_nu (singular di titik nol).
- **C3 (Menerapkan):** Menghitung frekuensi pancung cut-off pandu gelombang silinder menggunakan akar-akar nol fungsi Bessel alpha_nm.
- **C4 (Menganalisis):** Menganalisis redistribusi rapat arus radial konduktor silinder akibat induksi medan magnet bolak-balik (skin effect).
- **C5 (Mengevaluasi):** Mengevaluasi rasio kenaikan resistansi AC terhadap DC (R_ac / R_dc) pada konduktor transmisi ACSR IEC 61089.
- **C6 (Komputasi):** Memprogram evaluasi numerik fungsi Bessel dan visualisasi rapat arus skin effect menggunakan bahasa Julia.

---

## 3. Naskah Audio Narasi Per Salindia (15 Slide Lengkap)

### Salindia 01: Judul & Pembukaan Kuliah Minggu 14

Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, selamat datang kembali dalam perkuliahan daring Persamaan Diferensial semester genap 2026. Pada Minggu keempat belas ini, kita membedah kelas fungsi khusus yang sangat penting dalam analisis medan berkoordinat melingkar: Persamaan Diferensial Bessel dan Fenomena Efek Kulit atau Skin Effect pada Konduktor Listrik. Kita akan mendalami Metode Deret Frobenius pada titik singular reguler, fungsi Bessel jenis pertama J nu dan jenis kedua Y nu, penentuan frekuensi pancung pandu gelombang elektromagnetik, mekanisme redistribusi arus bolak-balik pada konduktor silinder, serta inovasi desain konduktor ACSR dan busbar berongga berbasis standar internasional IEC 61089. Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan.

### Salindia 02: Sub-CPMK Taksonomi Bloom (Minggu 14)

Berikut adalah Capaian Pembelajaran Sub-CPMK Minggu keempat belas berbasis Taksonomi Bloom. Pada C1 Mengingat, mahasiswa mampu menyatakan bentuk kanonik PDB Bessel dan struktur deret Frobenius. Pada C2 Memahami, mahasiswa mampu membedakan karakteristik fisis fungsi Bessel J nu yang terhingga di sumbu pusat versus Y nu yang singular meledak di titik nol. Pada C3 Menerapkan, mahasiswa mampu menghitung kedalaman kulit delta dan frekuensi pancung pandu gelombang silinder. Pada C4 Menganalisis, mahasiswa mampu menguraikan persamaan Helmholtz difusi medan magnetik ke dalam fungsi Bessel Kelvin. Pada C5 Mengevaluasi, mahasiswa mampu mengkaji kenaikan rasio resistansi R AC terhadap R DC pada saluran transmisi tegangan tinggi. Dan pada C6 Komputasi, mahasiswa mampu menyimulasikan fungsi Bessel dan profil rapat arus menggunakan bahasa Julia.

### Salindia 03: Peta Kurikulum: Geometri Melingkar & Koefisien Variabel

Perhatikan perubahan mendasar dalam struktur persamaan diferensial pada slide ini. Pada minggu-minggu sebelumnya, seluruh PDB yang kita pelajari memiliki koefisien konstan. Namun ketika kita memodelkan fenomena gelombang dan medan pada konduktor berpenampang bundar, kabel koaksial, atau tabung pandu gelombang silinder, operator Laplacian dalam koordinat silinder r, theta, z memunculkan suku satu per r dan satu per r kuadrat. Hal ini menghasilkan Persamaan Diferensial dengan Koefisien Variabel. PDB Bessel adalah prototipe universal dari persamaan diferensial koefisien variabel yang mengatur seluruh fenomena fisika bergeometri silinder melingkar.

### Salindia 04: Penurunan Persamaan Diferensial Bessel

Bentuk kanonik Persamaan Diferensial Bessel berorde nu dinyatakan sebagai: x kuadrat d kuadrat y per d x kuadrat ditambah x d y per d x ditambah kurung x kuadrat dikurang nu kuadrat dikali y sama dengan nol. Titik x sama dengan nol adalah Titik Singular Reguler, karena koefisien turunan kedua lenyap di titik tersebut tetapi hasil kali x P x dan x kuadrat Q x tetap bernilai analitik terhingga. Karena titik x sama dengan nol adalah singular, metode deret Taylor biasa gagal diterapkan. Penyelesaiannya menuntut penerapan metode deret umum yang dikembangkan oleh Ferdinand Georg Frobenius.

### Salindia 05: Metode Deret Frobenius di Sekitar Titik Singular Reguler

Metode Deret Frobenius mengasumsikan solusi dalam bentuk deret pangkat tergeneralisasi: y x sama dengan x pangkat r dikalikan jumlahan dari m sama dengan nol hingga tak hingga a m x pangkat m, dengan a nol tidak nol. Mensubstitusikan deret ini ke PDB Bessel menghasilkan Persamaan Indisial kuadratik: r kuadrat dikurang nu kuadrat sama dengan nol. Akar-akar indisialnya adalah r satu sama dengan plus nu dan r dua sama dengan minus nu. Melalui relasi rekursi dua langkah, kita peroleh bahwa seluruh suku ganjil bernilai nol, sedangkan suku-suku genap membentuk deret konvergen mutlak di seluruh bidang riil yang mendefinisikan Fungsi Bessel.

### Salindia 06: Fungsi Bessel Jenis Pertama J_nu(x) & Jenis Kedua Y_nu(x)

Solusi umum lengkap dari PDB Bessel dinyatakan sebagai kombinasi linier dari dua fungsi basis independen: y x sama dengan C satu J nu x ditambah C dua Y nu x. Fungsi Bessel Jenis Pertama J nu x memiliki sifat bernilai terhingga di titik pusat x sama dengan nol dan berosilasi mirip gelombang sinusoidal dengan amplitudo yang meluruh sebanding satu per akar x. Sebaliknya, Fungsi Bessel Jenis Kedua Y nu x atau fungsi Neumann memiliki singularitas logaritmik ekstrem yang meledak menuju minus tak hingga di titik pusat x sama dengan nol! Konsekuensi fisik yang sangat penting: untuk konduktor padat silinder yang mencakup sumbu tengah r sama dengan nol, koefisien C dua wajib dipilih nol mutlak agar medan listrik di pusat konduktor tetap bernilai riil dan terhingga.

### Salindia 07: Akar-Akar Nol Bessel (alpha_nm) & Frekuensi Pancung

Sebagaimana fungsi sinus bernilai nol pada kelipatan pi, fungsi Bessel J nu x memiliki tak hingga banyaknya akar-akar nol diskrit positif, dilambangkan sebagai alfa nu m. Sebagai contoh untuk J nol x, akar pertamanya adalah dua koma empat ratus lima, akar kedua lima koma lima ratus dua puluh, dan akar ketiga delapan koma enam ratus lima puluh empat. Ketika gelombang elektromagnetik merambat di dalam tabung pandu gelombang silinder berjejari a, syarat batas dinding konduktor sempurna mewajibkan medan listrik tangensial lenyap di permukaan r sama dengan a. Kondisi batas ini mengunci nilai eigen k sama dengan alfa nu m dibagi a, yang secara langsung menetapkan Frekuensi Pancung atau cut-off frequency pandu gelombang.

### Salindia 08: Mekanisme Fisika Efek Kulit (Skin Effect) pada Konduktor

Kini kita masuki Pilar pertama intuisi fisika rekayasa tenaga: fenomena Efek Kulit atau Skin Effect. Pada arus searah DC, rapat arus mengalir merata sempurna di seluruh penampang kawat tembaga. Namun ketika arus bolak-balik AC mengalir, fluks medan magnet bolak-balik timbul baik di luar maupun di dalam tubuh konduktor. Fluks magnetik internal ini paling padat melingkari sumbu pusat konduktor. Berdasarkan Hukum Induksi Faraday dan Hukum Lenz, perubahan fluks magnet internal menginduksi tegangan gerak listrik lawan yang membangkitkan arus pusar atau eddy current. Arus pusar ini melawan arah arus utama di inti pusat konduktor dan memperkuat arus di permukaan luar, memaksa elektron-elektron terdorong keluar berkonsentrasi pada lapisan kulit konduktor.

### Salindia 09: Contoh Terhitung: Frekuensi Pancung Pandu Gelombang TM_01

Mari kita selesaikan contoh perhitungan frekuensi pancung pandu gelombang silinder berongga berjejari a sama dengan dua koma lima sentimeter. Untuk mode transversal magnetik fundamental TM nol satu, akar nol Bessel yang relevan adalah alfa nol satu sama dengan dua koma empat ratus lima. Frekuensi pancung dihitung melalui rumus: f cut-off sama dengan kecepatan cahaya c dikalikan alfa nol satu dibagi kurung dua pi dikalikan jejari a. Substitusikan nilai: tiga kali sepuluh pangkat delapan dikali dua koma empat ratus lima dibagi kurung dua pi kali nol koma nol dua lima, menghasilkan frekuensi pancung sebesar empat koma lima sembilan giga Hertz. Sinyal gelombang mikro dengan frekuensi di bawah empat koma lima sembilan giga Hertz akan teratenuasi habis dan tidak dapat merambat melintasi tabung pandu gelombang ini.

### Salindia 10: Contoh Terhitung: Kedalaman Kulit Tembaga & Aluminium

Tingkat penetrasi medan elektromagnetik ke dalam konduktor diukur oleh Kedalaman Kulit atau Skin Depth delta: delta sama dengan satu dibagi akar kurung pi dikalikan frekuensi f dikalikan permeabilitas mu dikalikan konduktivitas sigma. Pada jarak satu delta dari permukaan luar, rapat arus telah meluruh hingga tiga puluh enam koma delapan persen dari nilai permukaannya. Untuk konduktor tembaga standar pada frekuensi sistem tenaga lima puluh Hertz, kedalaman kulit adalah sekitar sembilan koma dua milimeter. Sedangkan untuk konduktor aluminium dengan konduktivitas lebih rendah, kedalaman kulitnya sekitar sebelas koma enam milimeter. Bila diameter konduktor melebihi dua puluh milimeter, bagian inti dalam konduktor praktis tidak lagi dilewati oleh arus listrik!

### Salindia 11: Peningkatan Resistansi Efektif AC (R_ac / R_dc)

Konsekuensi rekayasa yang sangat merugikan dari efek kulit adalah berkurangnya luas penampang efektif yang dilalui arus listrik. Karena arus hanya berdesakan mengalir pada cincin selubung tipis di permukaan luar, resistansi efektif arus bolak-balik R AC menjadi jauh lebih besar daripada resistansi arus searah R DC! Rasio R AC terhadap R DC sebanding dengan perbandingan radius konduktor terhadap dua kali kedalaman kulit delta. Peningkatan resistansi ini melipatgandakan rugi-rugi daya transmisi Joule i kuadrat R AC pada saluran udara tegangan tinggi PLN, sekaligus mempercepat kenaikan suhu operasi konduktor.

### Salindia 12: Standar Industri: Solusi Konduktor ACSR & Busbar Tubular

Memahami Persamaan Bessel dan efek kulit memicu lahirnya inovasi cerdas dalam desain konduktor transmisi berstandar IEC 61089. Karena bagian inti tengah konduktor tidak dilewati arus AC, insinyur mengganti inti tembaga yang mahal dan berat dengan kawat baja berkekuatan mekanis tinggi, yang diselubungi oleh pilinan kawat aluminium murni di lapisan luarnya. Inilah Konduktor ACSR atau Aluminium Conductor Steel Reinforced yang digunakan pada seluruh menara transmisi SUTT dan SUTET di Indonesia! Lapisan aluminium luar menyalurkan seluruh arus listrik AC, sedangkan inti baja menahan beban tarikan mekanis bentang menara. Demikian pula pada gardu induk GITET, busbar dibuat berbentuk pipa tembaga berongga atau tubular busbar untuk menghemat logam mulia.

### Salindia 13: Praktikum Komputasi Julia: Fungsi Bessel & Skin Effect

Pada praktikum komputasi Julia ini, kita memprogram fungsi Bessel menggunakan paket SpecialFunctions dot j l dan mengevaluasi distribusi rapat arus radial J r pada kawat silinder pejal. Dengan memecahkan persamaan diferensial difusi Bessel Kelvin berargumen kompleks, kita hitung modulus rapat arus dari pusat r sama dengan nol hingga permukaan r sama dengan R. Grafik di sebelah kanan dengan sangat dramatis memperlihatkan efek kulit: pada frekuensi DC rapat arus mendatar seragam, sedangkan pada frekuensi AC lima puluh Hertz kurva melonjak tajam ke atas menyerupai mangkuk, di mana rapat arus di permukaan luar kawat mencapai lima kali lipat lebih padat dibandingkan rapat arus di pusat kawat. Simulasi Julia ini memberikan bukti numerik yang tak terbantahkan mengenai fenomena skin effect.

### Salindia 14: Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)

**[Bagian 1 - Pertanyaan Kuis]:**
Saatnya kuis interaktif untuk menguji pemahaman fisis fungsi Bessel dan efek kulit Anda. Perhatikan studi kasus pada layar: Pada saluran transmisi daya tinggi PLN, mengapa kabel konduktor dibuat dari aluminium di lapisan luar dan baja pejal di inti tengah seperti kawat ACSR standar IEC 61089, dan bukan sebaliknya? Pilihan A: Baja lebih tahan terhadap korosi kimia atmosfer dibanding aluminium. Pilihan B: Efek kulit mendesak arus AC mengalir di lapisan luar aluminium konduktif, sehingga inti tengah yang sepi arus diisi baja kuat penahan beban tarikan mekanis! Pilihan C: Aluminium memiliki densitas massa yang jauh lebih tinggi daripada baja. Pilihan D: Baja berfungsi menghalangi induksi medan petir masuk ke fasa transmisi. Silakan analisis fenomena efek kulit ini dan tentukan pilihan jawaban terbaik Anda dalam delapan detik ke depan.

*[Jeda Hening Berpikir: 8 Detik Terprogram]*

**[Bagian 2 - Pembahasan Kuis & Tantangan Bloom]:**
Waktu habis. Jawaban yang tepat adalah B: Efek kulit mendesak arus AC mengalir di luar, sehingga inti diisi baja kuat tarikan mekanis! Pada frekuensi lima puluh Hertz, distribusi kerapatan arus Bessel J nol mendesak arus AC menuju kulit luar konduktor. Inti pusat kawat praktis tidak dialiri arus, sehingga penempatan baja di pusat memberikan kekuatan tarik menopang bentang menara ratusan meter tanpa mengurangi kapasitas hantar arus kawat transmisi. Pada kolom tantangan sebelah kanan, Anda juga ditantang menghitung frekuensi pancung pandu gelombang silindris di level C4, mengevaluasi rasio resistansi AC terhadap DC pada inverter dua puluh kilo Hertz di level C5, serta merancang rel busbar tubular berongga GITET lima ratus kilo Volt di level C6.

### Salindia 15: Rangkuman Eksekutif & Jembatan ke Minggu 15

Sebagai rangkuman perkuliahan minggu keempat belas: Pertama, PDB Bessel timbul secara alami dari analisis koordinat silinder dengan koefisien variabel. Kedua, metode Frobenius menyelesaikan persamaan singular reguler dan menghasilkan fungsi Bessel J nu dan Y nu. Ketiga, akar-akar nol fungsi Bessel menetapkan frekuensi pancung pandu gelombang silinder. Dan keempat, pemahaman efek kulit mendasari inovasi desain konduktor ACSR dan busbar berongga sesuai standar IEC 61089. Silakan pelajari modul ajar dan selesaikan Lembar Kerja serta Problem Set Minggu keempat belas di portal ndaratha dot my dot id. Pada minggu kelima belas, kita akan mengakhiri perkuliahan dengan Polinomial Legendre pada koordinat bola dan Empat Persamaan Maxwell Diferensial. Terima kasih dan wassalamualaikum warahmatullahi wabarakatuh.

