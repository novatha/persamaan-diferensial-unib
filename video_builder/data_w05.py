"""
data_w05.py — Data Narasi 15 Salindia Minggu 05 v2.0
Topik: PDB Orde 2 Non-Homogen, Resonansi Frekuensi, & RLC AC
"""
import os

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA = {
    "week_num": "05",
    "pdf_path": os.path.join(PROJ_DIR, "ch5.pdf"),
    "title": "PDB Orde 2 Non-Homogen: Resonansi Seri & RLC AC",
    "subtitle": "Metode Koefisien Tak Tentu, Aturan Modifikasi t^s, Eksitasi AC Sinusoidal, Pelipatgandaan Tegangan Faktor-Q, Fenomena Beat, dan Resonansi Sub-Sinkron PLN",
    "cpmk": [
        ("C1", "Mengingat", "Menyatakan struktur dekomposisi solusi lengkap y = y_h + y_p pada PDB non-homogen."),
        ("C2", "Memahami", "Menjelaskan asal fisis aturan modifikasi pengali t^s saat frekuensi eksitasi memicu resonansi."),
        ("C3", "Menerapkan", "Menghitung respon partikular eksitasi sinusoidal dan penguatan tegangan reaktif faktor Q."),
        ("C4", "Menganalisis", "Menganalisis pembentukan fenomena denyut layangan atau beat saat frekuensi eksitasi mendekati frekuensi alami."),
        ("C5", "Mengevaluasi", "Mengevaluasi risiko mekanis-elektrik fenomena Resonansi Sub-Sinkron (SSR) pada poros turbin-generator PLN."),
        ("C6", "Komputasi", "Memprogram kurva respon frekuensi dan selektivitas filter RLC menggunakan bahasa Julia.")
    ],
    "slides": [
        {
            "num": 1,
            "title": "Judul & Pembukaan Kuliah Minggu 05",
            "chapter": "01. Pembukaan Perkuliahan Minggu 05",
            "quiz": False,
            "text": (
                "Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, "
                "selamat datang dalam perkuliahan daring Persamaan Diferensial semester genap 2026. "
                "Pada Minggu kelima ini, kita akan mempelajari dinamika sistem dengan gaya penggerak eksternal: "
                "Persamaan Diferensial Biasa Orde Dua Non-Homogen. "
                "Kita akan mendalami Metode Koefisien Tak Tentu, aturan modifikasi resonansi pengali t pangkat s, "
                "pemodelan rangkaian RLC dengan sumber eksitasi AC sinusoidal, fenomena resonansi dan pelipatgandaan tegangan faktor Q, "
                "serta studi kasus industri nyata berupa Resonansi Sub-Sinkron pada jaringan transmisi daya PLN. "
                "Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan."
            )
        },
        {
            "num": 2,
            "title": "Capaian Pembelajaran (Sub-CPMK 3) & Taksonomi Bloom",
            "chapter": "02. Sub-CPMK 3 & Taksonomi Bloom",
            "quiz": False,
            "text": (
                "Berikut adalah Capaian Pembelajaran Sub-CPMK Minggu kelima dalam ranah Bloom. "
                "Pada C1 Mengingat, mahasiswa mampu menyatakan dekomposisi solusi total menjadi penjumlahan solusi homogen dan partikular. "
                "Pada C2 Memahami, mahasiswa mampu menjelaskan secara fisis mengapa timbul resonansi saat frekuensi sumber menyamai frekuensi alami. "
                "Pada C3 Menerapkan, mahasiswa mampu menentukan solusi partikular menggunakan metode koefisien tak tentu. "
                "Pada C4 Menganalisis, mahasiswa mampu membedakan evolusi fasa transien cepat versus respon keadaan mantap permanen. "
                "Pada C5 Mengevaluasi, mahasiswa mampu mengkaji risiko torsi destruktif akibat Resonansi Sub-Sinkron pada generator listrik. "
                "Dan pada C6 Komputasi, mahasiswa mampu membuat kurva respon frekuensi dan faktor kualitas Q dengan Julia."
            )
        },
        {
            "num": 3,
            "title": "Peta Konsep: Struktur Solusi Lengkap Sistem Non-Homogen",
            "chapter": "03. Peta Konsep: Struktur Solusi Lengkap",
            "quiz": False,
            "text": (
                "Perhatikan struktur fundamental solusi sistem non-homogen pada diagram ini. "
                "Solusi umum lengkap y t selalu terdiri dari dua bagian yang terpisah: y h t yaitu Solusi Homogen atau respon alami sistem, "
                "ditambah y p t yaitu Solusi Partikular atau respon paksa akibat pengaruh gaya luar. "
                "Solusi homogen ditentukan oleh akar-akar persamaan karakteristik yang mencerminkan sifat intrinsik redaman sirkuit, "
                "dan pada sistem fisik nyata dengan redaman selalu meluruh menuju nol sebagai respon transien. "
                "Sebaliknya, solusi partikular memiliki bentuk gelombang yang seirama dengan fungsi sumber r t dan bertahan selamanya sebagai respon tunak."
            )
        },
        {
            "num": 4,
            "title": "Metode Koefisien Tak Tentu (Undetermined Coefficients)",
            "chapter": "04. Metode Koefisien Tak Tentu",
            "quiz": False,
            "text": (
                "Metode Koefisien Tak Tentu adalah teknik analitis yang sangat elegan bila ruas kanan r t berupa fungsi polinomial, eksponensial, atau sinusoidal. "
                "Aturan dasarnya menyatakan bahwa bentuk tebakan solusi partikular y p harus mencakup seluruh turunan independen dari r t. "
                "Jika ruas kanan adalah fungsi polinomial orde n, tebaklah polinomial lengkap berderajat n. "
                "Jika ruas kanan adalah eksponensial e pangkat alpha t, tebaklah A dikali e pangkat alpha t. "
                "Dan jika ruas kanan adalah fungsi sinusoidal sinus omega t atau kosinus omega t, tebakan wajib memuat kombinasi keduanya: "
                "A kosinus omega t ditambah B sinus omega t untuk mengantisipasi adanya pergeseran sudut fasa."
            )
        },
        {
            "num": 5,
            "title": "Aturan Modifikasi Resonansi: Pengali t^s",
            "chapter": "05. Aturan Modifikasi Resonansi",
            "quiz": False,
            "text": (
                "Apa yang terjadi jika bentuk tebakan solusi partikular ternyata sudah muncul di dalam himpunan basis solusi homogen y h? "
                "Inilah yang dinamakan Kondisi Resonansi. Jika kita mensubstitusikan tebakan awal ke ruas kiri PDB, hasilnya akan identik menjadi nol "
                "dan kita tidak akan pernah menemukan nilai koefisiennya. "
                "Aturan Modifikasi Resonansi menetapkan: kalikan tebakan awal dengan variabel waktu t pangkat s, di mana s adalah bilangan bulat terkecil "
                "satu atau dua yang memastikan tidak ada suku pada y p yang sama dengan suku pada y h. "
                "Kehadiran faktor pengali t secara fisik merepresentasikan fenomena resonansi di mana amplitudo osilasi tumbuh membesar seiring berjalannya waktu."
            )
        },
        {
            "num": 6,
            "title": "Pemodelan Fisis: Sirkuit RLC Seri Eksitasi AC",
            "chapter": "06. Pemodelan Sirkuit RLC AC",
            "quiz": False,
            "text": (
                "Mari kita tinjau pemodelan rangkaian RLC seri yang dihubungkan ke sumber tegangan sinusoidal AC: v sumber t sama dengan V m kosinus omega t. "
                "Berdasarkan Hukum Tegangan Kirchhoff: L d kuadrat i per d t kuadrat ditambah R d i per d t ditambah satu per C dikali i "
                "sama dengan minus omega V m sinus omega t. "
                "Dalam domain frekuensi, sirkuit ini memiliki impedansi total Z sama dengan R ditambah j kurung omega L dikurang satu per omega C. "
                "Kondisi Resonansi Seri terjadi ketika reaktansi induktif omega L tepat meniadakan reaktansi kapasitif satu per omega C, "
                "sehingga impedansi total rangkaian berada pada titik minimumnya yaitu murni sebesar resistansi R."
            )
        },
        {
            "num": 7,
            "title": "Evolusi Gelombang: Respon Transien vs Keadaan Mantap",
            "chapter": "07. Evolusi Gelombang Transien vs Tunak",
            "quiz": False,
            "text": (
                "Grafik pada slide ini memperlihatkan evolusi gelombang arus dan tegangan saat sakelar AC ditutup. "
                "Pada beberapa siklus awal, gelombang tampak tidak simetris dan memiliki pergeseran offset DC. "
                "Ini adalah superposisi antara respon transien teredam y h yang sedang meluruh dengan respon sinusoidal tunak y p. "
                "Setelah waktu berlalu sekitar lima kali konstanta waktu tau, respon alami telah padam sepenuhnya hingga di bawah satu persen. "
                "Sistem kini memasuki Keadaan Mantap Sinusoidal atau AC steady-state murni, di mana amplitudo dan pergeseran fasa "
                "sepenuhnya sejalan dengan fasor tegangan sumber."
            )
        },
        {
            "num": 8,
            "title": "Resonansi Seri & Pelipatgandaan Tegangan Reaktif Faktor-Q",
            "chapter": "08. Resonansi Seri & Faktor-Q",
            "quiz": False,
            "text": (
                "Pada kondisi resonansi seri, arus yang mengalir mencapai nilai puncak maksimum sebesar I peak sama dengan V m dibagi R. "
                "Perhatikan konsekuensi fisik yang sangat mengejutkan pada tegangan komponen reaktif! "
                "Tegangan pada induktor V L dan tegangan pada kapasitor V C masing-masing bernilai I peak dikalikan reaktansinya. "
                "Kita mendefinisikan Faktor Kualitas RLC sebagai Q sama dengan satu per R dikalikan akar L per C. "
                "Pada rangkaian dengan resistansi kecil, nilai Q dapat mencapai puluhan atau ratusan, sehingga tegangan pada kapasitor dan induktor "
                "dapat melonjak menjadi Q kali lipat lebih tinggi daripada tegangan sumber! "
                "Fenomena pelipatgandaan tegangan ini dapat merusak isolasi transformator bila tidak diantisipasi dengan baik."
            )
        },
        {
            "num": 9,
            "title": "Fenomena Denyut Layangan (Beat Phenomenon, omega approx omega_0)",
            "chapter": "09. Fenomena Beat (Denyut Layangan)",
            "quiz": False,
            "text": (
                "Jika rangkaian memiliki redaman sangat kecil atau tanpa redaman, dan frekuensi eksitasi sumber omega sangat dekat tetapi tidak persis sama "
                "dengan frekuensi alami omega nol, terjadilah fenomena akustik dan elektrik yang disebut Denyut Layangan atau Beat Phenomenon. "
                "Melalui identitas trigonometri pengurangan kosinus, solusi superposisi terurai menjadi perkalian dua gelombang sinusoidal: "
                "gelombang pembawa berfrekuensi tinggi omega nol ditambah omega per dua, yang termodulasi di dalam selubung atau amplop gelombang "
                "berfrekuensi rendah omega nol dikurang omega per dua. "
                "Amplitudo gelombang membengkak dan mengecil secara periodik, menimbulkan denyut energi yang sangat khas."
            )
        },
        {
            "num": 10,
            "title": "Studi Kasus Industri: Resonansi Sub-Sinkron (SSR) PLN",
            "chapter": "10. Studi Kasus Industri: Resonansi SSR PLN",
            "quiz": False,
            "text": (
                "Studi kasus industri yang sangat penting bagi insinyur sistem tenaga adalah Resonansi Sub-Sinkron atau SSR pada saluran transmisi tegangan tinggi PLN. "
                "Untuk meningkatkan kapasitas transfer daya, kapasitor seri sering dipasang pada saluran transmisi panjang. "
                "Namun, kombinasi kapasitor seri dengan induktansi jaringan menciptakan frekuensi resonansi alami sub-sinkron di bawah lima puluh Hertz. "
                "Jika frekuensi elektrik sub-sinkron ini bertepatan dengan salah satu frekuensi resonansi mekanis torsional poros turbin-generator, "
                "terjadi interaksi kopling elektro-mekanis destruktif. Torsi poros turbin berosilasi membesar secara tak terkendali hingga dapat mematahkan poros turbin raksasa dalam hitungan detik!"
            )
        },
        {
            "num": 11,
            "title": "Contoh Soal 1 (Worked Example): Resonansi Tegangan RLC",
            "chapter": "11. Contoh Soal 1: Resonansi Tegangan",
            "quiz": False,
            "text": (
                "Mari kita cermati contoh soal terhitung pertama. Suatu sirkuit RLC seri memiliki R sama dengan dua Ohm, L sama dengan lima puluh mili Henry, "
                "dan C sama dengan dua puluh mikrofarad, dieksitasi oleh sumber tegangan AC seratus Volt puncak. "
                "Langkah satu: frekuensi resonansi sudut omega nol adalah satu dibagi akar L C, yaitu seribu radian per detik. "
                "Langkah dua: faktor kualitas Q sama dengan omega nol dikali L per R, yaitu seribu dikali lima puluh mili Henry dibagi dua, menghasilkan Q sama dengan dua puluh lima. "
                "Langkah tiga: pada kondisi resonansi, arus rangkaian adalah seratus dibagi dua yaitu lima puluh Ampere. "
                "Tegangan puncak pada kapasitor melonjak mencapai Q dikalikan tegangan sumber, yaitu dua puluh lima dikali seratus sama dengan dua ribu lima ratus Volt! "
                "Terjadi lonjakan tegangan dua puluh lima kali lipat yang membutuhkan isolasi berdaya tahan tinggi."
            )
        },
        {
            "num": 12,
            "title": "Contoh Soal 2 (Worked Example): Denyut Layangan SSR",
            "chapter": "12. Contoh Soal 2: Beat SSR",
            "quiz": False,
            "text": (
                "Pada contoh soal kedua, kita analisis fenomena beat sub-sinkron. Sebuah tangki LC ideal memiliki frekuensi alami tiga puluh Hertz, "
                "dan dieksitasi oleh sumber gangguan harmonika berfrekuensi tiga puluh dua Hertz dengan amplitudo tegangan sepuluh Volt. "
                "Selisih frekuensi delta omega adalah dua Hertz atau empat pi radian per detik. "
                "Frekuensi selubung amplop beat adalah setengah delta omega, yaitu satu Hertz. "
                "Hal ini berarti periode denyut layangan adalah satu detik, di mana arus berosilasi memuncak setiap satu detik sekali. "
                "Amplitudo maksimum arus melonjak hingga enam kali lipat dari arus normal, mengonfirmasi bahaya getaran siklik pada peralatan listrik."
            )
        },
        {
            "num": 13,
            "title": "Praktikum Komputasi Julia: Resonansi RLC & Selektivitas",
            "chapter": "13. Praktikum Julia: Resonansi & Selektivitas",
            "quiz": False,
            "text": (
                "Pada praktikum komputasi Julia ini, kita membuat simulasi sapuan frekuensi atau frequency sweep untuk memetakan kurva selektivitas resonansi RLC. "
                "Menggunakan solver Tsit5, kita hitung respon steady-state untuk berbagai variasi rasio redaman zeta dari nol koma satu hingga satu koma nol. "
                "Kurva grafik sebelah kanan dengan jelas memperlihatkan kurva puncak resonansi yang tajam pada zeta rendah bernilai nol koma satu, "
                "yang menunjukkan selektivitas frekuensi tinggi dengan faktor Q besar. Sebaliknya, kurva pada zeta tinggi tampak datar dan tumpul. "
                "Skrip Julia ini memungkinkan Anda merancang filter pita frekuensi atau bandpass filter audio dan komunikasi secara interaktif."
            )
        },
        {
            "num": 14,
            "title": "Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)",
            "chapter": "14. Kuis Interaktif & Evaluasi Bloom",
            "quiz": True,
            "text_part1": (
                "Saatnya kuis interaktif untuk menguji intuisi fisika Anda. Perhatikan studi kasus pada layar: "
                "Rangkaian RLC seri AC mengalami resonansi seri dengan faktor kualitas Q sama dengan sepuluh. "
                "Voltmeter mengukur tegangan kapasitor V C sebesar seribu Volt, padahal tegangan sumber V s hanya seratus Volt. "
                "Apakah fenomena pelipatgandaan tegangan ini melanggar hukum kekekalan energi? "
                "Pilihan A: Ya, tegangan pada komponen rangkaian tidak boleh melebihi tegangan sumber. "
                "Pilihan B: Tidak, karena tegangan kapasitor V C dan induktor V L berbeda fasa seratus delapan puluh derajat sehingga saling meniadakan secara vektor total! "
                "Pilihan C: Ya, terjadi pembangkitan daya aktif tambahan secara spontan di dalam kapasitor. "
                "Pilihan D: Tidak, asalkan frekuensi sumber berada di atas satu kilo Hertz. "
                "Silakan analisis konsep energi resonansi ini dan tentukan pilihan terbaik Anda dalam delapan detik ke depan."
            ),
            "text_part2": (
                "Waktu habis. Jawaban yang tepat adalah B: Tidak melanggar hukum kekekalan energi! "
                "Pada kondisi resonansi seri, tegangan kapasitor dan induktor memiliki magnitudo sama besar namun berlawanan fasa tepat seratus delapan puluh derajat. "
                "Penjumlahan fasor keduanya bernilai nol, sehingga tegangan sumber seratus Volt sepenuhnya jatuh pada resistor. "
                "Tegangan seribu Volt adalah energi medan reaktif bolak-balik yang terperangkap di antara L dan C. "
                "Pada kolom tantangan sebelah kanan, Anda juga ditantang menganalisis risiko Sub-Synchronous Resonance atau SSR pada turbin generator di level C4, "
                "mengevaluasi lebar pita frekuensi minus tiga desibel pada level C5, serta merancang filter pasif RLC frekuensi dua ratus lima puluh Hertz pada level C6."
            )
        },
        {
            "num": 15,
            "title": "Rangkuman Inti Perkuliahan & Referensi",
            "chapter": "15. Rangkuman Perkuliahan & Penutup",
            "quiz": False,
            "text": (
                "Sebagai rangkuman perkuliahan minggu kelima: Pertama, solusi PDB non-homogen merupakan penjumlahan respon transien alami "
                "dan respon tunak paksa. Kedua, aturan modifikasi pengali t pangkat s wajib diterapkan bila frekuensi eksitasi memicu resonansi. "
                "Ketiga, resonansi seri RLC melipatgandakan tegangan reaktif hingga Q kali lipat dari tegangan sumber. "
                "Dan keempat, pemahaman resonansi sub-sinkron sangat penting untuk menjamin keselamatan mekanis turbin PLN. "
                "Silakan pelajari modul ajar dan tuntaskan Lembar Kerja serta Problem Set Minggu kelima di portal ndaratha dot my dot id. "
                "Pada minggu keenam, kita akan beralih ke Transformasi Laplace domain frekuensi kompleks s. Terima kasih dan wassalamualaikum warahmatullahi wabarakatuh."
            )
        }
    ]
}
