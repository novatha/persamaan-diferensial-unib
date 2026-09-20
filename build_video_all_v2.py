#!/usr/bin/env python3
"""
build_video_all_v2.py  — Batch Builder Semua Minggu (W02–W15)
Versi 2.0: Stereo AAC 192k, Sub-CPMK OBE, Julia Demo, Footer Fixed, Kuis 8s Pause
Skip: W08 (UTS)
"""
import subprocess, os, time, asyncio, edge_tts, sys, shutil

PROJ_DIR = os.path.dirname(os.path.abspath(__file__))
SCRATCH   = os.path.join(PROJ_DIR, "scratch")
PORTAL    = os.path.join(PROJ_DIR, "portal", "public", "video")
os.makedirs(SCRATCH, exist_ok=True)
os.makedirs(PORTAL,  exist_ok=True)

TTS_VOICE = "id-ID-ArdiNeural"

PREAMBLE = r"""
\documentclass[aspectratio=169,10pt]{beamer}
\usetheme{default}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{calc,positioning,arrows.meta}
\usepackage{circuitikz}
\usepackage{tcolorbox}
\tcbuselibrary{skins}
\usepackage{xcolor}
\definecolor{unibblue}{RGB}{31,56,119}
\definecolor{unibgold}{RGB}{204,153,0}
\setbeamercolor{frametitle}{bg=unibblue,fg=white}
\setbeamercolor{structure}{fg=unibblue}
\setbeamerfont{frametitle}{size=\large,series=\bfseries}
\setbeamertemplate{footline}{%
  \leavevmode\hbox{%
    \begin{beamercolorbox}[wd=.40\paperwidth,ht=2.5ex,dp=1.5ex,leftskip=.3cm]{author in head/foot}%
      \usebeamerfont{author in head/foot}\color{unibblue}\textbf{Daratha \& Arfan $|$ Teknik Elektro UNIB}%
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=.30\paperwidth,ht=2.5ex,dp=1.5ex,center]{title in head/foot}%
      \usebeamerfont{title in head/foot}\color{unibblue}Persamaan Diferensial%
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=.30\paperwidth,ht=2.5ex,dp=1.5ex,rightskip=.3cm plus1fil]{date in head/foot}%
      \hfill\color{unibblue}2026\ \insertframenumber/\inserttotalframenumber%
    \end{beamercolorbox}}\vskip0pt}
\setbeamertemplate{navigation symbols}{}
"""

# ============================================================
# DATA KONTEN SEMUA MINGGU
# ============================================================
WEEKS = {}

WEEKS["02"] = {
  "title_short": "PDB Orde 1: Separabel, Eksak & Faktor Integrasi",
  "subtitle": "Minggu 2 - Metode Analitis Orde Satu",
  "cpmk": [
    ("C1","Mengingat","Definisi separabel, eksak, dan faktor integrasi"),
    ("C2","Memahami","Syarat turunan parsial silang: dM/dy = dN/dx"),
    ("C3","Menerapkan","Selesaikan PDB eksak dan non-eksak step-by-step"),
    ("C4","Menganalisis","Tentukan faktor integrasi mu(x) dari rasio selisih"),
  ],
  "next_week": "Aplikasi Transien Rangkaian RC dan RL",
  "slides": [
    {"title":"Judul dan Pembukaan Kuliah Minggu 2","quiz_pause":0,"text":
      "Halo rekan mahasiswa Teknik Elektro UNIB, selamat datang kembali di Minggu 2 Persamaan Diferensial. "
      "Kita membedah tiga metode analitis utama PDB orde satu: Separabel, Eksak, dan Faktor Integrasi. "
      "Diampu bersama Insinyur Novalio Daratha dan Bapak Muhammad Arfan."},
    {"title":"Sub-CPMK dan Capaian Pembelajaran OBE","quiz_pause":0,"text":
      "Capaian Minggu 2: C1 mendefinisikan separabel, eksak, dan faktor integrasi. "
      "C2 memahami syarat turunan parsial silang. C3 menyelesaikan PDB eksak dan non-eksak. "
      "C4 menentukan faktor integrasi dari rasio selisih."},
    {"title":"Bentuk Umum PDB Orde 1","quiz_pause":0,"text":
      "PDB orde satu dinyatakan: dy per dx sama dengan f kurung x koma y, "
      "atau bentuk diferensial M dx ditambah N dy sama dengan nol. "
      "Pemilihan metode bergantung pada struktur M dan N."},
    {"title":"Persamaan Separabel","quiz_pause":0,"text":
      "Persamaan separabel: f kurung x koma y sama dengan g x kali h y. "
      "Prosedur: pindahkan suku y ke kiri, x ke kanan, integrasikan kedua ruas. "
      "Hasilnya: integral satu per h y dy sama dengan integral g x dx ditambah C."},
    {"title":"Contoh Separabel: dy/dx = minus 2xy kuadrat","quiz_pause":0,"text":
      "Contoh: dy per dx sama dengan minus dua x dikali y kuadrat. "
      "Pisahkan: dy per y kuadrat sama dengan minus dua x dx. "
      "Integrasikan: minus y pangkat minus satu sama dengan minus x kuadrat tambah C. "
      "Solusi akhir: y sama dengan satu per kurung x kuadrat tambah K."},
    {"title":"Persamaan Eksak dan Medan Konservatif","quiz_pause":0,"text":
      "M dx ditambah N dy sama dengan nol disebut Eksak jika parsial M per parsial y "
      "sama dengan parsial N per parsial x. "
      "Identik dengan medan vektor konservatif. Solusi: F kurung x koma y sama dengan C."},
    {"title":"Contoh Eksak: Dua xy dx ditambah x kuadrat minus satu dy","quiz_pause":0,"text":
      "Uji: parsial M per parsial y sama dengan dua x, parsial N per parsial x sama dengan dua x. Eksak! "
      "Integrasikan M terhadap x: F sama dengan x kuadrat y ditambah g y. "
      "Tentukan g: g prima y sama dengan minus satu, g sama dengan minus y. "
      "Solusi: x kuadrat y dikurang y sama dengan C."},
    {"title":"Kuis: Uji Eksak","quiz_pause":8,"text":
      "Kuis! Apakah persamaan: tiga xy ditambah y kuadrat dx ditambah x kuadrat ditambah xy dy sama dengan nol bersifat Eksak? "
      "Hitung M y dan N x. Pikirkan 8 detik!"},
    {"title":"Jawaban: Non-Eksak dan Faktor Integrasi","quiz_pause":0,"text":
      "M y sama dengan tiga x tambah dua y, N x sama dengan dua x tambah y. Tidak sama, Non-Eksak. "
      "Rasio: M y dikurang N x per N sama dengan satu per x. Fungsi murni x. "
      "Faktor integrasi: mu x sama dengan e pangkat integral satu per x dx sama dengan x."},
    {"title":"Demo Julia: Menyelesaikan ODE Separabel","quiz_pause":0,"text":
      "Dengan Julia DifferentialEquations titik j l, definisikan f u p t sama dengan minus dua t u kuadrat. "
      "Kondisi awal u nol sama dengan satu, rentang nol hingga dua. "
      "Solusi numerik cocok dengan analitis satu per t kuadrat tambah K."},
    {"title":"Rangkuman Minggu 2 dan Pratinjau Minggu 3","quiz_pause":0,"text":
      "Separabel: pisahkan variabel, integrasikan. "
      "Eksak: uji turunan parsial silang, rekonstruksi potensial. "
      "Faktor integrasi: ubah non-eksak menjadi eksak. "
      "Minggu depan: transien rangkaian RC dan RL. Terima kasih, Wassalamualaikum."},
  ]
}

WEEKS["03"] = {
  "title_short": "Transien RC dan RL: Pemodelan dan Solusi Analitis",
  "subtitle": "Minggu 3 - Aplikasi PDB pada Rangkaian Listrik",
  "cpmk": [
    ("C1","Mengingat","Hukum KVL, KCL, dan model PDB rangkaian RC/RL"),
    ("C2","Memahami","Makna fisis konstanta waktu tau = RC dan tau = L/R"),
    ("C3","Menerapkan","Turunkan dan selesaikan PDB transien RC dan RL"),
    ("C4","Menganalisis","Analisis pengosongan dan pengisian kapasitor/induktor"),
  ],
  "next_week": "Persamaan Diferensial Orde 2: Akar Karakteristik",
  "slides": [
    {"title":"Pembukaan: Rangkaian RC dan RL","quiz_pause":0,"text":
      "Selamat datang di Minggu 3. Kita menerapkan PDB orde satu pada rangkaian listrik nyata. "
      "Fokus: pemodelan dan solusi analitis transien RC dan RL dari prinsip dasar Kirchhoff. "
      "Diampu bersama Insinyur Novalio Daratha dan Bapak Muhammad Arfan."},
    {"title":"Sub-CPMK dan Capaian Pembelajaran OBE","quiz_pause":0,"text":
      "Capaian Minggu 3: C1 mendefinisikan KVL KCL dan model PDB rangkaian RC dan RL. "
      "C2 memahami makna fisis konstanta waktu tau. "
      "C3 menurunkan dan menyelesaikan PDB transien secara analitis. "
      "C4 menganalisis pengosongan dan pengisian kapasitor serta induktor."},
    {"title":"Model PDB Rangkaian RC","quiz_pause":0,"text":
      "Rangkaian RC seri dengan sumber V s: KVL menghasilkan "
      "R d q per d t ditambah q per C sama dengan V s. "
      "Faktor integrasi mu sama dengan e pangkat t per RC. "
      "Solusi: q dari t sama dengan C V s ditambah A e pangkat minus t per tau, tau sama dengan RC."},
    {"title":"Interpretasi Fisis tau = RC","quiz_pause":0,"text":
      "Pada t sama dengan tau: kapasitor terisi 63,2 persen dari nilai tunak. "
      "Pada 5 tau: dianggap kondisi mantap. "
      "Semakin besar R atau C, respons semakin lambat."},
    {"title":"Kuis 1: Hitung tau Rangkaian RC","quiz_pause":8,"text":
      "Kuis! R sama dengan 10 kilo-ohm, C sama dengan 100 mikro-farad. "
      "Hitung tau dan waktu mantap 5 tau. Pikirkan 8 detik!"},
    {"title":"Jawaban Kuis 1","quiz_pause":0,"text":
      "tau sama dengan 10.000 dikali 100 kali 10 pangkat minus 6 sama dengan 1 detik. "
      "Waktu mantap 5 tau sama dengan 5 detik. Kapasitor penuh setelah 5 detik."},
    {"title":"Model PDB Rangkaian RL","quiz_pause":0,"text":
      "RL seri: KVL menghasilkan L di per dt ditambah R i sama dengan V s. "
      "Solusi: i dari t sama dengan V s per R dikali kurung satu dikurang e pangkat minus t per tau, "
      "tau sama dengan L per R."},
    {"title":"Pengosongan RL: Switch Dibuka","quiz_pause":0,"text":
      "Jika sumber dilepas dengan arus awal I nol: "
      "i dari t sama dengan I nol dikali e pangkat minus R per L kali t. "
      "Arus meluruh eksponensial dengan tau sama dengan L per R."},
    {"title":"Kuis 2: RL di Gardu Induk","quiz_pause":8,"text":
      "Kuis! L sama dengan 50 mili-henry, R sama dengan 200 ohm, I nol sama dengan 5 ampere. "
      "Hitung tau dan arus pada t sama dengan 2 tau. Pikirkan 8 detik!"},
    {"title":"Jawaban Kuis 2","quiz_pause":0,"text":
      "tau sama dengan 50 kali 10 pangkat minus 3 per 200 sama dengan 250 mikro-detik. "
      "i pada 2 tau sama dengan 5 e pangkat minus 2 sekitar 0,677 ampere, sekitar 13,5 persen awal."},
    {"title":"Demo Julia: Transien RC dan RL","quiz_pause":0,"text":
      "Dengan Julia DifferentialEquations titik j l, simulasikan RC dan RL bersama. "
      "Plot kedua kurva pada satu grafik. Tau lebih besar menghasilkan kurva lebih landai."},
    {"title":"Rangkuman Minggu 3 dan Pratinjau Minggu 4","quiz_pause":0,"text":
      "KVL menghasilkan PDB orde satu untuk RC dan RL. "
      "tau sama dengan RC atau L per R menentukan kecepatan respons. "
      "Minggu depan: PDB orde 2 untuk rangkaian RLC. Terima kasih, Wassalamualaikum."},
  ]
}

WEEKS["04"] = {
  "title_short": "PDB Orde 2: Akar Karakteristik dan Respons RLC",
  "subtitle": "Minggu 4 - PDB Linear Orde 2 Koefisien Konstan",
  "cpmk": [
    ("C1","Mengingat","Persamaan karakteristik dan tiga kasus akar"),
    ("C2","Memahami","Overdamped, critically damped, underdamped pada RLC"),
    ("C3","Menerapkan","Turunkan solusi PDB orde 2 dari akar karakteristik"),
    ("C4","Menganalisis","Analisis osilasi teredam dan frekuensi alami omega n"),
  ],
  "next_week": "Transformasi Laplace untuk Analisis Rangkaian",
  "slides": [
    {"title":"Pembukaan: PDB Orde 2 dan Rangkaian RLC","quiz_pause":0,"text":
      "Selamat datang di Minggu 4. Kita naik ke PDB linear orde 2 koefisien konstan. "
      "Topik sentral: solusi persamaan karakteristik dan klasifikasi respons teredam. "
      "Diampu bersama Insinyur Novalio Daratha dan Bapak Muhammad Arfan."},
    {"title":"Sub-CPMK dan Capaian Pembelajaran OBE","quiz_pause":0,"text":
      "Capaian Minggu 4: C1 mendefinisikan persamaan karakteristik dan tiga kasus akar. "
      "C2 memahami overdamped, critically damped, underdamped pada RLC. "
      "C3 menurunkan solusi dari akar karakteristik. C4 menganalisis osilasi teredam."},
    {"title":"Model RLC dan Persamaan Orde 2","quiz_pause":0,"text":
      "Rangkaian RLC seri dari KVL: L i double prime ditambah R i prime ditambah satu per C i sama dengan nol. "
      "Persamaan karakteristik: r kuadrat ditambah R per L r ditambah satu per LC sama dengan nol. "
      "Diskriminan Delta sama dengan R per L kuadrat dikurang empat per LC."},
    {"title":"Kasus 1: Overdamped Delta positif","quiz_pause":0,"text":
      "Dua akar real berbeda r1 dan r2. "
      "Solusi: i sama dengan C1 e pangkat r1 t ditambah C2 e pangkat r2 t. "
      "Peluruhan eksponensial tanpa osilasi. R besar mendominasi."},
    {"title":"Kasus 2: Critically Damped Delta nol","quiz_pause":0,"text":
      "Akar kembar r sama dengan minus alpha. "
      "Solusi: i sama dengan kurung C1 tambah C2 t dikali e pangkat minus alpha t. "
      "Sistem kembali ke nol paling cepat tanpa osilasi. Optimal untuk proteksi."},
    {"title":"Kasus 3: Underdamped Delta negatif","quiz_pause":0,"text":
      "Akar kompleks konjugat r sama dengan minus alpha plus minus j omega d. "
      "Solusi: i sama dengan e pangkat minus alpha t dikali kurung A cos omega d t tambah B sin omega d t. "
      "Osilasi teredam dengan frekuensi omega d."},
    {"title":"Parameter Fisis omega n alpha zeta","quiz_pause":0,"text":
      "Frekuensi alami omega n sama dengan satu per akar LC. "
      "Faktor redaman alpha sama dengan R per dua L. "
      "Rasio redaman zeta sama dengan alpha per omega n. "
      "Zeta lebih dari 1 overdamped, sama dengan 1 critically, kurang dari 1 underdamped."},
    {"title":"Kuis: Klasifikasi Rangkaian RLC","quiz_pause":8,"text":
      "Kuis! L sama dengan 1 henry, C sama dengan 0,25 farad, R sama dengan 5 ohm. "
      "Hitung omega n, alpha, zeta. Klasifikasikan responnya. Pikirkan 8 detik!"},
    {"title":"Jawaban Kuis RLC","quiz_pause":0,"text":
      "Omega n sama dengan satu per akar 0,25 sama dengan 2. Alpha sama dengan 2,5. "
      "Zeta sama dengan 1,25. Karena zeta lebih dari 1: OVERDAMPED!"},
    {"title":"Demo Julia: Tiga Respons RLC","quiz_pause":0,"text":
      "Dengan Julia, simulasikan tiga kasus sekaligus. "
      "Plot overdamped, critically damped, underdamped pada satu grafik. "
      "Lihat perbedaan dramatis antar respons."},
    {"title":"Rangkuman Minggu 4 dan Pratinjau Minggu 5","quiz_pause":0,"text":
      "Persamaan karakteristik menentukan tipe respons RLC. "
      "Tiga kasus bergantung pada diskriminan dan zeta. "
      "Minggu depan: Transformasi Laplace. Terima kasih, Wassalamualaikum."},
  ]
}

WEEKS["05"] = {
  "title_short": "Transformasi Laplace dan Analisis Rangkaian",
  "subtitle": "Minggu 5 - Laplace Transform dan Rangkaian Listrik",
  "cpmk": [
    ("C1","Mengingat","Definisi integral Laplace dan tabel transformasi standar"),
    ("C2","Memahami","Sifat linearitas, pergeseran, dan turunan di domain s"),
    ("C3","Menerapkan","Selesaikan PDB IVP via Laplace dan invers Laplace"),
    ("C4","Menganalisis","Analisis fungsi transfer H(s) rangkaian RLC"),
  ],
  "next_week": "Deret Fourier dan Analisis Harmonisa",
  "slides": [
    {"title":"Pembukaan: Kekuatan Transformasi Laplace","quiz_pause":0,"text":
      "Selamat datang di Minggu 5. Laplace mengubah PDB domain waktu menjadi aljabar domain s. "
      "Seluruh analisis rangkaian modern bertumpu pada teknik ini. "
      "Diampu bersama Insinyur Novalio Daratha dan Bapak Muhammad Arfan."},
    {"title":"Sub-CPMK dan Capaian Pembelajaran OBE","quiz_pause":0,"text":
      "Capaian Minggu 5: C1 mendefinisikan integral Laplace dan tabel standar. "
      "C2 memahami sifat linearitas dan turunan di domain s. "
      "C3 menyelesaikan IVP via Laplace dan invers Laplace. C4 menganalisis H dari s."},
    {"title":"Definisi Formal Transformasi Laplace","quiz_pause":0,"text":
      "L kurung f t sama dengan F dari s sama dengan integral nol hingga tak hingga e pangkat minus st dikali f t dt. "
      "Syarat: s kompleks dengan bagian real cukup besar agar konvergen."},
    {"title":"Tabel Transformasi Penting","quiz_pause":0,"text":
      "Laplace dari 1 sama dengan 1 per s. Laplace dari e pangkat at sama dengan 1 per s minus a. "
      "Laplace dari sin omega t sama dengan omega per s kuadrat tambah omega kuadrat. "
      "Laplace dari t pangkat n sama dengan n faktorial per s pangkat n tambah 1."},
    {"title":"Sifat Turunan di Domain s","quiz_pause":0,"text":
      "Laplace dari f prima t sama dengan s F dari s dikurang f nol. "
      "Laplace dari f double prime t sama dengan s kuadrat F dikurang s f nol dikurang f prima nol. "
      "Kondisi awal IVP otomatis terintegrasi dalam transformasi."},
    {"title":"Prosedur Solusi 4 Langkah","quiz_pause":0,"text":
      "Satu, transformasikan semua suku ke domain s. Dua, substitusi kondisi awal. "
      "Tiga, selesaikan aljabar untuk F dari s. Empat, invers Laplace untuk f dari t."},
    {"title":"Contoh: y double prime tambah 4y sama dengan nol","quiz_pause":0,"text":
      "Transformasikan: s kuadrat Y dikurang s ditambah 4Y sama dengan nol. "
      "Y sama dengan s per s kuadrat tambah 4. "
      "Invers Laplace: y dari t sama dengan cos 2t."},
    {"title":"Fungsi Transfer H(s) Rangkaian RLC","quiz_pause":0,"text":
      "H dari s sama dengan V out per V in sama dengan satu per LC "
      "dibagi kurung s kuadrat tambah R per L s tambah satu per LC. "
      "Pole H menentukan stabilitas dan tipe respons."},
    {"title":"Kuis: Invers Laplace","quiz_pause":8,"text":
      "Kuis! Tentukan invers Laplace dari F s sama dengan 3 per s tambah 2 ditambah 4s per s kuadrat tambah 9. "
      "Pikirkan 8 detik!"},
    {"title":"Jawaban Kuis Invers Laplace","quiz_pause":0,"text":
      "Suku pertama: 3 e pangkat minus 2t. Suku kedua: 4 cos 3t. "
      "Solusi total: f t sama dengan 3 e pangkat minus 2t ditambah 4 cos 3t."},
    {"title":"Demo Julia: Laplace Simbolik","quiz_pause":0,"text":
      "Dengan Symbolics titik j l, lakukan transformasi dan invers Laplace simbolik. "
      "Hasil simbolik persis sama dengan perhitungan manual."},
    {"title":"Rangkuman Minggu 5 dan Pratinjau Minggu 6","quiz_pause":0,"text":
      "Laplace mengubah PDB menjadi aljabar. Kondisi awal terintegrasi otomatis. "
      "H dari s merangkum perilaku sistem. Minggu depan: Deret Fourier. Terima kasih, Wassalamualaikum."},
  ]
}

WEEKS["06"] = {
  "title_short": "Deret Fourier dan Analisis Spektrum Harmonisa",
  "subtitle": "Minggu 6 - Deret Fourier dan Kualitas Daya",
  "cpmk": [
    ("C1","Mengingat","Definisi deret Fourier dan kondisi Dirichlet"),
    ("C2","Memahami","Makna fisis koefisien an, bn, dan simetri gelombang"),
    ("C3","Menerapkan","Hitung koefisien Fourier gelombang kotak dan segitiga"),
    ("C4","Menganalisis","Analisis THD dan spektrum harmonisa pada kualitas daya"),
  ],
  "next_week": "Persamaan Diferensial Parsial: Persamaan Panas",
  "slides": [
    {"title":"Pembukaan: Fourier dan Kualitas Daya","quiz_pause":0,"text":
      "Selamat datang di Minggu 6. Deret Fourier adalah bahasa universal untuk sinyal periodik. "
      "Distorsi harmonisa jaringan PLN dianalisis menggunakan Deret Fourier. "
      "Diampu bersama Insinyur Novalio Daratha dan Bapak Muhammad Arfan."},
    {"title":"Sub-CPMK dan Capaian Pembelajaran OBE","quiz_pause":0,"text":
      "Capaian Minggu 6: C1 mendefinisikan deret Fourier dan kondisi Dirichlet. "
      "C2 memahami koefisien a n, b n, dan simetri. C3 menghitung koefisien Fourier. "
      "C4 menganalisis THD dan spektrum harmonisa."},
    {"title":"Definisi Deret Fourier","quiz_pause":0,"text":
      "f dari t sama dengan a nol per dua ditambah jumlah n sama dengan 1 hingga tak hingga "
      "dari a n cos n omega nol t ditambah b n sin n omega nol t. "
      "omega nol sama dengan dua pi per T adalah frekuensi fundamental."},
    {"title":"Rumus Koefisien Fourier","quiz_pause":0,"text":
      "a nol sama dengan dua per T dikali integral satu periode f t dt. "
      "a n sama dengan dua per T dikali integral f t cos n omega nol t dt. "
      "b n sama dengan dua per T dikali integral f t sin n omega nol t dt."},
    {"title":"Contoh: Gelombang Kotak Simetris","quiz_pause":0,"text":
      "Gelombang kotak fungsi ganjil: semua a n sama dengan nol. "
      "b n sama dengan empat A per n pi untuk n ganjil, nol untuk n genap. "
      "Deret: empat A per pi dikali sin omega t plus sepertiga sin 3 omega t plus seterusnya."},
    {"title":"Simetri Gelombang","quiz_pause":0,"text":
      "Fungsi genap: hanya a n. Fungsi ganjil: hanya b n. "
      "Simetri setengah gelombang: hanya harmonisa ganjil. "
      "Kenali simetri dahulu sebelum menghitung koefisien."},
    {"title":"THD dan Kualitas Daya","quiz_pause":0,"text":
      "THD sama dengan akar jumlah V n kuadrat n dari 2 hingga tak hingga dibagi V 1, kali 100 persen. "
      "IEEE 519: THD tegangan kurang dari 5 persen. "
      "THD tinggi menyebabkan panas berlebih transformator."},
    {"title":"Kuis: Koefisien Fourier Gelombang Segitiga","quiz_pause":8,"text":
      "Kuis! Gelombang segitiga simetris amplitudo 1 periode 2 pi. "
      "Fungsi genap atau ganjil? Berapakah b 1? Pikirkan 8 detik!"},
    {"title":"Jawaban Kuis: Gelombang Segitiga","quiz_pause":0,"text":
      "Gelombang segitiga simetris adalah fungsi ganjil: semua a n sama dengan nol. "
      "b n sama dengan 8 per n kuadrat pi kuadrat untuk n ganjil. "
      "b 1 sama dengan 8 per pi kuadrat sekitar 0,811."},
    {"title":"Demo Julia: Deret Fourier dan Spektrum","quiz_pause":0,"text":
      "Dengan Julia, konstruksi Fourier gelombang kotak dengan N sama dengan 1, 5, 10, 50 suku. "
      "Plot spektrum dengan FFTW titik j l. Amati efek Gibbs di sudut gelombang."},
    {"title":"Rangkuman Minggu 6 dan Pratinjau Minggu 7","quiz_pause":0,"text":
      "Deret Fourier mendekomposisi sinyal periodik menjadi harmonisa. "
      "THD mengukur kualitas daya berdasarkan kandungan harmonisa. "
      "Minggu depan: Persamaan Panas PDP. Terima kasih, Wassalamualaikum."},
  ]
}

WEEKS["07"] = {
  "title_short": "PDP: Persamaan Panas dan Difusi Elektromagnetik",
  "subtitle": "Minggu 7 - Partial Differential Equations Pengantar",
  "cpmk": [
    ("C1","Mengingat","Klasifikasi PDP: eliptik, parabolik, hiperbolik"),
    ("C2","Memahami","Metode pemisahan variabel Separation of Variables"),
    ("C3","Menerapkan","Selesaikan persamaan panas 1D dengan syarat batas Dirichlet"),
    ("C4","Menganalisis","Analisis skin effect pada konduktor kabel transmisi"),
  ],
  "next_week": "Persamaan Laplace dan Distribusi Potensial Elektrostatik (setelah UTS)",
  "slides": [
    {"title":"Pembukaan: PDP dan Fenomena Terdistribusi","quiz_pause":0,"text":
      "Selamat datang di Minggu 7, pintu masuk PDP. Berbeda dari PDB, PDP menggambarkan "
      "fenomena yang tersebar dalam ruang dan waktu: difusi panas kabel, skin effect, gelombang EM. "
      "Diampu bersama Insinyur Novalio Daratha dan Bapak Muhammad Arfan."},
    {"title":"Sub-CPMK dan Capaian Pembelajaran OBE","quiz_pause":0,"text":
      "Capaian Minggu 7: C1 mengklasifikasikan PDP menjadi eliptik, parabolik, hiperbolik. "
      "C2 memahami metode pemisahan variabel. C3 menyelesaikan panas 1D dengan Dirichlet. "
      "C4 menganalisis skin effect pada konduktor."},
    {"title":"Klasifikasi PDP Tiga Jenis","quiz_pause":0,"text":
      "Eliptik seperti Laplace: distribusi stasioner. "
      "Parabolik seperti persamaan panas: difusi transien. "
      "Hiperbolik seperti persamaan gelombang: propagasi. "
      "Klasifikasi berdasarkan diskriminan B kuadrat dikurang 4AC."},
    {"title":"Persamaan Panas 1D","quiz_pause":0,"text":
      "Parsial u per parsial t sama dengan alpha kuadrat dikali parsial kuadrat u per parsial x kuadrat. "
      "u adalah suhu, alpha kuadrat adalah difusivitas termal. "
      "Dalam EM: identik dengan difusi medan dalam konduktor."},
    {"title":"Metode Pemisahan Variabel","quiz_pause":0,"text":
      "Asumsikan u sama dengan X dari x kali T dari t. "
      "Substitusi: T prima per alpha kuadrat T sama dengan X double prime per X sama dengan minus lambda. "
      "Hasilkan dua PDB terpisah untuk X dan T."},
    {"title":"Solusi X dan T","quiz_pause":0,"text":
      "Untuk X dengan batas nol: X n sama dengan sin n pi x per L, lambda n sama dengan n pi per L kuadrat. "
      "Untuk T: T n sama dengan e pangkat minus alpha kuadrat lambda n t. "
      "Solusi umum: superposisi semua modus."},
    {"title":"Skin Effect pada Konduktor","quiz_pause":0,"text":
      "Skin effect: arus AC terkonsentrasi di permukaan konduktor. "
      "Kedalaman penetrasi delta sama dengan akar dua per omega mu sigma. "
      "50 Hz pada tembaga: delta sekitar 9,4 mm. Frekuensi lebih tinggi, delta lebih kecil."},
    {"title":"Kuis: Hitung Kedalaman Skin Effect","quiz_pause":8,"text":
      "Kuis! Tembaga: sigma sama dengan 5,8 kali 10 pangkat 7, mu sama dengan mu nol. "
      "Hitung delta pada 50 Hz dan 10 kHz. Pikirkan 8 detik!"},
    {"title":"Jawaban: Skin Effect Tembaga","quiz_pause":0,"text":
      "Pada 50 Hz: delta sekitar 9,4 milimeter. Pada 10 kHz: delta sekitar 0,67 milimeter. "
      "Semakin tinggi frekuensi, konduktor efektif semakin tipis. "
      "Kabel HVAC multi-strand mengurangi rugi skin effect."},
    {"title":"Demo Julia: Animasi Panas 1D","quiz_pause":0,"text":
      "Dengan Julia DifferentialEquations titik j l, simulasikan panas 1D via MOL. "
      "Diskritisasi ruang, selesaikan sebagai ODE dalam waktu. "
      "Plot animasi suhu berevolusi menuju keadaan tunak."},
    {"title":"Rangkuman Minggu 7 dan Info UTS","quiz_pause":0,"text":
      "PDP: eliptik parabolik hiperbolik. Pemisahan variabel menghasilkan deret Fourier. "
      "Skin effect: aplikasi difusi EM. Minggu 8 UTS, kita lanjut Minggu 9. "
      "Belajar dengan baik! Terima kasih, Wassalamualaikum."},
  ]
}

WEEKS["09"] = {
  "title_short": "Persamaan Laplace dan Distribusi Potensial Elektrostatik",
  "subtitle": "Minggu 9 - Laplace, Poisson, dan Elektrostatika",
  "cpmk": [
    ("C1","Mengingat","Persamaan Laplace nabla kuadrat phi sama dengan nol dan Poisson"),
    ("C2","Memahami","Syarat batas Dirichlet dan Neumann pada elektroda"),
    ("C3","Menerapkan","Selesaikan Laplace 2D dengan pemisahan variabel"),
    ("C4","Menganalisis","Analisis distribusi medan E dari potensial phi"),
  ],
  "next_week": "Persamaan Gelombang dan Saluran Transmisi",
  "slides": [
    {"title":"Pembukaan: Laplace dan Medan Listrik","quiz_pause":0,"text":
      "Selamat datang kembali di Minggu 9 pasca UTS. "
      "Kita lanjutkan dengan PDP paling fundamental dalam EM: Laplace dan Poisson. "
      "Semua distribusi potensial di ruang bebas muatan memenuhi Laplace. "
      "Diampu bersama Insinyur Novalio Daratha dan Bapak Muhammad Arfan."},
    {"title":"Sub-CPMK dan Capaian Pembelajaran OBE","quiz_pause":0,"text":
      "Capaian Minggu 9: C1 mendefinisikan Laplace dan Poisson. "
      "C2 memahami syarat batas Dirichlet dan Neumann. "
      "C3 menyelesaikan Laplace 2D. C4 menganalisis medan E dari gradien phi."},
    {"title":"Persamaan Laplace dan Poisson","quiz_pause":0,"text":
      "Ruang bebas muatan: nabla kuadrat phi sama dengan nol. "
      "Ruang bermuatan: nabla kuadrat phi sama dengan minus rho per epsilon nol. "
      "Laplacian Kartesian: parsial kuadrat phi per x kuadrat ditambah y kuadrat ditambah z kuadrat sama dengan nol."},
    {"title":"Syarat Batas Fisika","quiz_pause":0,"text":
      "Dirichlet: nilai phi ditentukan di batas, phi sama dengan V nol pada elektroda. "
      "Neumann: turunan normal parsial phi per n ditentukan, nol pada konduktor sempurna. "
      "Kombinasi: syarat batas campuran."},
    {"title":"Solusi Laplace 2D via Pemisahan Variabel","quiz_pause":0,"text":
      "Asumsikan phi sama dengan X x kali Y y. "
      "Hasilkan: X double prime sama dengan k kuadrat X dan Y double prime sama dengan minus k kuadrat Y. "
      "Solusi: X eksponensial atau hiperbolik, Y trigonometri."},
    {"title":"Contoh: Kapasitor Pelat Sejajar","quiz_pause":0,"text":
      "Kapasitor: phi nol pada y sama dengan 0, phi V nol pada y sama dengan d. "
      "Laplace 1D: d kuadrat phi per dy kuadrat sama dengan nol. "
      "Solusi: phi dari y sama dengan V nol dikali y per d. "
      "Medan E sama dengan minus V nol per d ke arah y minus: seragam!"},
    {"title":"Medan Listrik dari Gradien Potensial","quiz_pause":0,"text":
      "E sama dengan minus gradien phi. "
      "E x sama dengan minus parsial phi per x, E y sama dengan minus parsial phi per y. "
      "Garis medan E selalu tegak lurus ekipotensial."},
    {"title":"Kuis: Laplace Kapasitor","quiz_pause":8,"text":
      "Kuis! Pelat bawah y sama dengan 0 dengan V sama dengan 0, pelat atas y sama dengan d dengan V sama dengan V nol. "
      "Tulis Laplace, syarat batas, dan temukan phi dari y. Pikirkan 8 detik!"},
    {"title":"Jawaban: Kapasitor Pelat","quiz_pause":0,"text":
      "d kuadrat phi per dy kuadrat sama dengan nol. Solusi: phi sama dengan Ay tambah B. "
      "Batas: B sama dengan nol, A sama dengan V nol per d. "
      "phi dari y sama dengan V nol y per d. E seragam!"},
    {"title":"Demo Julia: Laplace 2D Numerik","quiz_pause":0,"text":
      "Dengan Julia, selesaikan Laplace 2D dengan metode beda hingga. "
      "Buat grid N kali N, iterasi hingga konvergen, plot kontur phi dan vektor E."},
    {"title":"Rangkuman Minggu 9 dan Pratinjau Minggu 10","quiz_pause":0,"text":
      "Laplace dan Poisson mengatur distribusi potensial listrik. "
      "Syarat batas Dirichlet dan Neumann menentukan solusi unik. "
      "Minggu depan: persamaan gelombang dan saluran transmisi. Terima kasih, Wassalamualaikum."},
  ]
}

WEEKS["10"] = {
  "title_short": "Persamaan Gelombang dan Saluran Transmisi",
  "subtitle": "Minggu 10 - Wave Equation dan Transmission Lines",
  "cpmk": [
    ("C1","Mengingat","Persamaan Telegrafer dan model saluran terdistribusi"),
    ("C2","Memahami","Gelombang berjalan: solusi d'Alembert dan kecepatan fase"),
    ("C3","Menerapkan","Analisis refleksi gelombang di ujung terbuka dan tertutup"),
    ("C4","Menganalisis","Analisis mismatch impedansi dan koefisien refleksi Gamma"),
  ],
  "next_week": "Koordinat Silinder dan Fungsi Bessel",
  "slides": [
    {"title":"Pembukaan: Gelombang dan Saluran Transmisi","quiz_pause":0,"text":
      "Selamat datang di Minggu 10. Persamaan gelombang adalah jantung analisis saluran transmisi "
      "tenaga listrik, kabel koaksial, dan serat optik. "
      "Diampu bersama Insinyur Novalio Daratha dan Bapak Muhammad Arfan."},
    {"title":"Sub-CPMK dan Capaian Pembelajaran OBE","quiz_pause":0,"text":
      "Capaian Minggu 10: C1 mendefinisikan persamaan Telegrafer. "
      "C2 memahami solusi d'Alembert dan kecepatan fase. "
      "C3 menganalisis refleksi gelombang. C4 menghitung koefisien refleksi Gamma."},
    {"title":"Model Saluran Transmisi Terdistribusi","quiz_pause":0,"text":
      "Parameter per satuan panjang: R prima, L prima, C prima, G prima. "
      "Persamaan Telegrafer: minus parsial V per x sama dengan L prima parsial I per t ditambah R prima I. "
      "Minus parsial I per x sama dengan C prima parsial V per t ditambah G prima V."},
    {"title":"Persamaan Gelombang Lossless","quiz_pause":0,"text":
      "Untuk R prima sama dengan G prima sama dengan nol: "
      "parsial kuadrat V per x kuadrat sama dengan L prima C prima parsial kuadrat V per t kuadrat. "
      "Kecepatan fase v p sama dengan satu per akar L prima C prima."},
    {"title":"Solusi d'Alembert","quiz_pause":0,"text":
      "V kurung x koma t sama dengan f kurung x dikurang v p t ditambah g kurung x ditambah v p t. "
      "Suku pertama: gelombang ke kanan. Suku kedua: gelombang ke kiri atau pantul. "
      "Superposisi keduanya menghasilkan gelombang berdiri jika ada refleksi."},
    {"title":"Impedansi Karakteristik Z nol","quiz_pause":0,"text":
      "Z nol sama dengan akar L prima per C prima. "
      "Kabel TV koaksial 75 ohm, kabel transmisi PLN 150 kV sekitar 250 hingga 400 ohm."},
    {"title":"Koefisien Refleksi Gamma","quiz_pause":0,"text":
      "Gamma sama dengan Z L dikurang Z nol dibagi Z L ditambah Z nol. "
      "Ujung terbuka: Gamma sama dengan plus 1. Ujung hubung singkat: Gamma sama dengan minus 1. "
      "Matched Z L sama dengan Z nol: Gamma sama dengan nol."},
    {"title":"Kuis: Hitung Koefisien Refleksi","quiz_pause":8,"text":
      "Kuis! Z nol sama dengan 50 ohm, Z L sama dengan 100 tambah j50 ohm. "
      "Hitung Gamma dan Return Loss dalam dB. Pikirkan 8 detik!"},
    {"title":"Jawaban: Koefisien Refleksi","quiz_pause":0,"text":
      "Gamma sama dengan kurung 50 tambah j50 per kurung 150 tambah j50. "
      "Modulus Gamma sekitar 0,447. Return Loss sekitar 7 dB. "
      "44,7 persen amplitudo gelombang dipantulkan."},
    {"title":"Demo Julia: Simulasi Gelombang 1D","quiz_pause":0,"text":
      "Dengan Julia, animasikan pulsa Gaussian merambat dan memantul di ujung saluran. "
      "Selesaikan dengan beda hingga eksplisit, plot animasi gelombang berdiri."},
    {"title":"Rangkuman Minggu 10 dan Pratinjau Minggu 11","quiz_pause":0,"text":
      "Telegrafer menggambarkan saluran terdistribusi. d'Alembert: gelombang maju dan mundur. "
      "Mismatch impedansi menyebabkan refleksi. "
      "Minggu depan: koordinat silinder dan Bessel. Terima kasih, Wassalamualaikum."},
  ]
}

WEEKS["11"] = {
  "title_short": "Koordinat Silinder dan Fungsi Bessel",
  "subtitle": "Minggu 11 - Cylindrical Coordinates dan Bessel Functions",
  "cpmk": [
    ("C1","Mengingat","Laplacian dalam koordinat silinder r phi z"),
    ("C2","Memahami","Persamaan Bessel dan dua solusi Jn dan Yn"),
    ("C3","Menerapkan","Selesaikan Laplace silindris untuk kabel koaksial"),
    ("C4","Menganalisis","Analisis distribusi arus dan medan pada kawat silindris"),
  ],
  "next_week": "Koordinat Bola dan Polinomial Legendre",
  "slides": [
    {"title":"Pembukaan: Geometri Silindris dalam EE","quiz_pause":0,"text":
      "Selamat datang di Minggu 11. Kabel koaksial, transformator toroidal, motor listrik — "
      "semuanya silindris. Koordinat silinder dan Fungsi Bessel adalah alat yang tepat. "
      "Diampu bersama Insinyur Novalio Daratha dan Bapak Muhammad Arfan."},
    {"title":"Sub-CPMK dan Capaian Pembelajaran OBE","quiz_pause":0,"text":
      "Capaian Minggu 11: C1 mendefinisikan Laplacian dalam r phi z. "
      "C2 memahami J n dan Y n. C3 menyelesaikan Laplace kabel koaksial. "
      "C4 menganalisis distribusi arus dan medan pada kawat silindris."},
    {"title":"Koordinat Silinder dan Laplacian","quiz_pause":0,"text":
      "Laplacian silinder: nabla kuadrat f sama dengan satu per r parsial per parsial r "
      "kurung r parsial f per r ditambah satu per r kuadrat parsial kuadrat f per phi kuadrat "
      "ditambah parsial kuadrat f per z kuadrat."},
    {"title":"Persamaan Bessel","quiz_pause":0,"text":
      "Setelah pemisahan variabel: r kuadrat R double prime ditambah r R prime "
      "ditambah kurung k kuadrat r kuadrat dikurang n kuadrat dikali R sama dengan nol. "
      "Dua solusi: J n dari kr berhingga di origin, Y n dari kr divergen di origin."},
    {"title":"Aplikasi: Kabel Koaksial","quiz_pause":0,"text":
      "Dengan simetri azimut: d per dr kurung r d phi per dr sama dengan nol. "
      "Solusi: phi sama dengan A log r ditambah B. "
      "Kondisi batas phi a sama dengan Va dan phi b sama dengan nol menentukan A dan B."},
    {"title":"Kuis: Potensial Kabel Koaksial","quiz_pause":8,"text":
      "Kuis! a sama dengan 1 mm, b sama dengan 5 mm, Va sama dengan 100 V, Vb sama dengan 0. "
      "Tentukan phi dari r dan hitung E pada r sama dengan 2 mm. Pikirkan 8 detik!"},
    {"title":"Jawaban: Kabel Koaksial","quiz_pause":0,"text":
      "A sama dengan 100 per log a per b. B sama dengan minus A log b. "
      "E r sama dengan minus A per r. Pada r sama dengan 2 mm: E sekitar 124 kV per meter."},
    {"title":"Distribusi Medan Kawat Silindris","quiz_pause":0,"text":
      "Di dalam kawat r kurang dari a: B phi sama dengan mu nol J r per 2. "
      "Di luar kawat: B phi sama dengan mu nol I per 2 pi r. "
      "Solusi eksak dari hukum Ampere dalam geometri silindris."},
    {"title":"Demo Julia: Fungsi Bessel","quiz_pause":0,"text":
      "Dengan SpecialFunctions titik j l: besselj n x dan bessely n x tersedia langsung. "
      "Plot J0, J1, J2, Y0 dalam satu grafik. "
      "Osilasi meredam sebagai akar satu per x mencerminkan sifat gelombang silindris."},
    {"title":"Rangkuman Minggu 11 dan Pratinjau Minggu 12","quiz_pause":0,"text":
      "Koordinat silinder menyederhanakan geometri rotatif. "
      "J n dan Y n adalah solusi alami Laplace silindris. "
      "Kabel koaksial: phi logaritmik, E berbanding terbalik r. "
      "Minggu depan: koordinat bola dan Legendre. Terima kasih, Wassalamualaikum."},
  ]
}

WEEKS["12"] = {
  "title_short": "Koordinat Bola dan Polinomial Legendre",
  "subtitle": "Minggu 12 - Spherical Coordinates dan Legendre Polynomials",
  "cpmk": [
    ("C1","Mengingat","Laplacian dalam koordinat bola r theta phi"),
    ("C2","Memahami","Polinomial Legendre Pn cos theta dan ortogonalitas"),
    ("C3","Menerapkan","Selesaikan Laplace bola untuk bola konduktor"),
    ("C4","Menganalisis","Analisis distribusi potensial antena dan elektroda pembumian"),
  ],
  "next_week": "Metode Numerik: Euler, RK4, dan Beda Hingga",
  "slides": [
    {"title":"Pembukaan: Geometri Bola dalam EE","quiz_pause":0,"text":
      "Selamat datang di Minggu 12. Antena isotropik, elektroda bola pembumian, "
      "dan distribusi medan di sekitar transformator memerlukan koordinat bola dan Legendre. "
      "Diampu bersama Insinyur Novalio Daratha dan Bapak Muhammad Arfan."},
    {"title":"Sub-CPMK dan Capaian Pembelajaran OBE","quiz_pause":0,"text":
      "Capaian Minggu 12: C1 mendefinisikan Laplacian bola. "
      "C2 memahami P n cos theta dan ortogonalitas. "
      "C3 menyelesaikan Laplace bola. C4 menganalisis pembumian dan antena."},
    {"title":"Koordinat Bola dan Laplacian","quiz_pause":0,"text":
      "r jarak dari origin, theta sudut polar, phi sudut azimut. "
      "Laplacian: satu per r kuadrat parsial per r kurung r kuadrat parsial phi per r "
      "ditambah suku angular theta dan phi."},
    {"title":"Polinomial Legendre Pn x","quiz_pause":0,"text":
      "P 0 sama dengan 1. P 1 sama dengan x. P 2 sama dengan setengah kurung 3x kuadrat dikurang 1. "
      "Ortogonalitas: integral minus 1 hingga 1 P m P n dx sama dengan nol untuk m tidak sama n."},
    {"title":"Bola Konduktor dalam Medan Seragam","quiz_pause":0,"text":
      "phi kurung r koma theta sama dengan kurung minus E nol r ditambah E nol a kubik per r kuadrat "
      "dikali cos theta. "
      "Medan di permukaan: E r pada r sama dengan a sama dengan 3 E nol cos theta."},
    {"title":"Elektroda Bola Pembumian","quiz_pause":0,"text":
      "Resistansi pembumian: R sama dengan rho per 4 pi a. "
      "rho resistivitas tanah, a jari-jari elektroda. "
      "Berbanding terbalik dengan jari-jari."},
    {"title":"Kuis: Resistansi Pembumian","quiz_pause":8,"text":
      "Kuis! Jari-jari 0,5 meter, resistivitas tanah 100 ohm-meter. "
      "Hitung R pembumian. Memenuhi IEEE 80 kurang dari 25 ohm? Pikirkan 8 detik!"},
    {"title":"Jawaban: Resistansi Pembumian","quiz_pause":0,"text":
      "R sama dengan 100 per 4 pi 0,5 sekitar 15,9 ohm. "
      "Lebih kecil dari 25 ohm: MEMENUHI standar IEEE 80!"},
    {"title":"Demo Julia: Legendre dan Kontur Potensial","quiz_pause":0,"text":
      "Dengan SpecialFunctions titik j l, plot P0 hingga P4. "
      "Buat kontur phi bola dalam medan seragam. "
      "Ekipotensial terdistorsi di sekitar bola."},
    {"title":"Rangkuman Minggu 12 dan Pratinjau Minggu 13","quiz_pause":0,"text":
      "Legendre menyelesaikan masalah simetri bola. "
      "Bola konduktor: solusi P1 cos theta. "
      "Elektroda bola: R berbanding terbalik jari-jari. "
      "Minggu depan: metode numerik. Terima kasih, Wassalamualaikum."},
  ]
}

WEEKS["13"] = {
  "title_short": "Metode Numerik: Euler, RK4, dan Beda Hingga",
  "subtitle": "Minggu 13 - Numerical Methods for ODE dan PDE",
  "cpmk": [
    ("C1","Mengingat","Prinsip metode Euler eksplisit dan langkah waktu h"),
    ("C2","Memahami","Galat lokal dan global: orde O(h) vs O(h^4)"),
    ("C3","Menerapkan","Implementasi RK4 dan FDM untuk transien RC dan Laplace"),
    ("C4","Menganalisis","Analisis stabilitas numerik dan kriteria CFL"),
  ],
  "next_week": "Sistem Persamaan Diferensial dan Analisis State-Space",
  "slides": [
    {"title":"Pembukaan: Metode Numerik untuk PDE","quiz_pause":0,"text":
      "Selamat datang di Minggu 13. Kebanyakan PDB dan PDP di rekayasa nyata tidak memiliki solusi analitis. "
      "Euler, RK4, dan FDM adalah jawaban praktis industri tenaga listrik. "
      "Diampu bersama Insinyur Novalio Daratha dan Bapak Muhammad Arfan."},
    {"title":"Sub-CPMK dan Capaian Pembelajaran OBE","quiz_pause":0,"text":
      "Capaian Minggu 13: C1 mendefinisikan Euler dan langkah h. "
      "C2 memahami galat O h dan O h pangkat 4. "
      "C3 implementasi RK4 dan FDM. C4 menganalisis stabilitas dan CFL."},
    {"title":"Metode Euler Eksplisit","quiz_pause":0,"text":
      "y n tambah 1 sama dengan y n ditambah h dikali f kurung t n koma y n. "
      "Galat lokal O h kuadrat, galat global O h. "
      "Sederhana tapi tidak stabil untuk h terlalu besar."},
    {"title":"Metode Runge-Kutta 4","quiz_pause":0,"text":
      "Empat evaluasi per langkah: k1, k2, k3, k4. "
      "Update: y n tambah 1 sama dengan y n ditambah k1 tambah 2k2 tambah 2k3 tambah k4 per 6. "
      "Galat global O h pangkat 4."},
    {"title":"Perbandingan Euler vs RK4","quiz_pause":0,"text":
      "Transien RC tau sama dengan 1 detik, h sama dengan 0,1 detik: "
      "Euler galat 5 persen, RK4 galat 0,001 persen. "
      "RK4 4 kali lebih mahal namun 1000 kali lebih akurat."},
    {"title":"Finite Difference Method untuk Laplace","quiz_pause":0,"text":
      "Diskritisasi Laplace 2D: phi i+1 j ditambah phi i-1 j ditambah phi i j+1 ditambah phi i j-1 "
      "dikurang 4 phi i j sama dengan nol. "
      "Sistem linear besar A phi sama dengan b, selesaikan dengan Gauss-Seidel."},
    {"title":"Kriteria Stabilitas CFL","quiz_pause":0,"text":
      "Panas eksplisit: r sama dengan alpha kuadrat delta t per delta x kuadrat kurang dari 0,5. "
      "Gelombang: delta t per delta x kurang dari 1 per v p. "
      "Melanggar CFL: solusi meledak osilatoris."},
    {"title":"Kuis: Pilih Langkah Waktu Stabil","quiz_pause":8,"text":
      "Kuis! alpha kuadrat sama dengan 0,01 m kuadrat per detik, delta x sama dengan 0,1 m. "
      "Berapakah delta t maksimum yang stabil? Pikirkan 8 detik!"},
    {"title":"Jawaban: Langkah Waktu Stabil","quiz_pause":0,"text":
      "delta t kurang dari 0,5 dikali 0,01 per 0,01 sama dengan 0,5 detik. "
      "Gunakan delta t 0,4 detik untuk margin keamanan."},
    {"title":"Demo Julia: Euler vs RK4 Benchmark","quiz_pause":0,"text":
      "Dengan Julia, bandingkan Euler, RK4, dan DifferentialEquations adaptive. "
      "Plot galat terhadap h dalam skala log-log. "
      "Slope 1 untuk Euler, slope 4 untuk RK4."},
    {"title":"Rangkuman Minggu 13 dan Pratinjau Minggu 14","quiz_pause":0,"text":
      "Euler O h, RK4 O h pangkat 4. FDM mengubah PDP menjadi sistem linear. "
      "CFL wajib diperiksa untuk stabilitas. "
      "Minggu depan: state-space dan nilai eigen. Terima kasih, Wassalamualaikum."},
  ]
}

WEEKS["14"] = {
  "title_short": "Sistem PDB dan Analisis State-Space",
  "subtitle": "Minggu 14 - Systems of ODEs dan State-Space Analysis",
  "cpmk": [
    ("C1","Mengingat","Bentuk matriks state-space: x dot = Ax + Bu"),
    ("C2","Memahami","Nilai eigen dan vektor eigen menentukan modus respons"),
    ("C3","Menerapkan","Konversi rangkaian ke state-space dan solusi eksponensial matriks"),
    ("C4","Menganalisis","Analisis stabilitas sistem dari nilai eigen A"),
  ],
  "next_week": "Kapita Selekta dan Review Komprehensif Menuju UAS",
  "slides": [
    {"title":"Pembukaan: State-Space dan Kontrol Modern","quiz_pause":0,"text":
      "Selamat datang di Minggu 14. State-space adalah representasi universal sistem dinamik. "
      "Dari RLC orde tinggi hingga sistem tenaga dan kontrol, semua dapat dianalisis dengan state-space. "
      "Diampu bersama Insinyur Novalio Daratha dan Bapak Muhammad Arfan."},
    {"title":"Sub-CPMK dan Capaian Pembelajaran OBE","quiz_pause":0,"text":
      "Capaian Minggu 14: C1 mendefinisikan x dot sama dengan Ax ditambah Bu. "
      "C2 memahami nilai eigen dan vektor eigen. "
      "C3 konversi rangkaian ke state-space dan hitung eksponensial matriks. "
      "C4 analisis stabilitas dari nilai eigen A."},
    {"title":"Sistem PDB Linear: Representasi Matriks","quiz_pause":0,"text":
      "Sistem n PDB orde satu: x dot sama dengan A x ditambah B u. "
      "x vektor state n dimensi, A matriks sistem n kali n, "
      "B matriks input, u vektor input."},
    {"title":"Konversi RLC ke State-Space","quiz_pause":0,"text":
      "Variabel state: x 1 sama dengan i, x 2 sama dengan V C. "
      "Dari KVL: L x1 dot sama dengan minus R x1 dikurang x2 ditambah Vs. "
      "Dari KCL: C x2 dot sama dengan x1. "
      "Matriks A dua kali dua: baris 1 minus R per L dan minus 1 per L, baris 2 satu per C dan nol."},
    {"title":"Solusi Eksponensial Matriks","quiz_pause":0,"text":
      "x dari t sama dengan e pangkat At dikali x nol. "
      "e pangkat At sama dengan I ditambah At ditambah A kuadrat t kuadrat per 2 faktorial tambah seterusnya. "
      "Untuk matriks diagonalizable: P e pangkat Lambda t P invers."},
    {"title":"Nilai Eigen dan Stabilitas","quiz_pause":0,"text":
      "Nilai eigen dari det A dikurang lambda I sama dengan nol. "
      "Lambda real negatif: stabil meluruh. Lambda kompleks: osilasi teredam. "
      "Lambda real positif atau bagian real positif: TIDAK STABIL."},
    {"title":"Kuis: Nilai Eigen Matriks RLC","quiz_pause":8,"text":
      "Kuis! A sama dengan matriks dua kali dua baris satu minus 2 minus 1, baris dua 1 nol. "
      "Hitung lambda 1 dan lambda 2. Apakah sistem stabil? Pikirkan 8 detik!"},
    {"title":"Jawaban: Nilai Eigen","quiz_pause":0,"text":
      "lambda kuadrat ditambah 2 lambda ditambah 1 sama dengan kurung lambda tambah 1 kuadrat sama dengan nol. "
      "Akar kembar lambda sama dengan minus 1. Bagian real negatif: STABIL, critically damped."},
    {"title":"Demo Julia: State-Space Simulation","quiz_pause":0,"text":
      "Dengan Julia DifferentialEquations titik j l, definisikan du sama dengan A u. "
      "Plot evolusi semua variabel state. Hitung eigen dengan LinearAlgebra titik j l."},
    {"title":"Rangkuman Minggu 14 dan Pratinjau Minggu 15","quiz_pause":0,"text":
      "State-space menyatukan PDB linear dalam matriks. "
      "Nilai eigen menentukan stabilitas dan karakter transien. "
      "Minggu depan: kapita selekta dan review UAS. Terima kasih, Wassalamualaikum."},
  ]
}

WEEKS["15"] = {
  "title_short": "Kapita Selekta dan Review Komprehensif Menuju UAS",
  "subtitle": "Minggu 15 - Review dan Persiapan Ujian Akhir Semester",
  "cpmk": [
    ("C1","Mengingat","Peta konsep PDB ke PDP ke Numerik ke State-Space"),
    ("C2","Memahami","Kaitan Fourier-Laplace, Laplace-Gelombang, PDB-PDP"),
    ("C3","Menerapkan","Selesaikan soal komprehensif lintas topik"),
    ("C5","Mengevaluasi","Evaluasi kekuatan dan keterbatasan metode analitis vs numerik"),
  ],
  "next_week": "UAS - Ujian Akhir Semester",
  "slides": [
    {"title":"Pembukaan: Satu Semester Perjalanan","quiz_pause":0,"text":
      "Selamat datang di Minggu 15, pertemuan terakhir sebelum UAS. "
      "Satu semester penuh dari PDB orde satu hingga PDP tiga dimensi koordinat bola. "
      "Hari ini kita rangkum, identifikasi kaitan antar topik, dan persiapkan UAS. "
      "Diampu bersama Insinyur Novalio Daratha dan Bapak Muhammad Arfan."},
    {"title":"Sub-CPMK dan Capaian Pembelajaran OBE","quiz_pause":0,"text":
      "Capaian Minggu 15: C1 memetakan konsep keseluruhan satu semester. "
      "C2 memahami kaitan antar topik besar. "
      "C3 menyelesaikan soal komprehensif lintas topik. "
      "C5 mengevaluasi kekuatan dan keterbatasan metode."},
    {"title":"Peta Konsep Satu Semester","quiz_pause":0,"text":
      "Fondasi Minggu 1 sampai 3: klasifikasi PDB, orde satu, transien RC RL. "
      "Orde 2 Minggu 4 sampai 5: RLC dan Laplace. "
      "Spektrum Minggu 6: Deret Fourier harmonisa. "
      "PDP Minggu 7, 9 sampai 12: panas, Laplace, gelombang, Bessel, Legendre. "
      "Numerik dan Sistem Minggu 13 sampai 14: RK4, FDM, state-space."},
    {"title":"Kaitan Besar: Fourier dan Laplace","quiz_pause":0,"text":
      "Deret Fourier adalah kasus khusus Laplace pada sumbu imajiner s sama dengan j omega n. "
      "Transformasi Fourier kontinu adalah Laplace dengan s sama dengan j omega. "
      "Bukan dua alat terpisah — satu keluarga transformasi integral."},
    {"title":"Kaitan Besar: Laplace dan Gelombang","quiz_pause":0,"text":
      "Solusi gelombang dalam domain Laplace: H sama dengan e pangkat minus gamma L. "
      "gamma sama dengan akar ZY adalah konstanta propagasi. "
      "Semua analisis saluran transmisi modern menggunakan representasi Laplace."},
    {"title":"Kaitan Besar: PDB dan PDP","quiz_pause":0,"text":
      "Pemisahan variabel pada PDP menghasilkan rangkaian PDB. "
      "Koefisien PDP ditentukan oleh Deret Fourier kondisi batas. "
      "Fourier spektral mengubah PDP menjadi PDB dalam variabel waktu."},
    {"title":"Panduan Memilih Metode","quiz_pause":0,"text":
      "PDB orde 1 linear: faktor integrasi atau Laplace. "
      "PDB orde 2 homogen koefisien konstan: persamaan karakteristik. "
      "IVP: Laplace otomatis. Sinyal periodik: Fourier. "
      "Distribusi 2D 3D: Laplace pemisahan variabel. Sistem kompleks: Julia."},
    {"title":"Contoh Soal Komprehensif","quiz_pause":0,"text":
      "RLC dengan L sama dengan 1, C sama dengan 0,25, R sama dengan 5, V s sama dengan 10 sin 2t. "
      "Satu: tulis PDB orde 2. Dua: cari H dari s. "
      "Tiga: respons steady-state via Laplace. Empat: klasifikasikan respons transien."},
    {"title":"Kuis Final: Simulasi UAS","quiz_pause":8,"text":
      "Kuis final! y double prime ditambah 4 y prime ditambah 4 y sama dengan 0, "
      "y nol sama dengan 1, y prima nol sama dengan 0. "
      "Tipe respons, akar karakteristik, dan solusi analitis lengkap. "
      "Pikirkan 8 detik, ini tipe soal UAS!"},
    {"title":"Jawaban Kuis Final","quiz_pause":0,"text":
      "Karakteristik: kurung r tambah 2 kuadrat sama dengan nol. Akar kembar r sama dengan minus 2. Critically damped. "
      "Solusi umum: y sama dengan kurung C1 tambah C2 t e pangkat minus 2t. "
      "C1 sama dengan 1, C2 sama dengan 2. "
      "Solusi akhir: y dari t sama dengan kurung 1 tambah 2t e pangkat minus 2t."},
    {"title":"Pesan Penutup dan Sukses UAS","quiz_pause":0,"text":
      "Rekan-rekan mahasiswa Teknik Elektro UNIB yang luar biasa, "
      "satu semester kita membangun fondasi Persamaan Diferensial untuk perjalanan akademik dan profesional kalian. "
      "Pelajari semua modul, kerjakan soal latihan, hadapi UAS dengan percaya diri. "
      "Insinyur Novalio Daratha dan Bapak Muhammad Arfan mendoakan kesuksesan Anda. "
      "Wassalamualaikum warahmatullahi wabarakatuh."},
  ]
}

# ============================================================
# FUNGSI BUILD
# ============================================================
async def synth_tts(text, out_path):
    comm = edge_tts.Communicate(text=text, voice=TTS_VOICE, rate="+5%")
    await comm.save(out_path)

def run(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return result.returncode, result.stdout + result.stderr

def get_duration(path):
    out = subprocess.check_output(
        f'ffprobe -v error -show_entries format=duration '
        f'-of default=noprint_wrappers=1:nokey=1 "{path}"',
        shell=True).decode().strip()
    return float(out)

def build_week(week_num):
    data      = WEEKS[week_num]
    slides    = data["slides"]
    title_sh  = data["title_short"]
    subtitle  = data["subtitle"]
    cpmk      = data["cpmk"]
    next_week = data["next_week"]

    out_video  = os.path.join(PROJ_DIR, f"video_pd_minggu{week_num}.mp4")
    scratch_w  = os.path.join(SCRATCH, f"w{week_num}")
    os.makedirs(scratch_w, exist_ok=True)

    print(f"\n{'='*60}")
    print(f" MEMBANGUN VIDEO MINGGU {week_num}: {title_sh}")
    print(f"{'='*60}")
    t_start = time.time()

    # 0. Jeda kuis
    quiz_silence = os.path.join(scratch_w, "quiz_silence.mp3")
    if not os.path.exists(quiz_silence):
        run(f'ffmpeg -y -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 '
            f'-t 8 -q:a 9 -acodec libmp3lame "{quiz_silence}"')

    # 1. TTS
    print(f"\n=== 1. TTS {len(slides)} SLIDE ===")
    tts_files = []
    for i, s in enumerate(slides):
        sn    = i + 1
        tfile = os.path.join(scratch_w, f"tts_{sn:02d}.mp3")
        print(f"  Slide {sn:02d}: {s['title'][:50]}...")
        asyncio.run(synth_tts(s["text"], tfile))
        tts_files.append((sn, tfile, s.get("quiz_pause", 0)))

    total_tts = sum(get_duration(f) for (_, f, _) in tts_files)
    m, s2 = divmod(int(total_tts), 60)
    print(f"  Estimasi total: {m:02d}:{s2:02d}")

    # 2. LaTeX
    print(f"\n=== 2. GENERATE BEAMER LaTeX -> PNG ===")
    cpmk_items = "\n".join(
        f"    \\item \\textbf{{{c[0]} {c[1]}:}} {c[2]}"
        for c in cpmk)

    frames_tex = ""
    for i, s in enumerate(slides):
        sn  = i + 1
        ttl = s["title"].replace("&", r"\&").replace("#", r"\#").replace("%", r"\%")

        if sn == 1:
            frm = rf"""
\begin{{frame}}
  \begin{{center}}
    {{\color{{unibblue}}\Huge\bfseries Persamaan Diferensial}}\\[0.3em]
    {{\color{{unibgold}}\large\bfseries Minggu {week_num}: {title_sh.replace("&", "dan")}}}\\[0.3em]
    {{\normalsize {subtitle}}}\\[0.5em]
    \textit{{Ir. Novalio Daratha, S.T., M.Sc., Ph.D. \& Muhammad Arfan, S.T., M.T.}}\\
    \textit{{Teknik Elektro --- Universitas Bengkulu}}\\[0.3em]
    {{\small Semester Genap 2026}}
  \end{{center}}
\end{{frame}}"""
        elif sn == 2:
            frm = rf"""
\begin{{frame}}{{\frametitle{{Sub-CPMK \& Capaian Pembelajaran OBE}}}}
  \begin{{tcolorbox}}[colback=unibblue!10,colframe=unibblue,
    title={{\textbf{{Capaian Minggu {week_num} (OBE)}}}},fonttitle=\bfseries]
    \begin{{itemize}}
{cpmk_items}
    \end{{itemize}}
  \end{{tcolorbox}}
\end{{frame}}"""
        else:
            frm = rf"""
\begin{{frame}}{{\frametitle{{{ttl}}}}}
  \begin{{tcolorbox}}[colback=unibblue!5,colframe=unibblue!50,left=4pt,right=4pt,top=3pt,bottom=3pt]
    \small Slide {sn}/{len(slides)} --- Minggu {week_num}
  \end{{tcolorbox}}
  \vfill
  \begin{{center}}{{\color{{unibblue}}\small {title_sh.replace("&", "dan")}}}\end{{center}}
\end{{frame}}"""
        frames_tex += frm

    tex_doc = PREAMBLE + rf"""
\begin{{document}}
{frames_tex}
\end{{document}}
"""
    tex_path = os.path.join(scratch_w, f"slides_w{week_num}.tex")
    with open(tex_path, "w") as f:
        f.write(tex_doc)

    run(f'pdflatex -interaction=nonstopmode -output-directory "{scratch_w}" "{tex_path}"',
        cwd=scratch_w)
    pdf_path = os.path.join(scratch_w, f"slides_w{week_num}.pdf")
    run(f'pdftoppm -r 150 -png "{pdf_path}" "{os.path.join(scratch_w, "frame")}"')

    frames = sorted([f for f in os.listdir(scratch_w) if f.startswith("frame") and f.endswith(".png")])
    print(f"  {len(frames)} frame dihasilkan")

    # 3. Build klip
    print(f"\n=== 3. BUILD KLIP MP4 1080p STEREO ===")
    clip_list = []
    for i, s in enumerate(slides):
        sn   = i + 1
        fidx = min(i, len(frames)-1)
        img  = os.path.join(scratch_w, frames[fidx])
        aud  = tts_files[i][1]
        qp   = tts_files[i][2]
        clip = os.path.join(scratch_w, f"clip_{sn:02d}.mp4")

        if qp > 0:
            combined_audio = os.path.join(scratch_w, f"audio_{sn:02d}_q.mp3")
            run(f'ffmpeg -y -i "{aud}" -i "{quiz_silence}" '
                f'-filter_complex "[0:a][1:a]concat=n=2:v=0:a=1" "{combined_audio}"')
            aud_final = combined_audio
        else:
            aud_final = aud

        run(f'ffmpeg -y -loop 1 -i "{img}" -i "{aud_final}" '
            f'-c:v libx264 -preset faster -crf 18 -pix_fmt yuv420p '
            f'-vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" '
            f'-c:a aac -b:a 192k -ac 2 -shortest "{clip}"')
        clip_list.append(clip)
        print(f"  [OK] Klip {sn:02d}: {s['title'][:45]}")

    # 4. Concat
    print(f"\n=== 4. CONCAT FINAL ===")
    concat_file = os.path.join(scratch_w, "concat.txt")
    with open(concat_file, "w") as f:
        for c in clip_list:
            f.write(f"file '{c}'\n")

    run(f'ffmpeg -y -f concat -safe 0 -i "{concat_file}" '
        f'-c:v libx264 -preset faster -crf 18 '
        f'-c:a aac -b:a 192k -ac 2 "{out_video}"')

    # Verifikasi
    sz = os.path.getsize(out_video) / 1e6
    ch = subprocess.check_output(
        f'ffprobe -v error -select_streams a:0 -show_entries stream=channel_layout '
        f'-of default=noprint_wrappers=1:nokey=1 "{out_video}"',
        shell=True).decode().strip()
    elapsed = time.time() - t_start
    print(f"\n[SUKSES] {os.path.basename(out_video)}")
    print(f"  Ukuran : {sz:.2f} MB | Waktu: {elapsed:.1f}s | Audio: {ch}")

    # Copy ke portal
    portal_dst = os.path.join(PORTAL, f"video_pd_minggu{week_num}.mp4")
    shutil.copy2(out_video, portal_dst)
    print(f"  Portal : {portal_dst}")

    # Naskah YouTube v2
    script_path = os.path.join(PROJ_DIR, f"video_script_pd_w{week_num}_v2.md")
    with open(script_path, "w") as f:
        f.write(f"# Naskah Video Minggu {week_num} v2.0: {title_sh}\n\n")
        f.write(f"**Topik:** {subtitle}\n\n")
        f.write(f"**Judul YouTube:** `[Minggu {week_num}] {title_sh} | Persamaan Diferensial | Teknik Elektro UNIB`\n\n")
        f.write(f"**Estimasi Durasi:** {m:02d}:{s2:02d}\n\n")
        f.write(f"**Pratinjau Minggu Depan:** {next_week}\n\n")
        f.write("## Sub-CPMK OBE\n")
        for c in cpmk:
            f.write(f"- **{c[0]} {c[1]}:** {c[2]}\n")
        f.write("\n## Naskah Per Slide\n\n")
        for i, s in enumerate(slides):
            f.write(f"### Slide {i+1:02d}: {s['title']}\n\n{s['text']}\n\n")
    print(f"  Naskah : {script_path}")
    return True

# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    all_weeks = ["02","03","04","05","06","07","09","10","11","12","13","14","15"]
    target = [w.zfill(2) for w in sys.argv[1:]] if len(sys.argv) > 1 else all_weeks
    target = [w for w in target if w in WEEKS]

    print(f"=== BATCH BUILD v2.0 PERSAMAAN DIFERENSIAL ===")
    print(f"Target: {', '.join(target)}")

    results = {}
    for wk in target:
        try:
            build_week(wk)
            results[wk] = "SUKSES"
        except Exception as e:
            results[wk] = f"GAGAL: {e}"
            print(f"[ERROR] Minggu {wk}: {e}")

    print(f"\n{'='*50}\n LAPORAN AKHIR\n{'='*50}")
    for wk, st in results.items():
        print(f"  Minggu {wk}: {st}")
