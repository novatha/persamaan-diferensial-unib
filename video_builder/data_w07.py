"""
data_w07.py — Data Narasi 15 Salindia Minggu 07 v2.0
Topik: Invers Transformasi Laplace & Analisis Rangkaian Domain-s
"""
import os

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA = {
    "week_num": "07",
    "pdf_path": os.path.join(PROJ_DIR, "ch7.pdf"),
    "title": "Invers Transformasi Laplace & Analisis Sirkuit Domain-s",
    "subtitle": "Metode Pecahan Parsial (Kutub Real, Berulang, Kompleks), Teorema Konvolusi, Teorema Nilai Awal/Akhir (IVT/FVT), Pemisahan Respon ZIR/ZSR, dan Transient Recovery Voltage (TRV) Pemutus Daya IEC 62271-100",
    "cpmk": [
        ("C1", "Mengingat", "Menyatakan definisi integral invers Bromwich dan teknik dekomposisi pecahan parsial."),
        ("C2", "Memahami", "Menjelaskan makna fisis kutub pada bidang kompleks s dan hubungannya dengan kestabilan respon waktu."),
        ("C3", "Menerapkan", "Menghitung invers Laplace menggunakan metode penutupan Heaviside, derivasi kutub berulang, dan melengkapkan kuadrat."),
        ("C4", "Menganalisis", "Menguraikan respon total rangkaian menjadi komponen Zero-Input Response (ZIR) dan Zero-State Response (ZSR)."),
        ("C5", "Mengevaluasi", "Mengevaluasi laju kenaikan tegangan Transient Recovery Voltage (TRV) pada pemutus tenaga gardu induk IEC 62271-100."),
        ("C6", "Komputasi", "Memprogram simulasi numerik kurva TRV dan invers transformasi Laplace menggunakan bahasa Julia.")
    ],
    "slides": [
        {
            "num": 1,
            "title": "Judul & Pembukaan Kuliah Minggu 07",
            "chapter": "01. Pembukaan Perkuliahan Minggu 07",
            "quiz": False,
            "text": (
                "Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, "
                "selamat datang kembali dalam perkuliahan daring Persamaan Diferensial semester genap 2026. "
                "Pada Minggu ketujuh ini, kita menyempurnakan siklus transformasi operasional kita: "
                "Invers Transformasi Laplace dan Analisis Rangkaian Listrik Langsung pada Domain Frekuensi Kompleks s. "
                "Kita akan membedah tiga metodologi ekspansi pecahan parsial untuk kutub real, kutub berulang, dan kutub kompleks, "
                "teorema integral konvolusi, teorema nilai awal dan akhir, pemisahan respon masukan-nol ZIR dan keadaan-nol ZSR, "
                "serta studi kasus industri pemutus daya gardu induk berupa Transient Recovery Voltage berbasis standar IEC 62271-100. "
                "Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan."
            )
        },
        {
            "num": 2,
            "title": "Capaian Pembelajaran (Sub-CPMK 4) & Taksonomi Bloom",
            "chapter": "02. Sub-CPMK 4 & Taksonomi Bloom",
            "quiz": False,
            "text": (
                "Mari kita cermati Capaian Pembelajaran Sub-CPMK Minggu ketujuh dalam Taksonomi Bloom. "
                "Pada C1 Mengingat, mahasiswa mampu menyatakan definisi invers Laplace dan prinsip dasar ekspansi pecahan parsial. "
                "Pada C2 Memahami, mahasiswa mampu mengaitkan posisi kutub di bidang kompleks s terhadap perilaku peluruhan atau osilasi waktu. "
                "Pada C3 Menerapkan, mahasiswa mampu menurunkan invers Laplace analitis dengan metode penutupan Heaviside. "
                "Pada C4 Menganalisis, mahasiswa mampu memisahkan respon total sirkuit menjadi respon akibat energi awal ZIR dan respon eksitasi ZSR. "
                "Pada C5 Mengevaluasi, mahasiswa mampu mengkaji risiko penyalaan kembali busur api akibat tegangan transien TRV pada circuit breaker. "
                "Dan pada C6 Komputasi, mahasiswa mampu menyimulasikan kurva transien TRV dengan bahasa Julia."
            )
        },
        {
            "num": 3,
            "title": "Peta Konsep: Metodologi Invers Transformasi Laplace",
            "chapter": "03. Peta Konsep: Metodologi Invers Laplace",
            "quiz": False,
            "text": (
                "Diagram alir pada slide ini merangkum peta jalan komputasi invers transformasi Laplace. "
                "Fungsi rasional di domain frekuensi Y s sama dengan N s dibagi D s pertama-tama dipastikan merupakan pecahan sejati di mana derajat pembilang lebih kecil dari penyebut. "
                "Langkah selanjutnya adalah memfaktorkan polinomial penyebut D s untuk menemukan lokasi kutub-kutubnya. "
                "Jika kutub berupa bilangan real sederhana, kita gunakan Metode Penutupan Heaviside yang sangat cepat. "
                "Jika terdapat kutub real berulang berorde m, kita terapkan aturan derivasi bertingkat. "
                "Dan jika terdapat pasangan kutub kompleks konjugat, kita gunakan teknik melengkapkan kuadrat untuk mencocokkan dengan bentuk baku sinusoidal teredam."
            )
        },
        {
            "num": 4,
            "title": "Metode 1: Kutub Real Sederhana (Metode Penutupan Heaviside)",
            "chapter": "04. Metode 1: Kutub Real Sederhana",
            "quiz": False,
            "text": (
                "Metode pertama adalah penanganan kutub real sederhana atau tidak berulang. "
                "Pecahan rasional Y s didekomposisi menjadi penjumlahan pecahan tunggal: A satu dibagi s dikurang p satu, ditambah A dua dibagi s dikurang p dua, dan seterusnya. "
                "Koefisien residu A k dapat dihitung secara instan menggunakan Metode Penutupan Heaviside: "
                "kalikan Y s dengan faktor kurung s dikurang p k untuk meniadakan penyebut nol, lalu evaluasi hasilnya pada nilai s sama dengan p k. "
                "Setelah seluruh koefisien residu ditemukan, invers Laplace dilakukan suku demi suku menggunakan pasangan baku eksponensial: "
                "y t sama dengan jumlah A k dikalikan e pangkat p k dikali t."
            )
        },
        {
            "num": 5,
            "title": "Metode 2: Kutub Real Berulang (Metode Derivasi Bertingkat)",
            "chapter": "05. Metode 2: Kutub Real Berulang",
            "quiz": False,
            "text": (
                "Bila polinomial penyebut memuat faktor berulang kurung s dikurang p dipangkatkan m, "
                "ekspansi pecahan parsial wajib memuat seluruh deret pangkat dari satu hingga m: "
                "B satu dibagi s dikurang p ditambah B dua dibagi kurung s dikurang p kuadrat hingga B m dibagi kurung s dikurang p pangkat m. "
                "Koefisien pada pangkat tertinggi B m dapat diperoleh langsung dengan metode penutupan Heaviside. "
                "Namun koefisien pangkat yang lebih rendah dihitung menggunakan rumus diferensiasi bertingkat: "
                "satu per faktorial dikalikan turunan ke-k terhadap s dari fungsi yang telah ditutup. "
                "Invers domain waktu dari suku berderajat k akan menghasilkan perkalian variabel waktu t pangkat k minus satu dengan fungsi eksponensial."
            )
        },
        {
            "num": 6,
            "title": "Metode 3: Kutub Kompleks Konjugat (Melengkapkan Kuadrat)",
            "chapter": "06. Metode 3: Kutub Kompleks Konjugat",
            "quiz": False,
            "text": (
                "Untuk penyebut kuadratik yang tidak dapat difaktorkan secara real dan menghasilkan kutub kompleks konjugat s sama dengan minus alpha plus minus j omega, "
                "teknik yang paling efisien adalah Melengkapkan Kuadrat pada penyebut menjadi kurung s ditambah alpha kuadrat ditambah omega kuadrat. "
                "Selanjutnya, pembilang diatur secara aljabar agar sesuai dengan kombinasi bentuk baku kosinus teredam dan sinus teredam: "
                "A dikalikan kurung s ditambah alpha ditambah B dikalikan omega. "
                "Invers langsung menghasilkan respon gelombang berosilasi teredam: e pangkat minus alpha t dikalikan kurung A kosinus omega t ditambah B sinus omega t. "
                "Teknik ini menghindari manipulasi aljabar bilangan imajiner yang rentan kesalahan."
            )
        },
        {
            "num": 7,
            "title": "Teorema Konvolusi Domain Waktu",
            "chapter": "07. Teorema Konvolusi Waktu",
            "quiz": False,
            "text": (
                "Teorema Konvolusi adalah salah satu teorema paling elegan dalam analisis sistem linier: "
                "perkalian dua fungsi di domain frekuensi F s dikalikan G s berkorespondensi dengan integral konvolusi f t konvolusi g t di domain waktu. "
                "Integral konvolusi didefinisikan sebagai integral dari nol hingga t dari f tau dikalikan g kurung t dikurang tau d tau. "
                "Secara fisis, respon keluaran sistem terhadap sebarang sinyal masukan masukan x t sama dengan konvolusi sinyal tersebut dengan Respon Impuls h t sistem. "
                "Teorema ini memungkinkan insinyur menghitung respon sistem linier terhadap masukan sebarang tanpa harus menyelesaikan kembali persamaan diferensialnya dari awal."
            )
        },
        {
            "num": 8,
            "title": "Teorema Nilai Awal (IVT) & Teorema Nilai Akhir (FVT)",
            "chapter": "08. Teorema Nilai Awal & Nilai Akhir",
            "quiz": False,
            "text": (
                "Dua teorema batas operasional yang sangat bermanfaat untuk memverifikasi perhitungan tanpa perlu melakukan invers penuh adalah IVT dan FVT. "
                "Teorema Nilai Awal atau Initial Value Theorem menyatakan bahwa nilai f pada t nol positif sama dengan limit s mendekati tak hingga dari s dikalikan F s. "
                "Sebaliknya, Teorema Nilai Akhir atau Final Value Theorem menyatakan bahwa nilai tunak f saat t menuju tak hingga sama dengan limit s mendekati nol dari s dikalikan F s, "
                "dengan syarat mutlak bahwa seluruh kutub dari s F s harus terletak di sebelah kiri sumbu imajiner bidang s. "
                "Kedua teorema ini memungkinkan kita menginspeksi nilai awal sesaat dan nilai tunak akhir rangkaian secara instan langsung dari fungsi transfer domain s."
            )
        },
        {
            "num": 9,
            "title": "Model Komponen Rangkaian di Domain-s dengan Energi Awal",
            "chapter": "09. Model Rangkaian Domain-s",
            "quiz": False,
            "text": (
                "Daripada menyusun PDB di domain waktu lalu mentransformasikannya, teknik rekayasa modern mentransformasikan komponen rangkaian secara langsung ke domain s. "
                "Resistor tetap menjadi impedansi R. "
                "Induktor dengan arus awal i nol dimodelkan sebagai impedansi s L yang terhubung seri dengan sumber tegangan impuls L dikali i nol, atau paralel dengan sumber arus i nol per s. "
                "Kapasitor dengan tegangan awal v nol dimodelkan sebagai impedansi satu per s C seri dengan sumber tegangan v nol per s. "
                "Dengan model ekivalen ini, seluruh hukum Kirchhoff KVL, KCL, analisis mesh, dan teorema Thevenin dapat diterapkan secara murni menggunakan aljabar fasor domain s."
            )
        },
        {
            "num": 10,
            "title": "Pemisahan Solusi: Respon Masukan-Nol (ZIR) & Keadaan-Nol (ZSR)",
            "chapter": "10. Pemisahan Respon ZIR dan ZSR",
            "quiz": False,
            "text": (
                "Berdasarkan sifat linieritas, respon total sistem rangkaian selalu dapat diuraikan menjadi dua komponen independen: "
                "Zero-Input Response atau ZIR, yaitu respon rangkaian yang timbul murni akibat energi awal yang tersimpan pada induktor dan kapasitor tanpa adanya sumber luar. "
                "Dan Zero-State Response atau ZSR, yaitu respon rangkaian yang timbul murni akibat gaya gerak sumber eksitasi luar dengan asumsi seluruh kondisi awal bernilai nol. "
                "Dekomposisi ZIR dan ZSR ini mempermudah insinyur kendali dan proteksi dalam mengisolasi efek gangguan transien awal dari respon kendali mantap."
            )
        },
        {
            "num": 11,
            "title": "Studi Kasus Industri: Transient Recovery Voltage (IEC 62271-100)",
            "chapter": "11. Transient Recovery Voltage IEC 62271-100",
            "quiz": False,
            "text": (
                "Studi kasus industri tegangan tinggi yang sangat kritis adalah Transient Recovery Voltage atau TRV pada pemutus tenaga atau circuit breaker gardu induk PLN. "
                "Ketika circuit breaker memutus arus hubung singkat pada saat arus melewati titik nol, induktansi transformator dan kapasitansi liar busbar "
                "membentuk rangkaian RLC transien berfrekuensi tinggi. "
                "Tegangan melintasi kontak sakelar melonjak tajam dengan frekuensi puluhan kilo Hertz mengikuti standar IEC 62271-100. "
                "Laju kenaikan tegangan transien RRRV yang terlalu curam dapat merusak kekuatan dielektrik gas SF6 pada ruang kontak, "
                "memicu penyalaan busur api kembali atau restrike yang dapat menghancurkan pemutus tenaga secara katastropik."
            )
        },
        {
            "num": 12,
            "title": "Contoh Soal Terhitung (Worked Example): Inversi Kutub Ganda",
            "chapter": "12. Contoh Soal Inversi Kutub Ganda",
            "quiz": False,
            "text": (
                "Mari kita cermati contoh soal terhitung inversi Laplace dengan kutub ganda. "
                "Diberikan fungsi aljabar Y s sama dengan lima s ditambah enam dibagi kurung s ditambah dua kuadrat dikali kurung s ditambah satu. "
                "Langkah satu: susun ekspansi pecahan parsial: A per s tambah satu ditambah B satu per s tambah dua ditambah B dua per s tambah dua kuadrat. "
                "Langkah dua: hitung A dengan menutup s tambah satu, diperoleh minus lima tambah enam dibagi satu kuadrat sama dengan satu. "
                "Langkah tiga: hitung B dua dengan menutup s tambah dua kuadrat, diperoleh minus sepuluh tambah enam dibagi minus satu sama dengan empat. "
                "Langkah empat: hitung B satu melalui turunan pertama, menghasilkan minus satu. "
                "Solusi waktu akhir adalah y t sama dengan e pangkat minus t dikurang e pangkat minus dua t ditambah empat t dikali e pangkat minus dua t."
            )
        },
        {
            "num": 13,
            "title": "Praktikum Komputasi Julia: Transient Recovery Voltage",
            "chapter": "13. Praktikum Julia: Simulasi TRV",
            "quiz": False,
            "text": (
                "Pada praktikum komputasi Julia ini, kita memprogram simulasi numerik tegangan transien pemulihan kontak pemutus daya gardu induk. "
                "Dengan parameter gardu induk lima ratus kilo Volt, induktansi setara L sama dengan sepuluh mili Henry dan kapasitansi liar C sama dengan lima puluh nano Farad, "
                "kita selesaikan respon transien sirkuit menggunakan paket DifferentialEquations dot j l solver Tsit5. "
                "Kurva grafik memperlihatkan lonjakan osilasi TRV berfrekuensi tinggi tujuh koma satu kilo Hertz yang mencapai puncak tegangan puncak satu koma delapan kali tegangan sistem normal. "
                "Simulasi Julia ini membantu insinyur transmisi merancang resistor pembatas dan kapasitor penyerap surja pada gardu induk."
            )
        },
        {
            "num": 14,
            "title": "Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)",
            "chapter": "14. Kuis Interaktif & Evaluasi Bloom",
            "quiz": True,
            "text_part1": (
                "Saatnya kuis interaktif untuk menguji intuisi rekayasa Anda. Perhatikan studi kasus pada layar: "
                "Mengapa momen paling berbahaya pada pemutusan arus hubung singkat oleh pemutus tenaga atau PMT gardu induk justru terjadi beberapa mikrodetik setelah kontak pemutus terbuka dan busur api padam? "
                "Pilihan A: Arus listrik membalik arah kembali menuju generator pembangkit. "
                "Pilihan B: Laju kenaikan tegangan pemulihan transien atau Transient Recovery Voltage d v per d t sangat curam; jika melampaui kekuatan dielektrik celah gas SF6, akan terjadi re-strike atau busur api menyala ulang! "
                "Pilihan C: Transformator arus atau CT meledak akibat saturasi magnetik inti. "
                "Pilihan D: Energi listrik pada jaringan musnah secara seketika. "
                "Silakan analisis dinamika transien ini dan tentukan pilihan jawaban terbaik Anda dalam delapan detik ke depan."
            ),
            "text_part2": (
                "Waktu habis. Jawaban yang tepat adalah B: Laju kenaikan tegangan pemulihan transien TRV sangat curam memicu re-strike busur api! "
                "Setelah arus diputus pada titik nol, sistem tenaga membangkitkan tegangan osilasi frekuensi tinggi transien TRV di antara celah kontak. "
                "Jika laju kenaikan tegangan melampaui kecepatan gas SF6 dalam memulihkan kekuatan dielektriknya, busur api menyala kembali dan dapat meledakkan ruang kontak pemutus. "
                "Pada kolom tantangan sebelah kanan, Anda juga ditantang menguraikan respon menjadi komponen Zero Input Response dan Zero State Response di level C4, "
                "mengevaluasi kestabilan kutub bidang-s di level C5, serta merancang kapasitor paralel peredam TRV gardu induk seratus lima puluh kilo Volt di level C6."
            )
        },
        {
            "num": 15,
            "title": "Rangkuman Inti Perkuliahan & Referensi",
            "chapter": "15. Rangkuman Perkuliahan & Penutup",
            "quiz": False,
            "text": (
                "Sebagai rangkuman perkuliahan minggu ketujuh: Pertama, invers Transformasi Laplace dilakukan melalui dekomposisi pecahan parsial yang sistematis. "
                "Kedua, posisi kutub pada bidang kompleks s mencerminkan secara langsung sifat kestabilan dan osilasi respon waktu. "
                "Ketiga, pemodelan komponen di domain s menyederhanakan analisis transien menjadi aljabar impedansi biasa dengan energi awal. "
                "Dan keempat, pemahaman TRV sangat krusial dalam perancangan sistem isolasi pemutus daya gardu induk. "
                "Silakan pelajari modul ajar dan tuntaskan Lembar Kerja serta Problem Set Minggu ketujuh di portal ndaratha dot my dot id sebelum menghadapi UTS pada minggu depan. "
                "Saya, Insinyur Novalio Daratha bersama Bapak Muhammad Arfan, mengucapkan selamat belajar dan sukses selalu. Wassalamu'alaikum warahmatullahi wabarakatuh."
            )
        }
    ]
}
