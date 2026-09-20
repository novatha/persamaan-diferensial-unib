"""
data_w10.py — Data Narasi 15 Salindia Minggu 10 v2.0
Topik: Metode Pemisahan Variabel (Separation of Variables) & Nilai Batas BVP
"""
import os

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA = {
    "week_num": "10",
    "pdf_path": os.path.join(PROJ_DIR, "ch10.pdf"),
    "title": "Pemisahan Variabel: Nilai Batas BVP & Difusi Busbar GITET",
    "subtitle": "Metode Pemisahan Variabel (Separation of Variables), Postulat Produk Fungsi, Masalah Nilai Eigen Sturm-Liouville, Syarat Batas Dirichlet/Neumann, Rekonstruksi Deret Fourier, dan Termal Busbar GITET 500 kV",
    "cpmk": [
        ("C1", "Mengingat", "Menyatakan postulat pemisahan variabel u(x,t) = X(x) T(t) dan syarat keterpisahan PDP."),
        ("C2", "Memahami", "Menjelaskan secara fisis mengapa konstanta pemisahan wajib bernilai negatif -lambda^2 untuk menjamin stabilitas."),
        ("C3", "Menerapkan", "Menurunkan fungsi eigen spasial dan nilai eigen dari Masalah Nilai Batas Sturm-Liouville."),
        ("C4", "Menganalisis", "Membandingkan dinamika peluruhan termal antara syarat batas Dirichlet (suhu tetap) dan Neumann (isolasi adiabatik)."),
        ("C5", "Mengevaluasi", "Mengevaluasi kapasitas batas termal konduktor busbar gardu induk GITET 500 kV saat memikul arus hubung singkat."),
        ("C6", "Komputasi", "Memprogram simulasi difusi spasial-temporal 1D pada busbar tembaga menggunakan bahasa Julia.")
    ],
    "slides": [
        {
            "num": 1,
            "title": "Judul & Pembukaan Kuliah Minggu 10",
            "chapter": "01. Pembukaan Perkuliahan Minggu 10",
            "quiz": False,
            "text": (
                "Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, "
                "selamat datang dalam perkuliahan daring Persamaan Diferensial semester genap 2026. "
                "Pada Minggu kesepuluh ini, kita membedah metode analitik paling fundamental dan elegan untuk menyelesaikan Persamaan Diferensial Parsial: "
                "Metode Pemisahan Variabel atau Separation of Variables. "
                "Kita akan mempelajari postulat perkalian fungsi atau product ansatz, pemilihan tanda konstanta pemisahan berdasarkan hukum fisika, "
                "masalah nilai eigen spasial Sturm-Liouville, penanganan syarat batas Dirichlet dan Neumann, "
                "serta penerapan pada manajemen termal konduktor busbar gardu induk ekstra tinggi GITET lima ratus kilo Volt. "
                "Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan."
            )
        },
        {
            "num": 2,
            "title": "Sub-CPMK Taksonomi Bloom (Minggu 10)",
            "chapter": "02. Sub-CPMK 10 & Taksonomi Bloom",
            "quiz": False,
            "text": (
                "Berikut adalah Capaian Pembelajaran Sub-CPMK Minggu kesepuluh berbasis Taksonomi Bloom. "
                "Pada C1 Mengingat, mahasiswa mampu menyatakan postulat pemisahan u x t sama dengan X x dikali T t. "
                "Pada C2 Memahami, mahasiswa mampu menjelaskan justifikasi fisis mengapa konstanta pemisahan k harus bernilai negatif minus lambda kuadrat. "
                "Pada C3 Menerapkan, mahasiswa mampu menurunkan nilai eigen dan fungsi eigen untuk batas Dirichlet dan Neumann. "
                "Pada C4 Menganalisis, mahasiswa mampu menguraikan distribusi suhu multi-mode menggunakan koefisien deret Fourier. "
                "Pada C5 Mengevaluasi, mahasiswa mampu mengkaji pemanasan adiabatik konduktor busbar gardu induk GITET saat gangguan arus besar. "
                "Dan pada C6 Komputasi, mahasiswa mampu menyimulasikan evolusi suhu spasial-temporal menggunakan bahasa Julia."
            )
        },
        {
            "num": 3,
            "title": "Peta Kurikulum: Jembatan PDP Menuju PDB Independen",
            "chapter": "03. Peta Kurikulum: Jembatan PDP ke PDB",
            "quiz": False,
            "text": (
                "Perhatikan filosofi inti metode pemisahan variabel pada diagram ini. "
                "Persamaan Diferensial Parsial tampak sangat menakutkan karena memuat turunan terhadap ruang spasial x dan waktu t secara simultan. "
                "Metode Pemisahan Variabel adalah jembatan brilian yang mereduksi satu PDP multi-variabel menjadi dua PDB biasa berorde satu dan dua yang saling independen. "
                "PDB spasial diselesaikan menggunakan konsep Masalah Nilai Batas untuk menghasilkan fungsi eigen, "
                "sedangkan PDB temporal menghasilkan peluruhan eksponensial. "
                "Kedua solusi ini kemudian disatukan kembali melalui Prinsip Superposisi Linier Deret Fourier untuk memenuhi kondisi awal sistem."
            )
        },
        {
            "num": 4,
            "title": "Postulat Produk Fungsi (Product Ansatz) & Reduksi PDP",
            "chapter": "04. Postulat Produk Fungsi",
            "quiz": False,
            "text": (
                "Mari kita pelajari prosedur reduksi matematisnya. "
                "Tinjau Persamaan Panas satu dimensi: parsial u per parsial t sama dengan alfa dikali parsial kuadrat u per parsial x kuadrat. "
                "Kita ajukan postulat bahwa solusi dapat dinyatakan sebagai perkalian murni: u x koma t sama dengan X x dikalikan T t. "
                "Substitusikan ke dalam PDP: X dikalikan T prima sama dengan alfa dikali X dobel prima dikalikan T. "
                "Bagi kedua ruas dengan alfa dikalikan X dikalikan T: kita peroleh T prima per alfa T sama dengan X dobel prima per X. "
                "Perhatikan: ruas kiri murni fungsi waktu t, sedangkan ruas kanan murni fungsi spasial x. "
                "Dua fungsi dengan variabel independen yang berbeda hanya dapat sama di setiap saat dan titik jika keduanya bernilai sama dengan suatu Konstanta Pemisahan k yang tetap."
            )
        },
        {
            "num": 5,
            "title": "Pemilihan Tanda Konstanta Pemisahan: Justifikasi Fisika",
            "chapter": "05. Pemilihan Tanda Konstanta Pemisahan",
            "quiz": False,
            "text": (
                "Kini kita masuki Pilar pertama, yaitu intuisi fisika dalam menentukan tanda konstanta k. Ada tiga kemungkinan: "
                "Jika k positif bernilai plus lambda kuadrat, solusi waktu adalah T t sama dengan e pangkat plus alfa lambda kuadrat t. "
                "Suhu sistem akan melonjak ke tak hingga saat t membesar, yang secara termodinamika melanggar hukum kekekalan energi! "
                "Jika k sama dengan nol, solusi spasial menjadi garis lurus statis yang tidak mampu membentuk profil gelombang. "
                "Satu-satunya pilihan yang memenuhi hukum fisika adalah k negatif: k sama dengan minus lambda kuadrat. "
                "Nilai k negatif menghasilkan osilasi harmonik spasial pada X x, dan peluruhan eksponensial stabil pada waktu T t."
            )
        },
        {
            "num": 6,
            "title": "Klasifikasi Fisis Syarat Batas (Boundary Conditions)",
            "chapter": "06. Klasifikasi Syarat Batas",
            "quiz": False,
            "text": (
                "Dalam rekayasa sistem tenaga, syarat batas spasial diklasifikasikan ke dalam tiga jenis fisik utama: "
                "Pertama, Syarat Batas Dirichlet: nilai variabel pada ujung batas ditetapkan konstan, misalnya ujung konduktor didinginkan pada suhu tetap nol derajat: u pada nol koma t sama dengan nol. "
                "Kedua, Syarat Batas Neumann: laju aliran gradien fluks pada ujung batas ditetapkan, misalnya ujung konduktor terisolasi sempurna secara adiabatik: parsial u per parsial x pada ujung sama dengan nol. "
                "Ketiga, Syarat Batas Campuran atau Robin: mengombinasikan nilai variabel dan fluks, memodelkan pendinginan konveksi udara bebas Newton. "
                "Jenis syarat batas menentukan bentuk fungsi eigen spasial yang dihasilkan."
            )
        },
        {
            "num": 7,
            "title": "Masalah Nilai Eigen Spasial Sturm-Liouville",
            "chapter": "07. Nilai Eigen Sturm-Liouville",
            "quiz": False,
            "text": (
                "Persamaan spasial X dobel prima ditambah lambda kuadrat X sama dengan nol bersama dengan syarat batas Dirichlet pada x sama dengan nol dan x sama dengan L "
                "membentuk Masalah Nilai Batas Sturm-Liouville klasik. "
                "Solusi umum spasial adalah X x sama dengan A kosinus lambda x ditambah B sinus lambda x. "
                "Syarat batas pada x sama dengan nol memaksa A bernilai nol. "
                "Syarat batas pada x sama dengan L menghasilkan persamaan: B sinus lambda L sama dengan nol. "
                "Agar diperoleh solusi non-trivial B tidak nol, argumen sinus wajib kelipatan bulat pi: lambda L sama dengan n pi. "
                "Kita peroleh Nilai Eigen diskrit: lambda n sama dengan n pi per L, dengan Fungsi Eigen spasial: X n x sama dengan sinus n pi x per L."
            )
        },
        {
            "num": 8,
            "title": "Diagram Fisik: Difusi Termal Konduktor Busbar GITET 500 kV",
            "chapter": "08. Difusi Termal Busbar GITET",
            "quiz": False,
            "text": (
                "Slide ini menampilkan diagram fisik konduktor busbar tembaga tubular pada Gardu Induk Tegangan Ekstra Tinggi GITET lima ratus kilo Volt. "
                "Busbar membentang sepanjang bentang L di antara dua isolator tumpu gardu induk. "
                "Saat memikul arus beban nominal hingga ribuan Ampere, timbul pemanasan internal Joule merata di sepanjang batang. "
                "Kedua ujung busbar terhubung ke klem konduktor pendingin besar yang bertindak sebagai penyerap kalor suhu konstan. "
                "Difusi kalor mengalir dari titik tengah busbar menuju kedua ujungnya. "
                "Solusi pemisahan variabel memetakan bagaimana profil distribusi temperatur berevolusi dari kondisi awal transien menuju kurva parabola tunak."
            )
        },
        {
            "num": 9,
            "title": "Contoh Terhitung: Masalah Nilai Batas Dirichlet",
            "chapter": "09. Contoh Soal Nilai Batas Dirichlet",
            "quiz": False,
            "text": (
                "Mari kita selesaikan contoh perhitungan difusi termal batang tembaga panjang satu meter dengan difusivitas alfa sama dengan satu koma satu kali sepuluh pangkat minus empat meter kuadrat per detik. "
                "Kedua ujung dijaga pada nol derajat Celsius, dengan distribusi suhu awal seratus derajat seragam. "
                "Melalui integrasi deret Fourier, kita peroleh koefisien Fourier: c n sama dengan empat ratus dibagi n pi untuk n ganjil, dan nol untuk n genap. "
                "Solusi analitis lengkapnya adalah: u x koma t sama dengan jumlahan dari n ganjil empat ratus per n pi dikalikan sinus n pi x "
                "dikalikan e pangkat minus alfa n kuadrat pi kuadrat t. "
                "Mode harmonisa fundamental n sama dengan satu memiliki konstanta waktu peluruhan terpanas sekitar dua jam."
            )
        },
        {
            "num": 10,
            "title": "Kasus Batas Neumann: Ujung Batang Terisolasi",
            "chapter": "10. Kasus Batas Neumann",
            "quiz": False,
            "text": (
                "Sekarang kita tinjau kasus kedua di mana kedua ujung batang diisolasi termal sempurna secara adiabatik. "
                "Syarat batas Neumann menyatakan turunan spasial X prima pada nol dan L bernilai nol. "
                "Menerapkan kondisi ini pada solusi kosinus dan sinus menghasilkan koefisien B sama dengan nol, "
                "dan nilai eigen lambda n sama dengan n pi per L berkorespondensi dengan fungsi eigen kosinus: X n x sama dengan kosinus n pi x per L. "
                "Sangat penting dicatat bahwa nilai eigen n sama dengan nol kini diizinkan, yang menghasilkan suku konstan a nol per dua. "
                "Secara fisik, karena tidak ada kalor yang dapat keluar melalui ujung yang terisolasi, "
                "temperatur akhir batang saat t menuju tak hingga akan merata pada nilai rata-rata suhu mula-mula."
            )
        },
        {
            "num": 11,
            "title": "Ekspansi Pemisahan Variabel 2D: Persamaan Laplace",
            "chapter": "11. Pemisahan Variabel 2D Laplace",
            "quiz": False,
            "text": (
                "Keandalan metode pemisahan variabel terbukti ketika diperluas ke geometri dua dimensi spasial, seperti Persamaan Laplace elektrostatika: "
                "parsial kuadrat V per parsial x kuadrat ditambah parsial kuadrat V per parsial y kuadrat sama dengan nol. "
                "Dengan memisalkan potensial V x koma y sama dengan X x dikalikan Y y, kita pisahkan persamaan menjadi: "
                "X dobel prima per X sama dengan minus Y dobel prima per Y sama dengan minus k kuadrat. "
                "Satu sumbu spasial akan memiliki solusi osilasi sinusoidal, sedangkan sumbu spasial lainnya memiliki solusi fungsi hiperbolik sinus dan kosinus hiperbolik sinh dan cosh. "
                "Kombinasi ini memungkinkan penentuan distribusi medan potensial listrik di dalam celah isolator atau palung konduktor gardu induk."
            )
        },
        {
            "num": 12,
            "title": "Standar Industri: Manajemen Termal Busbar GITET 500 kV",
            "chapter": "12. Standar Termal Busbar GITET",
            "quiz": False,
            "text": (
                "Standar industri IEEE Standard 738 dan IEC 60865 mengatur batas termal konduktor gardu induk tegangan ekstra tinggi. "
                "Batas temperatur operasi kontinu busbar tembaga ditetapkan maksimum sembilan puluh derajat Celsius untuk mencegah hilangnya kekuatan tarik mekanis atau annealing. "
                "Pada saat terjadi gangguan hubung singkat simetris tiga fasa hingga empat puluh kilo Ampere selama nol koma lima detik, "
                "kenaikan suhu berlangsung sangat cepat dan dianggap adiabatik. "
                "Persamaan diferensial difusi termal membuktikan bahwa kapasitas hantar arus busbar harus dirancang dengan margin keamanan "
                "agar suhu transien tidak pernah menembus batas kritis dua ratus derajat Celsius yang dapat melelehkan klem sambungan busbar."
            )
        },
        {
            "num": 13,
            "title": "Praktikum Komputasi Julia: Distribusi Suhu Busbar",
            "chapter": "13. Praktikum Julia: Suhu Busbar",
            "quiz": False,
            "text": (
                "Pada praktikum komputasi Julia ini, kita memprogram solver numerik metode beda hingga atau FDM untuk memecahkan difusi termal busbar tembaga. "
                "Kita diskretisasi panjang busbar satu meter menjadi lima puluh simpul spasial dan waktu simulasi selama dua jam. "
                "Grafik di sebelah kanan menampilkan visualisasi kurva suhu sepanjang busbar pada berbagai cuplikan waktu t: "
                "kurva awal yang mendatar secara bertahap melengkung menjadi kurva kubah lonceng yang mulus seiring pelepasan kalor ke ujung-ujung busbar. "
                "Simulasi Julia ini mempertegas ketelitian solusi analitis deret Fourier yang kita turunkan sebelumnya."
            )
        },
        {
            "num": 14,
            "title": "Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)",
            "chapter": "14. Kuis Interaktif & Evaluasi Bloom",
            "quiz": True,
            "text_part1": (
                "Saatnya kuis interaktif untuk menguji penguasaan konsep pemisahan variabel Anda. Perhatikan studi kasus pada layar: "
                "Pada pemisahan variabel u x koma t sama dengan X x dikalikan T t untuk persamaan difusi termal, mengapa konstanta pemisah k wajib dipilih bernilai negatif minus lambda kuadrat? "
                "Pilihan A: Konstanta positif dilarang dalam kalkulus diferensial. "
                "Pilihan B: Konstanta positif menghasilkan solusi waktu T t sama dengan C dikali e pangkat plus lambda kuadrat t yang meledak menuju tak hingga, melanggar hukum termodinamika bahwa energi panas harus meluruh stabil! "
                "Pilihan C: Konstanta negatif mempercepat proses perhitungan matriks determinan. "
                "Pilihan D: Nilai positif hanya diperbolehkan berlaku untuk perambatan gelombang suara akustik. "
                "Silakan analisis makna fisis konstanta pemisahan ini dan tentukan pilihan terbaik Anda dalam delapan detik ke depan."
            ),
            "text_part2": (
                "Waktu habis. Jawaban yang tepat adalah B: Konstanta positif menghasilkan solusi yang meledak menuju tak hingga, melanggar hukum termodinamika! "
                "Berdasarkan Hukum Kedua Termodinamika, gradien panas pada konduktor tanpa sumber internal harus meluruh secara asimtotik menuju kesetimbangan termal lingkungan. "
                "Pemilihan k bernilai minus lambda kuadrat menjamin faktor waktu e pangkat minus lambda kuadrat t meluruh mulus menuju nol. "
                "Pada kolom tantangan sebelah kanan, Anda juga ditantang menurunkan fungsi eigen spasial untuk syarat batas terisolasi adiabatik Neumann di level C4, "
                "mengevaluasi konvergensi deret Fourier di level C5, serta merancang panjang busbar gardu induk kapasitas arus tiga ribu Ampere di level C6."
            )
        },
        {
            "num": 15,
            "title": "Rangkuman Eksekutif & Jembatan ke Minggu 11",
            "chapter": "15. Rangkuman Eksekutif & Penutup",
            "quiz": False,
            "text": (
                "Sebagai rangkuman perkuliahan minggu kesepuluh: Pertama, Metode Pemisahan Variabel mereduksi PDP menjadi sistem PDB biasa yang saling independen. "
                "Kedua, justifikasi fisika kestabilan mewajibkan konstanta pemisahan bernilai negatif. "
                "Ketiga, syarat batas Dirichlet menghasilkan fungsi eigen sinus, sedangkan syarat batas Neumann menghasilkan fungsi eigen kosinus. "
                "Dan keempat, superposisi deret Fourier merekonstruksi distribusi termal pada konduktor busbar gardu induk. "
                "Silakan pelajari modul ajar dan selesaikan Lembar Kerja serta Problem Set Minggu kesepuluh di portal ndaratha dot my dot id. "
                "Pada minggu kesebelas, kita akan menerapkan metode ini pada Persamaan Gelombang satu dimensi dan saluran transmisi daya. Terima kasih dan wassalamualaikum warahmatullahi wabarakatuh."
            )
        }
    ]
}
