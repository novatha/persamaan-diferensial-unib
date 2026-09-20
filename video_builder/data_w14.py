"""
data_w14.py — Data Narasi 15 Salindia Minggu 14 v2.0
Topik: Fungsi Khusus Persamaan Bessel & Aplikasi Efek Kulit (Skin Effect)
"""
import os

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA = {
    "week_num": "14",
    "pdf_path": os.path.join(PROJ_DIR, "ch14.pdf"),
    "title": "Fungsi Bessel: Koordinat Silinder & Efek Kulit Konduktor ACSR",
    "subtitle": "Metode Deret Frobenius, Titik Singular Reguler, Fungsi Bessel J_nu & Y_nu, Frekuensi Pancung Pandu Gelombang TM01, Mekanisme Fisis Skin Effect, Kedalaman Penetrasi Delta, dan Konduktor ACSR IEC 61089",
    "cpmk": [
        ("C1", "Mengingat", "Menyatakan bentuk kanonik Persamaan Diferensial Bessel x^2 y'' + x y' + (x^2 - nu^2)y = 0 dan deret Frobenius."),
        ("C2", "Memahami", "Menjelaskan perilaku asimtotik fungsi Bessel jenis pertama J_nu (terhingga) dan jenis kedua Y_nu (singular di titik nol)."),
        ("C3", "Menerapkan", "Menghitung frekuensi pancung cut-off pandu gelombang silinder menggunakan akar-akar nol fungsi Bessel alpha_nm."),
        ("C4", "Menganalisis", "Menganalisis redistribusi rapat arus radial konduktor silinder akibat induksi medan magnet bolak-balik (skin effect)."),
        ("C5", "Mengevaluasi", "Mengevaluasi rasio kenaikan resistansi AC terhadap DC (R_ac / R_dc) pada konduktor transmisi ACSR IEC 61089."),
        ("C6", "Komputasi", "Memprogram evaluasi numerik fungsi Bessel dan visualisasi rapat arus skin effect menggunakan bahasa Julia.")
    ],
    "slides": [
        {
            "num": 1,
            "title": "Judul & Pembukaan Kuliah Minggu 14",
            "chapter": "01. Pembukaan Perkuliahan Minggu 14",
            "quiz": False,
            "text": (
                "Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, "
                "selamat datang kembali dalam perkuliahan daring Persamaan Diferensial semester genap 2026. "
                "Pada Minggu keempat belas ini, kita membedah kelas fungsi khusus yang sangat penting dalam analisis medan berkoordinat melingkar: "
                "Persamaan Diferensial Bessel dan Fenomena Efek Kulit atau Skin Effect pada Konduktor Listrik. "
                "Kita akan mendalami Metode Deret Frobenius pada titik singular reguler, fungsi Bessel jenis pertama J nu dan jenis kedua Y nu, "
                "penentuan frekuensi pancung pandu gelombang elektromagnetik, mekanisme redistribusi arus bolak-balik pada konduktor silinder, "
                "serta inovasi desain konduktor ACSR dan busbar berongga berbasis standar internasional IEC 61089. "
                "Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan."
            )
        },
        {
            "num": 2,
            "title": "Sub-CPMK Taksonomi Bloom (Minggu 14)",
            "chapter": "02. Sub-CPMK 14 & Taksonomi Bloom",
            "quiz": False,
            "text": (
                "Berikut adalah Capaian Pembelajaran Sub-CPMK Minggu keempat belas berbasis Taksonomi Bloom. "
                "Pada C1 Mengingat, mahasiswa mampu menyatakan bentuk kanonik PDB Bessel dan struktur deret Frobenius. "
                "Pada C2 Memahami, mahasiswa mampu membedakan karakteristik fisis fungsi Bessel J nu yang terhingga di sumbu pusat versus Y nu yang singular meledak di titik nol. "
                "Pada C3 Menerapkan, mahasiswa mampu menghitung kedalaman kulit delta dan frekuensi pancung pandu gelombang silinder. "
                "Pada C4 Menganalisis, mahasiswa mampu menguraikan persamaan Helmholtz difusi medan magnetik ke dalam fungsi Bessel Kelvin. "
                "Pada C5 Mengevaluasi, mahasiswa mampu mengkaji kenaikan rasio resistansi R AC terhadap R DC pada saluran transmisi tegangan tinggi. "
                "Dan pada C6 Komputasi, mahasiswa mampu menyimulasikan fungsi Bessel dan profil rapat arus menggunakan bahasa Julia."
            )
        },
        {
            "num": 3,
            "title": "Peta Kurikulum: Geometri Melingkar & Koefisien Variabel",
            "chapter": "03. Peta Kurikulum: Geometri Melingkar",
            "quiz": False,
            "text": (
                "Perhatikan perubahan mendasar dalam struktur persamaan diferensial pada slide ini. "
                "Pada minggu-minggu sebelumnya, seluruh PDB yang kita pelajari memiliki koefisien konstan. "
                "Namun ketika kita memodelkan fenomena gelombang dan medan pada konduktor berpenampang bundar, kabel koaksial, atau tabung pandu gelombang silinder, "
                "operator Laplacian dalam koordinat silinder r, theta, z memunculkan suku satu per r dan satu per r kuadrat. "
                "Hal ini menghasilkan Persamaan Diferensial dengan Koefisien Variabel. "
                "PDB Bessel adalah prototipe universal dari persamaan diferensial koefisien variabel yang mengatur seluruh fenomena fisika bergeometri silinder melingkar."
            )
        },
        {
            "num": 4,
            "title": "Penurunan Persamaan Diferensial Bessel",
            "chapter": "04. Penurunan PDB Bessel",
            "quiz": False,
            "text": (
                "Bentuk kanonik Persamaan Diferensial Bessel berorde nu dinyatakan sebagai: "
                "x kuadrat d kuadrat y per d x kuadrat ditambah x d y per d x ditambah kurung x kuadrat dikurang nu kuadrat dikali y sama dengan nol. "
                "Titik x sama dengan nol adalah Titik Singular Reguler, karena koefisien turunan kedua lenyap di titik tersebut "
                "tetapi hasil kali x P x dan x kuadrat Q x tetap bernilai analitik terhingga. "
                "Karena titik x sama dengan nol adalah singular, metode deret Taylor biasa gagal diterapkan. "
                "Penyelesaiannya menuntut penerapan metode deret umum yang dikembangkan oleh Ferdinand Georg Frobenius."
            )
        },
        {
            "num": 5,
            "title": "Metode Deret Frobenius di Sekitar Titik Singular Reguler",
            "chapter": "05. Metode Deret Frobenius",
            "quiz": False,
            "text": (
                "Metode Deret Frobenius mengasumsikan solusi dalam bentuk deret pangkat tergeneralisasi: "
                "y x sama dengan x pangkat r dikalikan jumlahan dari m sama dengan nol hingga tak hingga a m x pangkat m, dengan a nol tidak nol. "
                "Mensubstitusikan deret ini ke PDB Bessel menghasilkan Persamaan Indisial kuadratik: r kuadrat dikurang nu kuadrat sama dengan nol. "
                "Akar-akar indisialnya adalah r satu sama dengan plus nu dan r dua sama dengan minus nu. "
                "Melalui relasi rekursi dua langkah, kita peroleh bahwa seluruh suku ganjil bernilai nol, "
                "sedangkan suku-suku genap membentuk deret konvergen mutlak di seluruh bidang riil yang mendefinisikan Fungsi Bessel."
            )
        },
        {
            "num": 6,
            "title": "Fungsi Bessel Jenis Pertama J_nu(x) & Jenis Kedua Y_nu(x)",
            "chapter": "06. Fungsi Bessel J_nu & Y_nu",
            "quiz": False,
            "text": (
                "Solusi umum lengkap dari PDB Bessel dinyatakan sebagai kombinasi linier dari dua fungsi basis independen: "
                "y x sama dengan C satu J nu x ditambah C dua Y nu x. "
                "Fungsi Bessel Jenis Pertama J nu x memiliki sifat bernilai terhingga di titik pusat x sama dengan nol dan berosilasi mirip gelombang sinusoidal dengan amplitudo yang meluruh sebanding satu per akar x. "
                "Sebaliknya, Fungsi Bessel Jenis Kedua Y nu x atau fungsi Neumann memiliki singularitas logaritmik ekstrem yang meledak menuju minus tak hingga di titik pusat x sama dengan nol! "
                "Konsekuensi fisik yang sangat penting: untuk konduktor padat silinder yang mencakup sumbu tengah r sama dengan nol, "
                "koefisien C dua wajib dipilih nol mutlak agar medan listrik di pusat konduktor tetap bernilai riil dan terhingga."
            )
        },
        {
            "num": 7,
            "title": "Akar-Akar Nol Bessel (alpha_nm) & Frekuensi Pancung",
            "chapter": "07. Akar Nol Bessel & Frekuensi Pancung",
            "quiz": False,
            "text": (
                "Sebagaimana fungsi sinus bernilai nol pada kelipatan pi, fungsi Bessel J nu x memiliki tak hingga banyaknya akar-akar nol diskrit positif, "
                "dilambangkan sebagai alfa nu m. "
                "Sebagai contoh untuk J nol x, akar pertamanya adalah dua koma empat ratus lima, akar kedua lima koma lima ratus dua puluh, dan akar ketiga delapan koma enam ratus lima puluh empat. "
                "Ketika gelombang elektromagnetik merambat di dalam tabung pandu gelombang silinder berjejari a, "
                "syarat batas dinding konduktor sempurna mewajibkan medan listrik tangensial lenyap di permukaan r sama dengan a. "
                "Kondisi batas ini mengunci nilai eigen k sama dengan alfa nu m dibagi a, "
                "yang secara langsung menetapkan Frekuensi Pancung atau cut-off frequency pandu gelombang."
            )
        },
        {
            "num": 8,
            "title": "Mekanisme Fisika Efek Kulit (Skin Effect) pada Konduktor",
            "chapter": "08. Mekanisme Fisis Skin Effect",
            "quiz": False,
            "text": (
                "Kini kita masuki Pilar pertama intuisi fisika rekayasa tenaga: fenomena Efek Kulit atau Skin Effect. "
                "Pada arus searah DC, rapat arus mengalir merata sempurna di seluruh penampang kawat tembaga. "
                "Namun ketika arus bolak-balik AC mengalir, fluks medan magnet bolak-balik timbul baik di luar maupun di dalam tubuh konduktor. "
                "Fluks magnetik internal ini paling padat melingkari sumbu pusat konduktor. "
                "Berdasarkan Hukum Induksi Faraday dan Hukum Lenz, perubahan fluks magnet internal menginduksi tegangan gerak listrik lawan "
                "yang membangkitkan arus pusar atau eddy current. "
                "Arus pusar ini melawan arah arus utama di inti pusat konduktor dan memperkuat arus di permukaan luar, "
                "memaksa elektron-elektron terdorong keluar berkonsentrasi pada lapisan kulit konduktor."
            )
        },
        {
            "num": 9,
            "title": "Contoh Terhitung: Frekuensi Pancung Pandu Gelombang TM_01",
            "chapter": "09. Contoh Soal Pandu Gelombang",
            "quiz": False,
            "text": (
                "Mari kita selesaikan contoh perhitungan frekuensi pancung pandu gelombang silinder berongga berjejari a sama dengan dua koma lima sentimeter. "
                "Untuk mode transversal magnetik fundamental TM nol satu, akar nol Bessel yang relevan adalah alfa nol satu sama dengan dua koma empat ratus lima. "
                "Frekuensi pancung dihitung melalui rumus: f cut-off sama dengan kecepatan cahaya c dikalikan alfa nol satu dibagi kurung dua pi dikalikan jejari a. "
                "Substitusikan nilai: tiga kali sepuluh pangkat delapan dikali dua koma empat ratus lima dibagi kurung dua pi kali nol koma nol dua lima, "
                "menghasilkan frekuensi pancung sebesar empat koma lima sembilan giga Hertz. "
                "Sinyal gelombang mikro dengan frekuensi di bawah empat koma lima sembilan giga Hertz akan teratenuasi habis dan tidak dapat merambat melintasi tabung pandu gelombang ini."
            )
        },
        {
            "num": 10,
            "title": "Contoh Terhitung: Kedalaman Kulit Tembaga & Aluminium",
            "chapter": "10. Contoh Soal Kedalaman Kulit",
            "quiz": False,
            "text": (
                "Tingkat penetrasi medan elektromagnetik ke dalam konduktor diukur oleh Kedalaman Kulit atau Skin Depth delta: "
                "delta sama dengan satu dibagi akar kurung pi dikalikan frekuensi f dikalikan permeabilitas mu dikalikan konduktivitas sigma. "
                "Pada jarak satu delta dari permukaan luar, rapat arus telah meluruh hingga tiga puluh enam koma delapan persen dari nilai permukaannya. "
                "Untuk konduktor tembaga standar pada frekuensi sistem tenaga lima puluh Hertz, kedalaman kulit adalah sekitar sembilan koma dua milimeter. "
                "Sedangkan untuk konduktor aluminium dengan konduktivitas lebih rendah, kedalaman kulitnya sekitar sebelas koma enam milimeter. "
                "Bila diameter konduktor melebihi dua puluh milimeter, bagian inti dalam konduktor praktis tidak lagi dilewati oleh arus listrik!"
            )
        },
        {
            "num": 11,
            "title": "Peningkatan Resistansi Efektif AC (R_ac / R_dc)",
            "chapter": "11. Peningkatan Resistansi AC/DC",
            "quiz": False,
            "text": (
                "Konsekuensi rekayasa yang sangat merugikan dari efek kulit adalah berkurangnya luas penampang efektif yang dilalui arus listrik. "
                "Karena arus hanya berdesakan mengalir pada cincin selubung tipis di permukaan luar, "
                "resistansi efektif arus bolak-balik R AC menjadi jauh lebih besar daripada resistansi arus searah R DC! "
                "Rasio R AC terhadap R DC sebanding dengan perbandingan radius konduktor terhadap dua kali kedalaman kulit delta. "
                "Peningkatan resistansi ini melipatgandakan rugi-rugi daya transmisi Joule i kuadrat R AC pada saluran udara tegangan tinggi PLN, "
                "sekaligus mempercepat kenaikan suhu operasi konduktor."
            )
        },
        {
            "num": 12,
            "title": "Standar Industri: Solusi Konduktor ACSR & Busbar Tubular",
            "chapter": "12. Konduktor ACSR & Standar IEC 61089",
            "quiz": False,
            "text": (
                "Memahami Persamaan Bessel dan efek kulit memicu lahirnya inovasi cerdas dalam desain konduktor transmisi berstandar IEC 61089. "
                "Karena bagian inti tengah konduktor tidak dilewati arus AC, insinyur mengganti inti tembaga yang mahal dan berat "
                "dengan kawat baja berkekuatan mekanis tinggi, yang diselubungi oleh pilinan kawat aluminium murni di lapisan luarnya. "
                "Inilah Konduktor ACSR atau Aluminium Conductor Steel Reinforced yang digunakan pada seluruh menara transmisi SUTT dan SUTET di Indonesia! "
                "Lapisan aluminium luar menyalurkan seluruh arus listrik AC, sedangkan inti baja menahan beban tarikan mekanis bentang menara. "
                "Demikian pula pada gardu induk GITET, busbar dibuat berbentuk pipa tembaga berongga atau tubular busbar untuk menghemat logam mulia."
            )
        },
        {
            "num": 13,
            "title": "Praktikum Komputasi Julia: Fungsi Bessel & Skin Effect",
            "chapter": "13. Praktikum Julia: Bessel & Skin Effect",
            "quiz": False,
            "text": (
                "Pada praktikum komputasi Julia ini, kita memprogram fungsi Bessel menggunakan paket SpecialFunctions dot j l "
                "dan mengevaluasi distribusi rapat arus radial J r pada kawat silinder pejal. "
                "Dengan memecahkan persamaan diferensial difusi Bessel Kelvin berargumen kompleks, kita hitung modulus rapat arus dari pusat r sama dengan nol hingga permukaan r sama dengan R. "
                "Grafik di sebelah kanan dengan sangat dramatis memperlihatkan efek kulit: "
                "pada frekuensi DC rapat arus mendatar seragam, sedangkan pada frekuensi AC lima puluh Hertz kurva melonjak tajam ke atas menyerupai mangkuk, "
                "di mana rapat arus di permukaan luar kawat mencapai lima kali lipat lebih padat dibandingkan rapat arus di pusat kawat. "
                "Simulasi Julia ini memberikan bukti numerik yang tak terbantahkan mengenai fenomena skin effect."
            )
        },
        {
            "num": 14,
            "title": "Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)",
            "chapter": "14. Kuis Interaktif & Evaluasi Bloom",
            "quiz": True,
            "text_part1": (
                "Saatnya kuis interaktif untuk menguji pemahaman fisis fungsi Bessel dan efek kulit Anda. Perhatikan studi kasus pada layar: "
                "Pada saluran transmisi daya tinggi PLN, mengapa kabel konduktor dibuat dari aluminium di lapisan luar dan baja pejal di inti tengah seperti kawat ACSR standar IEC 61089, dan bukan sebaliknya? "
                "Pilihan A: Baja lebih tahan terhadap korosi kimia atmosfer dibanding aluminium. "
                "Pilihan B: Efek kulit mendesak arus AC mengalir di lapisan luar aluminium konduktif, sehingga inti tengah yang sepi arus diisi baja kuat penahan beban tarikan mekanis! "
                "Pilihan C: Aluminium memiliki densitas massa yang jauh lebih tinggi daripada baja. "
                "Pilihan D: Baja berfungsi menghalangi induksi medan petir masuk ke fasa transmisi. "
                "Silakan analisis fenomena efek kulit ini dan tentukan pilihan jawaban terbaik Anda dalam delapan detik ke depan."
            ),
            "text_part2": (
                "Waktu habis. Jawaban yang tepat adalah B: Efek kulit mendesak arus AC mengalir di luar, sehingga inti diisi baja kuat tarikan mekanis! "
                "Pada frekuensi lima puluh Hertz, distribusi kerapatan arus Bessel J nol mendesak arus AC menuju kulit luar konduktor. "
                "Inti pusat kawat praktis tidak dialiri arus, sehingga penempatan baja di pusat memberikan kekuatan tarik menopang bentang menara ratusan meter "
                "tanpa mengurangi kapasitas hantar arus kawat transmisi. "
                "Pada kolom tantangan sebelah kanan, Anda juga ditantang menghitung frekuensi pancung pandu gelombang silindris di level C4, "
                "mengevaluasi rasio resistansi AC terhadap DC pada inverter dua puluh kilo Hertz di level C5, serta merancang rel busbar tubular berongga GITET lima ratus kilo Volt di level C6."
            )
        },
        {
            "num": 15,
            "title": "Rangkuman Eksekutif & Jembatan ke Minggu 15",
            "chapter": "15. Rangkuman Eksekutif & Penutup",
            "quiz": False,
            "text": (
                "Sebagai rangkuman perkuliahan minggu keempat belas: Pertama, PDB Bessel timbul secara alami dari analisis koordinat silinder dengan koefisien variabel. "
                "Kedua, metode Frobenius menyelesaikan persamaan singular reguler dan menghasilkan fungsi Bessel J nu dan Y nu. "
                "Ketiga, akar-akar nol fungsi Bessel menetapkan frekuensi pancung pandu gelombang silinder. "
                "Dan keempat, pemahaman efek kulit mendasari inovasi desain konduktor ACSR dan busbar berongga sesuai standar IEC 61089. "
                "Silakan pelajari modul ajar dan selesaikan Lembar Kerja serta Problem Set Minggu keempat belas di portal ndaratha dot my dot id. "
                "Pada minggu kelima belas, kita akan mengakhiri perkuliahan dengan Polinomial Legendre pada koordinat bola dan Empat Persamaan Maxwell Diferensial. Terima kasih dan wassalamualaikum warahmatullahi wabarakatuh."
            )
        }
    ]
}
