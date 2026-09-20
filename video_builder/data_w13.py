"""
data_w13.py — Data Narasi 15 Salindia Minggu 13 v2.0
Topik: Persamaan Laplace 2D & Elektrostatika
"""
import os

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA = {
    "week_num": "13",
    "pdf_path": os.path.join(PROJ_DIR, "ch13.pdf"),
    "title": "Persamaan Laplace 2D: Distribusi Medan & Stres Isolator 150 kV",
    "subtitle": "Penurunan dari Hukum Gauss Elektrostatika, Sifat Harmonik Nilai Rata-Rata, Teorema Ketunggalan (Uniqueness), Metode Beda Hingga FDM Gauss-Seidel, Stres Dielektrik Rantai Isolator SUTT 150 kV, dan Regulasi Korona IEC 60060-1",
    "cpmk": [
        ("C1", "Mengingat", "Menyatakan bentuk operator Laplacian nabla^2 V = 0 pada ruang bebas muatan."),
        ("C2", "Memahami", "Menjelaskan sifat nilai rata-rata fungsi harmonik dan prinsip nilai ekstremum maksimum/minimum."),
        ("C3", "Menerapkan", "Menghitung distribusi potensial listrik menggunakan teknik beda hingga FDM 5-titik stensil."),
        ("C4", "Menganalisis", "Menganalisis gradien intensitas medan listrik E = -nabla V dan lokalisasi konsentrasi stres dielektrik tinggi."),
        ("C5", "Mengevaluasi", "Mengevaluasi distribusi tegangan tidak merata pada rantai isolator gantung 150 kV akibat kapasitansi liar tiang."),
        ("C6", "Komputasi", "Memprogram simulasi relaksasi FDM 2D iteratif dan pemetaan garis ekuipotensial menggunakan bahasa Julia.")
    ],
    "slides": [
        {
            "num": 1,
            "title": "Judul & Pembukaan Kuliah Minggu 13",
            "chapter": "01. Pembukaan Perkuliahan Minggu 13",
            "quiz": False,
            "text": (
                "Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, "
                "selamat datang kembali dalam perkuliahan daring Persamaan Diferensial semester genap 2026. "
                "Pada Minggu ketiga belas ini, kita membedah Persamaan Diferensial Parsial tipe Eliptik: "
                "Persamaan Laplace Dua Dimensi dan Teori Medan Elektrostatika Gardu Induk. "
                "Kita akan mempelajari penurunan matematis dari Hukum Gauss, sifat fundamental fungsi harmonik, "
                "teorema ketunggalan, metode numerik Beda Hingga atau FDM relaksasi Gauss-Seidel, "
                "studi kasus stres dielektrik rantai isolator gantung seratus lima puluh kilo Volt, "
                "serta pencegahan lucutan korona berbasis standar internasional IEC 60060-1. "
                "Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan."
            )
        },
        {
            "num": 2,
            "title": "Sub-CPMK Taksonomi Bloom (Minggu 13)",
            "chapter": "02. Sub-CPMK 13 & Taksonomi Bloom",
            "quiz": False,
            "text": (
                "Berikut adalah Capaian Pembelajaran Sub-CPMK Minggu ketiga belas berbasis Taksonomi Bloom. "
                "Pada C1 Mengingat, mahasiswa mampu menyatakan operator Laplacian nabla kuadrat V sama dengan nol. "
                "Pada C2 Memahami, mahasiswa mampu menjelaskan sifat rata-rata fungsi harmonik yang melarang adanya titik ekstremum lokal di dalam domain. "
                "Pada C3 Menerapkan, mahasiswa mampu menghitung potensial simpul menggunakan stensil beda hingga lima titik. "
                "Pada C4 Menganalisis, mahasiswa mampu mengekstrak vektor kuat medan listrik E sama dengan minus gradien V. "
                "Pada C5 Mengevaluasi, mahasiswa mampu mengkaji distribusi tegangan non-linier pada piringan isolator terdekat fasa konduktor. "
                "Dan pada C6 Komputasi, mahasiswa mampu menyusun visualisasi kontur medan ekuipotensial menggunakan bahasa Julia."
            )
        },
        {
            "num": 3,
            "title": "Peta Kurikulum: Medan Elektrostatik dalam Kesetimbangan",
            "chapter": "03. Peta Kurikulum: Medan Kesetimbangan",
            "quiz": False,
            "text": (
                "Perhatikan posisi Persamaan Laplace dalam peta kurikulum teknik elektro. "
                "Persamaan diferensial parsial eliptik memodelkan sistem fisika dalam kesetimbangan tunak statis tanpa ada perubahan terhadap waktu. "
                "Dalam elektrostatika, muatan listrik bebas telah diam dan medan listrik berada dalam kondisi ekuilibrium. "
                "Persamaan Laplace mengatur distribusi potensial elektrostatik di seluruh ruang dielektrik bebas muatan, "
                "seperti di dalam celah udara transformator, ruang antara kawat konduktor SUTT dengan tanah, "
                "serta di sepanjang permukaan isolator porselen gardu induk. "
                "Solusi persamaan ini memberikan peta intensitas medan listrik yang menentukan keandalan isolasi tegangan tinggi."
            )
        },
        {
            "num": 4,
            "title": "Penurunan Matematis dari Hukum Gauss Elektrostatika",
            "chapter": "04. Penurunan dari Hukum Gauss",
            "quiz": False,
            "text": (
                "Mari kita turunkan Persamaan Laplace dari prinsip dasar elektromagnetika. "
                "Hukum Gauss dalam bentuk diferensial Maxwell pertama menyatakan: divergensi dari vektor perpindahan listrik D sama dengan rapat muatan volume rho v: "
                "nabla dot D sama dengan rho v. "
                "Pada medium dielektrik linier, isotropik, dan homogen dengan permitivitas epsilon, D sama dengan epsilon dikalikan medan listrik E. "
                "Karena medan elektrostatik bersifat konservatif bebas pusaran curl E sama dengan nol, "
                "medan listrik dapat dinyatakan sebagai negatif gradien potensial skalar: E sama dengan minus nabla V. "
                "Mensubstitusikan E ke Hukum Gauss menghasilkan Persamaan Poisson: nabla kuadrat V sama dengan minus rho v per epsilon. "
                "Pada daerah ruang bebas muatan di mana rho v bernilai nol, kita peroleh Persamaan Laplace: nabla kuadrat V sama dengan nol."
            )
        },
        {
            "num": 5,
            "title": "Sifat Fundamental Fungsi Harmonik: Nilai Rata-rata & Ekstremum",
            "chapter": "05. Sifat Fungsi Harmonik",
            "quiz": False,
            "text": (
                "Setiap fungsi skalar yang memenuhi Persamaan Laplace disebut Fungsi Harmonik. "
                "Fungsi harmonik memiliki dua sifat matematis yang sangat indah dan mendalam: "
                "Pertama, Teorema Nilai Rata-Rata Gauss: nilai potensial V pada sembarang titik pusat sama persis dengan nilai rata-rata potensial "
                "pada permukaan bola atau lingkaran yang berpusat di titik tersebut. "
                "Kedua, Prinsip Nilai Ekstremum: fungsi harmonik tidak pernah memiliki nilai maksimum lokal ataupun minimum lokal di dalam interior domain! "
                "Titik potensial tertinggi dan terendah mutlak selalu terletak pada batas tepi domain atau permukaan elektroda konduktor. "
                "Konsekuensi fisisnya: muatan elektrostatik bebas tidak dapat dipertahankan dalam kesetimbangan stabil murni di ruang hampa, "
                "yang dikenal sebagai Teorema Earnshaw."
            )
        },
        {
            "num": 6,
            "title": "Teorema Ketunggalan (Uniqueness) & Vektor Medan",
            "chapter": "06. Teorema Ketunggalan & Vektor Medan",
            "quiz": False,
            "text": (
                "Teorema Ketunggalan atau Uniqueness Theorem adalah landasan teoritis paling vital dalam komputasi elektromagnetika. "
                "Teorema ini membuktikan bahwa jika terdapat suatu fungsi potensial V yang memenuhi Persamaan Laplace di dalam suatu volume "
                "dan memenuhi seluruh syarat batas yang ditetapkan pada permukaan tertutup pembatasnya, "
                "maka fungsi V tersebut adalah satu-satunya solusi yang unik dan benar mutlak! "
                "Tidak ada kemungkinan solusi lain yang berbeda. "
                "Setelah distribusi potensial V x koma y ditemukan secara unik, vektor intensitas medan listrik E langsung diperoleh "
                "melalui operasi gradien diferensial: E sama dengan minus kurung parsial V per parsial x i topi ditambah parsial V per parsial y j topi. "
                "Vektor E selalu mengarah dari potensial tinggi ke potensial rendah dan tegak lurus garis ekuipotensial."
            )
        },
        {
            "num": 7,
            "title": "Metode Beda Hingga (FDM) & Relaksasi Gauss-Seidel / SOR",
            "chapter": "07. Beda Hingga FDM Gauss-Seidel",
            "quiz": False,
            "text": (
                "Untuk geometri elektroda yang rumit di mana solusi analitis deret tidak dapat diturunkan, "
                "insinyur menggunakan Metode Beda Hingga atau Finite Difference Method FDM. "
                "Dengan menerapkan ekspansi deret Taylor terpusat pada turunan spasial kedua di sekitar simpul i koma j dengan jarak kisi h: "
                "operator Laplacian tereduksi menjadi Stensil Lima Titik yang sangat sederhana: "
                "potensial simpul tengah V i j sama dengan rata-rata aritmatika dari empat simpul tetangganya: "
                "seperempat dikalikan kurung V kanan ditambah V kiri ditambah V atas ditambah V bawah. "
                "Persamaan aljabar ini diselesaikan secara iteratif menggunakan algoritma Relaksasi Gauss-Seidel atau Successive Over-Relaxation SOR "
                "hingga konvergensi tercapai."
            )
        },
        {
            "num": 8,
            "title": "Geometri Palung Konduktor & Garis Ekuipotensial 2D",
            "chapter": "08. Palung Konduktor & Ekuipotensial",
            "quiz": False,
            "text": (
                "Slide ini menampilkan kasus standar palung konduktor dua dimensi berpenampang persegi panjang. "
                "Ketiga dinding bawah, kiri, dan kanan dihubungkan ke tanah ground berpotensial nol Volt. "
                "Sedangkan pelat penutup bagian atas terisolasi dari dinding dan diberi tegangan tinggi seratus Volt. "
                "Garis-garis ekuipotensial membentuk kurva melengkung simetris yang memadat di dekat sudut atas elektroda. "
                "Garis fluks medan listrik E merambat melengkung keluar dari pelat atas menuju dinding ground. "
                "Kerapatan garis ekuipotensial secara visual mencerminkan besarnya intensitas medan listrik: "
                "semakin rapat garisnya, semakin kuat medan listrik dan semakin tinggi risiko lucutan dielektrik."
            )
        },
        {
            "num": 9,
            "title": "Contoh Terhitung: Evaluasi Potensial di Titik Pusat Palung",
            "chapter": "09. Contoh Soal Titik Pusat Palung",
            "quiz": False,
            "text": (
                "Mari kita selesaikan perhitungan potensial pada palung persegi dengan kisi kisi FDM sederhana. "
                "Diberikan kisi empat simpul internal simetris dengan dinding bawah, kiri, dan kanan nol Volt, serta pelat atas seratus Volt. "
                "Berdasarkan simetri cermin terhadap sumbu tengah, simpul kiri atas dan kanan atas memiliki nilai potensial identik V satu, "
                "sedangkan simpul kiri bawah dan kanan bawah memiliki nilai identik V dua. "
                "Menyusun stensil lima titik: empat V satu sama dengan seratus ditambah nol ditambah V satu ditambah V dua, "
                "dan empat V dua sama dengan V satu ditambah nol ditambah V dua ditambah nol. "
                "Menyelesaikan sistem dua persamaan linier ini menghasilkan V dua sama dengan dua belas koma lima Volt, "
                "dan V satu sama dengan tiga puluh tujuh koma lima Volt. "
                "Perhitungan FDM sederhana ini mendekati solusi analitis deret Fourier dengan deviasi di bawah tiga persen."
            )
        },
        {
            "num": 10,
            "title": "Contoh Terhitung: Intensitas Medan Listrik dari Gradien E = -nabla V",
            "chapter": "10. Contoh Soal Gradien Medan E",
            "quiz": False,
            "text": (
                "Setelah distribusi potensial diskrit diperoleh, kita hitung intensitas medan listrik E. "
                "Pada jarak kisi h sama dengan dua koma lima sentimeter atau nol koma nol dua lima meter, "
                "komponen medan vertikal E y di antara pelat atas seratus Volt dan simpul atas tiga puluh tujuh koma lima Volt "
                "dihitung melalui beda hingga: minus kurung seratus dikurang tiga puluh tujuh koma lima dibagi nol koma nol dua lima, "
                "menghasilkan E y sama dengan minus dua ribu lima ratus Volt per meter atau dua koma lima kilo Volt per meter ke arah bawah. "
                "Medan terkuat terkonsentrasi tepat pada celah sempit antara ujung pelat atas tegangan tinggi dan dinding samping ground."
            )
        },
        {
            "num": 11,
            "title": "Stres Dielektrik Rantai Isolator 150 kV & Kapasitansi Liar",
            "chapter": "11. Stres Rantai Isolator 150 kV",
            "quiz": False,
            "text": (
                "Penerapan industri yang sangat krusial dari Persamaan Laplace adalah rantai isolator gantung porselen pada menara transmisi SUTT 150 kV. "
                "Rantai isolator terdiri dari sekitar sepuluh piringan porselen yang dihubungkan secara seri. "
                "Jika hanya terdapat kapasitansi antar-piringan C, tegangan akan terbagi rata sepuluh persen per piringan. "
                "Namun dalam kenyataan fisik, terdapat Kapasitansi Liar ke Tiang Menara C satu akibat induksi medan elektrostatik ke rangka baja menara. "
                "Solusi persamaan beda potensial membuktikan bahwa distribusi tegangan di sepanjang rantai isolator bersifat sangat non-linier hiperbolik! "
                "Piringan terbawah yang paling dekat dengan konduktor fasa memikul stres tegangan tertinggi mencapai dua puluh lima hingga tiga puluh persen dari total tegangan sistem."
            )
        },
        {
            "num": 12,
            "title": "Standar Industri: Regulasi Medan Korona IEC 60060-1 & IEEE 4",
            "chapter": "12. Regulasi Korona IEC 60060-1",
            "quiz": False,
            "text": (
                "Konsentrasi medan listrik yang melebihi kekuatan dielektrik udara tiga puluh kilo Volt puncak per sentimeter pada kondisi standar atmosfer "
                "memicu ionisasi udara yang dikenal sebagai Lucutan Korona atau Corona Discharge. "
                "Korona menimbulkan rugi-rugi daya transmisi, derau suara mendesis, emisi gas ozon korosif, dan interferensi radio frekuensi. "
                "Standar industri IEC 60060-1 dan IEEE Standard 4 menetapkan regulasi ketat mengenai batas medan elektrostatik maksimum. "
                "Untuk meratakan medan listrik dan melindungi piringan isolator terbawah dari stres berlebih, "
                "insinyur PLN memasang Cincin Perata Korona atau Corona Ring berbahan aluminium di ujung bawah rantai isolator."
            )
        },
        {
            "num": 13,
            "title": "Praktikum Komputasi Julia: FDM Laplace 2D Isolator",
            "chapter": "13. Praktikum Julia: FDM Laplace 2D",
            "quiz": False,
            "text": (
                "Pada praktikum komputasi Julia ini, kita memprogram solver FDM relaksasi Gauss-Seidel dua dimensi untuk memetakan medan elektrostatik palung konduktor berisolasi. "
                "Dengan memanfaatkan matriks kisi berukuran lima puluh kali lima puluh simpul, kita lakukan iterasi relaksasi hingga toleransi residu konvergensi sepuluh pangkat minus lima. "
                "Grafik kontur berwarna di sebelah kanan menampilkan visualisasi garis ekuipotensial multi-warna, "
                "lengkap dengan panah-panah vektor gradien medan listrik E yang tegak lurus terhadap kurva potensial. "
                "Simulasi Julia ini memperlihatkan secara jelas konsentrasi medan elektrostatik di sudut elektroda tajam."
            )
        },
        {
            "num": 14,
            "title": "Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)",
            "chapter": "14. Kuis Interaktif & Evaluasi Bloom",
            "quiz": True,
            "text_part1": (
                "Saatnya kuis interaktif untuk menguji pemahaman elektrostatika Anda. Perhatikan studi kasus pada layar: "
                "Teorema nilai rata-rata Gauss untuk Persamaan Laplace Laplacian V sama dengan nol membuktikan bahwa potensial di setiap titik sama dengan rata-rata ruang sekelilingnya. "
                "Apakah konsekuensi fisis paling penting dari teorema ini? "
                "Pilihan A: Medan listrik bernilai nol di seluruh titik ruang bebas. "
                "Pilihan B: Potensial elektrostatika tidak pernah memiliki titik ekstremum lokal, di mana nilai maksimum atau minimum selalu wajib terletak di elektroda batas! "
                "Pilihan C: Partikel bermuatan dapat melayang stabil tanpa gaya luar di ruang hampa udara bebas. "
                "Pilihan D: Kapasitansi selalu bernilai konstan sepenuhnya independen dari geometri elektroda. "
                "Silakan analisis implikasi fisis teorema ini dan tentukan pilihan terbaik Anda dalam delapan detik ke depan."
            ),
            "text_part2": (
                "Waktu habis. Jawaban yang tepat adalah B: Potensial elektrostatika tidak pernah memiliki titik ekstremum lokal di ruang bebas! "
                "Jika ada titik potensial maksimum lokal di ruang bebas muatan, maka seluruh medan listrik di sekelilingnya akan memancar keluar. "
                "Hal ini menuntut divergensi medan listrik bernilai positif, yang secara langsung melanggar Hukum Gauss Laplacian V sama dengan nol. "
                "Konsekuensinya, partikel bermuatan tidak dapat dijebak melayang stabil secara elektrostatik statis sesuai Teorema Earnshaw. "
                "Pada kolom tantangan sebelah kanan, Anda juga ditantang membuktikan Teorema Ketunggalan solusi Poisson dengan identitas Green di level C4, "
                "mengevaluasi laju konvergensi Jacobi versus SOR di level C5, serta merancang cincin korona perata medan pada isolator seratus lima puluh kilo Volt di level C6."
            )
        },
        {
            "num": 15,
            "title": "Rangkuman Eksekutif & Jembatan ke Minggu 14",
            "chapter": "15. Rangkuman Eksekutif & Penutup",
            "quiz": False,
            "text": (
                "Sebagai rangkuman perkuliahan minggu ketiga belas: Pertama, Persamaan Laplace memodelkan distribusi medan potensial elektrostatik kesetimbangan tunak. "
                "Kedua, fungsi harmonik memiliki sifat nilai rata-rata dan nilai ekstremum yang hanya muncul di batas elektroda. "
                "Ketiga, Teorema Ketunggalan menjamin keunikan solusi numerik FDM. "
                "Dan keempat, pemahaman stres dielektrik sangat krusial dalam perancangan isolasi gardu induk bebas korona sesuai standar IEC 60060-1. "
                "Silakan pelajari modul ajar dan selesaikan Lembar Kerja serta Problem Set Minggu ketiga belas di portal ndaratha dot my dot id. "
                "Pada minggu keempat belas, kita akan mempelajari Fungsi Khusus Persamaan Bessel pada koordinat silinder dan fenomena skin effect pada konduktor ACSR. Terima kasih dan wassalamualaikum warahmatullahi wabarakatuh."
            )
        }
    ]
}
