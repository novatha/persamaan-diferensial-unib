#!/usr/bin/env python3
"""
build_video_w01_v2.py  — Versi 2.0 (Semua Kelemahan Diperbaiki)

Perbaikan vs v1.0:
  [1] Audio Stereo AAC 192 kbps (bukan Mono ~81 kbps)
  [2] Slide Sub-CPMK OBE C1-C4 ditambahkan
  [3] Slide Demo Julia DifferentialEquations.jl (Pilar 3) ditambahkan
  [4] Footer bar diperbaiki: "Daratha & Arfan | Teknik Elektro UNIB"
  [5] Kuis interaktif: jeda 8 detik terprogram sebelum jawaban
  [6] Slide dikonsolidasi: 34 -> 20 slide (lebih padat)
  [7] Diagram circuitikz rangkaian RL
  [8] Video CRF 18 (lebih tinggi dari CRF 20)
"""
import subprocess, os, time, asyncio, edge_tts

# ==============================================================================
# DATA SLIDE v2.0 (20 slide, lebih padat)
# ==============================================================================
slides_data = [
    {"slide_num":1, "title":"Judul & Pembukaan Kuliah",
     "chapter":"01. Pembukaan Perkuliahan Persamaan Diferensial", "quiz_pause":0,
     "text":(
        "Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, "
        "selamat datang dalam perkuliahan daring Persamaan Diferensial semester genap 2026. "
        "Mata kuliah ini dirancang khusus untuk membangun fondasi analisis matematika yang kokoh "
        "dalam memodelkan fenomena fisis kelistrikan dan elektromagnetika. "
        "Pada pertemuan perdana minggu pertama ini, kita akan membahas: "
        "Klasifikasi PDB dan PDP, Konsep Orde dan Derajat, Syarat Linieritas, "
        "Solusi Umum versus Solusi Khusus, Masalah Nilai Awal atau Initial Value Problem, "
        "serta Pemodelan Fisis Rangkaian Listrik berbasis Hukum Kirchhoff. "
        "Kuliah ini diampu bersama saya, Insinyur Novalio Daratha dan Bapak Muhammad Arfan."
     )},
    {"slide_num":2, "title":"Sub-CPMK & Capaian Pembelajaran OBE",
     "chapter":"02. Capaian Pembelajaran Minggu 1", "quiz_pause":0,
     "text":(
        "Sebelum memulai materi, mari kita pahami Capaian Pembelajaran Mata Kuliah minggu ini. "
        "Pada level C1 Mengingat, mahasiswa mampu mendefinisikan PDB dan PDP "
        "serta membedakan konsep orde, derajat, dan linieritas. "
        "Pada level C2 Memahami, mahasiswa mampu menjelaskan makna fisis "
        "konstanta integrasi dan kondisi awal pada rangkaian listrik. "
        "Pada level C3 Menerapkan, mahasiswa mampu menurunkan dan menyelesaikan "
        "PDB orde satu dari rangkaian RL menggunakan Hukum Tegangan Kirchhoff. "
        "Dan pada level C4 Menganalisis, mahasiswa mampu menganalisis sifat "
        "transien peluruhan eksponensial dan mengidentifikasi konstanta waktu tau. "
        "Seluruh capaian ini sejalan dengan Sub-CPMK pada Lembar Kerja "
        "dan Problem Set Minggu Pertama."
     )},
    {"slide_num":3, "title":"Agenda & Peta Konsep Minggu 1",
     "chapter":"03. Agenda Pembelajaran Pekan 1", "quiz_pause":0,
     "text":(
        "Berikut adalah empat pilar agenda pembahasan kita hari ini. "
        "Pertama, komparasi fundamental antara PDB dan PDP "
        "beserta klasifikasi orde, derajat, dan linieritas. "
        "Kedua, konsep keluarga kurva solusi umum dan penentuan solusi khusus "
        "melalui Initial Value Problem. "
        "Ketiga, penurunan model matematika rangkaian RL dari Hukum Tegangan Kirchhoff "
        "secara first-principles. "
        "Dan keempat, demonstrasi komputasi numerik menggunakan Julia "
        "dan paket DifferentialEquations dot j l untuk memvisualisasikan "
        "kurva transien secara interaktif."
     )},
    {"slide_num":4, "title":"PDB vs PDP: Definisi & Contoh Teknik Elektro",
     "chapter":"04. Konsep Dasar PDB dan PDP", "quiz_pause":0,
     "text":(
        "Mari kita mulai dari definisi. "
        "Persamaan Diferensial Biasa atau PDB adalah persamaan yang memuat turunan "
        "terhadap satu variabel bebas tunggal, misalnya waktu t. "
        "Dalam Teknik Elektro, PDB memodelkan sistem elemen terpusat: "
        "pengosongan kapasitor, R d q per d t ditambah satu per C q sama dengan nol, "
        "atau osilasi rangkaian RLC, L d kuadrat i per d t kuadrat ditambah R d i per d t "
        "ditambah satu per C i sama dengan nol. "
        "Berbeda dengan PDB, Persamaan Diferensial Parsial atau PDP memuat turunan parsial "
        "terhadap dua atau lebih variabel bebas, misalnya spasial x, y, dan waktu t. "
        "PDP memodelkan fenomena terdistribusi seperti Persamaan Laplace "
        "untuk distribusi potensial elektrostatika, "
        "dan Persamaan Gelombang untuk perambatan sinyal pada saluran transmisi."
     )},
    {"slide_num":5, "title":"Kuis 1: Klasifikasi Persamaan",
     "chapter":"05. Kuis Interaktif: Klasifikasi PDB vs PDP", "quiz_pause":8,
     "text":(
        "Waktunya kuis interaktif! "
        "Perhatikan tiga persamaan berikut di layar. "
        "Nomor satu: turunan ketiga y terhadap x dikurang empat x d y per d x sama dengan e pangkat x. "
        "Nomor dua: parsial u per parsial t sama dengan alpha kuadrat "
        "jumlah parsial kuadrat u per parsial x kuadrat "
        "ditambah parsial kuadrat u per parsial y kuadrat. "
        "Nomor tiga: L d i per d t ditambah R i sama dengan V nol sinus omega t. "
        "Tentukan mana yang PDB dan mana yang PDP! "
        "Silakan jawab dulu sebelum melanjutkan. Anda punya delapan detik untuk berpikir."
     )},
    {"slide_num":6, "title":"Kuis 1: Analisis Jawaban Lengkap",
     "chapter":"06. Pembahasan Kuis Klasifikasi", "quiz_pause":0,
     "text":(
        "Berikut pembahasannya. "
        "Persamaan nomor satu adalah PDB, karena hanya memiliki satu variabel bebas x "
        "dan turunannya bersifat turunan biasa. "
        "Persamaan nomor dua adalah PDP, karena memiliki tiga variabel bebas sekaligus: "
        "waktu t dan koordinat spasial x dan y. "
        "Ini merepresentasikan difusi panas atau penetrasi medan elektromagnetik ke konduktor, "
        "fenomena yang dikenal sebagai efek kulit atau skin effect. "
        "Persamaan nomor tiga adalah PDB, karena satu-satunya variabel bebas "
        "yang mengatur dinamika arus adalah waktu t, "
        "meskipun di ruas kanan terdapat fungsi sinusoidal."
     )},
    {"slide_num":7, "title":"Orde vs Derajat: Jangan Tertukar!",
     "chapter":"07. Klasifikasi PDB: Orde dan Derajat", "quiz_pause":0,
     "text":(
        "Klasifikasi berikutnya adalah Orde dan Derajat. "
        "Orde ditentukan oleh orde turunan tertinggi di dalam persamaan. "
        "Contoh pertama: y double prime ditambah tiga y prime ditambah dua y sama dengan nol "
        "adalah PDB Orde dua, karena ada suku y double prime. "
        "Contoh kedua yang sering mengecoh: "
        "kurung d y per d t tutup pangkat tiga, ditambah y sama dengan nol. "
        "Persamaan ini tetap PDB Orde satu! "
        "Turunan tertingginya hanya d y per d t, yaitu turunan pertama. "
        "Angka tiga di luar tanda kurung adalah Derajat aljabar, bukan orde turunan. "
        "Ingat: Orde menyatakan seberapa tinggi turunan, "
        "sedangkan Derajat menyatakan seberapa besar pangkat aljabar dari turunan tersebut."
     )},
    {"slide_num":8, "title":"Tiga Syarat Linieritas & Uji Kasus",
     "chapter":"08. Syarat Linieritas Persamaan Diferensial", "quiz_pause":0,
     "text":(
        "Klasifikasi ketiga adalah Linieritas. "
        "Suatu PDB dinyatakan linier jika memenuhi tiga syarat mutlak. "
        "Pertama, variabel terikat dan seluruh turunannya hanya boleh berpangkat satu. "
        "Kedua, tidak ada perkalian silang antara variabel terikat dengan turunannya sendiri. "
        "Ketiga, tidak ada fungsi transendental yang memuat variabel terikat, "
        "seperti sinus y atau eksponensial y. "
        "Kasus satu: d kuadrat x per d t kuadrat ditambah lima x sama dengan sinus t, "
        "ini Linier, karena sinus t bekerja pada variabel bebas t. "
        "Kasus dua: d y per d x ditambah y kuadrat sama dengan nol, "
        "ini Non-Linier karena y berpangkat dua merusak prinsip superposisi. "
        "Kasus tiga: cosinus x dikali d y per d x sama dengan y, "
        "ini Linier karena cosinus x hanyalah koefisien pada variabel bebas x."
     )},
    {"slide_num":9, "title":"Kuis 2: Linier atau Non-Linier?",
     "chapter":"09. Kuis Interaktif: Uji Linieritas", "quiz_pause":8,
     "text":(
        "Kuis kedua. "
        "Perhatikan persamaan: d y per d x ditambah y dikali d y per d x sama dengan x. "
        "Apakah persamaan ini Linier atau Non-Linier? "
        "Periksa ketiga syarat linieritas dengan teliti. "
        "Silakan berpikir selama delapan detik."
     )},
    {"slide_num":10, "title":"Kuis 2: Jawaban & Penjelasan",
     "chapter":"10. Pembahasan Kuis Linieritas", "quiz_pause":0,
     "text":(
        "Jawabannya adalah Non-Linier! "
        "Perhatikan suku y dikali d y per d x. "
        "Ini adalah perkalian antara variabel terikat y dengan turunannya d y per d x. "
        "Hal ini melanggar syarat kedua linieritas secara eksplisit. "
        "Kehadiran suku perkalian silang ini menghancurkan prinsip superposisi "
        "dan menjadikan persamaan ini non-linier."
     )},
    {"slide_num":11, "title":"Solusi Umum & Solusi Khusus: Keluarga Kurva",
     "chapter":"11. Solusi Umum dan Initial Value Problem", "quiz_pause":0,
     "text":(
        "Kini kita beralih ke konsep Solusi. "
        "Solusi umum adalah solusi analitis yang masih memuat konstanta integrasi sembarang C, "
        "dan merepresentasikan seluruh keluarga kurva tak hingga di bidang koordinat, "
        "misalnya y t sama dengan C e pangkat t. "
        "Di dunia rekayasa nyata, tegangan kapasitor atau arus induktor "
        "pada saat saklar dinyalakan memiliki nilai yang pasti dan terukur. "
        "Inilah yang disebut Initial Condition atau kondisi awal. "
        "Jika diberikan syarat awal y pada saat t sama dengan nol bernilai dua, "
        "maka kita dapat mengunci konstanta C sama dengan dua, "
        "menghasilkan Solusi Khusus unik, yaitu satu lintasan kurva "
        "yang persis melewati titik koordinat nol koma dua."
     )},
    {"slide_num":12, "title":"Contoh Hitungan IVP Lengkap: 4 Langkah",
     "chapter":"12. Perhitungan Step-by-Step IVP", "quiz_pause":0,
     "text":(
        "Mari kita buktikan melalui contoh hitungan Masalah Nilai Awal. "
        "Diberikan PDB peluruhan: d y per d t sama dengan minus tiga y, "
        "dengan syarat awal y nol sama dengan sepuluh. "
        "Langkah satu: dengan metode pemisahan variabel, "
        "kita peroleh solusi umum: y t sama dengan C dikali e pangkat minus tiga t. "
        "Langkah dua: kita terapkan syarat awal, y pada saat t sama dengan nol adalah sepuluh. "
        "Langkah tiga: substitusikan t sama dengan nol ke solusi umum. "
        "Sepuluh sama dengan C dikali e pangkat nol, e pangkat nol sama dengan satu, "
        "maka C sama dengan sepuluh. "
        "Langkah empat: masukkan C sama dengan sepuluh. "
        "Solusi khusus akhir: y t sama dengan sepuluh dikali e pangkat minus tiga t. "
        "Fungsi ini merepresentasikan peluruhan eksponensial transien yang stabil menuju nol."
     )},
    {"slide_num":13, "title":"Pemodelan Rangkaian RL dari Hukum KVL",
     "chapter":"13. Pemodelan Fisis Rangkaian RL", "quiz_pause":0,
     "text":(
        "Sekarang kita masuki Pilar keempat: "
        "menghubungkan matematika dengan rekayasa nyata melalui penurunan first-principles. "
        "Perhatikan rangkaian seri resistor R dan induktor L "
        "yang terhubung dengan sumber tegangan V t. "
        "Berdasarkan Hukum Tegangan Kirchhoff atau KVL, "
        "jumlah aljabar tegangan pada loop tertutup harus sama dengan nol. "
        "Tegangan jatuh pada resistor V R sama dengan arus i t dikalikan R, "
        "mengikuti Hukum Ohm disipatif. "
        "Tegangan induktor V L sama dengan L dikalikan laju perubahan arus d i per d t, "
        "mengikuti Hukum Induksi Faraday. "
        "Induktor melawan perubahan arus sesaat dengan membangkitkan "
        "gaya gerak listrik induksi diri. "
        "Dengan mensubstitusikan kedua hubungan konstitutif ini ke KVL, "
        "kita memperoleh model matematika akhir: L d i per d t ditambah R i sama dengan V t. "
        "Inilah bentuk kanonik PDB linier orde satu non-homogen."
     )},
    {"slide_num":14, "title":"Kuis 3: Hitung Konstanta Waktu Tau",
     "chapter":"14. Kuis Interaktif: Konstanta Waktu", "quiz_pause":8,
     "text":(
        "Kuis ketiga untuk menguji Pilar dua analisis mendalam. "
        "Pada rangkaian RL seri dengan R sama dengan dua ratus ohm "
        "dan L sama dengan lima puluh mili henry, "
        "berapakah konstanta waktu tau dalam mikro detik? "
        "Ingat: konstanta waktu tau sama dengan L per R. "
        "Silakan hitung dalam delapan detik sebelum melihat jawabannya."
     )},
    {"slide_num":15, "title":"Kuis 3: Jawaban & Makna Fisis Tau",
     "chapter":"15. Pembahasan Kuis Konstanta Waktu", "quiz_pause":0,
     "text":(
        "Jawabannya adalah tau sama dengan L per R "
        "sama dengan lima puluh mili henry dibagi dua ratus ohm "
        "sama dengan dua ratus lima puluh mikro detik. "
        "Secara fisis, konstanta waktu tau adalah waktu yang dibutuhkan arus "
        "untuk mencapai sekitar enam puluh tiga persen dari nilai tunak finalnya. "
        "Setelah lima kali tau atau sekitar satu koma dua lima mili detik, "
        "arus dianggap telah mencapai kondisi mantap. "
        "Semakin besar induktansi L atau semakin kecil resistansi R, "
        "semakin lambat respons transiennya."
     )},
    {"slide_num":16, "title":"Pilar 3: Demo Julia DifferentialEquations.jl",
     "chapter":"16. Demo Julia: Kurva Transien RL", "quiz_pause":0,
     "text":(
        "Pilar ketiga kita adalah komputasi numerik terbuka menggunakan Julia. "
        "Di layar Anda dapat melihat kode Julia menggunakan paket "
        "DifferentialEquations dot j l dan Plots dot j l. "
        "Kita mendefinisikan fungsi ODE: "
        "arus prima t, i, p, t sama dengan kurung V nol dikurang R dikali i tutup per L. "
        "Dengan kondisi awal i nol sama dengan nol ampere, "
        "parameter R sama dengan dua ratus ohm dan L sama dengan lima puluh mili henry. "
        "Solver Tsit5 menyelesaikan sistem ini dalam mili detik. "
        "Grafik yang dihasilkan menunjukkan kurva transien arus "
        "yang mendekat secara asimptotik menuju nilai tunak V nol per R, "
        "melewati titik enam puluh tiga persen nilai akhir tepat pada waktu tau. "
        "Kode ini tersedia lengkap di portal ndaratha dot my dot id "
        "untuk Anda eksplorasi secara mandiri di laptop."
     )},
    {"slide_num":17, "title":"Interpretasi Grafik: Tiga Zona Respons Transien",
     "chapter":"17. Analisis Grafik Respons Transien", "quiz_pause":0,
     "text":(
        "Perhatikan grafik kurva transien yang dihasilkan Julia. "
        "Sumbu horizontal adalah waktu, sedangkan sumbu vertikal adalah arus. "
        "Tiga zona penting yang harus Anda pahami: "
        "Pertama, zona kenaikan cepat dari nol hingga satu kali tau, "
        "di mana arus naik paling tajam dengan gradien maksimum. "
        "Kedua, zona konvergensi dari satu tau hingga tiga tau, "
        "di mana kecepatan kenaikan melambat secara eksponensial. "
        "Ketiga, zona mantap setelah lima tau, "
        "di mana arus praktis konstan di nilai V nol per R. "
        "Inilah yang dimaksud respons overdamped murni pada sistem RL orde satu tanpa osilasi. "
        "Bandingkan dengan sistem RLC orde dua yang akan kita pelajari pada minggu berikutnya, "
        "di mana respons dapat berosilasi teredam bergantung pada rasio redaman zeta."
     )},
    {"slide_num":18, "title":"Jembatan ke Persamaan Maxwell",
     "chapter":"18. Relevansi ke Medan Elektromagnetika", "quiz_pause":0,
     "text":(
        "Sebelum menutup, mari kita lihat relevansi materi hari ini "
        "dengan mata kuliah Medan Elektromagnetika. "
        "Hukum Induksi Faraday yang kita gunakan untuk tegangan induktor V L sama dengan L d i per d t "
        "adalah bentuk integral dari Persamaan Faraday Maxwell: "
        "curl E sama dengan minus parsial B per parsial t. "
        "Hukum Ohm disipatif V R sama dengan R i "
        "adalah bentuk makroskopik dari Hubungan Konstitutif J sama dengan sigma E. "
        "Dengan demikian, Persamaan Diferensial yang Anda pelajari hari ini "
        "adalah fondasi matematis utama dari keempat Persamaan Maxwell "
        "yang akan Anda kuasai sepenuhnya pada mata kuliah Medan Elektromagnetika."
     )},
    {"slide_num":19, "title":"Rangkuman: 4 Pilar Minggu 1",
     "chapter":"19. Rangkuman Perkuliahan Minggu 01", "quiz_pause":0,
     "text":(
        "Sebagai rangkuman perkuliahan minggu pertama kita berdasarkan empat pilar. "
        "Pilar satu Intuisi Fisik: PDB memodelkan sistem terpusat dengan satu variabel bebas, "
        "PDP memodelkan medan terdistribusi multi-variabel. "
        "Pilar dua Derivasi Matematis: Orde ditentukan oleh turunan tertinggi, "
        "linieritas mensyaratkan tidak ada suku berpangkat lebih dari satu atau perkalian silang. "
        "Solusi umum dikonversi menjadi solusi khusus melalui Initial Value Problem. "
        "Pilar tiga Komputasi Julia: kurva transien i t divisualisasikan "
        "dengan DifferentialEquations dot j l dan Plots dot j l secara real-time. "
        "Pilar empat Standar Industri: model PDB rangkaian RL adalah fondasi analisis transien "
        "pada transformator, motor, dan saluran transmisi sesuai standar IEEE. "
        "Silakan unduh salindia, kerjakan Lembar Kerja dan Problem Set Minggu satu "
        "yang tersedia di portal ndaratha dot my dot id."
     )},
    {"slide_num":20, "title":"Pratinjau Minggu 2 & Penutup",
     "chapter":"20. Penutup & Pratinjau Minggu 02", "quiz_pause":0,
     "text":(
        "Pada minggu kedua, kita akan membedah secara tuntas tiga metode analitis "
        "penyelesaian PDB orde satu: "
        "Metode Separabel, Persamaan Eksak berbasis medan konservatif dan fungsi potensial, "
        "serta Faktor Integrasi pengubah persamaan non-eksak menjadi eksak. "
        "Seluruh metode ini akan langsung diaplikasikan pada analisis transien rangkaian RC dan RL. "
        "Saya, Insinyur Novalio Daratha bersama Bapak Muhammad Arfan, "
        "mengucapkan terima kasih atas fokus dan semangat belajar Anda hari ini. "
        "Jangan ragu mengajukan pertanyaan melalui forum diskusi di portal. "
        "Wassalamu'alaikum warahmatullahi wabarakatuh."
     )},
]

# ==============================================================================
# KONFIGURASI
# ==============================================================================
VOICE            = "id-ID-ArdiNeural"
OUTPUT_DIR       = "scratch/audio_w01_v2"
FRAMES_DIR       = "scratch/slide_frames_w01_v2"
CLIPS_DIR        = "scratch/clips_w01_v2"
VIDEO_OUT        = "scratch/video_pd_minggu01_v2.mp4"
ROOT_VIDEO       = "video_pd_minggu01.mp4"
SCRIPT_MD        = "video_script_pd_w01_v2.md"
QUIZ_PAUSE_AUDIO = "scratch/quiz_pause_8s.mp3"

# ==============================================================================
# TEMPLATE LaTeX BEAMER v2.0
# ==============================================================================
PREAMBLE = r"""\documentclass[aspectratio=169,10pt]{beamer}
\usetheme{Madrid}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usepackage{circuitikz}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{tcolorbox}
\tcbuselibrary{skins}

\definecolor{unibblue}{RGB}{45,54,145}
\definecolor{unibgold}{RGB}{212,175,55}
\definecolor{unibgreen}{RGB}{0,128,64}
\definecolor{juliagreen}{RGB}{0,150,80}
\definecolor{juliared}{RGB}{200,40,40}
\definecolor{juliapurple}{RGB}{130,0,200}
\definecolor{codebg}{RGB}{248,248,255}

\setbeamercolor{palette primary}{bg=unibblue,fg=white}
\setbeamercolor{palette secondary}{bg=unibblue!80!black,fg=white}
\setbeamercolor{palette tertiary}{bg=unibblue!60!black,fg=white}
\setbeamercolor{structure}{fg=unibblue}
\setbeamercolor{frametitle}{fg=white,bg=unibblue}

% PERBAIKAN FOOTER: separator | antara nama & prodi
\setbeamertemplate{footline}{
  \leavevmode\hbox{%
    \begin{beamercolorbox}[wd=.38\paperwidth,ht=2.5ex,dp=1ex,center]{palette primary}
      \usebeamerfont{author in head/foot}\insertshortauthor
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=.42\paperwidth,ht=2.5ex,dp=1ex,center]{palette secondary}
      \usebeamerfont{title in head/foot}\insertshorttitle
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=.20\paperwidth,ht=2.5ex,dp=1ex,right]{palette tertiary}
      \usebeamerfont{date in head/foot}\insertshortdate{}\hspace*{0.5em}
      \insertframenumber/\inserttotalframenumber\hspace*{1ex}
    \end{beamercolorbox}}%
}

\lstset{
  basicstyle=\ttfamily\scriptsize,
  keywordstyle=\color{juliapurple}\bfseries,
  commentstyle=\color{juliagreen}\itshape,
  stringstyle=\color{juliared},
  backgroundcolor=\color{codebg},
  frame=single, rulecolor=\color{unibblue!30},
  showstringspaces=false, breaklines=true,
  numbers=left, numberstyle=\tiny\color{gray},
  numbersep=4pt, xleftmargin=8pt,
}

\title[Persamaan Diferensial]{Persamaan Diferensial}
\subtitle{Minggu 1: Klasifikasi PDB/PDP, IVP \& Pemodelan Fisik}
\author[Daratha \& Arfan~|~Teknik Elektro UNIB]{Novalio Daratha \& Muhammad Arfan}
\institute[Teknik Elektro UNIB]{Program Studi Teknik Elektro -- Universitas Bengkulu}
\date{2026}
"""

def build_beamer(slides):
    out = [PREAMBLE, r"\begin{document}", r"\begin{frame}\titlepage\end{frame}"]
    for item in slides:
        sn = item["slide_num"]
        if sn == 1:
            continue  # titlepage sudah di atas
        elif sn == 2:
            out += [
                r"\begin{frame}{Sub-CPMK \& Capaian Pembelajaran OBE}",
                r"\begin{tcolorbox}[colback=unibblue!8,colframe=unibblue,title={\textbf{Capaian Minggu 1 (OBE)}},fonttitle=\bfseries]",
                r"\begin{itemize}\setlength\itemsep{3pt}",
                r"  \item \textbf{C1 Mengingat:} Definisi PDB, PDP, orde, derajat, linieritas",
                r"  \item \textbf{C2 Memahami:} Makna fisis konstanta integrasi \& kondisi awal",
                r"  \item \textbf{C3 Menerapkan:} Turunkan \& selesaikan PDB orde-1 RL via KVL",
                r"  \item \textbf{C4 Menganalisis:} Analisis $i(t)$ transien \& identifikasi $\tau$",
                r"\end{itemize}",
                r"\end{tcolorbox}",
                r"\end{frame}",
            ]
        elif sn == 3:
            out += [
                r"\begin{frame}{Agenda \& Peta Konsep Minggu 1}",
                r"\begin{columns}[T]",
                r"\column{0.55\textwidth}",
                r"\begin{enumerate}\setlength\itemsep{6pt}",
                r"  \item \textbf{PDB vs PDP} -- Klasifikasi, Orde, Linieritas",
                r"  \item \textbf{Solusi Umum \& IVP} -- Keluarga Kurva",
                r"  \item \textbf{Model RL} -- \emph{First-principles} via KVL",
                r"  \item \textbf{Julia Demo} -- \texttt{DifferentialEquations.jl}",
                r"\end{enumerate}",
                r"\column{0.42\textwidth}",
                r"\begin{tcolorbox}[colback=unibgold!15,colframe=unibgold,title={\small\textbf{4 Pilar OBE}},fonttitle=\bfseries]",
                r"\footnotesize",
                r"\textcolor{unibblue}{\textbf{P1}} Intuisi Fisik\\",
                r"\textcolor{unibblue}{\textbf{P2}} Derivasi Matematis\\",
                r"\textcolor{juliagreen}{\textbf{P3}} Komputasi Julia\\",
                r"\textcolor{juliared}{\textbf{P4}} Standar Industri IEEE",
                r"\end{tcolorbox}",
                r"\end{columns}",
                r"\end{frame}",
            ]
        elif sn == 4:
            out += [
                r"\begin{frame}{PDB vs PDP: Definisi \& Contoh Teknik Elektro}",
                r"\begin{columns}[T]",
                r"\column{0.48\textwidth}",
                r"\begin{block}{\textbf{Persamaan Diferensial Biasa (PDB)}}",
                r"\footnotesize Turunan terhadap \textbf{satu variabel bebas} $t$.\\[4pt]",
                r"$R\frac{dq}{dt}+\frac{1}{C}q=0~~\leftarrow$ RC\\[2pt]",
                r"$L\frac{d^2i}{dt^2}+R\frac{di}{dt}+\frac{i}{C}=0~~\leftarrow$ RLC",
                r"\end{block}",
                r"\column{0.48\textwidth}",
                r"\begin{block}{\textbf{Persamaan Diferensial Parsial (PDP)}}",
                r"\footnotesize Turunan parsial $\geq 2$ variabel bebas.\\[4pt]",
                r"$\nabla^2 V=0~~\leftarrow$ Laplace (Elektrostatik)\\[2pt]",
                r"$\frac{\partial^2 E}{\partial z^2}=\mu\epsilon\frac{\partial^2 E}{\partial t^2}~~\leftarrow$ Gelombang EM",
                r"\end{block}",
                r"\end{columns}",
                r"\end{frame}",
            ]
        elif sn == 5:
            out += [
                r"\begin{frame}{Kuis Interaktif: PDB atau PDP?}",
                r"\begin{tcolorbox}[colback=unibgold!10,colframe=unibgold,title={\textbf{Klasifikasikan 3 Persamaan!}},fonttitle=\bfseries]",
                r"\begin{enumerate}\setlength\itemsep{8pt}",
                r"  \item $\dfrac{d^3y}{dx^3}-4x\dfrac{dy}{dx}=e^x$",
                r"  \item $\dfrac{\partial u}{\partial t}=\alpha^2\!\left(\dfrac{\partial^2 u}{\partial x^2}+\dfrac{\partial^2 u}{\partial y^2}\right)$",
                r"  \item $L\dfrac{di}{dt}+Ri=V_0\sin\omega t$",
                r"\end{enumerate}",
                r"\end{tcolorbox}",
                r"\vspace{4pt}",
                r"\centering\textcolor{juliared}{\textbf{$\Rightarrow$ Jawab dulu! Jawaban muncul setelah 8 detik\ldots}}",
                r"\end{frame}",
            ]
        elif sn == 6:
            out += [
                r"\begin{frame}{Kuis 1: Pembahasan Jawaban}",
                r"\begin{enumerate}\setlength\itemsep{6pt}",
                r"  \item $\frac{d^3y}{dx^3}-4x\frac{dy}{dx}=e^x$\hfill\textcolor{unibblue}{\textbf{PDB}} -- satu variabel bebas $x$",
                r"  \item $\frac{\partial u}{\partial t}=\alpha^2(\ldots)$\hfill\textcolor{juliared}{\textbf{PDP}} -- variabel $t,x,y$",
                r"  \item $L\frac{di}{dt}+Ri=V_0\sin\omega t$\hfill\textcolor{unibblue}{\textbf{PDB}} -- satu variabel bebas $t$",
                r"\end{enumerate}",
                r"\vspace{6pt}",
                r"\begin{tcolorbox}[colback=unibgreen!8,colframe=unibgreen,title={\small\textbf{Kunci Pembeda}},fonttitle=\bfseries]",
                r"\footnotesize\textbf{PDB}: $\frac{d}{dx}$ (turunan biasa)\quad\textbf{PDP}: $\frac{\partial}{\partial x}$ (turunan parsial, $\geq2$ variabel)",
                r"\end{tcolorbox}",
                r"\end{frame}",
            ]
        elif sn == 7:
            out += [
                r"\begin{frame}{Orde vs Derajat: Jangan Tertukar!}",
                r"\begin{columns}[T]",
                r"\column{0.48\textwidth}",
                r"\begin{block}{\textbf{Contoh 1: Orde 2}}",
                r"$y''+3y'+2y=0$\\[6pt]",
                r"\footnotesize Suku $y''$: turunan ke-2\\$\Rightarrow$ \textbf{PDB Orde 2, Derajat 1}",
                r"\end{block}",
                r"\vspace{8pt}",
                r"\begin{block}{\textbf{Contoh 2: Sering Mengecoh!}}",
                r"$\left(\dfrac{dy}{dt}\right)^3+y=0$\\[6pt]",
                r"\footnotesize Turunan tertinggi: $\frac{dy}{dt}$ (orde 1)\\Pangkat 3 = \textbf{Derajat aljabar}\\$\Rightarrow$ \textbf{PDB Orde 1, Derajat 3}",
                r"\end{block}",
                r"\column{0.48\textwidth}",
                r"\begin{tcolorbox}[colback=juliared!8,colframe=juliared,title={\small\textbf{Ingat Selalu!}},fonttitle=\bfseries]",
                r"\small\textbf{Orde} = orde turunan tertinggi\\[4pt]\textbf{Derajat} = pangkat aljabar\\dari turunan tertinggi\\[4pt]Keduanya \textbf{berbeda konsep}!",
                r"\end{tcolorbox}",
                r"\end{columns}",
                r"\end{frame}",
            ]
        elif sn == 8:
            out += [
                r"\begin{frame}{Tiga Syarat Linieritas \& Uji Kasus}",
                r"\begin{tcolorbox}[colback=unibblue!6,colframe=unibblue,title={\textbf{Syarat Linieritas PDB}},fonttitle=\bfseries]",
                r"\footnotesize\begin{enumerate}",
                r"  \item $y$ dan turunannya \textbf{berpangkat 1}",
                r"  \item \textbf{Tidak ada} perkalian $y\cdot y^{(n)}$",
                r"  \item \textbf{Tidak ada} $\sin y$, $e^y$, $\ln y$",
                r"\end{enumerate}",
                r"\end{tcolorbox}",
                r"\vspace{4pt}\footnotesize",
                r"\begin{tabular}{lll}\hline\rule{0pt}{2.2ex}",
                r"\textbf{Persamaan} & \textbf{Status} & \textbf{Alasan}\\\hline\rule{0pt}{2.2ex}",
                r"$\ddot{x}+5x=\sin t$ & \textcolor{unibgreen}{\textbf{Linier}} & $\sin t$ pada $t$\\[2pt]",
                r"$\frac{dy}{dx}+y^2=0$ & \textcolor{juliared}{\textbf{Non-linier}} & $y^2$ melanggar syarat 1\\[2pt]",
                r"$\cos x\frac{dy}{dx}=y$ & \textcolor{unibgreen}{\textbf{Linier}} & $\cos x$ koefisien $x$\\\hline",
                r"\end{tabular}",
                r"\end{frame}",
            ]
        elif sn == 9:
            out += [
                r"\begin{frame}{Kuis 2: Linier atau Non-Linier? (Soal)}",
                r"\begin{tcolorbox}[colback=unibgold!10,colframe=unibgold,title={\textbf{Uji Linieritas!}},fonttitle=\bfseries]",
                r"\vspace{6pt}\centering$\dfrac{dy}{dx}+y\,\dfrac{dy}{dx}=x$\vspace{6pt}",
                r"\end{tcolorbox}",
                r"\vspace{8pt}\textbf{Periksa ketiga syarat linieritas!}\\[4pt]",
                r"\centering\textcolor{juliared}{\textbf{$\Rightarrow$ Jawab dulu! Jawaban muncul setelah 8 detik\ldots}}",
                r"\end{frame}",
            ]
        elif sn == 10:
            out += [
                r"\begin{frame}{Kuis 2: Jawaban \& Penjelasan}",
                r"\begin{tcolorbox}[colback=juliared!8,colframe=juliared,title={\textbf{Non-Linier!}},fonttitle=\bfseries]",
                r"$\dfrac{dy}{dx}+\underbrace{y\,\dfrac{dy}{dx}}_{\textcolor{juliared}{\text{Perkalian silang!}}}=x$",
                r"\end{tcolorbox}",
                r"\vspace{6pt}\begin{itemize}\setlength\itemsep{4pt}",
                r"  \item Suku $y\cdot\frac{dy}{dx}$ = perkalian variabel terikat dengan turunannya",
                r"  \item Melanggar \textbf{Syarat 2} linieritas",
                r"  \item Prinsip superposisi \textbf{tidak berlaku}",
                r"\end{itemize}",
                r"\end{frame}",
            ]
        elif sn == 11:
            out += [
                r"\begin{frame}{Solusi Umum vs Solusi Khusus: Keluarga Kurva}",
                r"\begin{columns}[T]",
                r"\column{0.48\textwidth}",
                r"\begin{block}{\textbf{Solusi Umum}}",
                r"Masih memuat konstanta $C$.\\$y'=y\implies y(t)=Ce^t$\\[4pt]",
                r"\footnotesize Merepresentasikan \textbf{keluarga kurva} tak hingga.",
                r"\end{block}\vspace{6pt}",
                r"\begin{block}{\textbf{Solusi Khusus (IVP)}}",
                r"Jika $y(0)=2\implies C=2$\\$\implies y(t)=2e^t$\\[4pt]",
                r"\footnotesize Kurva \textcolor{juliared}{\textbf{merah}} melewati $(0,2)$.",
                r"\end{block}",
                r"\column{0.48\textwidth}",
                r"\begin{tikzpicture}[scale=0.85]",
                r"  \draw[->](-0.3,0)--(2.5,0) node[right]{$t$};",
                r"  \draw[->](0,-0.3)--(0,3.0) node[above]{$y(t)$};",
                r"  \foreach \c in {0.3,0.6,1.0,1.5}{",
                r"    \draw[unibblue!50,domain=0:1.8,smooth,samples=50] plot(\x,{\c*exp(\x)});",
                r"  }",
                r"  \draw[juliared,very thick,domain=0:1.05,smooth,samples=50]",
                r"    plot(\x,{2*exp(\x)}) node[right]{\small$C{=}2$};",
                r"  \filldraw[juliared](0,2) circle(2pt) node[left]{\small$(0,2)$};",
                r"\end{tikzpicture}",
                r"\end{columns}",
                r"\end{frame}",
            ]
        elif sn == 12:
            out += [
                r"\begin{frame}{Contoh Hitungan IVP: 4 Langkah}",
                r"\textbf{Soal:} $\dfrac{dy}{dt}=-3y,\quad y(0)=10$\vspace{6pt}",
                r"\begin{enumerate}\setlength\itemsep{4pt}",
                r"  \item \textbf{Solusi Umum} (Separabel): $y(t)=Ce^{-3t}$",
                r"  \item \textbf{Terapkan IC}: $y(0)=10$",
                r"  \item \textbf{Substitusi}: $10=C\cdot e^0=C\implies C=10$",
                r"  \item \textbf{Solusi Khusus Akhir:}",
                r"  \begin{tcolorbox}[colback=unibblue!8,colframe=unibblue]",
                r"  \centering$y(t)=10\,e^{-3t}$",
                r"  \end{tcolorbox}",
                r"\end{enumerate}",
                r"\footnotesize Konstanta waktu $\tau=\frac{1}{3}\approx0.333\,\text{s}$; pada $t=\tau$: $y\approx3.68$ (36.8\%)",
                r"\end{frame}",
            ]
        elif sn == 13:
            out += [
                r"\begin{frame}{Pemodelan Rangkaian RL dari Hukum KVL}",
                r"\begin{columns}[T]",
                r"\column{0.42\textwidth}\vspace{-4pt}",
                r"\resizebox{\linewidth}{!}{",
                r"\begin{circuitikz}[american,scale=0.9]",
                r"  \draw (0,0) to[vsource,v=$V(t)$] (0,3)",
                r"              to[R,l=$R$,i>^={$i(t)$}] (3,3)",
                r"              to[L,l=$L$] (3,0)",
                r"              to[short] (0,0);",
                r"\end{circuitikz}}",
                r"\column{0.55\textwidth}\footnotesize",
                r"\textbf{KVL}: $V_R+V_L=V(t)$\\[4pt]",
                r"Ohm: $V_R=Ri(t)$\quad Faraday: $V_L=L\frac{di}{dt}$\\[6pt]",
                r"\begin{tcolorbox}[colback=unibblue!10,colframe=unibblue]",
                r"\centering$L\dfrac{di}{dt}+Ri=V(t)$\\[2pt]\scriptsize PDB Linier Orde-1 Non-Homogen",
                r"\end{tcolorbox}\vspace{4pt}",
                r"Solusi: $i(t)=\dfrac{V_0}{R}\!\left(1-e^{-t/\tau}\right)$\\[4pt]",
                r"Konstanta waktu: $\tau=\dfrac{L}{R}$",
                r"\end{columns}",
                r"\end{frame}",
            ]
        elif sn == 14:
            out += [
                r"\begin{frame}{Kuis 3: Hitung Konstanta Waktu $\tau$ (Soal)}",
                r"\begin{tcolorbox}[colback=unibgold!10,colframe=unibgold,title={\textbf{Hitung $\tau$!}},fonttitle=\bfseries]",
                r"Rangkaian RL seri: $R=200\,\Omega$, $L=50\,\text{mH}$. Berapakah $\tau$ dalam $\mu$s?",
                r"\end{tcolorbox}",
                r"\vspace{8pt}\centering\textcolor{juliared}{\textbf{$\Rightarrow$ Hitung dulu! Jawaban muncul setelah 8 detik\ldots}}",
                r"\end{frame}",
            ]
        elif sn == 15:
            out += [
                r"\begin{frame}{Kuis 3: Jawaban \& Makna Fisis $\tau$}",
                r"\begin{tcolorbox}[colback=unibblue!8,colframe=unibblue]",
                r"\centering$\tau=\dfrac{L}{R}=\dfrac{50\times10^{-3}}{200}=250\,\mu\text{s}$",
                r"\end{tcolorbox}\vspace{6pt}",
                r"\begin{itemize}\setlength\itemsep{4pt}",
                r"  \item Pada $t=\tau$: arus mencapai \textbf{63.2\%} nilai tunak $V_0/R$",
                r"  \item Setelah $5\tau=1.25\,\text{ms}$: arus dianggap \textbf{kondisi mantap}",
                r"  \item Semakin besar $L$ atau kecil $R\Rightarrow$ respons semakin \textbf{lambat}",
                r"\end{itemize}",
                r"\end{frame}",
            ]
        elif sn == 16:
            out += [
                r"\begin{frame}[fragile]{Pilar 3: Demo Julia --- \texttt{DifferentialEquations.jl}}",
                r"\begin{columns}[T]",
                r"\column{0.52\textwidth}",
                r"\begin{lstlisting}",
                r"using DifferentialEquations, Plots",
                r"",
                r"# Parameter Rangkaian RL",
                r"R, L, V0 = 200.0, 0.05, 12.0",
                r"",
                r"# Definisi ODE",
                r"function RL!(di, i, p, t)",
                r"    di[1] = (V0 - R*i[1]) / L",
                r"end",
                r"",
                r"# Selesaikan dengan Tsit5",
                r"i0 = [0.0]",
                r"tspan = (0.0, 5e-3)   # 0..5 ms",
                r"prob = ODEProblem(RL!, i0, tspan)",
                r"sol  = solve(prob, Tsit5())",
                r"",
                r"# Plot kurva transien",
                r"plot(sol, label=L""i(t)"",",
                r"     xlabel=""t (s)"", ylabel=""i (A)"")",
                r"\end{lstlisting}",
                r"\column{0.45\textwidth}",
                r"\begin{tcolorbox}[colback=juliagreen!8,colframe=juliagreen,title={\small\textbf{Kurva Transien RL}},fonttitle=\bfseries]",
                r"\begin{tikzpicture}[scale=0.72]",
                r"  \draw[->](-0.2,0)--(4.2,0) node[right]{\tiny$t$};",
                r"  \draw[->](0,-0.2)--(0,2.8) node[above]{\tiny$i(t)$};",
                r"  \draw[juliagreen,thick,domain=0:4,smooth,samples=60] plot(\x,{2.5*(1-exp(-\x))});",
                r"  \draw[dashed,gray](0,2.5)--(4,2.5) node[right]{\tiny$V_0/R$};",
                r"  \draw[dashed,unibblue](1,0)--(1,1.58) node[above,xshift=-4pt]{\tiny$\tau$};",
                r"  \filldraw[unibblue](1,1.58) circle(2pt);",
                r"  \node[unibblue,right] at(1.1,1.6){\tiny 63.2\%};",
                r"\end{tikzpicture}",
                r"\end{tcolorbox}",
                r"\footnotesize Kode lengkap: \texttt{ndaratha.my.id/pd}",
                r"\end{columns}",
                r"\end{frame}",
            ]
        elif sn == 17:
            out += [
                r"\begin{frame}{Interpretasi Grafik: Tiga Zona Respons Transien}",
                r"\begin{columns}[T]",
                r"\column{0.55\textwidth}",
                r"\begin{tikzpicture}[scale=0.85]",
                r"  \draw[->](-0.3,0)--(5.5,0) node[right]{\small$t$};",
                r"  \draw[->](0,-0.3)--(0,3.5) node[above]{\small$i(t)$};",
                r"  \draw[unibblue,very thick,domain=0:5.2,smooth,samples=80] plot(\x,{3*(1-exp(-\x))});",
                r"  \draw[dashed,gray!70](0,3)--(5.2,3) node[right]{\small$V_0/R$};",
                r"  \fill[juliared!20,opacity=0.4](0,0) rectangle(1,3.2);",
                r"  \node[juliared,font=\tiny] at(0.5,3.3){Zona 1};",
                r"  \fill[unibgold!25,opacity=0.4](1,0) rectangle(3,3.2);",
                r"  \node[unibgold!80!black,font=\tiny] at(2,3.3){Zona 2};",
                r"  \fill[unibgreen!20,opacity=0.4](3,0) rectangle(5.2,3.2);",
                r"  \node[unibgreen!70!black,font=\tiny] at(4.1,3.3){Zona 3};",
                r"\end{tikzpicture}",
                r"\column{0.42\textwidth}",
                r"\begin{itemize}\setlength\itemsep{6pt}\footnotesize",
                r"  \item \textcolor{juliared}{\textbf{Zona 1}} ($0$--$\tau$): Kenaikan cepat, gradien maks",
                r"  \item \textcolor{unibgold!80!black}{\textbf{Zona 2}} ($\tau$--$3\tau$): Konvergensi eksponensial",
                r"  \item \textcolor{unibgreen}{\textbf{Zona 3}} ($>5\tau$): Kondisi mantap $i\approx V_0/R$",
                r"\end{itemize}",
                r"\vspace{4pt}\footnotesize\textit{Sistem RL: overdamped murni, tanpa osilasi}",
                r"\end{columns}",
                r"\end{frame}",
            ]
        elif sn == 18:
            out += [
                r"\begin{frame}{Jembatan ke Persamaan Maxwell}",
                r"\begin{tcolorbox}[colback=unibblue!8,colframe=unibblue,title={\textbf{Rangkaian Terpusat $\rightarrow$ Medan Terdistribusi}},fonttitle=\bfseries]",
                r"\footnotesize\begin{tabular}{ll}",
                r"Faraday (Rangkaian): & $V_L=L\dfrac{di}{dt}$\\[6pt]",
                r"Maxwell (Medan): & $\nabla\times\mathbf{E}=-\dfrac{\partial\mathbf{B}}{\partial t}$\\[6pt]",
                r"Ohm (Makroskopik): & $V_R=Ri$\\[6pt]",
                r"Konstitutif: & $\mathbf{J}=\sigma\mathbf{E}$\\",
                r"\end{tabular}",
                r"\end{tcolorbox}",
                r"\vspace{4pt}\centering\small\textcolor{unibblue}{PDB Hari Ini $\longrightarrow$ PDP Maxwell $\longrightarrow$ Saluran Transmisi $\longrightarrow$ Antena}",
                r"\end{frame}",
            ]
        elif sn == 19:
            out += [
                r"\begin{frame}{Rangkuman: 4 Pilar Minggu 1}",
                r"\begin{columns}[T]",
                r"\column{0.48\textwidth}",
                r"\begin{tcolorbox}[colback=unibblue!8,colframe=unibblue,title={\small\textbf{P1 Intuisi Fisik}},fonttitle=\bfseries]",
                r"\footnotesize PDB=terpusat; PDP=terdistribusi",
                r"\end{tcolorbox}\vspace{4pt}",
                r"\begin{tcolorbox}[colback=unibblue!8,colframe=unibblue,title={\small\textbf{P2 Derivasi Matematis}},fonttitle=\bfseries]",
                r"\footnotesize Orde, Linieritas, IVP $\to$ menentukan $C$",
                r"\end{tcolorbox}",
                r"\column{0.48\textwidth}",
                r"\begin{tcolorbox}[colback=juliagreen!10,colframe=juliagreen,title={\small\textbf{P3 Komputasi Julia}},fonttitle=\bfseries]",
                r"\footnotesize \texttt{DifferentialEquations.jl} + \texttt{Plots.jl}: $i(t)$ real-time",
                r"\end{tcolorbox}\vspace{4pt}",
                r"\begin{tcolorbox}[colback=juliared!8,colframe=juliared,title={\small\textbf{P4 Standar Industri}},fonttitle=\bfseries]",
                r"\footnotesize Model PDB-RL = fondasi transien trafo, motor, saluran (IEEE)",
                r"\end{tcolorbox}",
                r"\end{columns}",
                r"\end{frame}",
            ]
        elif sn == 20:
            out += [
                r"\begin{frame}{Pratinjau Minggu 2 \& Penutup}",
                r"\begin{tcolorbox}[colback=unibblue!8,colframe=unibblue,title={\textbf{Minggu 2: PDB Orde-1 -- Tiga Metode}},fonttitle=\bfseries]",
                r"\begin{itemize}",
                r"  \item \textbf{Separabel} -- Pemisahan variabel",
                r"  \item \textbf{Eksak} -- Medan konservatif \& fungsi potensial",
                r"  \item \textbf{Faktor Integrasi} -- Non-eksak $\rightarrow$ eksak",
                r"\end{itemize}",
                r"Aplikasi: transien RC \& RL",
                r"\end{tcolorbox}",
                r"\vspace{8pt}\centering\large\textbf{Terima kasih!}\\[4pt]",
                r"\small Portal: \texttt{ndaratha.my.id/persamaan-diferensial}\\[6pt]",
                r"\normalsize\textit{Wassalamu'alaikum warahmatullahi wabarakatuh.}",
                r"\end{frame}",
            ]
    out.append(r"\end{document}")
    return "\n".join(out)

# ==============================================================================
# FUNGSI PEMBANTU
# ==============================================================================
async def generate_speech(text, outfile):
    for attempt in range(8):
        try:
            communicate = edge_tts.Communicate(text, VOICE, rate="-2%")
            await asyncio.wait_for(communicate.save(outfile), timeout=30.0)
            if os.path.exists(outfile) and os.path.getsize(outfile) > 8000:
                return
            if os.path.exists(outfile): os.remove(outfile)
        except Exception as e:
            print(f"  [Percobaan {attempt+1}/8] TTS Error: {e}, menunggu 2 detik...")
            if os.path.exists(outfile):
                try: os.remove(outfile)
                except: pass
            await asyncio.sleep(2)

def get_audio_duration(audio_file):
    cmd = ["ffprobe","-v","error","-show_entries","format=duration",
           "-of","default=noprint_wrappers=1:nokey=1",audio_file]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())

def format_timestamp(seconds):
    return f"{int(seconds//60):02d}:{int(seconds%60):02d}"

def make_quiz_pause(output_mp3, duration_sec=8):
    if not os.path.exists(output_mp3):
        subprocess.run([
            "ffmpeg","-y",
            "-f","lavfi","-i",f"anullsrc=r=44100:cl=stereo",
            "-t",str(duration_sec),
            "-c:a","libmp3lame","-b:a","64k", output_mp3
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print(f"  [OK] Jeda kuis {duration_sec}s dibuat")

def compile_latex(tex_path, frames_dir):
    base = os.path.splitext(tex_path)[0]
    tex_dir = os.path.dirname(tex_path)
    for _ in range(2):
        subprocess.run(
            ["pdflatex","-interaction=nonstopmode",
             "-output-directory", tex_dir, tex_path],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    pdf_path = base + ".pdf"
    subprocess.run([
        "pdftoppm","-r","150","-png",
        "-scale-to-x","1920","-scale-to-y","1080",
        pdf_path, os.path.join(frames_dir,"slide")
    ], check=True)
    frames = sorted([f for f in os.listdir(frames_dir)
                     if f.startswith("slide") and f.endswith(".png")])
    return [os.path.join(frames_dir, f) for f in frames]

# ==============================================================================
# MAIN
# ==============================================================================
async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(FRAMES_DIR, exist_ok=True)
    os.makedirs(CLIPS_DIR, exist_ok=True)
    scratch = os.path.dirname(VIDEO_OUT)
    if scratch: os.makedirs(scratch, exist_ok=True)

    print("\n=== 0. BUAT AUDIO JEDA KUIS 8 DETIK ===")
    make_quiz_pause(QUIZ_PAUSE_AUDIO, 8)

    print(f"\n=== 1. SINTESIS TTS ({len(slides_data)} SLIDE) ===")
    total_time = 0.0
    timestamps = []
    for item in slides_data:
        sn = item["slide_num"]
        narr_mp3   = os.path.join(OUTPUT_DIR, f"slide_{sn:02d}.mp3")
        padded_mp3 = os.path.join(OUTPUT_DIR, f"slide_{sn:02d}_padded.mp3")
        final_mp3  = os.path.join(OUTPUT_DIR, f"slide_{sn:02d}_final.mp3")

        if os.path.exists(narr_mp3) and os.path.getsize(narr_mp3) < 8000:
            os.remove(narr_mp3)
        if not os.path.exists(narr_mp3):
            print(f"  TTS Slide {sn:02d}: {item['title']}...")
            await generate_speech(item["text"], narr_mp3)

        subprocess.run(["ffmpeg","-y","-i",narr_mp3,
                        "-af","apad=pad_dur=1.2", padded_mp3],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        if item.get("quiz_pause", 0) > 0:
            list_f = os.path.join(OUTPUT_DIR, f"slide_{sn:02d}_list.txt")
            with open(list_f,"w") as lf:
                lf.write(f"file '{os.path.abspath(padded_mp3)}'\n")
                lf.write(f"file '{os.path.abspath(QUIZ_PAUSE_AUDIO)}'\n")
            subprocess.run(["ffmpeg","-y","-f","concat","-safe","0",
                            "-i", list_f, "-c","copy", final_mp3],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            item["_final"] = final_mp3
        else:
            item["_final"] = padded_mp3

        dur = get_audio_duration(item["_final"])
        timestamps.append((format_timestamp(total_time), item["chapter"], dur, item["title"]))
        total_time += dur

    print(f"  Estimasi total: {format_timestamp(total_time)}")

    print("\n=== 2. GENERATE BEAMER LaTeX → PNG ===")
    tex_src  = build_beamer(slides_data)
    tex_path = os.path.join(FRAMES_DIR, "beamer_w01_v2.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_src)
    frame_files = compile_latex(tex_path, FRAMES_DIR)
    print(f"  {len(frame_files)} frame dihasilkan")

    # Pad jika jumlah frame kurang
    while len(frame_files) < len(slides_data):
        frame_files.append(frame_files[-1])

    print("\n=== 3. BUILD KLIP MP4 1080p STEREO ===")
    for idx, item in enumerate(slides_data):
        sn       = item["slide_num"]
        frame    = frame_files[idx]
        audio    = item["_final"]
        clip_mp4 = os.path.join(CLIPS_DIR, f"clip_{sn:02d}.mp4")
        if not os.path.exists(clip_mp4) or os.path.getsize(clip_mp4) == 0:
            subprocess.run([
                "ffmpeg","-y",
                "-loop","1","-i", frame,
                "-i", audio,
                "-c:v","libx264","-tune","stillimage","-pix_fmt","yuv420p",
                "-vf","scale=1920:1080,format=yuv420p",
                # PERBAIKAN [1]: Stereo AAC 192k
                "-c:a","aac","-b:a","192k","-ac","2",
                "-shortest", clip_mp4
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"  [OK] Klip {sn:02d}: {item['title']}")

    print("\n=== 4. CONCAT SEMUA KLIP ===")
    cmd = ["ffmpeg","-y"]
    fi  = ""
    for i, item in enumerate(slides_data):
        cmd.extend(["-i", os.path.join(CLIPS_DIR, f"clip_{item['slide_num']:02d}.mp4")])
        fi += f"[{i}:v:0][{i}:a:0]"
    n = len(slides_data)
    cmd += ["-filter_complex", f"{fi}concat=n={n}:v=1:a=1[outv][outa]",
            "-map","[outv]","-map","[outa]",
            # PERBAIKAN [8]: CRF 18
            "-c:v","libx264","-preset","faster","-crf","18",
            # PERBAIKAN [1]: Stereo output
            "-c:a","aac","-b:a","192k","-ac","2",
            VIDEO_OUT]
    t0 = time.time()
    subprocess.run(cmd, check=True)
    t1 = time.time()

    mb = os.path.getsize(VIDEO_OUT) / 1e6
    print(f"\n[SUKSES] {VIDEO_OUT}")
    print(f"  Ukuran : {mb:.2f} MB | Waktu render: {t1-t0:.1f}s")

    # Verifikasi audio stereo
    vfy = subprocess.run(
        ["ffprobe","-v","error","-select_streams","a:0",
         "-show_entries","stream=channel_layout,bit_rate",
         "-of","default=noprint_wrappers=1", VIDEO_OUT],
        capture_output=True, text=True)
    print(f"  Verifikasi audio: {vfy.stdout.strip()}")

    print(f"\n=== 5. TULIS NASKAH YouTube v2: {SCRIPT_MD} ===")
    with open(SCRIPT_MD, "w", encoding="utf-8") as f:
        f.write("# Naskah & Metadata Video Kuliah Minggu 01 v2.0\n\n")
        f.write("### 1. Metadata YouTube\n\n")
        f.write("`[Minggu 01] PDB/PDP, IVP, Rangkaian RL & Demo Julia | Persamaan Diferensial`\n\n")
        f.write("```text\nKuliah Minggu 01 v2.0 — Persamaan Diferensial (Teknik Elektro UNIB)\n\n")
        f.write("Portal: https://www.ndaratha.my.id/persamaan-diferensial/\n\n")
        f.write("Timestamps:\n")
        for ts, ch, d, ti in timestamps:
            f.write(f"{ts} - {ch}\n")
        f.write("\n#TeknikElektro #PersamaanDiferensial #Julia #DifferentialEquationsJL #PDB #PDP\n```\n\n")
        f.write("### 2. Naskah Per Slide\n\n")
        for item in slides_data:
            f.write(f"#### Slide {item['slide_num']:02d}: {item['title']}\n\n{item['text']}\n\n")
            if item.get("quiz_pause", 0) > 0:
                f.write(f"*[JEDA KUIS: {item['quiz_pause']} DETIK]*\n\n")

    print(f"  Selesai: {SCRIPT_MD}")
    print("\n=== SELESAI — Video W01 v2.0 ===")

if __name__ == "__main__":
    asyncio.run(main())
