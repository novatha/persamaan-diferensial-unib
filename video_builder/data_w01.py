"""
data_w01.py — Data Narasi 15 Salindia Minggu 01 v2.0
Topik: Klasifikasi PDB/PDP, Nilai Awal (IVP), & Pemodelan Fisis Rangkaian RL
"""
import os

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA = {
    "week_num": "01",
    "pdf_path": os.path.join(PROJ_DIR, "ch1.pdf"),
    "title": "Klasifikasi PDB/PDP, Masalah Nilai Awal, & Pemodelan Rangkaian RL",
    "subtitle": "Klasifikasi Orde, Derajat, Linieritas, Solusi Umum & Khusus IVP, Transien RL, Arus Inrush Trafo PLN, dan Julia DifferentialEquations.jl",
    "cpmk": [
        ("C1", "Mengingat", "Mendefinisikan PDB dan PDP serta membedakan konsep orde, derajat, dan linieritas."),
        ("C2", "Memahami", "Menjelaskan makna fisis konstanta integrasi dan kontinuitas energi medan magnet induktor."),
        ("C3", "Menerapkan", "Menurunkan dan menyelesaikan PDB orde satu sirkuit RL dari Hukum Tegangan Kirchhoff."),
        ("C4", "Menganalisis", "Menganalisis profil transien peluruhan dan pengisian arus terhadap variasi konstanta waktu tau."),
        ("C5", "Mengevaluasi", "Mengevaluasi fenomena arus inrush transformator gardu induk PLN berbasis batas kejenuhan inti."),
        ("C6", "Komputasi", "Mengembangkan simulasi komputasi numerik transien RL menggunakan bahasa pemrograman Julia.")
    ],
    "slides": [
        {
            "num": 1,
            "title": "Judul & Pembukaan Kuliah Minggu 01",
            "chapter": "01. Pembukaan Perkuliahan Persamaan Diferensial",
            "quiz": False,
            "text": (
                "Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, "
                "selamat datang dalam perkuliahan daring Persamaan Diferensial semester genap 2026. "
                "Mata kuliah ini dirancang khusus untuk membangun fondasi analisis matematika yang kokoh "
                "dalam memodelkan fenomena fisis kelistrikan dan elektromagnetika. "
                "Pada pertemuan perdana minggu pertama ini, kita akan membahas: "
                "Klasifikasi PDB dan PDP, Konsep Orde dan Derajat, Syarat Linieritas, "
                "Solusi Umum versus Solusi Khusus, Masalah Nilai Awal atau Initial Value Problem, "
                "serta Pemodelan Fisis Rangkaian Listrik berbasis Hukum Kirchhoff. "
                "Kuliah ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan."
            )
        },
        {
            "num": 2,
            "title": "Capaian Pembelajaran (Sub-CPMK) & Taksonomi Bloom",
            "chapter": "02. Capaian Pembelajaran Sub-CPMK 1",
            "quiz": False,
            "text": (
                "Sebelum melangkah lebih jauh, mari kita pahami Capaian Pembelajaran Mata Kuliah minggu ini berbasis Taksonomi Bloom. "
                "Pada level C1 Mengingat, mahasiswa mampu mendefinisikan PDB dan PDP serta membedakan konsep orde, derajat, dan linieritas. "
                "Pada level C2 Memahami, mahasiswa mampu menjelaskan makna fisis konstanta integrasi dan kondisi awal pada rangkaian listrik. "
                "Pada level C3 Menerapkan, mahasiswa mampu menurunkan dan menyelesaikan PDB orde satu dari rangkaian RL menggunakan Hukum Tegangan Kirchhoff. "
                "Pada level C4 Menganalisis, mahasiswa mampu menganalisis sifat transien eksponensial dan mengidentifikasi konstanta waktu tau. "
                "Pada level C5 Mengevaluasi, mahasiswa mampu mengevaluasi dampak arus inrush trafo terhadap koordinasi relai pengaman. "
                "Dan pada level C6 Komputasi, mahasiswa mampu memprogram simulasi numerik respon transien rangkaian di Julia."
            )
        },
        {
            "num": 3,
            "title": "Peta Jalan Kurikulum & Filosofi Dinamika Elektro",
            "chapter": "03. Peta Konsep & Filosofi Dinamika Sistem",
            "quiz": False,
            "text": (
                "Perhatikan diagram alir kurikulum pada slide ini. Mata kuliah Persamaan Diferensial menjadi jembatan "
                "antara sains dasar fisika kalkulus dengan rekayasa terapan seperti Analisis Rangkaian Listrik, Medan Elektromagnetika, "
                "dan Sistem Tenaga Listrik. Mengapa insinyur elektro harus menguasai persamaan diferensial? "
                "Karena energi di alam semesta tidak dapat berubah seketika. Hubungan antara tegangan, arus, muatan, dan fluks magnetik "
                "selalu melibatkan laju perubahan terhadap waktu d per d t, maupun gradien spasial laplacian pada ruang tiga dimensi. "
                "Memahami persamaan diferensial berarti memahami bahasa alami alam semesta dalam mengalirkan energi."
            )
        },
        {
            "num": 4,
            "title": "Taksonomi Persamaan Diferensial: PDB vs PDP",
            "chapter": "04. Taksonomi PDB vs PDP",
            "quiz": False,
            "text": (
                "Mari kita klasifikasikan persamaan diferensial ke dalam dua keluarga besar. "
                "Pertama, Persamaan Diferensial Biasa atau PDB, yaitu persamaan yang hanya memuat turunan terhadap satu variabel bebas tunggal, "
                "seperti waktu t. PDB digunakan untuk memodelkan sistem elemen terpusat, misalnya pengosongan kapasitor RC atau dinamika mesin sinkron. "
                "Kedua, Persamaan Diferensial Parsial atau PDP, yang memuat turunan parsial terhadap dua atau lebih variabel bebas, "
                "seperti ruang spasial x, y, z dan waktu t. PDP memodelkan fenomena medan terdistribusi, seperti Persamaan Gelombang "
                "saluran transmisi tegangan tinggi, Persamaan Laplace potensial elektrostatika, serta difusi panas trafo daya."
            )
        },
        {
            "num": 5,
            "title": "Klasifikasi Formal: Orde, Derajat, & Linieritas",
            "chapter": "05. Klasifikasi Orde, Derajat, & Linieritas",
            "quiz": False,
            "text": (
                "Ada tiga atribut utama untuk mengklasifikasikan persamaan diferensial secara formal. "
                "Pertama, Orde, yaitu tingkat turunan tertinggi yang muncul di dalam persamaan. "
                "Kedua, Derajat, yaitu pangkat aljabar dari turunan tertinggi setelah persamaan dibebaskan dari bentuk pecahan atau akar. "
                "Ketiga, Linieritas. Suatu persamaan diferensial dikatakan linier jika memenuhi tiga kriteria ketat: "
                "variabel tak bebas y dan seluruh turunannya hanya berpangkat satu, tidak ada suku perkalian silang antar turunan, "
                "serta tidak ada fungsi non-linier transendental seperti sinus, eksponensial, atau logaritma yang memuat variabel terikat y."
            )
        },
        {
            "num": 6,
            "title": "Pemodelan Fisis: Sirkuit Pengisian RL",
            "chapter": "06. Pemodelan First-Principles Rangkaian RL",
            "quiz": False,
            "text": (
                "Sekarang kita masuki Pilar 1: pemodelan fisis dari hukum dasar rangkaian. "
                "Tinjau sirkuit RL seri yang dihubungkan ke sumber tegangan searah V nol saat sakelar ditutup pada t sama dengan nol. "
                "Berdasarkan Hukum Tegangan Kirchhoff, jumlah tegangan dalam loop tertutup sama dengan nol: "
                "tegangan sumber V nol sama dengan jatuh tegangan resistor v R ditambah tegangan induktor v L. "
                "Karena tegangan resistor adalah R dikali i, dan tegangan induktor menurut Hukum Faraday-Lenz adalah L dikali d i per d t, "
                "maka kita peroleh PDB linier orde satu koefisien konstan: L d i per d t ditambah R i sama dengan V nol."
            )
        },
        {
            "num": 7,
            "title": "Solusi Umum vs Solusi Khusus (IVP)",
            "chapter": "07. Solusi Umum & Masalah Nilai Awal",
            "quiz": False,
            "text": (
                "Dalam matematika, mengintegrasikan PDB orde satu akan selalu memunculkan satu konstanta integrasi sembarang C. "
                "Ekspresi yang masih memuat konstanta C sembarang disebut Solusi Umum, yang secara geometris merepresentasikan keluarga kurva "
                "tak berhingga banyaknya. Namun di laboratorium teknik elektro nyata, respons arus rangkaian pada saat sakelar ditutup "
                "hanya memiliki satu kurva riil yang unik. Untuk menentukan nilai spesifik konstanta C, kita memerlukan Masalah Nilai Awal "
                "atau Initial Value Problem, yaitu kondisi nilai variabel keadaan pada saat awal t sama dengan nol, i nol sama dengan nol."
            )
        },
        {
            "num": 8,
            "title": "Derivasi Analitik Solusi Khusus Rangkaian RL",
            "chapter": "08. Penurunan Solusi Analitik Rangkaian RL",
            "quiz": False,
            "text": (
                "Mari kita turunkan solusi khususnya langkah demi langkah menggunakan metode separabel. "
                "Dari L d i per d t sama dengan V nol dikurang R i, kita pisahkan variabel arus ke ruas kiri dan waktu ke ruas kanan: "
                "d i dibagi kurung V nol per R dikurang i sama dengan R per L d t. "
                "Integrasikan kedua ruas menghasilkan minus logaritma natural kurung V nol per R dikurang i sama dengan R per L t ditambah konstanta. "
                "Dengan mengeksponensialkan kedua ruas dan mensubstitusikan syarat batas arus awal nol pada t sama dengan nol, "
                "kita peroleh solusi khusus eksak: i t sama dengan V nol per R dikali kurung satu dikurang e pangkat minus t per tau."
            )
        },
        {
            "num": 9,
            "title": "Karakteristik Dinamika Transien & Konstanta Waktu tau",
            "chapter": "09. Dinamika Transien & Skala Waktu tau",
            "quiz": False,
            "text": (
                "Parameter tau didefinisikan sebagai L per R dan dinamakan konstanta waktu sirkuit dengan satuan detik. "
                "Konstanta waktu mengukur kelembaman sistem induktif dalam merespons perubahan energi magnetik. "
                "Pada saat t sama dengan satu tau, arus pengisian mencapai enam puluh tiga koma dua persen dari arus kondisi mantap. "
                "Pada tiga tau, arus telah mencapai sembilan puluh lima persen. Dan pada lima tau atau 5 tau, arus telah mencapai "
                "sembilan puluh sembilan koma tiga persen, sehingga secara praktis rekayasa dianggap telah mencapai keadaan tunak atau steady-state."
            )
        },
        {
            "num": 10,
            "title": "Studi Kasus Rekayasa: Arus Inrush Trafo Gardu Induk PLN",
            "chapter": "10. Studi Kasus Arus Inrush Trafo Gardu Induk",
            "quiz": False,
            "text": (
                "Mari kita lihat aplikasi nyata di industri kelistrikan PLN. Ketika transformator daya gardu induk dihubungkan "
                "ke grid pada saat gelombang tegangan berada di titik nol derajat, fluks magnetik inti trafo harus berlipat ganda "
                "menjadi dua kali fluks nominal demi memenuhi hukum Faraday. Akibatnya, inti besi trafo mengalami saturasi magnetik hebat, "
                "menyebabkan induktansi efektif L anjlok drastis ke nilai induktansi udara. Penurunan drastis nilai L ini memicu lonjakan arus "
                "yang disebut arus inrush hingga delapan sampai dua belas kali lipat arus nominal. Pemodelan transien PDB memungkinkan para insinyur "
                "merancang kurva koordinasi relai diferensial agar tidak memutus pemutus tenaga secara keliru saat pensaklaran."
            )
        },
        {
            "num": 11,
            "title": "Contoh Soal Terhitung (Worked Example): Solenoida PMT",
            "chapter": "11. Contoh Soal Terhitung Solenoida PMT",
            "quiz": False,
            "text": (
                "Mari kita selesaikan contoh soal numerik perancangan koil solenoida pemutus tenaga atau PMT. "
                "Koil memiliki induktansi L sama dengan dua koma lima Henry dan resistansi R sama dengan lima puluh ohm, dihubungkan ke sumber DC seratus volt. "
                "Pertama, kita hitung konstanta waktu tau sama dengan L per R, yaitu dua koma lima dibagi lima puluh, menghasilkan nol koma nol lima detik "
                "atau lima puluh milidetik. Kedua, arus tunak adalah V nol per R sama dengan seratus dibagi lima puluh, yaitu dua Ampere. "
                "Ketiga, arus pada t sama dengan tiga puluh milidetik dihitung dari rumus analitik, menghasilkan nol koma sembilan nol dua Ampere. "
                "Keempat, waktu yang dibutuhkan untuk mencapai satu koma delapan Ampere atau sembilan puluh persen arus maksimum "
                "adalah minus tau dikali logaritma natural nol koma satu, menghasilkan seratus lima belas milidetik."
            )
        },
        {
            "num": 12,
            "title": "Praktikum Komputasi Numerik Terbuka Berbasis Julia",
            "chapter": "12. Praktikum Komputasi Julia DifferentialEquations",
            "quiz": False,
            "text": (
                "Sekarang kita masuk ke Pilar 3, yaitu komputasi ilmiah modern berbasis bahasa pemrograman berkecepatan tinggi: Julia. "
                "Pada salindia ini ditampilkan kode ringkas menggunakan pustaka terdepan dunia, DifferentialEquations dot j l dan Plots dot j l. "
                "Kita definisikan fungsi dinamika sirkuit RL f r l kurung i koma p koma t sama dengan kurung V nol dikurang R dikali i dibagi L. "
                "Selanjutnya kita inisialisasi masalah nilai awal menggunakan konstruktor O D E Problem dengan kondisi awal arus nol, "
                "lalu menyelesaikannya menggunakan solver numerik adaptif Tsit lima. Julia mengeksekusi kode ini dengan kompilasi JIT mendekati kecepatan bahasa C."
            )
        },
        {
            "num": 13,
            "title": "Verifikasi Hasil Komputasi Julia & Dinamika Transien",
            "chapter": "13. Verifikasi Simulasi Julia vs Solusi Eksak",
            "quiz": False,
            "text": (
                "Pada salindia ini kita bandingkan kurva respon hasil solver Julia dengan garis analitis eksak. "
                "Perhatikan bahwa titik-titik diskret komputasi Tsit lima berimpit secara sempurna tanpa deviasi sedikit pun pada solusi eksak. "
                "Grafik di sebelah kanan juga memvisualisasikan bagaimana laju perubahan arus d i per d t mencapai nilai maksimum pada t sama dengan nol "
                "dan meluruh secara mulus menuju nol saat kondisi mantap tercapai. Ini membuktikan bahwa pustaka numerik terbuka memberikan akurasi "
                "yang sangat tinggi untuk analisis dinamika sistem keteknikan."
            )
        },
        {
            "num": 14,
            "title": "Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)",
            "chapter": "14. Kuis Interaktif & Evaluasi Bloom",
            "quiz": True,
            "text_part1": (
                "Saatnya kuis interaktif untuk menguji intuisi fisika Anda. Tinjau kasus rekayasa berikut: "
                "Sakelar rangkaian RL dihubungkan ke sumber tegangan DC V nol. Saat sakelar ditutup pada t sama dengan nol, "
                "mengapa arus awal i nol positif bernilai tepat nol, padahal tegangan sumber V nol sudah aktif penuh? "
                "Pilihan A: Resistor R memblokir aliran arus pada awal transien. "
                "Pilihan B: Induktor menginduksi gaya gerak listrik lawan v L sama dengan minus L d i per d t yang menentang lonjakan arus demi kekekalan fluks! "
                "Pilihan C: Baterai memerlukan jeda waktu untuk melepaskan muatan listrik. "
                "Pilihan D: Energi medan magnetik membutuhkan hambatan luar untuk stabil. "
                "Silakan pikirkan dan tentukan pilihan jawaban Anda dalam delapan detik ke depan."
            ),
            "text_part2": (
                "Waktu habis. Jawaban yang tepat adalah B: Induktor menginduksi gaya gerak listrik lawan v L sama dengan minus L d i per d t! "
                "Sesuai Hukum Faraday-Lenz dan prinsip kekekalan energi medan magnetik setengah L i kuadrat, energi tidak dapat berubah diskontinu. "
                "Oleh karena itu arus induktor harus kontinu, memaksa arus bernilai nol tepat pada saat sakelar ditutup. "
                "Pada panel sebelah kanan, Anda juga ditantang untuk menganalisis disipasi energi kalor resistor pada C4, "
                "mengevaluasi respons relai proteksi pada C5, serta merancang sirkuit snubber pada level C6."
            )
        },
        {
            "num": 15,
            "title": "Rangkuman Inti Perkuliahan & Referensi",
            "chapter": "15. Rangkuman Perkuliahan & Penutup",
            "quiz": False,
            "text": (
                "Sebagai penutup pertemuan perdana, mari kita rangkum tiga pilar utama materi hari ini. "
                "Pertama, dinamika sistem tenaga dan rangkaian elektrik dimodelkan oleh persamaan diferensial melalui Hukum Kirchhoff "
                "dan prinsip kontinuitas energi medan. Kedua, solusi umum memuat konstanta integrasi sembarang, sedangkan solusi khusus "
                "ditentukan secara tunggal oleh Masalah Nilai Awal atau IVP. Ketiga, konstanta waktu tau sama dengan L per R menjadi penentu kecepatan respons transien. "
                "Untuk memperdalam pemahaman, silakan kerjakan Lembar Kerja Mahasiswa dan Problem Set C1 sampai C6 pada portal web perkuliahan. "
                "Terima kasih atas perhatian Anda, sampai jumpa pada perkuliahan minggu kedua."
            )
        }
    ]
}
