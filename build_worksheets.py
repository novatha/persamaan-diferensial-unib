#!/usr/bin/env python3
"""
build_worksheets.py
Master generator and compiler for all 14 Student Worksheets (LKM)
Course: Persamaan Diferensial (S1 Teknik Elektro, Universitas Bengkulu)
Complies with:
- 4-Pilar Pedagogis (Engineering Intuition, Derivations, Julia 1.12+, Industry Standards)
- Taksonomi Bloom berjenjang (C1 s.d. C6 lengkap pada setiap lembar kerja)
- Standard 2-Page Double-Sided Layout (Zero widow/orphan text, Zero overfulls)
- Official UNIB Palette (unibblue #002060, unibgold #C5A059, unibgreen #22703C)
- CircuiTikZ & TikZ physical schematics in every single worksheet
"""

import os
import subprocess
import re

WORKSHEETS = {
    1: {
        "title": "Klasifikasi PDB/PDP, Nilai Awal (IVP), & Rangkaian RL",
        "subcpmk_num": "1",
        "subcpmk_text": "Mahasiswa mampu mengidentifikasi, mengklasifikasi, dan memodelkan fenomena dinamika sistem elektrik terpusat ke dalam Persamaan Diferensial Biasa (PDB) orde 1 serta memvalidasinya secara numerik.",
        "c1_text": "Sebutkan definisi formal Persamaan Diferensial Biasa (PDB) vs Persamaan Diferensial Parsial (PDP), serta jelaskan kriteria linearitas suatu PDB terhadap variabel terikat beserta seluruh turunannya.",
        "c1_box": "Ruang Pengerjaan C1 (Konsep Formal & Klasifikasi Linearitas)",
        "c1_h": "2.0cm",
        "c2_text": "Tinjau solusi umum $y(t) = C e^{-t/\\tau} + y_{\\text{ss}}$. Jelaskan mengapa konstanta $C$ hanya dapat ditentukan jika diberikan Masalah Nilai Awal (IVP), serta jelaskan makna fisis konstanta waktu $\\tau = L/R$ pada respons transien arus induktor.",
        "c2_box": "Ruang Pengerjaan C2 (Intuisi Fisika Transien & Nilai Awal)",
        "c2_h": "2.1cm",
        "c3_prompt": "Pada rangkaian RL di samping, sakelar ditutup pada $t=0$ dengan kondisi awal $i(0) = 0$. Turunkan persamaan diferensial loop arus dari KVK dan tentukan fungsi analitis arus $i(t)$ untuk $t \\ge 0$ jika $V_s = 24\\text{ V}$, $R = 8\\,\\Omega$, dan $L = 0{,}4\\text{ H}$.",
        "circuitikz": r"""\begin{circuitikz}[american, scale=0.65, transform shape]
    \draw (0,0) to[battery2, l=$V_s$, invert] (0,1.8)
          to[switch, l={$t{=}0$}] (1.6,1.8)
          to[R, l=$R$] (3.2,1.8)
          to[L, l=$L$, v=$v_L(t)$] (3.2,0)
          to[short] (0,0);
    \draw[->, >=stealth, thick, unibblue] (1.4,0.8) arc (160:-160:0.35);
    \node at (1.8,0.8) [unibblue, font=\tiny\bfseries] {$i(t)$};
  \end{circuitikz}""",
        "c3_box": "Ruang Pengerjaan C3 (Penurunan Solusi Eksak & Perhitungan Nilai)",
        "c3_h": "2.8cm",
        "c4_text": "Berdasarkan fungsi arus $i(t)$ pada Soal 3, analisis profil disipasi daya sesaat pada resistor $p_R(t) = R i^2(t)$ dan laju penyimpanan energi medan magnetik pada induktor $w_L(t) = \\frac{1}{2} L i^2(t)$. Hitung energi total yang tersimpan dalam induktor saat sistem telah mencapai keadaan tunak (\\textit{steady-state}, $t \\to \\infty$).",
        "c4_box": "Ruang Pengerjaan C4 (Analisis Neraca Energi & Daya Transien)",
        "c4_h": "3.8cm",
        "c5_text": "Suatu koil relay kontaktor gardu memiliki spesifikasi $R = 12\\,\\Omega$ dan $L = 2{,}4\\text{ H}$. Pabrikan menyatakan bahwa arus kontaktor membutuhkan waktu minimal $3\\tau$ untuk mencapai batas arus angkat (*pick-up current* $95\\%$ dari $I_{\\text{maks}}$). Evaluasi pernyataan teknis tersebut secara matematis, dan buktikan apakah waktu $t = 3\\tau$ memang mencukupi batas $95\\%$ tersebut!",
        "c5_box": "Ruang Pengerjaan C5 (Evaluasi Kinerja Teknis Kontaktor)",
        "c5_h": "3.8cm",
        "c6_text": "Rancang skrip program ilmiah berbasis \\textbf{Julia} (\\texttt{DifferentialEquations.jl} \\& \\texttt{Plots.jl}) untuk menyelesaikan PDB $\\frac{di}{dt} = \\frac{V_s - R i}{L}$ dengan solver \\texttt{Tsit5()} pada selang $t \\in [0, 0{,}5]\\text{ s}$. Tuliskan sintaks fungsi ODE dan blok pemecahannya di bawah ini.",
        "c6_box": "Ruang Pengerjaan C6 (Sintaks Program Ilmiah Julia & Parameter Desain)",
        "c6_h": "3.8cm",
    },
    2: {
        "title": "Metode Analitik PDB Orde 1: Separabel & Eksak",
        "subcpmk_num": "2",
        "subcpmk_text": "Mahasiswa mampu mengidentifikasi dan menyelesaikan PDB orde 1 secara analitik (separabel, eksak, dan faktor integrasi) serta memodelkan dinamika pengisian muatan kapasitor RC.",
        "c1_text": "Jelaskan definisi matematis persamaan diferensial terpisahkan (*separable ODE*) dan tuliskan syarat perlu dan cukup agar bentuk diferensial $M(x,y)dx + N(x,y)dy = 0$ merupakan persamaan diferensial eksak.",
        "c1_box": "Ruang Pengerjaan C1 (Definisi Separabel & Syarat Eksak Euler)",
        "c1_h": "2.0cm",
        "c2_text": "Tinjau persamaan non-eksak yang dapat dieksakkan melalui faktor integrasi $\\mu(x) = \\exp\\left(\\int \\frac{M_y - N_x}{N} dx\\right)$. Jelaskan secara fisis mengapa pengali $\\mu(x)$ tidak mengubah kurva integral solusi fisik sistem kelistrikan.",
        "c2_box": "Ruang Pengerjaan C2 (Interpretasi Geometris & Fisis Faktor Integrasi)",
        "c2_h": "2.1cm",
        "c3_prompt": "Pada rangkaian pengisian kapasitor di samping, sakelar ditutup pada $t=0$ dengan tegangan awal $v_C(0) = 0$. Turunkan PDB separabel untuk tegangan $v_C(t)$ dan tentukan solusi khususnya jika $V_s = 12\\text{ V}$, $R = 10\\text{ k}\\Omega$, dan $C = 100\\,\\mu\\text{F}$.",
        "circuitikz": r"""\begin{circuitikz}[american, scale=0.65, transform shape]
    \draw (0,0) to[battery2, l=$V_s$, invert] (0,1.8)
          to[switch, l={$t{=}0$}] (1.6,1.8)
          to[R, l=$R$] (3.2,1.8)
          to[C, l=$C$, v=$v_C(t)$] (3.2,0)
          to[short] (0,0);
    \draw[->, >=stealth, thick, unibblue] (1.4,0.8) arc (160:-160:0.35);
    \node at (1.8,0.8) [unibblue, font=\tiny\bfseries] {$i(t)$};
  \end{circuitikz}""",
        "c3_box": "Ruang Pengerjaan C3 (Penurunan Solusi Separabel RC)",
        "c3_h": "2.8cm",
        "c4_text": "Analisis paradoks energi pengisian kapasitor: Hitung energi total yang disuplai oleh sumber $W_s = \\int_0^\\infty V_s i(t) dt$, energi yang tersimpan pada medan listrik kapasitor $W_C = \\frac{1}{2} C V_s^2$, dan energi yang terdisipasi menjadi kalor pada resistor $W_R = \\int_0^\\infty R i^2(t) dt$. Buktikan bahwa $W_R$ selalu tepat $50\\%$ berapapun nilai resistansi $R$!",
        "c4_box": "Ruang Pengerjaan C4 (Pembuktian Analitis Paradoks 50% Energi RC)",
        "c4_h": "3.8cm",
        "c5_text": "Diberikan persamaan distribusi fluks medan magnetik non-linier: $(2x y + e^y)dx + (x^2 + x e^y - 2y)dy = 0$. Evaluasi apakah persamaan ini eksak. Jika eksak, temukan fungsi potensial medan $\\phi(x,y) = C$ langkah demi langkah!",
        "c5_box": "Ruang Pengerjaan C5 (Uji Eksak & Penurunan Solusi Potensial)",
        "c5_h": "3.8cm",
        "c6_text": "Rancang algoritma numerik eksplisit (Metode Euler Satu Langkah) dalam bahasa \\textbf{Julia} untuk menyelesaikan pengosongan RC: $\\frac{dv_C}{dt} = -\\frac{v_C}{RC}$ dengan langkah waktu $\\Delta t = 0{,}1\\tau$. Tuliskan fungsi pembaruan loop komputasinya.",
        "c6_box": "Ruang Pengerjaan C6 (Skrip Algoritma Numerik Euler Julia)",
        "c6_h": "3.8cm",
    },
    3: {
        "title": "Aplikasi Transien Rekayasa & Pemodelan Termal Transformator",
        "subcpmk_num": "3",
        "subcpmk_text": "Mahasiswa mampu menerapkan metodologi PDB orde 1 untuk memodelkan fenomena transien termal peralatan tenaga listrik (Hukum Pendinginan Newton & IEEE Std C57.91) serta memvalidasinya secara numerik.",
        "c1_text": "Tuliskan formulasi matematis Hukum Pendinginan Newton untuk dinamika temperatur benda $T(t)$ dalam medium bertemperatur lingkungan konstan $T_a$, dan sebutkan analogi fisis besaran termal terhadap besaran rangkaian listrik.",
        "c1_box": "Ruang Pengerjaan C1 (Formulasi Termal & Analogi Rangkaian Listrik)",
        "c1_h": "2.0cm",
        "c2_text": "Jelaskan konsep kapasitas kalor termal ($C_{\\text{th}}$) dan resistansi termal ($R_{\\text{th}}$). Bagaimana konstanta waktu termal $\\tau_{\\text{th}} = R_{\\text{th}} C_{\\text{th}}$ mempengaruhi inersia kenaikan suhu belitan transformator saat memikul beban puncak mendadak?",
        "c2_box": "Ruang Pengerjaan C2 (Inersia Termal & Konstanta Waktu Pendinginan)",
        "c2_h": "2.1cm",
        "c3_prompt": "Berdasarkan sirkuit termal ekuivalen trafo daya di samping, sumber arus kalor rugi tembaga $P_{\\text{loss}} = 50\\text{ kW}$ memanaskan minyak trafo dengan $C_{\\text{th}} = 2{,}5\\text{ MJ/}^\\circ\\text{C}$ dan $R_{\\text{th}} = 0{,}8\\times 10^{-3}\\,^\\circ\\text{C/W}$. Jika suhu awal sama dengan suhu sekitar $T(0) = T_a = 30^\\circ\\text{C}$, tentukan fungsi kenaikan suhu minyak $T(t)$.",
        "circuitikz": r"""\begin{circuitikz}[american, scale=0.65, transform shape]
    \draw (0,0) to[I, l=$P_{\text{loss}}$] (0,1.8)
          to[short] (1.6,1.8)
          to[R, l=$R_{\text{th}}$] (1.6,0)
          to[short] (0,0);
    \draw (1.6,1.8) to[short] (3.0,1.8)
          to[C, l=$C_{\text{th}}$, v=$\theta(t)$] (3.0,0)
          to[short] (1.6,0);
    \node at (3.0,2.1) [font=\tiny\bfseries, unibblue] {$T(t) - T_a$};
  \end{circuitikz}""",
        "c3_box": "Ruang Pengerjaan C3 (Penurunan Model Kenaikan Suhu Trafo)",
        "c3_h": "2.8cm",
        "c4_text": "Analisis dampak pembebanan lebih (\\textit{overload}) terhadap umur pakai isolasi kertas transformator. Jika batas suhu aman kontinu menurut \\textbf{IEEE Std C57.91} adalah $110^\\circ\\text{C}$, hitung waktu kritis $t_{\\text{kritis}}$ saat suhu minyak trafo mencapai $105^\\circ\\text{C}$ berdasarkan model transien Soal 3.",
        "c4_box": "Ruang Pengerjaan C4 (Analisis Waktu Kritis Pembebanan Lebih IEEE C57.91)",
        "c4_h": "3.8cm",
        "c5_text": "Sebuah sensor termal mengalami penurunan eksponensial saat dicelupkan ke air es $0^\\circ\\text{C}$: tercatat suhu turun dari $80^\\circ\\text{C}$ menjadi $40^\\circ\\text{C}$ dalam 15 detik. Evaluasi apakah laju pendinginan tersebut konsisten dengan model linier orde 1, dan prediksi suhu sensor pada detik ke-45!",
        "c5_box": "Ruang Pengerjaan C5 (Evaluasi Validitas Model Eksponensial & Prediksi)",
        "c5_h": "3.8cm",
        "c6_text": "Rancang skrip program \\textbf{Julia} menggunakan paket \\texttt{DifferentialEquations.jl} untuk memodelkan sistem pendinginan dinamis dengan suhu lingkungan berosilasi harian $T_a(t) = 28 + 6\\sin(\\frac{2\\pi t}{86400})$. Tuliskan definisi fungsi laju termal \\texttt{dT/dt} secara modular.",
        "c6_box": "Ruang Pengerjaan C6 (Skrip Model Dinamis Termal Julia dengan Suhu Ambien Sinusoidal)",
        "c6_h": "3.8cm",
    },
    4: {
        "title": "PDB Orde 2 Homogen & Karakteristik Redaman RLC",
        "subcpmk_num": "3",
        "subcpmk_text": "Mahasiswa mampu memformulasikan dan menyelesaikan PDB linier orde 2 homogen koefisien konstan serta menganalisis tiga ragam redaman rangkaian RLC bebas sumber.",
        "c1_text": "Tuliskan bentuk baku persamaan karakteristik dari PDB $a y'' + b y' + c y = 0$ dan sebutkan hubungan diskriminan $\\Delta = b^2 - 4ac$ dengan tiga kemungkinan ragam solusi fisisnya.",
        "c1_box": "Ruang Pengerjaan C1 (Persamaan Karakteristik & Klasifikasi Diskriminan)",
        "c1_h": "2.0cm",
        "c2_text": "Jelaskan makna fisis faktor redaman $\\alpha = R/(2L)$ dan frekuensi sudut alami tak-teredam $\\omega_0 = 1/\\sqrt{LC}$. Apa yang terjadi pada respons transien tegangan kapasitor ketika rasio redaman $\\zeta = \\alpha/\\omega_0 = 1$ (redaman kritis)?",
        "c2_box": "Ruang Pengerjaan C2 (Intuisi Fisika Parameter Redaman RLC)",
        "c2_h": "2.1cm",
        "c3_prompt": "Pada rangkaian RLC seri di samping, kapasitor telah dimuati hingga $v_C(0) = 100\\text{ V}$ dan $i(0) = 0$. Jika sakelar ditutup pada $t=0$ dengan $R = 20\\,\\Omega$, $L = 0{,}1\\text{ H}$, dan $C = 100\\,\\mu\\text{F}$, turunkan persamaan arus $i(t)$ dan tentukan ragam redamannya.",
        "circuitikz": r"""\begin{circuitikz}[american, scale=0.65, transform shape]
    \draw (0,0) to[C, l=$C$, v=$v_C(0){=}V_0$] (0,1.8)
          to[switch, l={$t{=}0$}] (1.5,1.8)
          to[R, l=$R$] (3.0,1.8)
          to[L, l=$L$, v=$v_L(t)$] (3.0,0)
          to[short] (0,0);
    \draw[->, >=stealth, thick, unibblue] (1.3,0.8) arc (160:-160:0.35);
    \node at (1.7,0.8) [unibblue, font=\tiny\bfseries] {$i(t)$};
  \end{circuitikz}""",
        "c3_box": "Ruang Pengerjaan C3 (Penurunan Solusi Transien RLC Seri)",
        "c3_h": "2.8cm",
        "c4_text": "Analisis nilai resistansi kritis $R_{\\text{kritis}}$ agar rangkaian pada Soal 3 bertransisi tepat pada kondisi redaman kritis (\\textit{critically damped}). Hitung waktu puncak ($t_{\\text{puncak}}$) saat arus mencapai nilai ekstremum pertamanya pada kondisi tersebut.",
        "c4_box": "Ruang Pengerjaan C4 (Analisis Desain Nilai Redaman Kritis & Arus Puncak)",
        "c4_h": "3.8cm",
        "c5_text": "Tinjau rangkaian resonansi underdamped dengan redaman sangat kecil ($R \\to 0$). Buktikan secara matematis melalui teorema Euler bahwa solusi kompleks konjugat $r_{1,2} = -\\alpha \\pm j\\omega_d$ bertransformasi menjadi gelombang sinusoidal murni tak teredam dengan hukum kekekalan energi $W_{\\text{total}} = \\text{konstan}$.",
        "c5_box": "Ruang Pengerjaan C5 (Pembuktian Kekekalan Energi Osilasi LC Murni)",
        "c5_h": "3.8cm",
        "c6_text": "Rancang skrip program \\textbf{Julia} untuk menyelesaikan sistem persamaan diferensial keadaan (\\textit{state-space}) 2 variabel: $\\frac{dv_C}{dt} = -\\frac{i}{C}$, $\\frac{di}{dt} = \\frac{v_C - R i}{L}$. Plot lintasan ruang keadaan (*phase plane*) $i(t)$ vs $v_C(t)$ dengan paket \\texttt{Plots.jl}.",
        "c6_box": "Ruang Pengerjaan C6 (Skrip Julia State-Space & Phase-Plane Plotting)",
        "c6_h": "3.8cm",
    },
    5: {
        "title": "PDB Orde 2 Non-Homogen & Resonansi RLC Eksitasi AC",
        "subcpmk_num": "3",
        "subcpmk_text": "Mahasiswa mampu memecahkan PDB linier orde 2 non-homogen menggunakan metode koefisien tak tentu dan variasi parameter untuk menganalisis resonansi dan faktor kualitas rangkaian AC.",
        "c1_text": "Jelaskan prinsip superposisi solusi total PDB non-homogen $y(t) = y_h(t) + y_p(t)$, dan sebutkan aturan pemilihan bentuk tebakan solusi partikular $y_p(t)$ jika fungsi pemaksa berbentuk $F(t) = V_m \\sin(\\omega t)$.",
        "c1_box": "Ruang Pengerjaan C1 (Prinsip Solusi Lengkap & Bentuk Tebakan Partikular)",
        "c1_h": "2.0cm",
        "c2_text": "Jelaskan fenomena resonansi listrik seri secara fisis. Mengapa pada frekuensi resonansi $\\omega_0 = 1/\\sqrt{LC}$, impedansi total rangkaian menjadi minimum ($Z = R$) dan arus mencapai nilai maksimum?",
        "c2_box": "Ruang Pengerjaan C2 (Intuisi Fisika Resonansi Seri & Pembatalan Reaktansi)",
        "c2_h": "2.1cm",
        "c3_prompt": "Rangkaian RLC seri di samping dihubungkan ke sumber tegangan AC $v_s(t) = 100 \\cos(1000 t)\\text{ V}$. Dengan $R = 10\\,\\Omega$, $L = 0{,}05\\text{ H}$, dan $C = 20\\,\\mu\\text{F}$, tentukan solusi partikular tunak (*steady-state*) arus $i_{\\text{ss}}(t) = I_m \\cos(1000 t - \\phi)$.",
        "circuitikz": r"""\begin{circuitikz}[american, scale=0.65, transform shape]
    \draw (0,0) to[sV, l=$v_s(t)$] (0,1.8)
          to[R, l=$R$] (1.6,1.8)
          to[L, l=$L$] (3.0,1.8)
          to[C, l=$C$] (3.0,0)
          to[short] (0,0);
    \draw[->, >=stealth, thick, unibblue] (1.4,0.8) arc (160:-160:0.35);
    \node at (1.8,0.8) [unibblue, font=\tiny\bfseries] {$i(t)$};
  \end{circuitikz}""",
        "c3_box": "Ruang Pengerjaan C3 (Penurunan Solusi Partikular Arus AC Tunak)",
        "c3_h": "2.8cm",
        "c4_text": "Analisis perbesaran tegangan kapasitor pada kondisi resonansi: Definisikan Faktor Kualitas $Q = \\frac{\\omega_0 L}{R}$. Buktikan secara matematis bahwa pada kondisi resonansi, amplitudo tegangan pada kapasitor memenuhi hubungan $V_{C,\\text{maks}} = Q \\cdot V_s$. Apa bahaya fenomena ini terhadap dielektrik isolasi?",
        "c4_box": "Ruang Pengerjaan C4 (Analisis Faktor Kualitas Q & Perbesaran Tegangan Kritis)",
        "c4_h": "3.8cm",
        "c5_text": "Suatu sistem mengalami eksitasi tepat pada frekuensi alami tanpa redaman: $y'' + \\omega_0^2 y = F_0 \\cos(\\omega_0 t)$. Evaluasi kegagalan tebakan standar dan buktikan dengan metode variasi parameter bahwa solusinya tumbuh secara linier terhadap waktu ($t \\sin(\\omega_0 t)$) menuju resonansi tak-hingga (destruktif).",
        "c5_box": "Ruang Pengerjaan C5 (Evaluasi Resonansi Murni Tak-Hingga & Amplifikasi Linier)",
        "c5_h": "3.8cm",
        "c6_text": "Rancang program simulasi frekuensi sapuan (\\textit{frequency sweep}) dalam \\textbf{Julia} untuk menghitung respons amplitudo arus terhadap variasi frekuensi eksitasi $\\omega \\in [0{,}2\\omega_0, 2\\omega_0]$. Tuliskan algoritma vektorisasi perhitungan magnitudo impedansi $|Z(\\omega)|$.",
        "c6_box": "Ruang Pengerjaan C6 (Skrip Julia Kurva Respon Resonansi & Lebar Pita)",
        "c6_h": "3.8cm",
    },
    6: {
        "title": "Transformasi Laplace & Sinyal Transien Impuls Surja Petir",
        "subcpmk_num": "4",
        "subcpmk_text": "Mahasiswa mampu memetakan fungsi waktu ke domain frekuensi kompleks $s$ menggunakan Transformasi Laplace serta memodelkan respons sistem terhadap sinyal diskontinu (Heaviside & Dirac).",
        "c1_text": "Tuliskan definisi integral dari Transformasi Laplace unilateral $\\mathcal{L}\\{f(t)\\}$, dan sebutkan dua kondisi eksistensi agar suatu fungsi waktu $f(t)$ memiliki transformasi Laplace yang konvergen.",
        "c1_box": "Ruang Pengerjaan C1 (Definisi Integral Laplace & Kondisi Konvergensi)",
        "c1_h": "2.0cm",
        "c2_text": "Jelaskan Teorema Diferensiasi Laplace: $\\mathcal{L}\\{f'(t)\\} = s F(s) - f(0^-)$. Mengapa sifat ini sangat ampuh mentransformasi persamaan diferensial kalkulus menjadi persamaan aljabar linier biasa?",
        "c2_box": "Ruang Pengerjaan C2 (Makna Aljabar Teorema Diferensiasi Laplace)",
        "c2_h": "2.1cm",
        "c3_prompt": "Berdasarkan standar \\textbf{IEC 60060-1}, gelombang impuls petir $1{,}2/50\\,\\mu\\text{s}$ dimodelkan dengan selisih dua fungsi eksponensial: $v(t) = V_0 (e^{-\\alpha t} - e^{-\\beta t}) u(t)$. Tentukan representasi domain Laplace $V(s) = \\mathcal{L}\\{v(t)\\}$ secara eksplisit.",
        "circuitikz": r"""\begin{circuitikz}[american, scale=0.65, transform shape]
    \draw (0,0) to[I, l=$I_0 \delta(t)$] (0,1.8)
          to[short] (1.5,1.8)
          to[R, l=$R_1$] (1.5,0)
          to[short] (0,0);
    \draw (1.5,1.8) to[R, l=$R_2$] (3.0,1.8)
          to[C, l=$C_2$, v=$v_{\text{impuls}}(t)$] (3.0,0)
          to[short] (1.5,0);
  \end{circuitikz}""",
        "c3_box": "Ruang Pengerjaan C3 (Transformasi Laplace Gelombang Impuls Petir IEC)",
        "c3_h": "2.8cm",
        "c4_text": "Analisis respons rangkaian RL terhadap sinyal tegangan pulsa persegi dengan durasi $T$: $v_s(t) = V_0 [u(t) - u(t-T)]$. Gunakan Teorema Pergeseran Waktu (*Second Shifting Theorem*) untuk menemukan arus domain-$s$ $I(s)$ dan analisis bentuk gelombang transiennya.",
        "c4_box": "Ruang Pengerjaan C4 (Analisis Respons Pulsa Kotak Heaviside pada Koil RL)",
        "c4_h": "3.8cm",
        "c5_text": "Evaluasi perilaku nilai awal dan nilai akhir fungsi menggunakan Teorema Nilai Awal (IVT) $\\lim_{t \\to 0^+} f(t) = \\lim_{s \\to \\infty} s F(s)$ dan Teorema Nilai Akhir (FVT) $\\lim_{t \\to \\infty} f(t) = \\lim_{s \\to 0} s F(s)$ pada fungsi transfer arus $I(s) = \\frac{10}{s(s+5)}$. Validasi hasilnya terhadap solusi domain waktu.",
        "c5_box": "Ruang Pengerjaan C5 (Evaluasi Teorema Nilai Awal & Akhir Laplace)",
        "c5_h": "3.8cm",
        "c6_text": "Rancang skrip program \\textbf{Julia} untuk menghasilkan dan memplot gelombang surja impuls petir standar IEC 60060-1 ($V_0 = 100\\text{ kV}, \\alpha = 14658\\text{ s}^{-1}, \\beta = 2469135\\text{ s}^{-1}$) pada selang waktu mikrodetik $t \\in [0, 100\\,\\mu\\text{s}]$.",
        "c6_box": "Ruang Pengerjaan C6 (Skrip Plotting Surja Petir Resolusi Mikrodetik Julia)",
        "c6_h": "3.8cm",
    },
    7: {
        "title": "Invers Transformasi Laplace & Pemutus Tenaga (TRV)",
        "subcpmk_num": "4",
        "subcpmk_text": "Mahasiswa mampu merekonstruksi sinyal waktu melalui Invers Transformasi Laplace (pecahan parsial & integral konvolusi) serta menganalisis fenomena Transient Recovery Voltage (TRV) pada pemutus tenaga PMT.",
        "c1_text": "Tuliskan tiga kasus dekomposisi pecahan parsial (*partial fraction expansion*) untuk fungsi rasional $F(s) = P(s)/Q(s)$ (akar riil berbeda, akar riil berulang, dan pasangan akar kompleks konjugat).",
        "c1_box": "Ruang Pengerjaan C1 (Kaidah Dekomposisi Pecahan Parsial)",
        "c1_h": "2.0cm",
        "c2_text": "Jelaskan definisi fisis *Transient Recovery Voltage* (TRV) yang muncul melintasi kontak Pemutus Tenaga (PMT / *Circuit Breaker*) sesaat setelah pemutusan arus hubung singkat menurut standar \\textbf{IEC 62271-100}.",
        "c2_box": "Ruang Pengerjaan C2 (Intuisi Fisika TRV & Kegagalan Dielektrik PMT)",
        "c2_h": "2.1cm",
        "c3_prompt": "Model domain-$s$ dari tegangan pemulihan transien PMT diberikan oleh $V_{\\text{TRV}}(s) = V_m \\left( \\frac{1}{s} - \\frac{s}{s^2 + \\omega_0^2} \\right)$. Gunakan invers transformasi Laplace untuk menurunkan fungsi waktu analitis $v_{\\text{TRV}}(t)$, dan tentukan nilai puncak maksimumnya!",
        "circuitikz": r"""\begin{circuitikz}[american, scale=0.65, transform shape]
    \draw (0,0) to[sV, l=$v_s(t)$] (0,1.8)
          to[L, l=$L_{\text{trafo}}$] (1.6,1.8)
          to[switch, l={PMT Buka}] (3.0,1.8)
          to[short] (3.0,0)
          to[short] (0,0);
    \draw (1.6,1.8) to[C, l=$C_{\text{bus}}$, v=$v_{\text{TRV}}$] (1.6,0);
  \end{circuitikz}""",
        "c3_box": "Ruang Pengerjaan C3 (Invers Laplace & Penentuan Nilai Puncak TRV)",
        "c3_h": "2.8cm",
        "c4_text": "Analisis laju kenaikan tegangan pemulihan (\\textit{Rate of Rise of Recovery Voltage} / RRRV) yang didefinisikan sebagai $\\text{RRRV} = \\left. \\frac{dv_{\\text{TRV}}}{dt} \\right|_{\\text{maks}}$. Jelaskan mengapa jika RRRV melebihi kekuatan dielektrik celah busur gas $\\text{SF}_6$, pemutus tenaga akan mengalami *re-strike* (kegagalan interupsi).",
        "c4_box": "Ruang Pengerjaan C4 (Analisis Kritis Parameter RRRV Standar IEC 62271)",
        "c4_h": "3.8cm",
        "c5_text": "Selesaikan PDB sistem kendali eksitasi dengan nilai awal tidak nol: $y'' + 4y' + 13y = 0$, $y(0) = 5$, $y'(0) = -10$. Evaluasi apakah respons waktu mengalami osilasi teredam, dan tentukan frekuensi osilasi teredamnya $\\omega_d$.",
        "c5_box": "Ruang Pengerjaan C5 (Penyelesaian Lengkap IVP Domain-s & Evaluasi Redaman)",
        "c5_h": "3.8cm",
        "c6_text": "Rancang skrip numerik berbasis \\textbf{Julia} untuk menyelesaikan PDB TRV orde 2 non-homogen dengan paket \\texttt{DifferentialEquations.jl} serta memplot kurva $v_{\\text{TRV}}(t)$ bersama garis batas dielektrik PMT.",
        "c6_box": "Ruang Pengerjaan C6 (Skrip Simulasi Numerik TRV PMT Gardu Induk Julia)",
        "c6_h": "3.8cm",
    },
    9: {
        "title": "Deret Fourier Trigonometrik & Analisis Harmonisa Beban",
        "subcpmk_num": "5",
        "subcpmk_text": "Mahasiswa mampu merepresentasikan gelombang periodik tak-sinusoidal ke dalam Deret Fourier trigonometrik dan menganalisis distorsi harmonisa (THD) pada sistem kelistrikan sesuai IEEE Std 519.",
        "c1_text": "Tuliskan bentuk umum Deret Fourier trigonometrik untuk fungsi periodik $f(t)$ dengan periode $T = 2\\pi/\\omega_0$, dan tuliskan rumus integral penentuan koefisien $a_0$, $a_n$, dan $b_n$.",
        "c1_box": "Ruang Pengerjaan C1 (Definisi Deret Fourier & Integral Euler-Fourier)",
        "c1_h": "2.0cm",
        "c2_text": "Jelaskan sifat kesimetrian fungsi genap ($f(-t) = f(t)$), fungsi ganjil ($f(-t) = -f(t)$), dan kesimetrian setengah gelombang (*half-wave symmetry*). Bagaimana kesimetrian ini menyederhanakan perhitungan koefisien Fourier?",
        "c2_box": "Ruang Pengerjaan C2 (Pemanfaatan Sifat Kesimetrian Sinyal Listrik)",
        "c2_h": "2.1cm",
        "c3_prompt": "Tegangan keluaran inverter fotovoltaik satu fasa berbentuk gelombang persegi simetris ganjil: $v(t) = +V_d$ untuk $0 < t < T/2$ dan $-V_d$ untuk $T/2 < t < T$. Turunkan deret Fourier trigonometrik analitis dari tegangan tersebut.",
        "circuitikz": r"""\begin{circuitikz}[scale=0.65, transform shape]
    \draw[->, >=stealth] (-0.2,0) -- (3.5,0) node[right, font=\tiny] {$t$};
    \draw[->, >=stealth] (0,-1.3) -- (0,1.5) node[above, font=\tiny] {$v(t)$};
    \draw[very thick, unibblue] (0,1) -- (1.5,1) -- (1.5,-1) -- (3,-1) -- (3,1) -- (3.3,1);
    \draw[dashed, gray] (1.5,0) node[below, font=\tiny] {$T/2$} -- (1.5,1);
    \draw[dashed, gray] (3,0) node[below, font=\tiny] {$T$} -- (3,-1);
    \node at (-0.4,1) [font=\tiny\bfseries] {$+V_d$};
    \node at (-0.4,-1) [font=\tiny\bfseries] {$-V_d$};
  \end{circuitikz}""",
        "c3_box": "Ruang Pengerjaan C3 (Penurunan Koefisien Fourier Gelombang Inverter)",
        "c3_h": "2.8cm",
        "c4_text": "Analisis Distorsi Harmonisa Total (\\textit{Total Harmonic Distortion} / THD) tegangan yang didefinisikan oleh \\textbf{IEEE Std 519}: $\\text{THD}_v = \\frac{\\sqrt{\\sum_{n=2}^\\infty V_n^2}}{V_1} \\times 100\\%$. Berdasarkan deret Fourier Soal 3, buktikan bahwa $\\text{THD}_v$ gelombang persegi murni bernilai $\\approx 48{,}34\\%$!",
        "c4_box": "Ruang Pengerjaan C4 (Pembuktian Analitis THD Tegangan Standar IEEE 519)",
        "c4_h": "3.8cm",
        "c5_text": "Evaluasi Fenomena Gibbs: Saat merekonstruksi diskontinuitas loncatan gelombang persegi dengan jumlah harmonisa berhingga ($N \\to \\infty$), lonjakan (*overshoot*) tidak lenyap melainkan konvergen ke $8{,}95\\%$. Jelaskan mengapa penambahan suku harmonisa tinggi tidak dapat menghilangkan lonjakan ini!",
        "c5_box": "Ruang Pengerjaan C5 (Evaluasi Fenomena Gibbs & Konvergensi Titik Diskontinu)",
        "c5_h": "3.8cm",
        "c6_text": "Rancang skrip program \\textbf{Julia} untuk merekonstruksi deret Fourier gelombang persegi hingga harmonisa ke-$N$ ($N=1, 3, 5, 25$) dan memplot perbandingan kurvanya untuk memvisualisasikan fenomena Gibbs.",
        "c6_box": "Ruang Pengerjaan C6 (Skrip Rekonstruksi Parsial Deret Fourier Julia)",
        "c6_h": "3.8cm",
    },
    10: {
        "title": "Metode Pemisahan Variabel & Transien Busbar Gardu Induk",
        "subcpmk_num": "5",
        "subcpmk_text": "Mahasiswa mampu menyelesaikan Persamaan Diferensial Parsial linier homogen menggunakan metode pemisahan variabel serta memodelkan distribusi panas konduktor busbar gardu induk sesuai IEEE Std 738.",
        "c1_text": "Jelaskan postulat dasar metode pemisahan variabel (*separation of variables*) untuk mencari solusi PDP $u(x,t)$ sebagai perkalian dua fungsi variabel tunggal $u(x,t) = X(x) \\cdot T(t)$.",
        "c1_box": "Ruang Pengerjaan C1 (Postulat Produk Pemisahan Variabel)",
        "c1_h": "2.0cm",
        "c2_text": "Mengapa konstanta pemisahan $k$ pada persamaan difusi/gelombang fisik harus dipilih bernilai riil negatif ($k = -\\lambda^2$)? Jelaskan konsekuensi termodinamika jika konstanta dipilih nol ($k=0$) atau positif ($k=+\\lambda^2$).",
        "c2_box": "Ruang Pengerjaan C2 (Argumen Kestabilan Termodinamika Pemilihan Nilai Eigen)",
        "c2_h": "2.1cm",
        "c3_prompt": "Sebuah rel busbar tembaga gardu induk sepanjang $L=2\\text{ m}$ memenuhi PDP difusi panas $\\frac{\\partial u}{\\partial t} = \\alpha \\frac{\\partial^2 u}{\\partial x^2}$. Jika kedua ujung busbar dihubungkan ke penyangga bertemperatur konstan $u(0,t) = u(L,t) = 0$, turunkan persamaan nilai eigen $\\lambda_n$ dan fungsi eigen spasial $X_n(x)$.",
        "circuitikz": r"""\begin{tikzpicture}[scale=0.65]
    \draw[top color=unibgold!60, bottom color=unibgold!90, draw=black, thick] (0,0.4) rectangle (3.5,-0.4);
    \draw[fill=unibblue!80] (-0.3,0.7) rectangle (0,-0.7);
    \draw[fill=unibblue!80] (3.5,0.7) rectangle (3.8,-0.7);
    \node at (-0.15,0.9) [font=\tiny] {$u(0,t)=0$};
    \node at (3.65,0.9) [font=\tiny] {$u(L,t)=0$};
    \draw[<->, >=stealth] (0,-0.7) -- (3.5,-0.7) node[midway, below, font=\tiny] {$L = 2\text{ m}$};
    \node at (1.75,0) [font=\tiny\bfseries, color=black] {Rel Busbar Gardu};
  \end{tikzpicture}""",
        "c3_box": "Ruang Pengerjaan C3 (Penurunan Nilai Eigen & Fungsi Ortogonal)",
        "c3_h": "2.8cm",
        "c4_text": "Analisis peran ortogonalitas fungsi sinus: $\\int_0^L \\sin\\left(\\frac{n\\pi x}{L}\\right) \\sin\\left(\\frac{m\\pi x}{L}\\right) dx = \\frac{L}{2} \\delta_{nm}$. Tunjukkan bagaimana sifat ortogonalitas ini digunakan untuk mengisolasi koefisien Fourier $C_n$ dari distribusi temperatur awal $u(x,0) = f(x)$.",
        "c4_box": "Ruang Pengerjaan C4 (Analisis Ortogonalitas dalam Penentuan Koefisien Awal)",
        "c4_h": "3.8cm",
        "c5_text": "Evaluasi waktu pendinginan busbar: Ragam fundamental ($n=1$) memiliki faktor redaman waktu $e^{-\\alpha (\\pi/L)^2 t}$, sedangkan harmonisa ketiga ($n=3$) meluruh dengan faktor $e^{-\\alpha (3\\pi/L)^2 t}$. Buktikan bahwa ragam spasial tinggi meluruh 9 kali lebih cepat daripada ragam fundamental!",
        "c5_box": "Ruang Pengerjaan C5 (Evaluasi Skala Waktu Disipasi Multiragam)",
        "c5_h": "3.8cm",
        "c6_text": "Rancang skrip pemodelan \\textbf{Julia} untuk menghitung distribusi suhu ruang-waktu $u(x,t)$ dengan menjumlahkan 15 suku pertama deret Fourier, dan plot profil spasial suhu pada 3 waktu berbeda ($t_1=0$, $t_2=5\\text{ s}$, $t_3=20\\text{ s}$).",
        "c6_box": "Ruang Pengerjaan C6 (Skrip Rekonstruksi Multiragam Ruang-Waktu Julia)",
        "c6_h": "3.8cm",
    },
    11: {
        "title": "Persamaan Gelombang 1D & Telegrafer Saluran Transmisi",
        "subcpmk_num": "6",
        "subcpmk_text": "Mahasiswa mampu memecahkan persamaan gelombang 1D dan persamaan telegrafer saluran transmisi daya serta menganalisis refleksi surja petir sesuai standar proteksi IEC 60071.",
        "c1_text": "Tuliskan bentuk baku Persamaan Gelombang 1D $\\frac{\\partial^2 u}{\\partial t^2} = v^2 \\frac{\\partial^2 u}{\\partial x^2}$, dan tuliskan kecepatan rambat gelombang $v$ serta impedansi karakteristik $Z_0$ dinyatakan dalam parameter saluran transmisi per satuan panjang ($L'$ dan $C'$).",
        "c1_box": "Ruang Pengerjaan C1 (Persamaan Gelombang 1D & Karakteristik Saluran)",
        "c1_h": "2.0cm",
        "c2_text": "Jelaskan makna fisis solusi d'Alembert $u(x,t) = f(x - vt) + g(x + vt)$. Bagaimana fungsi $f$ dan $g$ merepresentasikan fenomena gelombang berjalan maju dan gelombang berjalan pantul pada kawat transmisi?",
        "c2_box": "Ruang Pengerjaan C2 (Intuisi Fisika Solusi d'Alembert & Perambatan Gelombang)",
        "c2_h": "2.1cm",
        "c3_prompt": "Sebuah surja tegangan petir $V_0 = 500\\text{ kV}$ merambat pada saluran transmisi udara ($Z_{01} = 400\\,\\Omega$) menuju kabel bawah tanah ($Z_{02} = 50\\,\\Omega$). Turunkan koefisien refleksi $\\Gamma_L$ dan koefisien transmisi $T_L$, serta hitung tegangan gelombang yang diteruskan ke kabel tanah!",
        "circuitikz": r"""\begin{tikzpicture}[scale=0.65]
    \draw[very thick, unibblue] (0,0.8) -- (2.0,0.8) node[midway, above, font=\tiny] {$Z_{01}=400\,\Omega$};
    \draw[very thick, unibblue] (0,0) -- (2.0,0);
    \draw[line width=1.5mm, unibgold] (2.0,0.8) -- (3.8,0.8) node[midway, above, font=\tiny] {$Z_{02}=50\,\Omega$};
    \draw[line width=1.5mm, unibgold] (2.0,0) -- (3.8,0);
    \draw[dashed, red] (2.0,-0.3) -- (2.0,1.2) node[above, font=\tiny] {Antarmuka};
    \draw[->, >=stealth, thick, red] (0.5,0.4) -- (1.5,0.4) node[above, font=\tiny] {$V^+$};
  \end{tikzpicture}""",
        "c3_box": "Ruang Pengerjaan C3 (Penurunan Koefisien Refleksi & Transmisi Surja)",
        "c3_h": "2.8cm",
        "c4_text": "Analisis fenomena pelipatgandaan tegangan pada ujung saluran terbuka (\\textit{open-circuit termination}, $Z_L \\to \\infty$). Buktikan bahwa koefisien refleksi bernilai $\\Gamma_L = +1$ dan tegangan transien pada titik ujung terbuka meningkat tepat menjadi 2 kali lipat ($2\\text{ pu}$), yang dapat merusak arrester gardu induk!",
        "c4_box": "Ruang Pengerjaan C4 (Analisis Tegangan Lebih Ujung Terbuka 2 pu IEC 60071)",
        "c4_h": "3.8cm",
        "c5_text": "Evaluasi Rasio Gelombang Berdiri (\\textit{Voltage Standing Wave Ratio} / VSWR): Diberikan saluran tanpa rugi-rugi terhubung ke beban kompleks dengan $|\\Gamma_L| = 0{,}6$. Hitung nilai $\\text{VSWR} = \\frac{1 + |\\Gamma_L|}{1 - |\\Gamma_L|}$ dan evaluasi dampak disonansi impedansi terhadap rugi transmisi daya.",
        "c5_box": "Ruang Pengerjaan C5 (Evaluasi Parameter VSWR & Keselamatan Transmisi)",
        "c5_h": "3.8cm",
        "c6_text": "Rancang program simulasi gelombang datang dan pantul berbasis \\textbf{Julia} untuk memodelkan solusi d'Alembert interaksi dua pulsa gelombang yang bergerak berlawanan arah. Plot diagram kisi ruang-waktu (*lattice diagram*).",
        "c6_box": "Ruang Pengerjaan C6 (Skrip Simulasi Kisi Pantulan Gelombang Julia)",
        "c6_h": "3.8cm",
    },
    12: {
        "title": "Persamaan Panas 1D & Kemampuan Hantar Arus Kabel XLPE",
        "subcpmk_num": "6",
        "subcpmk_text": "Mahasiswa mampu memformulasikan persamaan difusi panas 1D dengan suku pembangkitan kalor Joule serta mengevaluasi batas kemampuan hantar arus kabel tanah sesuai IEC 60287.",
        "c1_text": "Tuliskan bentuk baku Persamaan Panas 1D dengan suku sumber kalor Joule internal: $\\frac{\\partial u}{\\partial t} = \\alpha \\frac{\\partial^2 u}{\\partial x^2} + \\frac{q_{\\text{gen}}}{\\rho c_p}$, dan sebutkan definisi fisis konduktivitas termal $k$ serta difusivitas termal $\\alpha$.",
        "c1_box": "Ruang Pengerjaan C1 (Persamaan Difusi Termal dengan Pembangkitan Kalor)",
        "c1_h": "2.0cm",
        "c2_text": "Jelaskan metode pemecahan transien termal menggunakan dekomposisi tunak-transien $u(x,t) = u_{\\text{ss}}(x) + u_{\\text{tr}}(x,t)$. Mengapa solusi tunak $u_{\\text{ss}}(x)$ memenuhi persamaan Poisson/Laplace 1D sementara komponen transien meluruh menuju nol?",
        "c2_box": "Ruang Pengerjaan C2 (Prinsip Dekomposisi Solusi Tunak dan Transien Kalor)",
        "c2_h": "2.1cm",
        "c3_prompt": "Sebuah kabel tanah berisolasi XLPE 20 kV memiliki ketebalan isolasi $d=15\\text{ mm}$. Pada kondisi tunak, rugi tembaga menghasilkan fluks panas konstan pada konduktor ($x=0$) sehingga $-k \\left.\\frac{\\partial u}{\\partial x}\\right|_{x=0} = q_0$, sementara permukaan luar ($x=d$) dijaga pada suhu tanah $T_{\\text{tanah}} = 25^\\circ\\text{C}$. Turunkan profil temperatur tunak $u_{\\text{ss}}(x)$.",
        "circuitikz": r"""\begin{tikzpicture}[scale=0.65]
    \draw[fill=unibgold!80] (0,0) rectangle (0.6,1.4);
    \draw[fill=unibblue!40] (0.6,0) rectangle (2.8,1.4);
    \draw[fill=unibgreen!40] (2.8,0) rectangle (3.5,1.4);
    \node at (0.3,0.7) [font=\tiny\bfseries, rotate=90] {Inti Cu};
    \node at (1.7,0.7) [font=\tiny\bfseries] {Isolasi XLPE};
    \node at (3.15,0.7) [font=\tiny, rotate=90] {Tanah};
    \draw[<->, >=stealth] (0.6,-0.3) -- (2.8,-0.3) node[midway, below, font=\tiny] {$d=15\text{ mm}$};
  \end{tikzpicture}""",
        "c3_box": "Ruang Pengerjaan C3 (Penurunan Profil Suhu Tunak Isolasi Kabel)",
        "c3_h": "2.8cm",
        "c4_text": "Analisis Batas Kemampuan Hantar Arus (\\textit{Ampacity}) kabel tanah menurut standar \\textbf{IEC 60287}: Jika temperatur operasi kontinu maksimum isolasi XLPE tidak boleh melampaui $90^\\circ\\text{C}$, analisis hubungan antara arus beban maksimum $I_{\\text{maks}}$ dengan resistansi konduktor $R_{\\text{ac}}$ dan resistansi termal lingkungan $R_{\\text{th,total}}$.",
        "c4_box": "Ruang Pengerjaan C4 (Analisis Ampacity Kabel Tanah Sesuai Standar IEC 60287)",
        "c4_h": "3.8cm",
        "c5_text": "Evaluasi risiko *thermal runaway*: Sifat resistansi konduktor meningkat linier terhadap suhu: $R(T) = R_0(1 + \\alpha_{\\text{Cu}} \\Delta T)$. Evaluasi bagaimana umpan balik positif antara kenaikan suhu dan peningkatan disipasi Joule dapat memicu ketidakstabilan termal jika disipasi ke tanah tersumbat.",
        "c5_box": "Ruang Pengerjaan C5 (Evaluasi Stabilitas Termal & Risiko Kegagalan Dielektrik)",
        "c5_h": "3.8cm",
        "c6_text": "Rancang kode simulasi beda hingga (FDM skema eksplisit FTCS) dalam bahasa \\textbf{Julia} untuk menyelesaikan persamaan difusi panas 1D pada batang tembaga. Pastikan kriteria stabilitas numerik Von Neumann $\\Delta t \\le \\frac{\\Delta x^2}{2\\alpha}$ terpenuhi.",
        "c6_box": "Ruang Pengerjaan C6 (Skrip Algoritma FDM Difusi Termal Julia)",
        "c6_h": "3.8cm",
    },
    13: {
        "title": "Persamaan Laplace 2D & Medan Elektrostatika Isolator 150 kV",
        "subcpmk_num": "6",
        "subcpmk_text": "Mahasiswa mampu memformulasikan Persamaan Laplace 2D elektrostatika, menganalisis sifat fungsi harmonik, dan menyelesaikan distribusi potensial menggunakan metode beda hingga (FDM).",
        "c1_text": "Tuliskan bentuk Persamaan Laplace 2D dalam koordinat Kartesian $\\nabla^2 V = 0$, dan jelaskan hubungan antara fungsi potensial skalar elektrostatika $V(x,y)$ dengan vektor intensitas medan listrik $\\vec{E}(x,y)$.",
        "c1_box": "Ruang Pengerjaan C1 (Persamaan Laplace & Gradien Potensial Elektrostatik)",
        "c1_h": "2.0cm",
        "c2_text": "Jelaskan Teorema Nilai Rata-rata Gauss untuk fungsi harmonik: $V(x_0, y_0) = \\frac{1}{2\\pi} \\oint V dl$. Mengapa teorema ini menjamin bahwa medan potensial elektrostatika di ruang bebas muatan tidak mungkin memiliki titik ekstremum lokal (puncak/lembah)?",
        "c2_box": "Ruang Pengerjaan C2 (Prinsip Ekstremum Maksimum/Minimum Fungsi Harmonik)",
        "c2_h": "2.1cm",
        "c3_prompt": "Tinjau palung konduktor persegi panjang pada gambar di samping dengan lebar $a=10\\text{ cm}$ dan tinggi tak-hingga. Ketiga dinding ($x=0, x=a, y=0$) ditanahkan ($V=0$), sedangkan pelat atas pada $y \\to \\infty$ berada pada potensial $V_0 = 150\\text{ kV}$. Turunkan bentuk umum fungsi potensial $V(x,y)$ menggunakan metode pemisahan variabel.",
        "circuitikz": r"""\begin{tikzpicture}[scale=0.65]
    \draw[line width=1mm, unibblue] (0,1.8) -- (0,0) -- (3.0,0) -- (3.0,1.8);
    \draw[dashed, red, thick] (0,1.8) -- (3.0,1.8) node[midway, above, font=\tiny] {$V=V_0$};
    \node at (1.5,0.4) [font=\tiny] {$\nabla^2 V = 0$};
    \node at (-0.4,0.9) [font=\tiny, rotate=90] {$V=0$};
    \node at (3.4,0.9) [font=\tiny, rotate=-90] {$V=0$};
    \node at (1.5,-0.3) [font=\tiny] {$V=0$};
    \draw[<->, >=stealth] (0,-0.6) -- (3.0,-0.6) node[midway, below, font=\tiny] {$a = 10\text{ cm}$};
  \end{tikzpicture}""",
        "c3_box": "Ruang Pengerjaan C3 (Penurunan Solusi Analitis Potensial Laplace 2D)",
        "c3_h": "2.8cm",
        "c4_text": "Berdasarkan fungsi potensial $V(x,y)$, hitung komponen vektor medan listrik $E_x = -\\frac{\\partial V}{\\partial x}$ dan $E_y = -\\frac{\\partial V}{\\partial y}$. Analisis lokasi di mana konsentrasi stres medan listrik ($|\\vec{E}|$) mencapai nilai tertinggi pada geometri tersebut.",
        "c4_box": "Ruang Pengerjaan C4 (Analisis Vektor Medan Listrik & Konsentrasi Stres)",
        "c4_h": "3.8cm",
        "c5_text": "Evaluasi batas medan tembus korona Peek ($E_{\\text{kritis}} \\approx 30\\text{ kV/cm}$ di udara pada kondisi atmosfer standar) pada permukaan isolator rantai 150 kV. Evaluasi efektivitas pemasangan cincin korona (\\textit{corona ring}) untuk meratakan gradien potensial.",
        "c5_box": "Ruang Pengerjaan C5 (Evaluasi Bahaya Korona & Efektivitas Cincin Perata)",
        "c5_h": "3.8cm",
        "c6_text": "Rancang skrip algoritma iterasi relaksasi Gauss-Seidel / SOR (\\textit{Successive Over-Relaxation}) dalam bahasa \\textbf{Julia} untuk menghitung matriks grid beda hingga (FDM) potensial 2D: $V_{i,j} = \\frac{1}{4}(V_{i+1,j} + V_{i-1,j} + V_{i,j+1} + V_{i,j-1})$.",
        "c6_box": "Ruang Pengerjaan C6 (Skrip Algoritma FDM Relaksasi Gauss-Seidel Julia)",
        "c6_h": "3.8cm",
    },
    14: {
        "title": "Fungsi Khusus: Persamaan Bessel & Fenomena Efek Kulit",
        "subcpmk_num": "6",
        "subcpmk_text": "Mahasiswa mampu memecahkan Persamaan Diferensial Bessel dalam koordinat silindris serta memodelkan fenomena Efek Kulit (Skin Effect) pada konduktor ACSR sesuai IEC 61089.",
        "c1_text": "Tuliskan bentuk baku Persamaan Diferensial Bessel berorde $n$: $x^2 y'' + x y' + (x^2 - n^2) y = 0$, dan sebutkan dua solusi bebas liniernya $J_n(x)$ (jenis pertama) dan $Y_n(x)$ (jenis kedua).",
        "c1_box": "Ruang Pengerjaan C1 (Bentuk Standar Persamaan Bessel & Solusi Kanonikal)",
        "c1_h": "2.0cm",
        "c2_text": "Jelaskan mengapa fungsi Bessel jenis kedua $Y_n(x)$ harus dibuang ($C_2 = 0$) saat menyelesaikan medan fisik di dalam konduktor silinder pejal yang mencakup sumbu tengah $r=0$.",
        "c2_box": "Ruang Pengerjaan C2 (Prinsip Keberhinggaan Fisik Medan pada Sumbu Pusat)",
        "c2_h": "2.1cm",
        "c3_prompt": "Fenomena efek kulit pada kawat silindris berarus bolak-balik frekuensi tinggi menghasilkan persamaan rapat arus radial $J_z(r) = J_0 \\frac{J_0(k r)}{J_0(k a)}$. Turunkan ekspresi kedalaman kulit (\\textit{skin depth}) $\\delta = \\sqrt{\\frac{2}{\\omega \\mu \\sigma}}$, dan hitung $\\delta$ tembaga pada frekuensi kerja $f=50\\text{ Hz}$ ($\\sigma = 5{,}8 \\times 10^7\\text{ S/m}, \\mu = 4\\pi \\times 10^{-7}\\text{ H/m}$).",
        "circuitikz": r"""\begin{tikzpicture}[scale=0.65]
    \draw[fill=unibblue!15, thick] (0,0) circle (1.2);
    \draw[pattern=north east lines, pattern color=unibblue, thick] (0,0) circle (1.2);
    \draw[fill=white, thick] (0,0) circle (0.7);
    \draw[<->, >=stealth] (0,0) -- (1.2,0) node[midway, above, font=\tiny] {$a$};
    \draw[<->, >=stealth, red, thick] (0.7,0) -- (1.2,0) node[midway, below, font=\tiny] {$\delta$};
    \node at (0,-0.2) [font=\tiny] {Inti};
  \end{tikzpicture}""",
        "c3_box": "Ruang Pengerjaan C3 (Penurunan Kedalaman Kulit & Perhitungan Nilai Numerik)",
        "c3_h": "2.8cm",
        "c4_text": "Analisis rasio kenaikan resistansi arus bolak-balik terhadap arus searah ($R_{\\text{ac}}/R_{\\text{dc}}$) pada kawat transmisi daya. Jelaskan mengapa pada kabel transmisi berpenampang besar, konduktor tidak dibuat dari tembaga pejal melainkan dibuat berongga atau berpilin (*stranded*).",
        "c4_box": "Ruang Pengerjaan C4 (Analisis Kenaikan Resistansi AC & Desain Geometri Konduktor)",
        "c4_h": "3.8cm",
        "c5_text": "Evaluasi desain konduktor ACSR (\\textit{Aluminium Conductor Steel Reinforced}) menurut standar \\textbf{IEC 61089}: Mengapa secara cerdas inti baja (konduktivitas rendah, kekuatan mekanik tinggi) diletakkan di bagian tengah kawat, sedangkan untaian aluminium diletakkan di lapisan luar?",
        "c5_box": "Ruang Pengerjaan C5 (Evaluasi Struktur ACSR Terhadap Distribusi Rapat Arus)",
        "c5_h": "3.8cm",
        "c6_text": "Rancang skrip program \\textbf{Julia} menggunakan paket \\texttt{SpecialFunctions.jl} untuk menghitung fungsi Bessel $J_0(x)$ dan memplot profil rapat arus radial ternormalisasi $|J_z(r)/J_0|$ dari pusat kawat ($r=0$) hingga ke permukaan kawat ($r=a$).",
        "c6_box": "Ruang Pengerjaan C6 (Skrip Plotting Profil Rapat Arus Radial Bessel Julia)",
        "c6_h": "3.8cm",
    },
    15: {
        "title": "Polinomial Legendre & 4 Persamaan Maxwell Diferensial",
        "subcpmk_num": "15",
        "subcpmk_text": "Mahasiswa mampu memecahkan Persamaan Diferensial Legendre dalam koordinat bola, menguasai 4 Persamaan Maxwell diferensial/integral, serta menyintesis kurikulum menuju medan elektromagnetika.",
        "c1_text": "Tuliskan bentuk baku Persamaan Diferensial Legendre: $(1-x^2)y'' - 2x y' + n(n+1)y = 0$, serta sebutkan fungsi ortogonal Polinomial Legendre berorde nol hingga dua: $P_0(x)$, $P_1(x)$, dan $P_2(x)$.",
        "c1_box": "Ruang Pengerjaan C1 (Persamaan Legendre & Polinomial Tiga Orde Pertama)",
        "c1_h": "2.0cm",
        "c2_text": "Tuliskan 4 Persamaan Maxwell dalam bentuk diferensial di ruang bebas, dan jelaskan peran fisis arus pergeseran Maxwell (*displacement current* $\\vec{J}_d = \\frac{\\partial \\vec{D}}{\\partial t}$) dalam menjaga kontinuitas kekekalan muatan.",
        "c2_box": "Ruang Pengerjaan C2 (Hukum Kekekalan Muatan & Arus Pergeseran Maxwell)",
        "c2_h": "2.1cm",
        "c3_prompt": "Sebuah bola konduktor netral beradius $R$ diletakkan dalam medan listrik seragam luar $\\vec{E}_0 = E_0 \\hat{a}_z$. Solusi potensial elektrostatika di luar bola dinyatakan dalam deret Legendre: $V(r,\\theta) = \\sum_{n=0}^\\infty \\left( A_n r^n + \\frac{B_n}{r^{n+1}} \\right) P_n(\\cos\\theta)$. Turunkan solusi eksak untuk $V(r,\\theta)$ dengan menerapkan syarat batas pada $r=R$ dan $r \\to \\infty$.",
        "circuitikz": r"""\begin{tikzpicture}[scale=0.65]
    \draw[fill=unibblue!20, thick] (0,0) circle (1.0);
    \node at (0,0) [font=\tiny\bfseries] {Bola $R$};
    \foreach \y in {-1.2, -0.6, 0, 0.6, 1.2} {
      \draw[->, >=stealth, thin, gray] (-1.8,\y) -- (-1.1,\y);
      \draw[->, >=stealth, thin, gray] (1.1,\y) -- (1.8,\y);
    }
    \node at (1.5,1.5) [font=\tiny\bfseries, unibblue] {$\vec{E}_0 = E_0 \hat{a}_z$};
  \end{tikzpicture}""",
        "c3_box": "Ruang Pengerjaan C3 (Penurunan Solusi Potensial Bola Konduktor)",
        "c3_h": "2.8cm",
        "c4_text": "Analisis penurunan persamaan gelombang elektromagnetik 3D: Terapkan operasi kurva rotor ($\\nabla \\times (\\nabla \\times \\vec{E})$) pada Hukum Faraday dan Hukum Ampere-Maxwell di ruang bebas muatan. Buktikan bahwa gelombang merambat dengan kecepatan $c = \\frac{1}{\\sqrt{\\mu_0 \\epsilon_0}} \\approx 3 \\times 10^8\\text{ m/s}$!",
        "c4_box": "Ruang Pengerjaan C4 (Pembuktian Gelombang EM 3D & Kecepatan Cahaya Maxwell)",
        "c4_h": "3.8cm",
        "c5_text": "Evaluasi Vektor Poynting $\\vec{S} = \\vec{E} \\times \\vec{H}$: Hitung densitas daya radiasi elektromagnetik rata-rata di bawah saluran udara tegangan ekstra tinggi (SUTET 500 kV PLN). Evaluasi apakah nilai densitas fluks magnetik dan medan listrik berada dalam ambang batas aman paparan publik \\textbf{IEEE Std C95.1}.",
        "c5_box": "Ruang Pengerjaan C5 (Evaluasi Rapat Daya Poynting & Standar Paparan SUTET IEEE C95.1)",
        "c5_h": "3.8cm",
        "c6_text": "Rancang skrip program ilmiah berbasis \\textbf{Julia} untuk memvisualisasikan garis gaya medan listrik dipol bola hasil turunan Soal 3 menggunakan pustaka \\texttt{Plots.jl}. Tuliskan algoritma perhitungan komponen medan radial $E_r(r,\\theta)$ dan transversal $E_\\theta(r,\\theta)$.",
        "c6_box": "Ruang Pengerjaan C6 (Skrip Plotting Vektor Medan Dipol Bola Maxwell Julia)",
        "c6_h": "3.8cm",
    }
}

TEMPLATE = r"""\documentclass[10pt,a4paper]{article}
\usepackage[top=1.5cm, bottom=1.5cm, left=1.6cm, right=1.6cm, headheight=14pt, footskip=18pt]{geometry}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amsfonts,amssymb}
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{circuitikz}
\usetikzlibrary{calc,patterns}
\usepackage[most]{tcolorbox}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{colortbl}
\usepackage{hyperref}

% --- Palet Warna Resmi UNIB ---
\definecolor{unibblue}{RGB}{0, 32, 96}
\definecolor{unibgold}{RGB}{197, 160, 89}
\definecolor{unibgreen}{RGB}{34, 112, 60}
\definecolor{boxbg}{RGB}{248, 250, 253}
\definecolor{linegray}{RGB}{210, 215, 225}

% --- Pengaturan Header & Footer ---
\pagestyle{fancy}
\fancyhf{}
\lhead{\footnotesize\textbf{\color{unibblue}Universitas Bengkulu} \textbar\ Program Studi S1 Teknik Elektro}
\rhead{\footnotesize\color{gray}Persamaan Diferensial (Genap 2026)}
\lfoot{\footnotesize\color{gray}Lembar Kerja Mahasiswa (LKM) Berbasis OBE}
\cfoot{\footnotesize\color{gray}Hal. \thepage\ dari 2}
\rfoot{\footnotesize\color{unibblue}\textbf{Minggu __WEEK__: __TITLE_SHORT__}}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.4pt}

% --- Custom Box untuk Lembar Jawab ---
\newtcolorbox{answerbox}[1]{%
  colback=white,
  colframe=unibblue!70!black,
  coltitle=white,
  fonttitle=\bfseries\scriptsize,
  colbacktitle=unibblue,
  title={#1},
  arc=2pt,
  left=5pt,right=5pt,top=3pt,bottom=3pt,
  boxrule=0.6pt
}

\begin{document}

% ==================== HALAMAN 1 ====================
\noindent\begin{minipage}[c]{0.68\textwidth}%
  {\large\textbf{\color{unibblue}LEMBAR KERJA MAHASISWA (LKM)}}\\[1mm]
  {\normalsize\textbf{Mata Kuliah: Persamaan Diferensial (2 SKS)}}\\[0.5mm]
  {\small\textbf{Topik Minggu __WEEK__:} __TITLE__}%
\end{minipage}%
\hfill%
\begin{minipage}[c]{0.30\textwidth}%
  \begin{tcolorbox}[colback=unibblue!5,colframe=unibblue,boxrule=0.6pt,arc=2pt,left=4pt,right=4pt,top=2pt,bottom=2pt]
    \scriptsize
    \textbf{Nama:} \dotfill\\[1.2mm]
    \textbf{NPM:} \dotfill\\[1.2mm]
    \textbf{Kelas/Klp:} \dotfill\\[1.2mm]
    \textbf{Nilai Final:} \hfill \textbf{/ 100}
  \end{tcolorbox}%
\end{minipage}\par

\vspace{1.5mm}

% Kotak Sub-CPMK & Pedoman
\begin{tcolorbox}[colback=boxbg,colframe=unibgold!90!black,boxrule=0.6pt,arc=2pt,left=5pt,right=5pt,top=3pt,bottom=3pt,title=\textbf{\scriptsize Capaian Pembelajaran (Sub-CPMK __SUBCPMK_NUM__) \& Pedoman Evaluasi OBE}]
  \scriptsize
  \textbf{Sub-CPMK __SUBCPMK_NUM__:} __SUBCPMK_TEXT__\\
  \textbf{Alokasi Waktu:} 50--60 Menit \quad\textbar\quad \textbf{Model:} Kolaboratif / Mandiri Terstruktur \quad\textbar\quad \textbf{Bahasa Komputasi:} Julia 1.12+
\end{tcolorbox}

\vspace{1mm}

% Soal C1
\noindent\textbf{1. (C1 - Mengingat \textbar\ Bobot: 10 Poin)}\par\vspace{0.5mm}
{\footnotesize __C1_TEXT__}
\begin{answerbox}{__C1_BOX__}
  \vspace{__C1_H__}
\end{answerbox}

\vspace{1mm}

% Soal C2
\noindent\textbf{2. (C2 - Memahami \textbar\ Bobot: 15 Poin)}\par\vspace{0.5mm}
{\footnotesize __C2_TEXT__}
\begin{answerbox}{__C2_BOX__}
  \vspace{__C2_H__}
\end{answerbox}

\vspace{1mm}

% Soal C3
\noindent\textbf{3. (C3 - Menerapkan \textbar\ Bobot: 20 Poin)}\par\vspace{0.5mm}
\noindent\begin{minipage}[t]{0.60\textwidth}%
  {\footnotesize __C3_PROMPT__}%
\end{minipage}%
\hfill%
\begin{minipage}[t]{0.37\textwidth}%
  \centering
  \resizebox{0.95\linewidth}{!}{%
  __CIRCUITIKZ__%
  }%
\end{minipage}\par\vspace{1mm}
\begin{answerbox}{__C3_BOX__}
  \vspace{__C3_H__}
\end{answerbox}

\newpage
% ==================== HALAMAN 2 ====================

% Soal C4
\noindent\textbf{4. (C4 - Menganalisis \textbar\ Bobot: 20 Poin)}\par\vspace{0.5mm}
{\footnotesize __C4_TEXT__}
\begin{answerbox}{__C4_BOX__}
  \vspace{__C4_H__}
\end{answerbox}

\vspace{1.5mm}

% Soal C5
\noindent\textbf{5. (C5 - Mengevaluasi \textbar\ Bobot: 20 Poin)}\par\vspace{0.5mm}
{\footnotesize __C5_TEXT__}
\begin{answerbox}{__C5_BOX__}
  \vspace{__C5_H__}
\end{answerbox}

\vspace{1.5mm}

% Soal C6
\noindent\textbf{6. (C6 - Merancang \& Komputasi Julia \textbar\ Bobot: 15 Poin)}\par\vspace{0.5mm}
{\footnotesize __C6_TEXT__}
\begin{answerbox}{__C6_BOX__}
  \vspace{__C6_H__}
\end{answerbox}

\vspace{1.5mm}

% Tabel Rekapitulasi Skor OBE & Tanda Tangan
\noindent\begin{minipage}[b]{0.65\textwidth}%
  \centering
  \scriptsize
  \begin{tabular}{|c|c|c|c|c|c|c|}
    \hline
    \rowcolor{unibblue}
    \textbf{\color{white}C1} & \textbf{\color{white}C2} & \textbf{\color{white}C3} & \textbf{\color{white}C4} & \textbf{\color{white}C5} & \textbf{\color{white}C6} & \textbf{\color{white}Total} \\
    \rowcolor{unibblue!10}
    10 Pts & 15 Pts & 20 Pts & 20 Pts & 20 Pts & 15 Pts & 100 Pts \\
    \hline
    & & & & & & \\[2.5mm]
    \hline
  \end{tabular}%
\end{minipage}%
\hfill%
\begin{minipage}[b]{0.32\textwidth}%
  \centering
  \scriptsize
  \textbf{Verifikasi Dosen / Asisten:}\\[5mm]
  (\dotfill)
\end{minipage}\par

\end{document}
"""

def sanitize_latex(s, is_circuit=False):
    if is_circuit:
        return s
    # replace unescaped & with \&
    s = re.sub(r'(?<!\\)&', r'\\&', s)
    # replace unescaped % with \%
    s = re.sub(r'(?<!\\)%', r'\\%', s)
    # allow hyphenation in long package names
    s = s.replace("DifferentialEquations.jl", r"Differential\-Equations.jl")
    return s

def generate_tex(w_num):
    data = WORKSHEETS[w_num]
    content = TEMPLATE
    content = content.replace("__WEEK__", str(w_num))
    content = content.replace("__TITLE__", sanitize_latex(data["title"]))
    # short title for header
    short_title = data["title"].split(":")[0] if ":" in data["title"] else data["title"]
    if len(short_title) > 35:
        short_title = short_title[:32] + "..."
    content = content.replace("__TITLE_SHORT__", sanitize_latex(short_title))
    content = content.replace("__SUBCPMK_NUM__", data["subcpmk_num"])
    content = content.replace("__SUBCPMK_TEXT__", sanitize_latex(data["subcpmk_text"]))
    content = content.replace("__C1_TEXT__", sanitize_latex(data["c1_text"]))
    content = content.replace("__C1_BOX__", sanitize_latex(data["c1_box"]))
    content = content.replace("__C1_H__", data["c1_h"])
    content = content.replace("__C2_TEXT__", sanitize_latex(data["c2_text"]))
    content = content.replace("__C2_BOX__", sanitize_latex(data["c2_box"]))
    content = content.replace("__C2_H__", data["c2_h"])
    content = content.replace("__C3_PROMPT__", sanitize_latex(data["c3_prompt"]))
    content = content.replace("__CIRCUITIKZ__", data["circuitikz"])
    content = content.replace("__C3_BOX__", sanitize_latex(data["c3_box"]))
    content = content.replace("__C3_H__", data["c3_h"])
    content = content.replace("__C4_TEXT__", sanitize_latex(data["c4_text"]))
    content = content.replace("__C4_BOX__", sanitize_latex(data["c4_box"]))
    content = content.replace("__C4_H__", data["c4_h"])
    content = content.replace("__C5_TEXT__", sanitize_latex(data["c5_text"]))
    content = content.replace("__C5_BOX__", sanitize_latex(data["c5_box"]))
    content = content.replace("__C5_H__", data["c5_h"])
    content = content.replace("__C6_TEXT__", sanitize_latex(data["c6_text"]))
    content = content.replace("__C6_BOX__", sanitize_latex(data["c6_box"]))
    content = content.replace("__C6_H__", data["c6_h"])
    
    filename = f"worksheet{w_num}.tex"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filename}")

if __name__ == "__main__":
    for w in sorted(WORKSHEETS.keys()):
        generate_tex(w)
