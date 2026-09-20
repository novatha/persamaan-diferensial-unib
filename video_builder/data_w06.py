"""
data_w06.py — Data Narasi 15 Salindia Minggu 06 v2.0
Topik: Transformasi Laplace Dasar & Teorema Pergeseran Domain-s
"""
import os

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA = {
    "week_num": "06",
    "pdf_path": os.path.join(PROJ_DIR, "ch6.pdf"),
    "title": "Transformasi Laplace Dasar: Domain-s & Teorema Pergeseran",
    "subtitle": "Definisi Formal Integral Laplace, Sifat Linieritas, Operator Turunan & Kondisi Awal, Fungsi Heaviside & Dirac, Teorema Pergeseran Frekuensi/Waktu, dan Surja Petir IEC 60060-1",
    "cpmk": [
        ("C1", "Mengingat", "Menyatakan definisi integral satu sisi Transformasi Laplace dan syarat keberadaan orde eksponensial."),
        ("C2", "Memahami", "Menjelaskan keuntungan aljabar transformasi turunan d^n y / dt^n yang menyertakan kondisi awal secara otomatis."),
        ("C3", "Menerapkan", "Menerapkan pasangan transformasi baku dan teorema pergeseran pertama/kedua pada fungsi waktu."),
        ("C4", "Menganalisis", "Memodelkan sinyal diskontinu pensaklaran tangga Heaviside dan surja petir Dirac impulsif."),
        ("C5", "Mengevaluasi", "Mengevaluasi bentuk gelombang surja petir standar gardu induk 1.2/50 mikrodetik IEC 60060-1."),
        ("C6", "Komputasi", "Memprogram sintesis kurva tegangan surja petir dan transformasi Laplace numerik dengan Julia.")
    ],
    "slides": [
        {
            "num": 1,
            "title": "Judul & Pembukaan Kuliah Minggu 06",
            "chapter": "01. Pembukaan Perkuliahan Minggu 06",
            "quiz": False,
            "text": (
                "Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, "
                "selamat datang kembali dalam perkuliahan daring Persamaan Diferensial semester genap 2026. "
                "Pada Minggu keenam ini, kita membuka pintu gerbang metode operasional paling berdaya guna dalam rekayasa elektro: "
                "Transformasi Laplace dan Teorema Pergeseran pada Domain Frekuensi Kompleks s. "
                "Kita akan mempelajari bagaimana transformasi integral mengubah kalkulus diferensial yang rumit menjadi aljabar linier biasa, "
                "menangani fungsi khusus tak kontinu seperti Tangga Heaviside dan Impuls Dirac, "
                "serta memodelkan gelombang surja petir standar gardu induk IEC 60060-1. "
                "Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan."
            )
        },
        {
            "num": 2,
            "title": "Capaian Pembelajaran (Sub-CPMK 4) & Taksonomi Bloom",
            "chapter": "02. Sub-CPMK 4 & Taksonomi Bloom",
            "quiz": False,
            "text": (
                "Berikut adalah Capaian Pembelajaran Sub-CPMK Minggu keenam berbasis Taksonomi Bloom. "
                "Pada C1 Mengingat, mahasiswa mampu menyatakan definisi integral Transformasi Laplace dan wilayah konvergensi ROC. "
                "Pada C2 Memahami, mahasiswa mampu menjelaskan keunggulan domain s dalam menggabungkan kondisi awal secara langsung. "
                "Pada C3 Menerapkan, mahasiswa mampu menghitung transformasi fungsi elementer dan menerapkan teorema translasi. "
                "Pada C4 Menganalisis, mahasiswa mampu memodelkan sinyal pulsa sepotong-sepotong menggunakan fungsi Heaviside. "
                "Pada C5 Mengevaluasi, mahasiswa mampu mengkaji parameter waktu muka dan ekor gelombang surja petir IEC. "
                "Dan pada C6 Komputasi, mahasiswa mampu memvisualisasikan sinyal surja transien dengan bahasa Julia."
            )
        },
        {
            "num": 3,
            "title": "Peta Konsep: Mengapa Beralih ke Domain Kompleks s?",
            "chapter": "03. Peta Konsep: Mengapa Domain-s?",
            "quiz": False,
            "text": (
                "Perhatikan diagram alir paradigma operasional Laplace pada slide ini. "
                "Dalam domain waktu riil t, menyelesaikan Masalah Nilai Awal PDB membutuhkan proses integrasi, pencarian akar karakteristik, "
                "dan penyusunan sistem persamaan aljabar untuk konstanta C satu dan C dua. "
                "Transformasi Laplace menawarkan jembatan transformasi: PDB di domain waktu diubah menjadi persamaan aljabar linier di domain frekuensi s. "
                "Di domain s, kita hanya melakukan manipulasi aljabar pecahan sederhana untuk mengisolasi variabel Y s. "
                "Setelah itu, melalui invers transformasi Laplace, kita langsung memperoleh solusi waktu lengkap yang sudah otomatis memuat seluruh kondisi awal. "
                "Metode ini menghilangkan kebutuhan mencari solusi homogen dan partikular secara terpisah."
            )
        },
        {
            "num": 4,
            "title": "Definisi Formal & Syarat Keberadaan Transformasi Laplace",
            "chapter": "04. Definisi Formal Integral Laplace",
            "quiz": False,
            "text": (
                "Secara formal, Transformasi Laplace satu sisi dari fungsi waktu f t didefinisikan sebagai integral tak wajar: "
                "L kurung f t sama dengan F s sama dengan integral dari nol hingga tak hingga f t dikalikan e pangkat minus s t d t. "
                "Variabel s adalah frekuensi kompleks s sama dengan sigma ditambah j omega. "
                "Teorema Keberadaan menjamin bahwa F s pasti ada dan konvergen pada setengah bidang kanan riil s lebih besar dari gamma, "
                "asalkan f t memenuhi dua syarat: Pertama, f t kontinu sepotong-sepotong pada setiap interval berhingga. "
                "Kedua, f t berorde eksponensial, yaitu nilai mutlak f t tidak tumbuh lebih cepat daripada M dikalikan e pangkat gamma t saat t menuju tak hingga. "
                "Seluruh sinyal fisik rekayasa elektro selalu memenuhi kriteria ini."
            )
        },
        {
            "num": 5,
            "title": "Pasangan Transformasi Laplace Baku Fungsi Elementer",
            "chapter": "05. Pasangan Transformasi Baku",
            "quiz": False,
            "text": (
                "Melalui evaluasi integral definisi, kita memperoleh tabel pasangan transformasi baku fungsi-fungsi elementer. "
                "Fungsi konstan satu bertransformasi menjadi satu per s. "
                "Fungsi waktu polinomial t pangkat n bertransformasi menjadi n faktorial dibagi s pangkat n ditambah satu. "
                "Fungsi peluruhan eksponensial e pangkat a t bertransformasi menjadi satu dibagi s dikurang a. "
                "Fungsi sinusoidal kosinus omega t bertransformasi menjadi s dibagi s kuadrat ditambah omega kuadrat, "
                "sedangkan sinus omega t bertransformasi menjadi omega dibagi s kuadrat ditambah omega kuadrat. "
                "Tabel baku ini menjadi kamus operasional utama Anda dalam menyelesaikan analisis rangkaian listrik."
            )
        },
        {
            "num": 6,
            "title": "Sifat Linieritas & Transformasi Operator Turunan",
            "chapter": "06. Linieritas & Transformasi Turunan",
            "quiz": False,
            "text": (
                "Transformasi Laplace memiliki sifat linieritas sempurna: transformasi dari kombinasi linier fungsi sama dengan kombinasi linier transformasinya. "
                "Namun keunggulan paling revolusioner terletak pada Teorema Diferensiasi: "
                "transformasi Laplace dari turunan pertama d f per d t adalah s dikalikan F s dikurang kondisi awal f nol. "
                "Sedangkan turunan kedua d kuadrat f per d t kuadrat bertransformasi menjadi s kuadrat F s dikurang s f nol dikurang f prima nol. "
                "Perhatikan bahwa operator kalkulus d per d t berganti menjadi perkalian dengan variabel aljabar s, "
                "dan kondisi awal f nol serta laju f prima nol secara otomatis langsung terintegrasi ke dalam persamaan aljabar."
            )
        },
        {
            "num": 7,
            "title": "Fungsi Khusus 1: Tangga Satuan Heaviside u(t - a)",
            "chapter": "07. Fungsi Tangga Satuan Heaviside",
            "quiz": False,
            "text": (
                "Dalam teknik pensaklaran listrik, kita sering menghadapi sinyal yang dinyalakan atau dimatikan secara mendadak pada waktu t sama dengan a. "
                "Oliver Heaviside memperkenalkan Fungsi Tangga Satuan u kurung t dikurang a, yang bernilai nol untuk t kurang dari a, "
                "dan bernilai satu untuk t lebih besar dari atau sama dengan a. "
                "Transformasi Laplace dari fungsi tangga satuan u kurung t dikurang a adalah e pangkat minus a s dibagi s. "
                "Fungsi Heaviside berfungsi sebagai sakelar aljabar yang sangat efektif untuk menyusun sinyal gelombang pulsa, segitiga, "
                "dan gelombang sepotong-sepotong tanpa perlu membagi interval integrasi secara manual."
            )
        },
        {
            "num": 8,
            "title": "Fungsi Khusus 2: Impuls Satuan Dirac delta(t - a)",
            "chapter": "08. Fungsi Impuls Dirac",
            "quiz": False,
            "text": (
                "Untuk memodelkan fenomena kejutan instan seperti sambaran petir, lonjakan elektrostatik ESD, atau ketukan mekanis sesaat, "
                "Paul Dirac merumuskan Fungsi Impuls delta kurung t dikurang a. "
                "Fungsi delta bernilai nol di semua titik kecuali pada t sama dengan a di mana nilainya menuju tak hingga, "
                "dengan luas integral total tepat sama dengan satu satuan. "
                "Sifat penyaring atau sifting property menyatakan bahwa integral f t dikali delta t dikurang a menghasilkan nilai f di titik a. "
                "Transformasi Laplace dari impuls satuan Dirac delta t dikurang a adalah fungsi eksponensial murni e pangkat minus a s. "
                "Bila impuls terjadi pada t sama dengan nol, transformasinya bernilai tepat satu."
            )
        },
        {
            "num": 9,
            "title": "Teorema Pergeseran Pertama (Translasi Frekuensi Sumbu-s)",
            "chapter": "09. Teorema Pergeseran Pertama",
            "quiz": False,
            "text": (
                "Teorema Pergeseran Pertama atau Translasi Frekuensi menyatakan: "
                "jika transformasi dari f t adalah F s, maka perkalian f t dengan fungsi eksponensial e pangkat a t "
                "menggeser variabel kompleks s menjadi F kurung s dikurang a. "
                "Teorema ini sangat ampuh untuk mentransformasikan gelombang sinusoidal teredam yang muncul pada rangkaian underdamped. "
                "Sebagai contoh, fungsi e pangkat minus alpha t dikalikan kosinus omega t langsung bertransformasi menjadi "
                "s ditambah alpha dibagi kurung s ditambah alpha kuadrat ditambah omega kuadrat. "
                "Peredaman waktu di domain t berkorespondensi langsung dengan pergeseran kutub ke kiri pada bidang s."
            )
        },
        {
            "num": 10,
            "title": "Teorema Pergeseran Kedua (Translasi Waktu Sumbu-t)",
            "chapter": "10. Teorema Pergeseran Kedua",
            "quiz": False,
            "text": (
                "Teorema Pergeseran Kedua atau Translasi Waktu adalah pasangan simetris dari teorema pertama: "
                "jika suatu sinyal f t mengalami penundaan waktu sebesar a detik menjadi f kurung t dikurang a dikalikan tangga u t dikurang a, "
                "maka hasil transformasinya di domain s adalah F s dikalikan faktor modulasi fasa e pangkat minus a s. "
                "Teorema ini menjadi tulang punggung analisis saluran transmisi daya, saluran tunda komunikasi, "
                "dan sistem kendali berbasis mikrokontroler dengan jeda waktu transportasi atau dead-time. "
                "Penundaan waktu murni tidak mengubah spektrum frekuensi F s selain memberikan pergeseran fasa linier."
            )
        },
        {
            "num": 11,
            "title": "Aplikasi Industri: Surja Petir Standar IEC 60060-1 / IEEE Std 4",
            "chapter": "11. Surja Petir IEC 60060-1",
            "quiz": False,
            "text": (
                "Aplikasi industri bertegangan tinggi yang sangat vital adalah pengujian koordinasi isolasi transformator dan kabel terhadap surja petir. "
                "Standar internasional IEC 60060-1 dan IEEE Standard 4 mendefinisikan bentuk gelombang impuls petir standar satu koma dua per lima puluh mikrodetik. "
                "Secara matematis, impuls petir ini dibentuk oleh selisih dua fungsi eksponensial: "
                "v t sama dengan V nol dikalikan kurung e pangkat minus alpha t dikurang e pangkat minus beta t dikalikan u t. "
                "Parameter beta yang besar mengatur waktu muka gelombang yang sangat curam satu koma dua mikrodetik, "
                "sedangkan alpha mengatur waktu paruh ekor gelombang lima puluh mikrodetik. "
                "Melalui Transformasi Laplace, respon tegangan tembus pada peralatan gardu induk dapat dianalisis secara analitik eksak."
            )
        },
        {
            "num": 12,
            "title": "Contoh Soal Terhitung (Worked Example): Konversi IVP ke Domain-s",
            "chapter": "12. Contoh Soal Konversi IVP ke Domain-s",
            "quiz": False,
            "text": (
                "Mari kita bedah contoh soal terhitung konversi Masalah Nilai Awal ke domain s. "
                "Diberikan PDB rangkaian: d kuadrat y per d t kuadrat ditambah empat d y per d t ditambah tiga belas y sama dengan nol, "
                "dengan syarat awal y nol sama dengan dua dan y prima nol sama dengan minus dua. "
                "Langkah satu: kita terapkan transformasi Laplace pada setiap suku. "
                "Turunan kedua menjadi s kuadrat Y s dikurang dua s ditambah dua. "
                "Turunan pertama menjadi empat dikali s Y s dikurang dua. Suku ketiga menjadi tiga belas Y s. "
                "Langkah dua: kumpulkan suku Y s di ruas kiri: kurung s kuadrat ditambah empat s ditambah tiga belas dikali Y s "
                "sama dengan dua s ditambah enam. Solusi aljabar di domain s adalah Y s sama dengan dua s ditambah enam dibagi s kuadrat tambah empat s tambah tiga belas."
            )
        },
        {
            "num": 13,
            "title": "Praktikum Komputasi Julia: Surja Petir IEC 60060-1",
            "chapter": "13. Praktikum Julia: Surja Petir IEC",
            "quiz": False,
            "text": (
                "Pada praktikum komputasi Julia ini, kita memprogram perumusan analitik impuls petir standar IEC 60060-1 dan mengevaluasi respon transiennya. "
                "Kita definisikan konstanta V nol satu koma nol tiga delapan mega Volt, alpha empat belas koma enam ribu detik minus satu, "
                "dan beta dua koma empat ratus enam puluh ribu detik minus satu. "
                "Grafik di sebelah kanan menunjukkan kurva gelombang surja petir yang melonjak tajam ke puncak satu mega Volt dalam satu koma dua mikrodetik, "
                "lalu meluruh perlahan hingga separuh tegangan puncak tepat pada lima puluh mikrodetik. "
                "Simulasi numerik Julia ini memungkinkan insinyur menguji margin ketahanan isolator polimer dan transformator transmisi sebelum diproduksi di pabrik."
            )
        },
        {
            "num": 14,
            "title": "Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)",
            "chapter": "14. Kuis Interaktif & Evaluasi Bloom",
            "quiz": True,
            "text_part1": (
                "Saatnya kuis interaktif untuk menguji pemahaman konsep Laplace Anda. Perhatikan studi kasus pada layar: "
                "Mengapa metode Transformasi Laplace jauh lebih unggul daripada metode PDB klasik dalam menganalisis fenomena surja pensaklaran atau switching di gardu induk? "
                "Pilihan A: Transformasi Laplace tidak lagi memerlukan penerapan Hukum Tegangan Kirchhoff. "
                "Pilihan B: Transformasi Laplace secara otomatis mengonversi fungsi diskontinu seperti fungsi undak Heaviside dan impuls Dirac serta turunan waktu menjadi aljabar rasional domain-s dengan kondisi awal terintegrasi langsung! "
                "Pilihan C: Transformasi Laplace hanya dapat diaplikasikan jika frekuensi sistem bernilai tepat nol Hertz. "
                "Pilihan D: Transformasi Laplace meniadakan kebutuhan nilai induktansi reaktif komponen. "
                "Silakan pertimbangkan dan tentukan jawaban terbaik Anda dalam delapan detik ke depan."
            ),
            "text_part2": (
                "Waktu habis. Jawaban yang tepat adalah B: Mengubah fungsi diskontinu dan turunan menjadi aljabar domain-s dengan kondisi awal otomatis! "
                "Metode klasik sangat kesulitan saat menghadapi fungsi masukan terpotong-potong atau diskontinu seperti sambaran petir dan pensaklaran PMT. "
                "Dengan Transformasi Laplace, kalkulus diferensial diubah menjadi manipulasi aljabar pecahan parsial sederhana. "
                "Pada kolom tantangan sebelah kanan, Anda juga ditantang menentukan tegangan transien dengan teorema pergeseran waktu pada level C4, "
                "membuktikan Teorema Nilai Akhir pada level C5, serta merancang rangkaian pembangkit impuls Marx Generator laboratorium tegangan tinggi pada level C6."
            )
        },
        {
            "num": 15,
            "title": "Rangkuman Inti Perkuliahan & Referensi",
            "chapter": "15. Rangkuman Perkuliahan & Penutup",
            "quiz": False,
            "text": (
                "Sebagai rangkuman perkuliahan minggu keenam: Pertama, Transformasi Laplace mengonversi kalkulus diferensial menjadi aljabar linier pada domain kompleks s. "
                "Kedua, transformasi operator turunan secara otomatis menyertakan kondisi awal tanpa perlu proses terpisah. "
                "Ketiga, fungsi khusus Heaviside dan Dirac memungkinkan representasi sinyal pensaklaran dan surja petir secara elegan. "
                "Dan keempat, teorema translasi waktu dan frekuensi mempermudah analisis transien kompleks. "
                "Silakan pelajari modul ajar dan tuntaskan Lembar Kerja serta Problem Set Minggu keenam di portal ndaratha dot my dot id. "
                "Pada minggu ketujuh, kita akan mendalami Invers Transformasi Laplace, metode pecahan parsial, dan analisis sirkuit domain s. Terima kasih dan wassalamualaikum warahmatullahi wabarakatuh."
            )
        }
    ]
}
