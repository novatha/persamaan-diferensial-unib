# Naskah & Metadata Video Kuliah Minggu 05: Persamaan Diferensial v2.0

### 1. Metadata Siap Unggah YouTube (SEO Optimized)

**Tautan Resmi YouTube:** [https://youtu.be/x15SuJBvZQE](https://youtu.be/x15SuJBvZQE)  

**Judul Resmi:** `[Minggu 05] PDB Orde 2 Non-Homogen: Resonansi Seri & RLC AC | Persamaan Diferensial | Teknik Elektro UNIB`

**Deskripsi Siap Unggah:**
```text
Kuliah Daring Minggu 05 - Persamaan Diferensial (Teknik Elektro UNIB)
Topik: Metode Koefisien Tak Tentu, Aturan Modifikasi t^s, Eksitasi AC Sinusoidal, Pelipatgandaan Tegangan Faktor-Q, Fenomena Beat, dan Resonansi Sub-Sinkron PLN

Dosen Pengampu:
- Ir. Novalio Daratha, S.T., M.Sc., Ph.D.
- Muhammad Arfan, S.T., M.T.
Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika
Fakultas Teknik, Universitas Bengkulu

Akses portal perkuliahan, modul ajar, lembar kerja C1-C6, dan problem set:
https://www.ndaratha.my.id/persamaan-diferensial/

Linimasa Bab (Timestamps):
00:00 - 01. Pembukaan Perkuliahan Minggu 05
00:42 - 02. Sub-CPMK 3 & Taksonomi Bloom
01:33 - 03. Peta Konsep: Struktur Solusi Lengkap
02:09 - 04. Metode Koefisien Tak Tentu
02:49 - 05. Aturan Modifikasi Resonansi
03:29 - 06. Pemodelan Sirkuit RLC AC
04:09 - 07. Evolusi Gelombang Transien vs Tunak
04:45 - 08. Resonansi Seri & Faktor-Q
05:27 - 09. Fenomena Beat (Denyut Layangan)
06:04 - 10. Studi Kasus Industri: Resonansi SSR PLN
06:44 - 11. Contoh Soal 1: Resonansi Tegangan
07:37 - 12. Contoh Soal 2: Beat SSR
08:17 - 13. Praktikum Julia: Resonansi & Selektivitas
08:57 - 14. Kuis Interaktif & Evaluasi Bloom
10:44 - 15. Rangkuman Perkuliahan & Penutup

Buku Referensi Pembelajaran:
1. Erwin Kreyszig, "Advanced Engineering Mathematics", 10th Edition, John Wiley & Sons.
2. Dennis G. Zill, "A First Course in Differential Equations with Modeling Applications", 11th Edition.
3. William H. Hayt & John A. Buck, "Engineering Electromagnetics", 9th Edition, McGraw-Hill.
4. Standar Industri Terkait (IEEE & IEC).

#PersamaanDiferensial #TeknikElektro #UniversitasBengkulu #KalkulusLanjut #DifferentialEquations #JuliaLang
```

---

## 2. Capaian Pembelajaran (Sub-CPMK 5 OBE Taksonomi Bloom)
- **C1 (Mengingat):** Menyatakan struktur dekomposisi solusi lengkap y = y_h + y_p pada PDB non-homogen.
- **C2 (Memahami):** Menjelaskan asal fisis aturan modifikasi pengali t^s saat frekuensi eksitasi memicu resonansi.
- **C3 (Menerapkan):** Menghitung respon partikular eksitasi sinusoidal dan penguatan tegangan reaktif faktor Q.
- **C4 (Menganalisis):** Menganalisis pembentukan fenomena denyut layangan atau beat saat frekuensi eksitasi mendekati frekuensi alami.
- **C5 (Mengevaluasi):** Mengevaluasi risiko mekanis-elektrik fenomena Resonansi Sub-Sinkron (SSR) pada poros turbin-generator PLN.
- **C6 (Komputasi):** Memprogram kurva respon frekuensi dan selektivitas filter RLC menggunakan bahasa Julia.

---

## 3. Naskah Audio Narasi Per Salindia (15 Slide Lengkap)

### Salindia 01: Judul & Pembukaan Kuliah Minggu 05

Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, selamat datang dalam perkuliahan daring Persamaan Diferensial semester genap 2026. Pada Minggu kelima ini, kita akan mempelajari dinamika sistem dengan gaya penggerak eksternal: Persamaan Diferensial Biasa Orde Dua Non-Homogen. Kita akan mendalami Metode Koefisien Tak Tentu, aturan modifikasi resonansi pengali t pangkat s, pemodelan rangkaian RLC dengan sumber eksitasi AC sinusoidal, fenomena resonansi dan pelipatgandaan tegangan faktor Q, serta studi kasus industri nyata berupa Resonansi Sub-Sinkron pada jaringan transmisi daya PLN. Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan.

### Salindia 02: Capaian Pembelajaran (Sub-CPMK 3) & Taksonomi Bloom

Berikut adalah Capaian Pembelajaran Sub-CPMK Minggu kelima dalam ranah Bloom. Pada C1 Mengingat, mahasiswa mampu menyatakan dekomposisi solusi total menjadi penjumlahan solusi homogen dan partikular. Pada C2 Memahami, mahasiswa mampu menjelaskan secara fisis mengapa timbul resonansi saat frekuensi sumber menyamai frekuensi alami. Pada C3 Menerapkan, mahasiswa mampu menentukan solusi partikular menggunakan metode koefisien tak tentu. Pada C4 Menganalisis, mahasiswa mampu membedakan evolusi fasa transien cepat versus respon keadaan mantap permanen. Pada C5 Mengevaluasi, mahasiswa mampu mengkaji risiko torsi destruktif akibat Resonansi Sub-Sinkron pada generator listrik. Dan pada C6 Komputasi, mahasiswa mampu membuat kurva respon frekuensi dan faktor kualitas Q dengan Julia.

### Salindia 03: Peta Konsep: Struktur Solusi Lengkap Sistem Non-Homogen

Perhatikan struktur fundamental solusi sistem non-homogen pada diagram ini. Solusi umum lengkap y t selalu terdiri dari dua bagian yang terpisah: y h t yaitu Solusi Homogen atau respon alami sistem, ditambah y p t yaitu Solusi Partikular atau respon paksa akibat pengaruh gaya luar. Solusi homogen ditentukan oleh akar-akar persamaan karakteristik yang mencerminkan sifat intrinsik redaman sirkuit, dan pada sistem fisik nyata dengan redaman selalu meluruh menuju nol sebagai respon transien. Sebaliknya, solusi partikular memiliki bentuk gelombang yang seirama dengan fungsi sumber r t dan bertahan selamanya sebagai respon tunak.

### Salindia 04: Metode Koefisien Tak Tentu (Undetermined Coefficients)

Metode Koefisien Tak Tentu adalah teknik analitis yang sangat elegan bila ruas kanan r t berupa fungsi polinomial, eksponensial, atau sinusoidal. Aturan dasarnya menyatakan bahwa bentuk tebakan solusi partikular y p harus mencakup seluruh turunan independen dari r t. Jika ruas kanan adalah fungsi polinomial orde n, tebaklah polinomial lengkap berderajat n. Jika ruas kanan adalah eksponensial e pangkat alpha t, tebaklah A dikali e pangkat alpha t. Dan jika ruas kanan adalah fungsi sinusoidal sinus omega t atau kosinus omega t, tebakan wajib memuat kombinasi keduanya: A kosinus omega t ditambah B sinus omega t untuk mengantisipasi adanya pergeseran sudut fasa.

### Salindia 05: Aturan Modifikasi Resonansi: Pengali t^s

Apa yang terjadi jika bentuk tebakan solusi partikular ternyata sudah muncul di dalam himpunan basis solusi homogen y h? Inilah yang dinamakan Kondisi Resonansi. Jika kita mensubstitusikan tebakan awal ke ruas kiri PDB, hasilnya akan identik menjadi nol dan kita tidak akan pernah menemukan nilai koefisiennya. Aturan Modifikasi Resonansi menetapkan: kalikan tebakan awal dengan variabel waktu t pangkat s, di mana s adalah bilangan bulat terkecil satu atau dua yang memastikan tidak ada suku pada y p yang sama dengan suku pada y h. Kehadiran faktor pengali t secara fisik merepresentasikan fenomena resonansi di mana amplitudo osilasi tumbuh membesar seiring berjalannya waktu.

### Salindia 06: Pemodelan Fisis: Sirkuit RLC Seri Eksitasi AC

Mari kita tinjau pemodelan rangkaian RLC seri yang dihubungkan ke sumber tegangan sinusoidal AC: v sumber t sama dengan V m kosinus omega t. Berdasarkan Hukum Tegangan Kirchhoff: L d kuadrat i per d t kuadrat ditambah R d i per d t ditambah satu per C dikali i sama dengan minus omega V m sinus omega t. Dalam domain frekuensi, sirkuit ini memiliki impedansi total Z sama dengan R ditambah j kurung omega L dikurang satu per omega C. Kondisi Resonansi Seri terjadi ketika reaktansi induktif omega L tepat meniadakan reaktansi kapasitif satu per omega C, sehingga impedansi total rangkaian berada pada titik minimumnya yaitu murni sebesar resistansi R.

### Salindia 07: Evolusi Gelombang: Respon Transien vs Keadaan Mantap

Grafik pada slide ini memperlihatkan evolusi gelombang arus dan tegangan saat sakelar AC ditutup. Pada beberapa siklus awal, gelombang tampak tidak simetris dan memiliki pergeseran offset DC. Ini adalah superposisi antara respon transien teredam y h yang sedang meluruh dengan respon sinusoidal tunak y p. Setelah waktu berlalu sekitar lima kali konstanta waktu tau, respon alami telah padam sepenuhnya hingga di bawah satu persen. Sistem kini memasuki Keadaan Mantap Sinusoidal atau AC steady-state murni, di mana amplitudo dan pergeseran fasa sepenuhnya sejalan dengan fasor tegangan sumber.

### Salindia 08: Resonansi Seri & Pelipatgandaan Tegangan Reaktif Faktor-Q

Pada kondisi resonansi seri, arus yang mengalir mencapai nilai puncak maksimum sebesar I peak sama dengan V m dibagi R. Perhatikan konsekuensi fisik yang sangat mengejutkan pada tegangan komponen reaktif! Tegangan pada induktor V L dan tegangan pada kapasitor V C masing-masing bernilai I peak dikalikan reaktansinya. Kita mendefinisikan Faktor Kualitas RLC sebagai Q sama dengan satu per R dikalikan akar L per C. Pada rangkaian dengan resistansi kecil, nilai Q dapat mencapai puluhan atau ratusan, sehingga tegangan pada kapasitor dan induktor dapat melonjak menjadi Q kali lipat lebih tinggi daripada tegangan sumber! Fenomena pelipatgandaan tegangan ini dapat merusak isolasi transformator bila tidak diantisipasi dengan baik.

### Salindia 09: Fenomena Denyut Layangan (Beat Phenomenon, omega approx omega_0)

Jika rangkaian memiliki redaman sangat kecil atau tanpa redaman, dan frekuensi eksitasi sumber omega sangat dekat tetapi tidak persis sama dengan frekuensi alami omega nol, terjadilah fenomena akustik dan elektrik yang disebut Denyut Layangan atau Beat Phenomenon. Melalui identitas trigonometri pengurangan kosinus, solusi superposisi terurai menjadi perkalian dua gelombang sinusoidal: gelombang pembawa berfrekuensi tinggi omega nol ditambah omega per dua, yang termodulasi di dalam selubung atau amplop gelombang berfrekuensi rendah omega nol dikurang omega per dua. Amplitudo gelombang membengkak dan mengecil secara periodik, menimbulkan denyut energi yang sangat khas.

### Salindia 10: Studi Kasus Industri: Resonansi Sub-Sinkron (SSR) PLN

Studi kasus industri yang sangat penting bagi insinyur sistem tenaga adalah Resonansi Sub-Sinkron atau SSR pada saluran transmisi tegangan tinggi PLN. Untuk meningkatkan kapasitas transfer daya, kapasitor seri sering dipasang pada saluran transmisi panjang. Namun, kombinasi kapasitor seri dengan induktansi jaringan menciptakan frekuensi resonansi alami sub-sinkron di bawah lima puluh Hertz. Jika frekuensi elektrik sub-sinkron ini bertepatan dengan salah satu frekuensi resonansi mekanis torsional poros turbin-generator, terjadi interaksi kopling elektro-mekanis destruktif. Torsi poros turbin berosilasi membesar secara tak terkendali hingga dapat mematahkan poros turbin raksasa dalam hitungan detik!

### Salindia 11: Contoh Soal 1 (Worked Example): Resonansi Tegangan RLC

Mari kita cermati contoh soal terhitung pertama. Suatu sirkuit RLC seri memiliki R sama dengan dua Ohm, L sama dengan lima puluh mili Henry, dan C sama dengan dua puluh mikrofarad, dieksitasi oleh sumber tegangan AC seratus Volt puncak. Langkah satu: frekuensi resonansi sudut omega nol adalah satu dibagi akar L C, yaitu seribu radian per detik. Langkah dua: faktor kualitas Q sama dengan omega nol dikali L per R, yaitu seribu dikali lima puluh mili Henry dibagi dua, menghasilkan Q sama dengan dua puluh lima. Langkah tiga: pada kondisi resonansi, arus rangkaian adalah seratus dibagi dua yaitu lima puluh Ampere. Tegangan puncak pada kapasitor melonjak mencapai Q dikalikan tegangan sumber, yaitu dua puluh lima dikali seratus sama dengan dua ribu lima ratus Volt! Terjadi lonjakan tegangan dua puluh lima kali lipat yang membutuhkan isolasi berdaya tahan tinggi.

### Salindia 12: Contoh Soal 2 (Worked Example): Denyut Layangan SSR

Pada contoh soal kedua, kita analisis fenomena beat sub-sinkron. Sebuah tangki LC ideal memiliki frekuensi alami tiga puluh Hertz, dan dieksitasi oleh sumber gangguan harmonika berfrekuensi tiga puluh dua Hertz dengan amplitudo tegangan sepuluh Volt. Selisih frekuensi delta omega adalah dua Hertz atau empat pi radian per detik. Frekuensi selubung amplop beat adalah setengah delta omega, yaitu satu Hertz. Hal ini berarti periode denyut layangan adalah satu detik, di mana arus berosilasi memuncak setiap satu detik sekali. Amplitudo maksimum arus melonjak hingga enam kali lipat dari arus normal, mengonfirmasi bahaya getaran siklik pada peralatan listrik.

### Salindia 13: Praktikum Komputasi Julia: Resonansi RLC & Selektivitas

Pada praktikum komputasi Julia ini, kita membuat simulasi sapuan frekuensi atau frequency sweep untuk memetakan kurva selektivitas resonansi RLC. Menggunakan solver Tsit5, kita hitung respon steady-state untuk berbagai variasi rasio redaman zeta dari nol koma satu hingga satu koma nol. Kurva grafik sebelah kanan dengan jelas memperlihatkan kurva puncak resonansi yang tajam pada zeta rendah bernilai nol koma satu, yang menunjukkan selektivitas frekuensi tinggi dengan faktor Q besar. Sebaliknya, kurva pada zeta tinggi tampak datar dan tumpul. Skrip Julia ini memungkinkan Anda merancang filter pita frekuensi atau bandpass filter audio dan komunikasi secara interaktif.

### Salindia 14: Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)

**[Bagian 1 - Pertanyaan Kuis]:**
Saatnya kuis interaktif untuk menguji intuisi fisika Anda. Perhatikan studi kasus pada layar: Rangkaian RLC seri AC mengalami resonansi seri dengan faktor kualitas Q sama dengan sepuluh. Voltmeter mengukur tegangan kapasitor V C sebesar seribu Volt, padahal tegangan sumber V s hanya seratus Volt. Apakah fenomena pelipatgandaan tegangan ini melanggar hukum kekekalan energi? Pilihan A: Ya, tegangan pada komponen rangkaian tidak boleh melebihi tegangan sumber. Pilihan B: Tidak, karena tegangan kapasitor V C dan induktor V L berbeda fasa seratus delapan puluh derajat sehingga saling meniadakan secara vektor total! Pilihan C: Ya, terjadi pembangkitan daya aktif tambahan secara spontan di dalam kapasitor. Pilihan D: Tidak, asalkan frekuensi sumber berada di atas satu kilo Hertz. Silakan analisis konsep energi resonansi ini dan tentukan pilihan terbaik Anda dalam delapan detik ke depan.

*[Jeda Hening Berpikir: 8 Detik Terprogram]*

**[Bagian 2 - Pembahasan Kuis & Tantangan Bloom]:**
Waktu habis. Jawaban yang tepat adalah B: Tidak melanggar hukum kekekalan energi! Pada kondisi resonansi seri, tegangan kapasitor dan induktor memiliki magnitudo sama besar namun berlawanan fasa tepat seratus delapan puluh derajat. Penjumlahan fasor keduanya bernilai nol, sehingga tegangan sumber seratus Volt sepenuhnya jatuh pada resistor. Tegangan seribu Volt adalah energi medan reaktif bolak-balik yang terperangkap di antara L dan C. Pada kolom tantangan sebelah kanan, Anda juga ditantang menganalisis risiko Sub-Synchronous Resonance atau SSR pada turbin generator di level C4, mengevaluasi lebar pita frekuensi minus tiga desibel pada level C5, serta merancang filter pasif RLC frekuensi dua ratus lima puluh Hertz pada level C6.

### Salindia 15: Rangkuman Inti Perkuliahan & Referensi

Sebagai rangkuman perkuliahan minggu kelima: Pertama, solusi PDB non-homogen merupakan penjumlahan respon transien alami dan respon tunak paksa. Kedua, aturan modifikasi pengali t pangkat s wajib diterapkan bila frekuensi eksitasi memicu resonansi. Ketiga, resonansi seri RLC melipatgandakan tegangan reaktif hingga Q kali lipat dari tegangan sumber. Dan keempat, pemahaman resonansi sub-sinkron sangat penting untuk menjamin keselamatan mekanis turbin PLN. Silakan pelajari modul ajar dan tuntaskan Lembar Kerja serta Problem Set Minggu kelima di portal ndaratha dot my dot id. Pada minggu keenam, kita akan beralih ke Transformasi Laplace domain frekuensi kompleks s. Terima kasih dan wassalamualaikum warahmatullahi wabarakatuh.

