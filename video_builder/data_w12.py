"""
data_w12.py — Data Narasi 15 Salindia Minggu 12 v2.0
Topik: Persamaan Panas 1D & Manajemen Termal Konduktor Listrik
"""
import os

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA = {
    "week_num": "12",
    "pdf_path": os.path.join(PROJ_DIR, "ch12.pdf"),
    "title": "Persamaan Panas 1D: Difusi Termal Kabel Bawah Tanah IEC 60287",
    "subtitle": "Hukum Fourier Konduksi Panas, Metode Dekomposisi Keadaan Tunak/Transien, Skala Waktu Relaksasi Termal, Kuat Hantar Arus (Ampacity) Kabel XLPE 20 kV, dan Standar IEC 60287 / IEEE 835",
    "cpmk": [
        ("C1", "Mengingat", "Menyatakan bentuk baku Persamaan Panas 1D difusif dan Hukum Fourier konduksi termal."),
        ("C2", "Memahami", "Menjelaskan konsep dekomposisi suhu total u(x,t) = v(x) + w(x,t) menjadi komponen tunak dan transien teredam."),
        ("C3", "Menerapkan", "Menghitung distribusi suhu spasial kabel dan waktu relaksasi termal pendinginan eksponensial."),
        ("C4", "Menganalisis", "Menganalisis batas kuat hantar arus atau ampacity konduktor berdasarkan degradasi termal isolasi XLPE."),
        ("C5", "Mengevaluasi", "Mengevaluasi perhitungan kapasitas kabel tanah sistem distribusi 20 kV berdasarkan standar IEC 60287."),
        ("C6", "Komputasi", "Memprogram simulasi difusi radial 1D pada isolasi kabel XLPE menggunakan bahasa Julia.")
    ],
    "slides": [
        {
            "num": 1,
            "title": "Judul & Pembukaan Kuliah Minggu 12",
            "chapter": "01. Pembukaan Perkuliahan Minggu 12",
            "quiz": False,
            "text": (
                "Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, "
                "selamat datang dalam perkuliahan daring Persamaan Diferensial semester genap 2026. "
                "Pada Minggu kedua belas ini, kita membedah Persamaan Diferensial Parsial tipe Parabolik: "
                "Persamaan Panas Satu Dimensi dan Manajemen Termal Konduktor Listrik. "
                "Kita akan mempelajari Hukum Fourier konduksi panas, metode dekomposisi keadaan tunak dan transien, "
                "skala waktu pendinginan eksponensial, batas kuat hantar arus atau ampacity kabel bawah tanah XLPE dua puluh kilo Volt, "
                "serta standar industri internasional IEC 60287 dan IEEE 835. "
                "Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan."
            )
        },
        {
            "num": 2,
            "title": "Sub-CPMK Taksonomi Bloom (Minggu 12)",
            "chapter": "02. Sub-CPMK 12 & Taksonomi Bloom",
            "quiz": False,
            "text": (
                "Berikut adalah Capaian Pembelajaran Sub-CPMK Minggu kedua belas berbasis Taksonomi Bloom. "
                "Pada C1 Mengingat, mahasiswa mampu menyatakan Hukum Fourier dan bentuk baku Persamaan Panas satu dimensi. "
                "Pada C2 Memahami, mahasiswa mampu menjelaskan prinsip dekomposisi pemisahan solusi tunak spasial v x dan transien w x t. "
                "Pada C3 Menerapkan, mahasiswa mampu menghitung waktu pendinginan relaksasi termal konduktor tembaga. "
                "Pada C4 Menganalisis, mahasiswa mampu mengaitkan pemanasan internal Joule arus listrik terhadap batas temperatur isolasi kabel. "
                "Pada C5 Mengevaluasi, mahasiswa mampu mengkaji penurunan rating ampacity kabel bawah tanah akibat resistivitas termal tanah IEC 60287. "
                "Dan pada C6 Komputasi, mahasiswa mampu menyimulasikan profil difusi suhu kabel menggunakan bahasa Julia."
            )
        },
        {
            "num": 3,
            "title": "Peta Kurikulum: Manajemen Termal sebagai Pembatas Kapasitas Daya",
            "chapter": "03. Peta Kurikulum: Manajemen Termal Daya",
            "quiz": False,
            "text": (
                "Perhatikan posisi krusial manajemen termal pada peta kurikulum teknik elektro ini. "
                "Dalam sistem tenaga listrik, kapasitas penyaluran daya suatu saluran transmisi, kabel bawah tanah, atau transformator "
                "hampir tidak pernah dibatasi oleh batas tegangan tembus isolasi, melainkan dibatasi oleh Batas Termal Konduktor. "
                "Aliran arus yang melebihi kapasitas membangkitkan panas Joule i kuadrat R yang mempercepat penuaan isolasi polimer XLPE. "
                "Bila temperatur konduktor melampaui sembilan puluh derajat Celsius dalam waktu lama, isolasi kabel akan mengalami degradasi termal getas, "
                "kehilangan kekuatan dielektrik, dan memicu hubung singkat tanah yang melumpuhkan pasokan listrik kota."
            )
        },
        {
            "num": 4,
            "title": "Hukum Fourier Konduksi & Penurunan Persamaan Panas",
            "chapter": "04. Hukum Fourier & Persamaan Panas",
            "quiz": False,
            "text": (
                "Mari kita turunkan Persamaan Panas satu dimensi secara first-principles. "
                "Hukum Fourier Konduksi Panas menyatakan bahwa fluks kalor q sebanding dengan negatif gradien temperatur: "
                "q sama dengan minus k konduktivitas termal dikalikan parsial u per parsial x. "
                "Menerapkan hukum kekekalan energi pada segmen konduktor sepanjang delta x dengan massa jenis rho, kapasitas kalor spesifik c, "
                "dan pembangkitan panas internal Joule g: laju akumulasi kalor sama dengan fluks netto yang masuk ditambah pembangkitan internal. "
                "Hasilnya adalah Persamaan Panas 1D: parsial u per parsial t sama dengan alfa dikalikan parsial kuadrat u per parsial x kuadrat ditambah g dibagi rho c, "
                "di mana alfa sama dengan k dibagi rho c dinamakan Difusivitas Termal bahan."
            )
        },
        {
            "num": 5,
            "title": "Metode Dekomposisi: Keadaan Tunak & Transien",
            "chapter": "05. Metode Dekomposisi Tunak-Transien",
            "quiz": False,
            "text": (
                "Ketika persamaan panas memuat pembangkitan kalor internal konstan atau syarat batas tak nol yang tidak homogen, "
                "metode pemisahan variabel tidak dapat diterapkan secara langsung. "
                "Solusinya adalah Metode Dekomposisi: kita uraikan solusi suhu total u x koma t menjadi penjumlahan dua komponen: "
                "u x koma t sama dengan v x yaitu Solusi Keadaan Tunak murni spasial saat t menuju tak hingga, "
                "ditambah w x koma t yaitu Solusi Transien Teredam yang memenuhi syarat batas homogen. "
                "Komponen v x diselesaikan menggunakan integrasi PDB biasa sederhana, "
                "sedangkan komponen w x t diselesaikan dengan metode pemisahan variabel deret Fourier standar."
            )
        },
        {
            "num": 6,
            "title": "Pendinginan Dirichlet & Skala Waktu Relaksasi Termal",
            "chapter": "06. Pendinginan Dirichlet & Relaksasi",
            "quiz": False,
            "text": (
                "Pada kasus pendinginan konduktor dengan syarat batas Dirichlet homogen di mana kedua ujung dijaga pada nol derajat Celsius, "
                "setiap mode harmonisa deret Fourier meluruh secara eksponensial dengan faktor e pangkat minus t dibagi tau n. "
                "Konstanta waktu relaksasi termal untuk mode ke-n adalah tau n sama dengan L kuadrat dibagi kurung n kuadrat pi kuadrat alfa. "
                "Perhatikan bahwa mode harmonisa tinggi n sama dengan dua, tiga, dan seterusnya meluruh sangat cepat sebanding n kuadrat. "
                "Setelah waktu singkat berlalu, seluruh harmonisa tinggi telah lenyap, menyisakan mode fundamental n sama dengan satu "
                "yang mendominasi seluruh proses pendinginan jangka panjang konduktor."
            )
        },
        {
            "num": 7,
            "title": "Kondisi Batas Campuran: Insulasi & Pendinginan Kuartal Gelombang",
            "chapter": "07. Kondisi Batas Campuran",
            "quiz": False,
            "text": (
                "Dalam banyak aplikasi praktis, satu ujung batang konduktor didinginkan pada suhu tetap Dirichlet, "
                "sedangkan ujung lainnya terisolasi termal sempurna secara adiabatik Neumann. "
                "Kombinasi syarat batas campuran ini menghasilkan Masalah Nilai Eigen Kuartal Gelombang: "
                "fungsi eigen spasial yang memenuhi kedua batas adalah X n x sama dengan sinus kurung dua n dikurang satu pi x per dua L. "
                "Panjang konduktor L kini menampung seperempat panjang gelombang ganjil. "
                "Konstanta waktu pendinginannya menjadi empat kali lebih lambat dibandingkan batang yang didinginkan di kedua ujungnya, "
                "karena jalur pelepasan kalor hanya tersedia pada satu sisi."
            )
        },
        {
            "num": 8,
            "title": "Struktur Termal Kabel Tenaga Bawah Tanah 20 kV XLPE",
            "chapter": "08. Struktur Termal Kabel XLPE 20 kV",
            "quiz": False,
            "text": (
                "Slide ini menampilkan penampang melintang struktur kabel tanah tegangan menengah dua puluh kilo Volt jenis XLPE. "
                "Panas Joule dibangkitkan pada inti konduktor tembaga di pusat kabel. "
                "Kalor ini harus merambat menembus lapisan pelindung semikonduktor dalam, isolasi utama polietilena silang XLPE, "
                "layar pita tembaga penahan medan, selubung luar polietilena HDPE, dan akhirnya berdifusi ke medium tanah urug pasir di sekitarnya. "
                "Secara termal, setiap lapisan konsentris silinder ini bertindak sebagai resistansi termal radial R termal. "
                "Kapasitas penghantaran arus kabel sepenuhnya dibatasi oleh kemampuan tanah membuang kalor tersebut ke atmosfer."
            )
        },
        {
            "num": 9,
            "title": "Contoh Terhitung: Pendinginan Batang Tembaga 100°C -> 50°C",
            "chapter": "09. Contoh Soal Pendinginan Batang",
            "quiz": False,
            "text": (
                "Mari kita selesaikan contoh perhitungan relaksasi termal batang tembaga panjang setengah meter dengan difusivitas satu koma satu kali sepuluh pangkat minus empat meter kuadrat per detik. "
                "Suhu awal seratus derajat Celsius seragam, dan kedua ujung tiba-tiba dicelupkan ke dalam air es nol derajat. "
                "Konstanta waktu mode fundamental adalah tau satu sama dengan L kuadrat dibagi pi kuadrat alfa, yaitu nol koma dua lima dibagi sembilan koma delapan tujuh kali satu koma satu kali sepuluh pangkat minus empat, "
                "menghasilkan dua ratus tiga puluh detik atau sekitar tiga koma delapan menit. "
                "Untuk menurunkan suhu di titik tengah batang menjadi lima puluh derajat Celsius, waktu yang dibutuhkan adalah sekitar dua ratus empat puluh lima detik atau empat menit."
            )
        },
        {
            "num": 10,
            "title": "Contoh Terhitung: Pemanasan Internal Joule Kawat Listrik",
            "chapter": "10. Contoh Soal Pemanasan Joule",
            "quiz": False,
            "text": (
                "Pada contoh soal kedua, kita analisis kawat tembaga penghantar arus dengan pembangkitan panas internal seragam g sama dengan sepuluh pangkat enam Watt per meter kubik. "
                "Panjang kawat satu meter, konduktivitas termal empat ratus Watt per meter Kelvin, dan kedua ujung dijaga pada suhu lingkungan tiga puluh derajat Celsius. "
                "Persamaan keadaan tunak PDB biasa adalah: minus empat ratus d kuadrat v per d x kuadrat sama dengan sepuluh pangkat enam. "
                "Dengan mengintegrasikan dua kali dan memasukkan syarat batas nol di ujung-ujung, diperoleh profil suhu parabola simetris: "
                "v x sama dengan tiga puluh ditambah seribu dua ratus lima puluh dikalikan x dikalikan kurung satu dikurang x derajat Celsius. "
                "Suhu puncak terjadi tepat di tengah bentang kawat mencapai enam puluh satu koma dua lima derajat Celsius."
            )
        },
        {
            "num": 11,
            "title": "Kuat Hantar Arus (Ampacity) & Degradasi Isolasi",
            "chapter": "11. Ampacity & Degradasi Isolasi",
            "quiz": False,
            "text": (
                "Kuat Hantar Arus atau Ampacity didefinisikan sebagai arus kontinu maksimum yang dapat dipikul konduktor "
                "tanpa menyebabkan temperatur isolasi melampaui batas batas aman desainnya. "
                "Untuk kabel isolasi XLPE, batas temperatur kontinu adalah sembilan puluh derajat Celsius, dengan batas darurat beban lebih seratus tiga puluh derajat, "
                "dan batas hubung singkat sesaat dua ratus lima puluh derajat Celsius. "
                "Berdasarkan neraca kesetimbangan panas keadaan tunak, arus ampacity I maks sebanding dengan akar dari selisih suhu maksimum "
                "dikurangi suhu lingkungan, dibagi resistansi elektrik ac konduktor dikalikan total resistansi termal lingkungan."
            )
        },
        {
            "num": 12,
            "title": "Standar Industri: Perhitungan Ampacity IEC 60287 & IEEE 835",
            "chapter": "12. Standar Ampacity IEC 60287",
            "quiz": False,
            "text": (
                "Standar internasional IEC 60287 dan IEEE Standard 835 menetapkan metodologi baku perhitungan kapasitas termal kabel tenaga. "
                "Standar ini memperhitungkan secara rinci resistivitas termal tanah rho tanah, kedalaman penanaman kabel di bawah permukaan tanah, "
                "efek pemanasan silang antar kabel yang berdampingan atau mutual heating, serta faktor beban harian. "
                "Jika kabel ditanam pada tanah kering berpasir dengan resistivitas termal tinggi, terjadi fenomena thermal runaway "
                "di mana tanah mengering dan kehilangan kemampuan konduksi panas. "
                "Insinyur distribusi PLN wajib menerapkan faktor koreksi penurunan rating atau derating factor agar kabel tidak mengalami kegagalan isolasi fatal."
            )
        },
        {
            "num": 13,
            "title": "Praktikum Komputasi Julia: Difusi Termal Kabel XLPE",
            "chapter": "13. Praktikum Julia: Termal Kabel XLPE",
            "quiz": False,
            "text": (
                "Pada praktikum komputasi Julia ini, kita membuat simulasi numerik difusi termal radial 1D melintasi lapisan silinder kabel tenaga XLPE. "
                "Dengan memanfaatkan skema implisit Crank-Nicolson yang stabil tanpa batas langkah waktu, kita selesaikan evolusi gradien temperatur dari inti tembaga hingga permukaan luar selubung. "
                "Grafik di sebelah kanan memperlihatkan profil penurunan temperatur radial: "
                "inti tembaga mencapai suhu tertinggi delapan puluh lima derajat Celsius, temperatur turun tajam melintasi lapisan isolasi polimer XLPE, "
                "dan menyentuh suhu tanah empat puluh derajat di permukaan luar. "
                "Simulasi Julia ini menjadi perangkat analisis berharga dalam verifikasi desain kabel bawah laut dan transmisi kota."
            )
        },
        {
            "num": 14,
            "title": "Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)",
            "chapter": "14. Kuis Interaktif & Evaluasi Bloom",
            "quiz": True,
            "text_part1": (
                "Saatnya kuis interaktif untuk menguji pemahaman manajemen termal kabel daya Anda. Perhatikan studi kasus pada layar: "
                "Mengapa kabel tanah XLPE dua puluh kilo Volt yang ditanam di dalam parit tanah memiliki batas kuat hantar arus atau ampacity yang jauh lebih rendah dibanding kawat ACSR berdiameter sama di udara terbuka? "
                "Pilihan A: Tembaga pada kabel tanah memiliki konduktivitas listrik yang lebih rendah. "
                "Pilihan B: Lapisan isolasi padat polimer XLPE dan timbunan tanah memiliki resistansi termal yang jauh lebih besar dibanding konveksi udara bebas! "
                "Pilihan C: Medan gravitasi bumi menahan aliran arus listrik di dalam tanah. "
                "Pilihan D: Kabel tanah rentan mengalami kehilangan tegangan akibat induksi bolak-balik. "
                "Silakan analisis mekanisme perpindahan panas ini dan tentukan pilihan jawaban terbaik Anda dalam delapan detik ke depan."
            ),
            "text_part2": (
                "Waktu habis. Jawaban yang tepat adalah B: Lapisan isolasi polimer XLPE dan timbunan tanah memiliki resistansi termal sangat tinggi! "
                "Pada kawat udara ACSR, panas dilepas langsung melalui konveksi udara terbuka dan radiasi alami. "
                "Sebaliknya pada kabel tanah, panas terperangkap oleh konduktivitas termal tanah yang buruk, membentuk hambatan termal masif. "
                "Akibatnya, arus harus dibatasi agar temperatur inti tembaga tidak melampaui batas kritis isolasi sembilan puluh derajat Celsius. "
                "Pada kolom tantangan sebelah kanan, Anda juga ditantang menurunkan dekomposisi solusi tunak dan transien di level C4, "
                "mengevaluasi bahaya thermal runaway isolasi di level C5, serta merancang kedalaman parit dan pasir termal sesuai IEC 60287 di level C6."
            )
        },
        {
            "num": 15,
            "title": "Rangkuman Eksekutif & Jembatan ke Minggu 13",
            "chapter": "15. Rangkuman Eksekutif & Penutup",
            "quiz": False,
            "text": (
                "Sebagai rangkuman perkuliahan minggu kedua belas: Pertama, Persamaan Panas 1D memodelkan difusi energi termal yang mengatur batas kapasitas fisik sistem kelistrikan. "
                "Kedua, metode dekomposisi memisahkan solusi menjadi profil tunak spasial dan peluruhan transien deret Fourier. "
                "Ketiga, ampacity kabel tanah dibatasi oleh batas degradasi polimer XLPE sembilan puluh derajat Celsius sesuai standar IEC 60287. "
                "Dan keempat, simulasi numerik Julia memvalidasi gradien temperatur radial melintasi lapisan insulasi. "
                "Silakan pelajari modul ajar dan tuntaskan Lembar Kerja serta Problem Set Minggu kedua belas di portal ndaratha dot my dot id. "
                "Pada minggu ketiga belas, kita akan mendalami Persamaan Laplace 2D dan distribusi medan elektrostatika gardu induk. Terima kasih dan wassalamualaikum warahmatullahi wabarakatuh."
            )
        }
    ]
}
