# Naskah & Metadata Video Kuliah Minggu 03: Persamaan Diferensial v2.0

### 1. Metadata Siap Unggah YouTube (SEO Optimized)

**Judul Resmi:** `[Minggu 03] Aplikasi Rekayasa PDB Orde 1: Transien RC, RL, & Termal Trafo | Persamaan Diferensial | Teknik Elektro UNIB`

**Deskripsi Siap Unggah:**
```text
Kuliah Daring Minggu 03 - Persamaan Diferensial (Teknik Elektro UNIB)
Topik: Transien Sirkuit RL/RC, Inductive Kickback, Dioda Freewheeling, dan Pemodelan Termal Trafo IEEE Std C57.91

Dosen Pengampu:
- Ir. Novalio Daratha, S.T., M.Sc., Ph.D.
- Muhammad Arfan, S.T., M.T.
Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika
Fakultas Teknik, Universitas Bengkulu

Akses portal perkuliahan, modul ajar, lembar kerja C1-C6, dan problem set:
https://www.ndaratha.my.id/persamaan-diferensial/

Linimasa Bab (Timestamps):
00:00 - 01. Pembukaan Perkuliahan Minggu 03
00:40 - 02. Sub-CPMK 3 & Taksonomi Bloom
01:30 - 03. Peta Konsep: Analogi Elektrik-Termal
02:13 - 04. Inductive Kickback Sirkuit RL
02:57 - 05. Mitigasi Dioda Freewheeling
03:36 - 06. Pensaklaran Multi-Interval RC
04:20 - 07. Dinamika Termal Hukum Newton
04:58 - 08. Model Termal Trafo Daya
05:38 - 09. Standar IEEE C57.91 Penuaan Insulasi
06:20 - 10. Contoh Soal 1: Kickback Koil
07:03 - 11. Contoh Soal 2: Termal Trafo 60 MVA
07:46 - 12. Praktikum Julia: Termal Trafo
08:25 - 13. Verifikasi Simulasi & Stabilitas
09:00 - 14. Kuis Interaktif & Evaluasi Bloom
10:40 - 15. Rangkuman Perkuliahan & Penutup

Buku Referensi Pembelajaran:
1. Erwin Kreyszig, "Advanced Engineering Mathematics", 10th Edition, John Wiley & Sons.
2. Dennis G. Zill, "A First Course in Differential Equations with Modeling Applications", 11th Edition.
3. William H. Hayt & John A. Buck, "Engineering Electromagnetics", 9th Edition, McGraw-Hill.
4. Standar Industri Terkait (IEEE & IEC).

#PersamaanDiferensial #TeknikElektro #UniversitasBengkulu #KalkulusLanjut #DifferentialEquations #JuliaLang
```

---

## 2. Capaian Pembelajaran (Sub-CPMK 3 OBE Taksonomi Bloom)
- **C1 (Mengingat):** Menyatakan bentuk PDB respon alami dan respon paksa sirkuit transien.
- **C2 (Memahami):** Menjelaskan asal fisis lonjakan tegangan balik induktif v_L = L di/dt saat sakelar dibuka.
- **C3 (Menerapkan):** Menghitung respon multi-interval sirkuit RC dan profil kenaikan suhu transformator daya.
- **C4 (Menganalisis):** Menganalisis efektivitas dioda freewheeling dalam meredam tegangan tembus sakelar.
- **C5 (Mengevaluasi):** Mengevaluasi laju penuaan insulasi kertas-minyak transformator berdasarkan IEEE Std C57.91.
- **C6 (Komputasi):** Mengembangkan simulasi transien multi-domain elektrik-termal menggunakan bahasa Julia.

---

## 3. Naskah Audio Narasi Per Salindia (15 Slide Lengkap)

### Salindia 01: Judul & Pembukaan Kuliah Minggu 03

Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, berjumpa kembali dalam perkuliahan daring Persamaan Diferensial semester genap 2026. Pada Minggu ketiga ini, kita akan memperluas cakrawala penerapan PDB orde satu ke ranah rekayasa nyata: dinamika transien pensaklaran sirkuit induktif RL, fenomena lonjakan tegangan balik atau inductive kickback, proteksi sakelar menggunakan dioda freewheeling, pensaklaran multi-interval pada sirkuit RC, serta pemodelan termal transformator daya berbasis standar industri IEEE C57.91. Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan.

### Salindia 02: Capaian Pembelajaran (Sub-CPMK 3) & Taksonomi Bloom

Mari kita cermati Capaian Pembelajaran Sub-CPMK Minggu ketiga berbasis Taksonomi Bloom. Pada C1 Mengingat, mahasiswa mampu menyatakan bentuk PDB respon alami dan respon paksa sirkuit transien. Pada C2 Memahami, mahasiswa mampu menjelaskan asal fisis lonjakan tegangan induktif v L sama dengan L d i per d t. Pada C3 Menerapkan, mahasiswa mampu menghitung respon multi-interval sirkuit RC dan kenaikan suhu minyak trafo. Pada C4 Menganalisis, mahasiswa mampu menguji efektivitas dioda freewheeling dalam membatasi lonjakan tegangan. Pada C5 Mengevaluasi, mahasiswa mampu mengkaji faktor percepatan penuaan termal insulasi minyak trafo IEEE. Dan pada C6 Komputasi, mahasiswa mampu memprogram simulasi numerik transien elektrik dan termal di Julia.

### Salindia 03: Peta Konsep: Transien Elektrik vs Analogi Termal

Perhatikan tabel analogi multi-domain pada slide ini yang memperlihatkan prinsip kesatuan matematika. Pada sirkuit induktif RL, variabel keadaannya adalah arus induktor i L dengan konstanta waktu tau sama dengan L per R. Pada sirkuit kapasitif RC, variabel keadaannya adalah tegangan kapasitor v C dengan konstanta waktu tau sama dengan R C. Sedangkan pada sistem termal trafo, variabel keadaannya adalah temperatur minyak T t dengan konstanta waktu termal tau termal sama dengan R termal dikali C termal. Ketiga fenomena fisik yang tampak sangat berbeda ini sebenarnya diatur oleh struktur kanonik PDB linier orde satu yang persis sama: d x per d t ditambah satu per tau dikali x sama dengan x kondisi tunak dibagi tau.

### Salindia 04: Transien Pemutusan Sirkuit RL: Lonjakan Tegangan Balik

Mari kita pelajari fenomena berbahaya yang disebut Inductive Kickback. Pada kondisi tunak DC, arus mengalir mantap melalui induktor sebesar I nol sama dengan V nol dibagi R. Ketika sakelar dibuka secara tiba-tiba pada t sama dengan nol, arus dipaksa turun menuju nol dalam selang waktu delta t yang sangat singkat mendekati nol. Akibatnya, laju penurunan arus d i per d t melonjak mendekati minus tak hingga. Mengikuti Hukum Induksi Faraday, induktor membangkitkan gaya gerak listrik lawan sebesar v L sama dengan L d i per d t. Tegangan balik ini dapat mencapai ribuan volt, memicu percikan busur api pada sakelar mekanis, atau menghancurkan lapisan dielektrik semikonduktor daya seperti MOSFET dan IGBT dalam orde mikrodetik.

### Salindia 05: Mitigasi Lonjakan Induktif: Dioda Freewheeling (Flyback)

Untuk melindungi sakelar semikonduktor dari lonjakan induktif, insinyur teknik elektro memasang Dioda Freewheeling atau dioda flyback secara paralel terbalik terhadap beban induktif. Saat sakelar tertutup, dioda terbias mundur sehingga bersifat sebagai rangkaian terbuka. Namun saat sakelar dibuka, polaritas tegangan induktor seketika berbalik dan membias maju dioda. Arus induktor kini memiliki jalur sirkulasi tertutup yang aman, di mana energi medan magnet dilepaskan secara eksponensial meluruh dengan konstanta waktu L per R. Tegangan pada sakelar berhasil dikunci pada nilai aman, yaitu tegangan sumber V nol ditambah tegangan jatuh maju dioda sebesar nol koma tujuh volt saja.

### Salindia 06: Transien Pensaklaran Multi-Interval Sirkuit RC

Dalam aplikasi industri nyata seperti sistem radar pulsa dan konverter daya, pensaklaran terjadi secara berulang dalam beberapa interval. Pada interval pengisian dari t nol hingga t satu, kapasitor diisi menuju tegangan target dengan solusi eksponensial naik. Kunci analitik yang sangat krusial adalah Prinsip Kontinuitas Energi: tegangan kapasitor dan arus induktor tidak boleh melonjak diskontinu. Oleh karena itu, nilai tegangan akhir pada interval pertama menjadi kondisi awal yang mengikat bagi interval kedua. Saat sakelar dialihkan ke mode pengosongan pada t satu, solusi PDB meluruh secara eksponensial dari nilai tegangan awal tersebut. Penyusunan solusi sepotong-sepotong ini mendasari seluruh analisis modulasi lebar pulsa atau PWM modern.

### Salindia 07: Dinamika Termal Sistem Tenaga: Hukum Pendinginan Newton

Kini kita beralih ke Pilar pertama analogi fisika, yaitu dinamika termal konduktor dan transformator tenaga. Berdasarkan Hukum Pendinginan Newton dan hukum kekekalan energi kalor, laju akumulasi panas di dalam konduktor sama dengan laju pembangkitan panas Joule akibat aliran arus dikurangi laju pelepasan kalor ke lingkungan sekitar. Model matematika yang mengatur dinamika ini adalah PDB linier orde satu: C termal dikalikan d T per d t ditambah T dikurang T lingkungan dibagi R termal sama dengan daya rugi-rugi P loss. PDB termal ini memiliki solusi waktu yang menunjukkan kenaikan suhu eksponensial asimtotik menuju temperatur kesetimbangan tunak.

### Salindia 08: Model Rangkaian Termal Ekivalen Transformator Daya

Pada transformator daya gardu induk PLN, panas timbul dari rugi-rugi tembaga pada belitan dan rugi-rugi besi pada inti trafo. Panas ini ditransfer ke minyak isolasi trafo lalu dilepaskan ke udara atmosfer melalui radiator pendingin. Sistem pendinginan minyak ONAN dapat dimodelkan secara matematis sebagai rangkaian termal lumped-parameter. Kapasitas termal minyak dan tangki C termal menyimpan energi kalor, sedangkan konveksi radiator dimodelkan sebagai resistansi termal R termal. Konstanta waktu termal trafo biasanya berkisar antara dua hingga empat jam. Hal ini menjelaskan mengapa transformator mampu menahan beban lebih sesaat tanpa langsung mengalami panas berlebih yang fatal.

### Salindia 09: Standar Industri: Penuaan Insulasi Trafo (IEEE Std C57.91)

Mengapa pemodelan PDB termal sangat krusial bagi keandalan sistem tenaga? Standar industri IEEE C57.91 menetapkan bahwa umur pakai transformator daya ditentukan langsung oleh laju degradasi termal kertas isolasi selulosa. Temperatur titik terpanas belitan atau hot-spot temperature theta H memicu reaksi kimia penuaan isolasi mengikuti hukum laju reaksi Arrhenius. Berdasarkan aturan empiris baku industri, setiap kenaikan temperatur sebesar enam hingga tujuh derajat Celsius di atas batas normal seratus sepuluh derajat Celsius akan melipatgandakan laju penuaan isolasi menjadi dua kali lipat lebih cepat. Solusi PDB termal memungkinkan operator PLN memprediksi penuaan aset secara real-time.

### Salindia 10: Contoh Soal 1 (Worked Example): Inductive Kickback Koil

Mari kita bedah contoh soal terhitung pertama. Sebuah koil kontaktor memiliki induktansi dua Henry dan resistansi dua puluh Ohm, terhubung ke sumber DC empat puluh delapan Volt. Pada kondisi tunak, arus bernilai empat puluh delapan dibagi dua puluh sama dengan dua koma empat Ampere. Bila sakelar dibuka mendadak dan arus dipaksa turun ke nol dalam waktu sepuluh mikrodetik tanpa dioda proteksi, maka laju penurunan arus adalah minus dua ratus empat puluh ribu Ampere per detik. Tegangan balik yang dibangkitkan induktor mencapai minus empat ratus delapan puluh ribu Volt! Sebaliknya, bila dipasang dioda freewheeling dengan V F satu Volt, tegangan maksimum sakelar hanya sebesar empat puluh sembilan Volt, dan arus meluruh aman dengan konstanta waktu nol koma satu detik.

### Salindia 11: Contoh Soal 2 (Worked Example): Manajemen Termal Trafo 60 MVA

Contoh soal terhitung kedua menganalisis transformator daya enam puluh MVA pada gardu induk. Trafo memiliki kapasitas panas termal dua koma lima kali sepuluh pangkat tujuh Joule per derajat Celsius, dan resistansi termal tiga kali sepuluh pangkat minus empat derajat Celsius per Watt, menghasilkan konstanta waktu termal dua koma nol delapan jam. Rugi-rugi total daya trafo pada beban puncak adalah seratus lima puluh kilo Watt, dengan temperatur lingkungan tiga puluh derajat Celsius. Kenaikan suhu minyak tunak adalah seratus lima puluh ribu Watt dikalikan resistansi termal, yaitu empat puluh lima derajat Celsius, sehingga suhu minyak akhir mencapai tujuh puluh lima derajat Celsius. Dalam waktu dua jam, suhu minyak naik mencapai lima puluh delapan koma lima derajat Celsius.

### Salindia 12: Praktikum Komputasi Julia: Dinamika Termal Trafo

Sekarang kita terapkan Pilar ketiga komputasi ilmiah terbuka berbasis Julia. Pada slide ini kita simulasikan PDB termal transformator menggunakan paket DifferentialEquations dot j l dan Plots dot j l. Kita definisikan fungsi ODE f trafo kurung T koma p koma t sama dengan P loss dikurang kurung T dikurang T ambient dibagi R termal, lalu seluruhnya dibagi C termal. Dengan waktu simulasi nol hingga sepuluh jam dan kondisi awal suhu tiga puluh derajat Celsius, solver Tsit5 memecahkan dinamika pemanasan trafo secara sangat cepat dan akurat. Kurva grafik memperlihatkan respon transien eksponensial yang mulus menuju saturasi.

### Salindia 13: Verifikasi Hasil Simulasi & Analisis Kestabilan Termal

Pada slide verifikasi ini, kita bandingkan solusi numerik Julia Tsit5 dengan solusi analitis eksak. Keduanya berimpit sempurna dengan galat relatif di bawah sepuluh pangkat minus enam. Analisis kestabilan membuktikan bahwa nilai eigen sistem termal ini adalah minus satu per tau termal yang bernilai negatif real, sehingga sistem bersifat stabil asimtotik mutlak. Pada grafik juga ditampilkan respon terhadap beban lebih mendadak sebesar seratus dua puluh persen. Kita dapat melihat laju kenaikan suhu tambahan yang dapat dipantau oleh algoritma proteksi termal gardu induk sebelum mencapai ambang bahaya.

### Salindia 14: Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)

**[Bagian 1 - Pertanyaan Kuis]:**
Saatnya kuis interaktif untuk menguji pemahaman fisis Anda. Perhatikan kasus rekayasa di layar: Transformator daya enam puluh MVA dibebani lebih mendadak sebesar seratus lima puluh persen. Mengapa temperatur minyak atas naik sangat lambat, sedangkan hotspot kawat tembaga belitan langsung melonjak drastis hanya dalam hitungan menit? Pilihan A: Viskositas minyak isolasi trafo sangat tinggi. Pilihan B: Kapasitas kalor massa minyak puluhan ton sangat masif dengan tau minyak jauh lebih besar dari tau belitan, sedangkan massa kawat tembaga sangat kecil! Pilihan C: Sirkulasi minyak isolasi terhenti saat terjadi beban lebih. Pilihan D: Resistansi kawat tembaga menyusut saat dipanaskan. Silakan analisis fenomena termal ini dan tentukan jawaban terbaik Anda dalam delapan detik ke depan.

*[Jeda Hening Berpikir: 8 Detik Terprogram]*

**[Bagian 2 - Pembahasan Kuis & Tantangan Bloom]:**
Waktu habis. Jawaban yang tepat adalah B: Kapasitas kalor massa minyak puluhan ton sangat masif, sedangkan massa kawat tembaga relatif kecil! Konstanta waktu termal berbanding lurus dengan kapasitas kalor massa benda. Massa minyak trafo yang mencapai puluhan ton membutuhkan waktu berjam-jam untuk menyerap panas, sehingga tau minyak bernilai sekitar tiga jam. Sebaliknya, kawat tembaga memiliki massa yang jauh lebih kecil sehingga merespons rugi-rugi tembaga i kuadrat R secara seketika dengan tau belitan hanya beberapa menit. Pada kolom tantangan sebelah kanan, Anda juga ditantang untuk menghitung laju degradasi kertas isolasi pada level C4, mengevaluasi peredaman dioda freewheeling pada level C5, serta merancang tunda waktu relai termal empat puluh sembilan pada level C6.

### Salindia 15: Rangkuman Inti Perkuliahan & Referensi

Sebagai rangkuman perkuliahan minggu ketiga: Pertama, pemutusan arus induktif menghasilkan lonjakan tegangan balik ekstrem yang wajib dimitigasi dengan dioda freewheeling. Kedua, pensaklaran multi-interval sirkuit RC dihubungkan oleh prinsip kontinuitas tegangan. Ketiga, dinamika termal peralatan listrik memiliki analogi matematika yang identik dengan sirkuit transien orde satu. Dan keempat, pemodelan termal berbasis standar IEEE C57.91 sangat krusial untuk mencegah penuaan dini trafo tenaga. Silakan pelajari modul ajar, lembar kerja, dan problem set minggu ketiga di portal ndaratha dot my dot id. Pada minggu keempat, kita akan melangkah ke PDB orde dua homogen dan tiga ragam redaman RLC. Terima kasih dan wassalamualaikum warahmatullahi wabarakatuh.

