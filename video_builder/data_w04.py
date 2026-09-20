"""
data_w04.py — Data Narasi 15 Salindia Minggu 04 v2.0
Topik: PDB Orde 2 Homogen Koefisien Konstan & Tiga Ragam Redaman RLC
Disesuaikan secara presisi dengan berkas presentasi Beamer ch4.tex
"""
import os

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA = {
    "week_num": "04",
    "pdf_path": os.path.join(PROJ_DIR, "ch4.pdf"),
    "title": "PDB Orde 2 Homogen: Karakteristik Akar & Tiga Ragam Redaman RLC",
    "subtitle": "Persamaan Karakteristik, Determinan Wronskian, Respon RLC Bebas Sumber (Overdamped, Critically Damped, Underdamped), dan Analisis Ruang Fasa",
    "cpmk": [
        ("C1", "Mengingat", "Menyatakan bentuk umum persamaan karakteristik kuadrat dan Wronskian."),
        ("C2", "Memahami", "Menjelaskan makna fisis interaksi medan magnet (L) dan medan listrik (C)."),
        ("C3", "Menerapkan", "Menurunkan solusi analitik IVP untuk 3 kasus diskriminan (D > 0, = 0, < 0)."),
        ("C4", "Menganalisis", "Menghitung rasio redaman zeta = alpha / omega_0 dan frekuensi teredam omega_d."),
        ("C5", "Mengevaluasi", "Mengklasifikasikan kestabilan trajektori ruang fasa (phase portrait)."),
        ("C6", "Komputasi", "Memprogram simulasi numerik komparatif 3 respon redaman dengan Julia.")
    ],
    "slides": [
        {
            "num": 1,
            "title": "Judul & Pembukaan Kuliah Minggu 04",
            "chapter": "01. Pembukaan Perkuliahan Minggu 04",
            "quiz": False,
            "text": (
                "Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, "
                "selamat datang dalam perkuliahan daring Persamaan Diferensial semester genap 2026. "
                "Pada Minggu keempat ini, topik bahasan kita adalah Persamaan Diferensial Biasa Orde Dua Linier Homogen Koefisien Konstan "
                "dan Tiga Ragam Redaman RLC. Kita akan menurunkan persamaan karakteristik kuadrat, menguji kebebasan linier solusi dengan determinan Wronskian, "
                "serta memodelkan dinamika sirkuit RLC seri dan tangki osilator LC bebas sumber. "
                "Perkuliahan ini diasuh oleh tim pengampu, saya Insinyur Novalio Daratha, Ph.D. bersama Bapak Muhammad Arfan, M.T."
            )
        },
        {
            "num": 2,
            "title": "Capaian Pembelajaran (Sub-CPMK 3) & Taksonomi Bloom",
            "chapter": "02. Sub-CPMK 3 & Taksonomi Bloom",
            "quiz": False,
            "text": (
                "Perhatikan Capaian Pembelajaran Lulusan berbasis OBE pada layar. "
                "Sub-CPMK Minggu keempat menetapkan bahwa mahasiswa mampu memformulasikan dan menyelesaikan PDB linier orde dua homogen koefisien konstan, "
                "membedah tiga ragam redaman transien yaitu overdamped, critically damped, dan underdamped, serta menguji kekekalan energi tangki LC. "
                "Target kognitif berjenjang meliputi: pada C1 Mengingat, menyatakan bentuk umum persamaan karakteristik kuadrat dan Wronskian. "
                "Pada C2 Memahami, menjelaskan makna fisis interaksi medan magnet induktor L dan medan listrik kapasitor C. "
                "Pada C3 Menerapkan, menurunkan solusi analitik masalah nilai awal untuk tiga kasus diskriminan D lebih besar dari nol, sama dengan nol, dan kurang dari nol. "
                "Pada C4 Menganalisis, menghitung rasio redaman zeta sama dengan alpha per omega nol dan frekuensi teredam omega d. "
                "Pada C5 Mengevaluasi, mengklasifikasikan kestabilan trajektori ruang fasa. "
                "Serta pada C6 Komputasi, memprogram simulasi numerik komparatif tiga respon redaman dengan bahasa Julia."
            )
        },
        {
            "num": 3,
            "title": "Peta Konsep: Lompatan dari Orde 1 Menuju Orde 2",
            "chapter": "03. Peta Konsep: Lompatan ke Orde 2",
            "quiz": False,
            "text": (
                "Perhatikan peta konsep perbandingan sistem orde satu menuju orde dua pada salindia ini. "
                "Sistem orde satu yang kita pelajari pada Minggu pertama hingga ketiga hanya memuat satu elemen penyimpan energi, yaitu induktor L atau kapasitor C, "
                "dengan dinamika relaksasi eksponensial monotonik tanpa osilasi yang dicirikan oleh konstanta waktu tunggal tau. "
                "Sebaliknya, sistem orde dua pada Minggu keempat dan kelima memuat dua elemen reaktif independen, yakni L dan C secara simultan. "
                "Hal ini memicu pertukaran energi bolak-balik yang melahirkan fenomena osilasi dan gelombang, dengan parameter kunci frekuensi alami omega nol dan rasio redaman zeta. "
                "Inti fisisnya: energi berpindah secara siklis antara medan magnet setengah L i kuadrat dan medan listrik setengah C v kuadrat, "
                "dengan resistor R bertindak sebagai elemen disipator peredam."
            )
        },
        {
            "num": 4,
            "title": "Bentuk Standar PDB Orde 2 Homogen & Persamaan Karakteristik",
            "chapter": "04. Bentuk Standar & Karakteristik",
            "quiz": False,
            "text": (
                "Pada salindia keempat, kita telaah bentuk baku PDB linier orde dua homogen: "
                "a dikali d kuadrat y per d x kuadrat ditambah b dikali d y per d x ditambah c dikali y sama dengan nol, dengan konstanta a tidak sama dengan nol. "
                "Kita terapkan postulat solusi basis eksponensial: asumsikan solusi berbentuk y x sama dengan e pangkat r dikali x. "
                "Maka turunan pertamanya adalah y aksen x sama dengan r dikali e pangkat r x, dan turunan keduanya y dobel aksen x sama dengan r kuadrat dikali e pangkat r x. "
                "Mensubstitusikan kedua turunan ini menghasilkan persamaan kurung a r kuadrat ditambah b r ditambah c tutup kurung dikalikan e pangkat r x sama dengan nol. "
                "Karena suku eksponensial e pangkat r x tidak pernah bernilai nol, kita peroleh Persamaan Karakteristik kuadrat: a r kuadrat ditambah b r ditambah c sama dengan nol. "
                "Akar-akar kuadratnya dihitung dengan rumus abc: r satu dan r dua sama dengan minus b plus minus akar b kuadrat dikurang empat a c seluruhnya dibagi dua a, "
                "dengan diskriminan D sama dengan b kuadrat dikurang empat a c yang menentukan watak solusi sistem."
            )
        },
        {
            "num": 5,
            "title": "Teorema Superposisi & Determinan Wronskian",
            "chapter": "05. Superposisi & Determinan Wronskian",
            "quiz": False,
            "text": (
                "Salindia kelima memuat dua fondasi analitik penting. "
                "Pertama, Teorema Superposisi Linier pada kolom kiri: jika y satu x dan y dua x adalah dua solusi bebas linier dari persamaan diferensial homogen, "
                "maka kombinasi linier keduanya, yaitu y x sama dengan C satu dikali y satu x ditambah C dua dikali y dua x, merupakan solusi umum yang lengkap. "
                "Kedua, Uji Bebas Linier Wronskian di sebelah kanan: solusi y satu dan y dua saling bebas linier jika determinan Wronskian tidak bernilai nol, "
                "yaitu W kurung y satu koma y dua sama dengan y satu dikali y dua aksen dikurang y satu aksen dikali y dua tidak sama dengan nol. "
                "Sebaliknya, jika determinan Wronskian bernilai nol, maka kedua solusi saling bergantung secara linier sehingga tidak dapat membentuk basis solusi fundamental."
            )
        },
        {
            "num": 6,
            "title": "Pemodelan Fisis: Rangkaian RLC Seri Bebas Sumber",
            "chapter": "06. Pemodelan Sirkuit RLC Seri",
            "quiz": False,
            "text": (
                "Mari kita turunkan pemodelan fisis rangkaian RLC seri tertutup bebas sumber yang tampak pada diagram skematis di sebelah kiri. "
                "Berdasarkan Formulasi Hukum Tegangan Kirchhoff atau KVL pada satu loop tertutup: "
                "tegangan resistor v R ditambah tegangan induktor v L ditambah tegangan kapasitor v C sama dengan nol. "
                "Selanjutnya, nyatakan seluruh variabel dalam muatan kapasitor q t, di mana arus i sama dengan d q per d t dan tegangan kapasitor v C sama dengan q dibagi C. "
                "Kita peroleh persamaan: L dikali d kuadrat q per d t kuadrat ditambah R dikali d q per d t ditambah satu per C dikali q sama dengan nol. "
                "Dengan mendiferensiasikan persamaan muatan ini satu kali terhadap waktu, kita peroleh PDB standar rangkaian RLC seri untuk dinamika arus i t: "
                "d kuadrat i t per d t kuadrat ditambah R per L dikali d i t per d t ditambah satu per L C dikali i t sama dengan nol."
            )
        },
        {
            "num": 7,
            "title": "Parameter Standar Karakteristik RLC",
            "chapter": "07. Parameter Standar Karakteristik RLC",
            "quiz": False,
            "text": (
                "Dalam literatur rekayasa elektro dan teori kontrol, PDB orde dua dinyatakan ke dalam parameter sistem standar pada kolom kiri: "
                "pertama, Frekuensi Sudut Alami omega nol sama dengan satu dibagi akar L C dalam satuan radian per detik. "
                "Kedua, Faktor Redaman Neper alpha sama dengan R dibagi dua L dalam satuan Neper per detik. "
                "Dan ketiga, Rasio Redaman tanpa dimensi zeta sama dengan alpha dibagi omega nol, atau R per dua dikalikan akar C per L. "
                "Di kolom sebelah kanan, persamaan karakteristik rekayasa dituliskan sebagai: s kuadrat ditambah dua alpha dikali s ditambah omega nol kuadrat sama dengan nol, "
                "yang ekuivalen dengan s kuadrat ditambah dua zeta omega nol dikali s ditambah omega nol kuadrat sama dengan nol. "
                "Akar-akarnya adalah s satu dua sama dengan minus alpha plus minus akar alpha kuadrat dikurang omega nol kuadrat. "
                "Nilai relatif alpha terhadap omega nol memunculkan tiga ragam redaman transien."
            )
        },
        {
            "num": 8,
            "title": "Ragam 1: Teredam Lebih (Overdamped, alpha > omega_0 atau zeta > 1)",
            "chapter": "08. Ragam 1: Overdamped",
            "quiz": False,
            "text": (
                "Salindia kedelapan membahas Ragam Pertama, yaitu Teredam Lebih atau Overdamped, yang terjadi saat alpha lebih besar dari omega nol "
                "atau rasio redaman zeta lebih besar dari satu. Karakteristik fisiknya terjadi jika nilai resistansi R lebih besar dari dua kali akar L per C, "
                "di mana resistansi peredam sangat dominan. Diskriminan D bernilai positif, menghasilkan dua akar real negatif yang berbeda: "
                "s satu sama dengan minus alpha ditambah akar alpha kuadrat dikurang omega nol kuadrat, dan s dua sama dengan minus alpha dikurang akar alpha kuadrat dikurang omega nol kuadrat. "
                "Bentuk solusi umumnya adalah arus i t sama dengan C satu dikali e pangkat s satu t ditambah C dua dikali e pangkat s dua t. "
                "Seperti terlihat pada grafik di sebelah kanan, respon arus merupakan peluruhan eksponensial murni yang lambat kembali ke titik nol tanpa pernah berosilasi."
            )
        },
        {
            "num": 9,
            "title": "Ragam 2: Teredam Kritis (Critically Damped, alpha = omega_0 atau zeta = 1)",
            "chapter": "09. Ragam 2: Critically Damped",
            "quiz": False,
            "text": (
                "Salindia kesembilan memaparkan Ragam Kedua, yaitu Teredam Kritis atau Critically Damped, yang terjadi bila alpha persis sama dengan omega nol "
                "atau rasio redaman zeta sama dengan satu. Kondisi ini terjadi tepat saat resistansi bernilai R kritis sama dengan dua kali akar L per C. "
                "Diskriminan bernilai nol sehingga menghasilkan akar kembar real negatif: s satu sama dengan s dua sama dengan minus alpha. "
                "Berdasarkan metode reduksi orde d Alembert, solusi basis kedua dikalikan dengan variabel waktu t, menghasilkan bentuk solusi umum: "
                "arus i t sama dengan kurung C satu ditambah C dua dikali t tutup kurung dikalikan e pangkat minus alpha t. "
                "Keistimewaan rekayasanya adalah respon sistem mencapai kondisi tunak dalam waktu tercepat tanpa mengalami lentingan atau overshoot. "
                "Pada kotak aplikasi kritis di sebelah kanan, karakteristik ini menjadi standar wajib pada peredam kejut mekanik, jarum ukur analog, dan aktuator kontrol servo."
            )
        },
        {
            "num": 10,
            "title": "Ragam 3: Teredam Kurang (Underdamped, alpha < omega_0 atau zeta < 1)",
            "chapter": "10. Ragam 3: Underdamped",
            "quiz": False,
            "text": (
                "Salindia kesepuluh membedah Ragam Ketiga, yaitu Teredam Kurang atau Underdamped, yang terjadi saat alpha lebih kecil dari omega nol "
                "atau rasio redaman zeta kurang dari satu. Hal ini terjadi jika resistansi R lebih kecil dari dua kali akar L per C. "
                "Diskriminan bernilai negatif, melahirkan sepasang akar kompleks konjugat: s satu dua sama dengan minus alpha plus minus j dikali omega d, "
                "dengan Frekuensi Sudut Teredam omega d sama dengan akar omega nol kuadrat dikurang alpha kuadrat, atau omega nol dikali akar satu dikurang zeta kuadrat. "
                "Bentuk solusi umum arusnya adalah i t sama dengan e pangkat minus alpha t dikalikan kurung C satu kosinus omega d t ditambah C dua sinus omega d t. "
                "Grafik di sebelah kanan memperlihatkan kurva gelombang sinusoidal berosilasi yang teredam di dalam selubung batas eksponensial putus-putus menuju nol."
            )
        },
        {
            "num": 11,
            "title": "Kasus Khusus Tangki LC Murni & Analisis Ruang Fasa",
            "chapter": "11. Tangki LC & Ruang Fasa",
            "quiz": False,
            "text": (
                "Salindia kesebelas meninjau kasus khusus tangki LC murni tanpa resistansi, yaitu R sama dengan nol sehingga alpha bernilai nol. "
                "Persamaan diferensial tereduksi menghasilkan tegangan kapasitor v C t sama dengan V m kosinus kurung omega nol t ditambah fasa phi, "
                "dan arus i t sama dengan minus omega nol C V m sinus kurung omega nol t ditambah fasa phi. "
                "Pada kotak merah Hukum Kekekalan Energi Abadi, energi total sistem bernilai konstan sepanjang waktu, yaitu E total sama dengan setengah C v C kuadrat "
                "ditambah setengah L i kuadrat sama dengan setengah C V m kuadrat. "
                "Diagram di sebelah kanan menyajikan tipologi ruang fasa koordinat tegangan kapasitor v C terhadap arus i. "
                "Pada kondisi tanpa disipasi, trajektori membentuk orbit elips tertutup yang berputar abadi di sekitar pusat eliptik center point. "
                "Sebaliknya bila zeta kurang dari satu lintasannya spiral memusar masuk, dan bila zeta lebih dari satu lintasannya meluncur stabil langsung ke titik asal."
            )
        },
        {
            "num": 12,
            "title": "Contoh Soal Terhitung (Worked Example): RLC Seri Industri",
            "chapter": "12. Contoh Soal Terhitung RLC",
            "quiz": False,
            "text": (
                "Mari kita cermati contoh soal terhitung filter industri pada salindia kedua belas. "
                "Diketahui parameter induktor L sama dengan nol koma lima Henry, kapasitor C sama dengan dua puluh mikrofarad, "
                "dengan tegangan awal kapasitor v C nol sama dengan seratus Volt dan arus awal i nol sama dengan nol. "
                "Pada langkah pertama di kolom kiri, kita hitung frekuensi alami omega nol sama dengan satu dibagi akar nol koma lima dikali dua puluh mikrofarad, "
                "diperoleh hasil tiga ratus enam belas koma dua radian per detik, dan resistansi kritis R kritis sama dengan dua kali akar L per C yaitu tiga ratus enam belas koma dua Ohm. "
                "Pada langkah kedua dengan nilai resistor R sama dengan enam puluh Ohm, diperoleh faktor redaman alpha sama dengan enam puluh dibagi dua kali nol koma lima, "
                "yaitu enam puluh Neper per detik, dan frekuensi teredam omega d sama dengan akar tiga ratus enam belas koma dua kuadrat dikurang enam puluh kuadrat, "
                "yaitu tiga ratus sepuluh koma lima radian per detik. "
                "Pada kolom kanan langkah ketiga, kondisi awal menentukan konstanta C satu sama dengan seratus Volt dan C dua sama dengan alpha per omega d dikali C satu "
                "yaitu sembilan belas koma tiga puluh dua Volt, sehingga solusi tegangan kapasitor adalah v C t sama dengan e pangkat minus enam puluh t dikalikan kurung "
                "seratus kosinus tiga ratus sepuluh koma lima t ditambah sembilan belas koma tiga sinus tiga ratus sepuluh koma lima t Volt. "
                "Langkah keempat menghasilkan periode osilasi teredam T d sama dengan dua pi dibagi omega d, yaitu sekitar dua puluh koma dua milidetik."
            )
        },
        {
            "num": 13,
            "title": "Praktikum Komputasi Julia: Tiga Ragam Redaman RLC",
            "chapter": "13. Praktikum Julia: Tiga Ragam Redaman",
            "quiz": False,
            "text": (
                "Salindia ketiga belas menyajikan praktikum komputasi ilmiah menggunakan pustaka DifferentialEquations dot j l dan Plots dot j l pada bahasa Julia. "
                "Pada blok kode di sebelah kiri, kita definisikan fungsi dinamika sirkuit r l c tanda seru dengan parameter zeta dan omega nol, "
                "serta mendefinisikan turunan keadaan du satu sama dengan u dua dan du dua sama dengan minus dua dikali zeta dikali omega nol dikali u dua dikurang omega nol kuadrat dikali u satu. "
                "Dengan kondisi awal u nol sama dengan satu koma nol dan rentang waktu tspan nol hingga nol koma nol lima detik, "
                "kita memanggil solver Tsit5 untuk memecahkan problem underdamped dengan parameter zeta nol koma dua dan omega nol lima ratus radian per detik. "
                "Kotak visualisasi di sebelah kanan menampilkan perbandingan respon ketiga ragam: ragam underdamped berosilasi pada frekuensi omega d, "
                "ragam critically damped paling lekas tunak tanpa overshoot, dan ragam overdamped bergerak lambat akibat redaman resistor yang dominan."
            )
        },
        {
            "num": 14,
            "title": "Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)",
            "chapter": "14. Kuis Interaktif & Evaluasi Bloom",
            "quiz": True,
            "text_part1": (
                "Saatnya menguji pemahaman konsep rekayasa Anda pada salindia keempat belas. "
                "Perhatikan pertanyaan Peer Instruction di sebelah kiri: Mengapa aktuator penutup pemutus tenaga atau PMT gardu induk dan jarum ukur analog "
                "selalu dirancang tepat pada kondisi redaman kritis dengan zeta sama dengan satu? "
                "Pilihan A: Mengurangi konsumsi daya listrik baterai DC. "
                "Pilihan B: Mencapai posisi tunak dalam waktu tersingkat tanpa mengalami lenting atau osilasi overshoot! "
                "Pilihan C: Menghasilkan tegangan transien paling besar. "
                "Pilihan D: Mencegah panas pada kumparan elektromagnet. "
                "Silakan pikirkan jawabannya dalam jeda hening delapan detik berikut."
            ),
            "text_part2": (
                "Waktu habis. Jawaban yang tepat adalah Pilihan B: Mencapai posisi tunak dalam waktu tersingkat tanpa mengalami lenting atau osilasi overshoot! "
                "Jika dirancang underdamped, kontak PMT akan bergetar dan memantul atau contact bounce yang dapat memicu ledakan busur api listrik tegangan tinggi. "
                "Sebaliknya jika dirancang overdamped, kontak akan menutup terlalu lambat sehingga waktu pemutusan gangguan menjadi kritis. "
                "Kondisi redaman kritis zeta sama dengan satu memberikan kecepatan optimal tanpa getaran. "
                "Di kolom kanan, Anda juga ditantang menyelesaikan problem Bloom tingkat tinggi: membuktikan Wronskian tidak nol pada C4, "
                "mengevaluasi rugi radiasi tangki LC pada C5, serta mendesain resistor filter agar frekuensi teredam mencapai tiga ratus empat belas radian per detik pada C6."
            )
        },
        {
            "num": 15,
            "title": "Rangkuman Inti Perkuliahan & Referensi",
            "chapter": "15. Rangkuman Perkuliahan & Penutup",
            "quiz": False,
            "text": (
                "Sebagai penutup perkuliahan Minggu keempat, mari kita simpulkan tiga intisari utama pada salindia kelima belas: "
                "Pertama, sistem orde dua dicirikan oleh interaksi dua elemen reaktif penyimpan energi L dan C dengan persamaan karakteristik kuadrat "
                "s kuadrat ditambah dua alpha s ditambah omega nol kuadrat sama dengan nol. "
                "Kedua, nilai rasio redaman zeta membagi dinamika sistem ke dalam tiga ragam fisis: overdamped saat zeta lebih dari satu, "
                "critically damped saat zeta sama dengan satu, dan underdamped saat zeta kurang dari satu. "
                "Ketiga, pada tangki LC tanpa rugi-rugi R sama dengan nol, energi berosilasi bolak-balik secara kekal abadi membentuk orbit elips tertutup pada bidang ruang fasa. "
                "Referensi utama kita adalah buku Erwin Kreyszig edisi kesepuluh dan William Hayt. "
                "Silakan unduh modul lengkap, worksheet, dan problem set di portal resmi perkuliahan kita ndaratha dot my dot id garis miring persamaan strip diferensial. "
                "Terima kasih atas perhatian rekan-rekan sekalian, sampai jumpa pada perkuliahan Minggu kelima. Wassalamualaikum warahmatullahi wabarakatuh."
            )
        }
    ]
}
