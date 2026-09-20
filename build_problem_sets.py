r"""
Generator Master Problem Set (problem_set1.tex s.d. problem_set15.tex)
Mata Kuliah: Persamaan Diferensial (Teknik Elektro Universitas Bengkulu)
Standar:
- OBE & 4-Pilar Pedagogis (Intuisi Fisika, Derivasi Matematis, Komputasi Numerik Julia, Aplikasi Standar Industri)
- Taksonomi Bloom Berjenjang C1 s.d. C6 Lengkap (Total 100 Poin)
- Tepat 2 Halaman (1 lembar bolak-balik)
- Zero Overfull \hbox dan Zero Overfull \vbox
- Palet Warna Resmi UNIB
"""

import os
import re

PROBLEM_SETS = {
    1: {
        "title": "Klasifikasi PDB/PDP, Nilai Awal (IVP), & Pemodelan RL",
        "subcpmk_num": "1",
        "subcpmk_text": "Mahasiswa mampu mengidentifikasi, mengklasifikasi, dan memodelkan fenomena dinamika sistem elektrik terpusat ke dalam Persamaan Diferensial Biasa (PDB) orde 1 serta memvalidasinya secara numerik.",
        "c1_text": "Tuliskan definisi lengkap Persamaan Diferensial Biasa (PDB) linier orde 1 beserta bentuk kanonikalnya $\\frac{dy}{dt} + P(t)y = Q(t)$. Berikan satu contoh nyata fenomena kelistrikan yang direpresentasikan oleh bentuk tersebut.",
        "c2_text": "Jelaskan perbedaan mendasar antara 'Solusi Umum' dan 'Solusi Khusus' pada penyelesaian suatu Masalah Nilai Awal (IVP). Jelaskan mengapa hukum kontinuitas fluks magnetik induktor mensyaratkan arus tidak boleh melompat seketika ($i(0^-) = i(0^+)$).",
        "c3_prompt": "Tinjau rangkaian pengisian induktor pada gambar di samping. Sakelar ditutup pada $t=0$ dengan arus mula-mula $i(0) = 0$. Jika sumber tegangan DC bernilai $V_s = 48\\text{ V}$, resistansi $R = 12\\,\\Omega$, dan induktansi $L = 0{,}6\\text{ H}$, turunkan persamaan diferensial arus dari KVK dan tentukan solusi khusus arus transien $i(t)$ untuk $t \\ge 0$.",
        "circuitikz": r"""\begin{circuitikz}[american, scale=0.68, transform shape]
    \draw (0,0) to[battery2, l=$V_s$, invert] (0,1.8)
          to[switch, l={$t{=}0$}] (1.6,1.8)
          to[R, l=$R$] (3.2,1.8)
          to[L, l=$L$, v=$v_L(t)$] (3.2,0)
          to[short] (0,0);
    \draw[->, >=stealth, thick, unibblue] (1.4,0.8) arc (160:-160:0.35);
    \node at (1.8,0.8) [unibblue, font=\tiny\bfseries] {$i(t)$};
  \end{circuitikz}""",
        "formula_ref": r"""\begin{itemize}[leftmargin=*, nosep]
  \item Hukum Tegangan Kirchhoff (KVK): $\sum v = 0 \implies V_s - v_R(t) - v_L(t) = 0$
  \item Karakteristik Dinamika Induktor: $v_L(t) = L \frac{di}{dt}$ \quad\textbar\quad Fluks Magnetik: $\lambda = L i$
  \item Konstanta Waktu Rangkaian: $\tau = \frac{L}{R}$ (detik) \quad\textbar\quad Respons Arus: $i(t) = \frac{V_s}{R} \left(1 - e^{-t/\tau}\right)$
  \item Energi Medan Magnetik Tersimpan: $W_L(t) = \frac{1}{2} L i^2(t)$ (Joule)
\end{itemize}""",
        "c4_text": "Berdasarkan solusi arus $i(t)$ pada Soal 3: (a) Tentukan ekspresi analitis tegangan induktor $v_L(t) = L \\frac{di}{dt}$ dan buktikan bahwa $v_L(0^+) = V_s$; (b) Analisis waktu yang dibutuhkan agar arus mencapai tepat $95\\%$ dari nilai arus tunaknya ($I_{\\text{ss}} = V_s/R$); (c) Hitung energi total yang disuplai sumber $W_{\\text{sumber}}$ selama selang waktu $0 \\le t \\le 3\\tau$.",
        "c5_text": "Seorang teknisi mengklaim bahwa dengan menggandakan nilai induktansi $L$ menjadi dua kali lipat tanpa mengubah nilai $R$, energi akhir yang tersimpan dalam medan magnetik induktor pada kondisi tunak ($t \\to \\infty$) akan meningkat 4 kali lipat. Evaluasi kebenaran klaim teknis tersebut secara matematis berdasarkan rumus energi medan magnetik $W_L = \\frac{1}{2} L i^2$.",
        "c6_text": "Rancang sebuah program ilmiah berbasis \\textbf{Julia} (\\texttt{DifferentialEquations.jl} \\& \\texttt{Plots.jl}) untuk mensimulasikan respons arus transien rangkaian RL pada Soal 3 dengan solver \\texttt{Tsit5()}. Program harus memplot kurva $i(t)$ dan $v_L(t)$ pada satu kanvas grafik terpisah dengan anotasi garis konstanta waktu $\\tau = L/R$. Lampirkan sintaks kode Julia dan interpretasi kurvanya.",
    },
    2: {
        "title": "Metode Analitik PDB Orde 1: Separabel & Eksak (RC)",
        "subcpmk_num": "2",
        "subcpmk_text": "Mahasiswa mampu mengidentifikasi dan menyelesaikan PDB orde 1 secara analitik (separabel, eksak, dan faktor integrasi) serta memodelkan dinamika pengisian muatan kapasitor RC.",
        "c1_text": "Sebutkan definisi matematis Persamaan Diferensial Terpisahkan (*Separable ODE*) dan tuliskan formulasi uji eksak Euler untuk bentuk diferensial $M(x,y)dx + N(x,y)dy = 0$.",
        "c2_text": "Tinjau proses pengosongan kapasitor pada rangkaian RC tanpa sumber luar: $R \\frac{dq}{dt} + \\frac{q}{C} = 0$. Jelaskan secara fisis mengapa laju peluruhan muatan $\\frac{dq}{dt}$ berbanding lurus dengan muatan tersisa $q(t)$, dan apa makna fisis konstanta waktu $\\tau = RC$.",
        "c3_prompt": "Pada rangkaian pengisian kapasitor di samping, kapasitor awalnya kosong $q(0) = 0$. Sakelar ditutup pada $t=0$. Dengan parameter $V_s = 24\\text{ V}$, $R = 50\\text{ k}\\Omega$, dan $C = 20\\,\\mu\\text{F}$, turunkan persamaan diferensial muatan $q(t)$ secara separabel dan tentukan fungsi tegangan kapasitor $v_C(t)$ untuk seluruh $t \\ge 0$.",
        "circuitikz": r"""\begin{circuitikz}[american, scale=0.68, transform shape]
    \draw (0,0) to[battery2, l=$V_s$, invert] (0,1.8)
          to[switch, l={$t{=}0$}] (1.6,1.8)
          to[R, l=$R$] (3.2,1.8)
          to[C, l=$C$, v=$v_C(t)$] (3.2,0)
          to[short] (0,0);
    \draw[->, >=stealth, thick, unibblue] (1.4,0.8) arc (160:-160:0.35);
    \node at (1.8,0.8) [unibblue, font=\tiny\bfseries] {$i(t)$};
  \end{circuitikz}""",
        "formula_ref": r"""\begin{itemize}[leftmargin=*, nosep]
  \item Hukum Arus Kirchhoff (KAK): $\sum i = 0$ \quad\textbar\quad Karakteristik Kapasitor: $i_C(t) = C \frac{dv_C}{dt} = \frac{dq}{dt}$
  \item Syarat Keeksakan Euler: $\frac{\partial M(x,y)}{\partial y} = \frac{\partial N(x,y)}{\partial x}$ untuk bentuk $M\,dx + N\,dy = 0$
  \item Konstanta Waktu Rangkaian RC: $\tau = R C$ (detik) \quad\textbar\quad Tegangan Kapasitor: $v_C(t) = V_s \left(1 - e^{-t/\tau}\right)$
  \item Energi Elektrostatika Tersimpan: $W_C(t) = \frac{1}{2} C v_C^2(t)$ (Joule)
\end{itemize}""",
        "c4_text": "Analisis Paradoks Efisiensi Energi Pengisian RC: (a) Hitung energi total yang dikeluarkan sumber tegangan $W_{\\text{in}} = \\int_0^\\infty V_s i(t) dt$; (b) Hitung energi elektrostatika yang tersimpan pada kapasitor $W_C = \\frac{1}{2} C V_s^2$; (c) Buktikan secara matematis bahwa disipasi kalor pada resistor selalu tepat $W_R = 50\\% W_{\\text{in}}$, independen terhadap nilai resistansi $R$!",
        "c5_text": "Tinjau persamaan medan fluks: $(3x^2 + 2xy + y^2)dx + (x^2 + 2xy + 3y^2)dy = 0$. Evaluasi apakah persamaan diferensial ini memenuhi syarat eksak. Jika eksak, temukan fungsi keluarga kurva integral $\\phi(x,y) = C$ secara sistematis langkah demi langkah!",
        "c6_text": "Rancang algoritma numerik eksplisit (Metode Euler) dalam bahasa \\textbf{Julia} untuk menyelesaikan pengisian kapasitor non-linier: $\\frac{dv_C}{dt} = \\frac{V_s - v_C}{R \\cdot C(v_C)}$ di mana kapasitansi bervariasi terhadap tegangan: $C(v_C) = C_0 (1 + 0{,}1 v_C)$. Tuliskan skrip fungsi pembaruan waktu dan plot hasilnya.",
    },
    3: {
        "title": "Aplikasi Transien Rekayasa & Pemodelan Termal Transformator",
        "subcpmk_num": "3",
        "subcpmk_text": "Mahasiswa mampu menerapkan metodologi PDB orde 1 untuk memodelkan fenomena transien termal peralatan tenaga listrik (Hukum Pendinginan Newton & IEEE Std C57.91) serta memvalidasinya secara numerik.",
        "c1_text": "Tuliskan formulasi matematis Hukum Pendinginan Newton untuk temperatur benda $T(t)$ dalam medium sekitar $T_a$, serta sebutkan dimensi dan satuan SI untuk resistansi termal $R_{\\text{th}}$ dan kapasitas kalor termal $C_{\\text{th}}$.",
        "c2_text": "Jelaskan analogi langsung antara parameter sistem kelistrikan (tegangan $V$, arus $I$, resistansi $R$, kapasitansi $C$) dengan parameter sistem termal (temperatur $T$, laju kalor $q$, resistansi termal $R_{\\text{th}}$, kapasitas termal $C_{\\text{th}}$).",
        "c3_prompt": "Sebuah transformator distribusi gardu induk 20 kV memikul rugi daya tembaga $P_{\\text{loss}} = 40\\text{ kW}$. Sirkuit termal ekuivalen di samping memiliki kapasitas termal minyak $C_{\\text{th}} = 2{,}0\\text{ MJ/}^\\circ\\text{C}$ dan resistansi disipasi $R_{\\text{th}} = 1{,}0 \\times 10^{-3}\\,^\\circ\\text{C/W}$. Jika suhu sekitar konstan $T_a = 32^\\circ\\text{C}$, tentukan fungsi kenaikan suhu minyak trafo $T(t)$ jika operasi dimulai dari keadaan dingin ($T(0) = T_a$).",
        "circuitikz": r"""\begin{circuitikz}[american, scale=0.68, transform shape]
    \draw (0,0) to[I, l=$P_{\text{loss}}$] (0,1.8)
          to[short] (1.6,1.8)
          to[R, l=$R_{\text{th}}$] (1.6,0)
          to[short] (0,0);
    \draw (1.6,1.8) to[short] (3.0,1.8)
          to[C, l=$C_{\text{th}}$, v=$\theta(t)$] (3.0,0)
          to[short] (1.6,0);
    \node at (3.0,2.1) [font=\tiny\bfseries, unibblue] {$T(t) - T_a$};
  \end{circuitikz}""",
        "formula_ref": r"""\begin{itemize}[leftmargin=*, nosep]
  \item Hukum Pendinginan Newton: $\frac{dT}{dt} = -k (T - T_a)$ dengan $k = \frac{1}{R_{\text{th}} C_{\text{th}}}$
  \item Neraca Transien Termal Transformator: $C_{\text{th}} \frac{dT}{dt} + \frac{T - T_a}{R_{\text{th}}} = P_{\text{loss}}$
  \item Standar \textbf{IEEE Std C57.91}: Batas temperatur titik panas isolasi kertas-minyak: $T_{\text{kritis}} = 110^\circ\text{C}$
  \item Kenaikan Temperatur Tunak Minyak: $\Delta T_{\text{tunak}} = P_{\text{loss}} \cdot R_{\text{th}}$
\end{itemize}""",
        "c4_text": "Berdasarkan standar \\textbf{IEEE Std C57.91}, suhu belitan transformator tidak boleh melampaui batas kritis isolasi kertas minyak $110^\\circ\\text{C}$. Jika transformator pada Soal 3 mengalami beban lebih mendadak sehingga rugi kalor meningkat menjadi $P_{\\text{loss}} = 85\\text{ kW}$, analisis berapa lama waktu operasi aman yang tersisa sebelum suhu mencapai batas kritis $110^\\circ\\text{C}$!",
        "c5_text": "Sebuah sensor suhu RTD Pt100 diuji di laboratorium kalibrasi: saat dipindahkan dari bejana air mendidih ($100^\\circ\\text{C}$) ke penampung air es ($0^\\circ\\text{C}$), tercatat pembacaan suhu menjadi $36{,}8^\\circ\\text{C}$ pada detik ke-12. Evaluasi apakah sensor tersebut memiliki konstanta waktu termal $\\tau = 12\\text{ detik}$, dan tentukan pembacaan sensor pada detik ke-30!",
        "c6_text": "Rancang skrip program ilmiah berbasis \\textbf{Julia} (\\texttt{DifferentialEquations.jl}) untuk memodelkan sistem pendinginan transformator dengan siklus pembebanan harian berfluktuasi: $P_{\\text{loss}}(t) = 30 + 25\\sin^2(\\frac{\\pi t}{43200})\\text{ kW}$ selama 24 jam ($86400\\text{ detik}$). Plot kurva suhu minyak $T(t)$ bersama batas aman IEEE C57.91.",
    },
    4: {
        "title": "PDB Orde 2 Homogen & Karakteristik Redaman RLC",
        "subcpmk_num": "3",
        "subcpmk_text": "Mahasiswa mampu memformulasikan dan menyelesaikan PDB linier orde 2 homogen koefisien konstan serta menganalisis tiga ragam redaman rangkaian RLC bebas sumber.",
        "c1_text": "Tuliskan bentuk umum PDB linier homogen orde 2 koefisien konstan $a y'' + b y' + c y = 0$ beserta persamaan karakteristiknya, dan sebutkan hubungan nilai diskriminan dengan 3 ragam solusi fisisnya.",
        "c2_text": "Jelaskan definisi fisis frekuensi sudut alami tak-teredam $\\omega_0 = 1/\\sqrt{LC}$ dan faktor redaman Neper $\\alpha = R/(2L)$ pada rangkaian RLC seri. Bagaimana perbandingan $\\alpha$ dan $\\omega_0$ menentukan perilaku osilasi transien arus?",
        "c3_prompt": "Rangkaian RLC seri di samping memiliki kapasitor yang awalnya terisi muatan hingga tegangan $v_C(0) = 200\\text{ V}$ dan arus awal $i(0) = 0$. Sakelar ditutup pada $t=0$. Jika $R = 40\\,\\Omega$, $L = 0{,}2\\text{ H}$, dan $C = 50\\,\\mu\\text{F}$, turunkan persamaan arus transien $i(t)$ dan tentukan apakah sistem tergolong overdamped, critically damped, atau underdamped.",
        "circuitikz": r"""\begin{circuitikz}[american, scale=0.68, transform shape]
    \draw (0,0) to[C, l_=$C$] (0,1.8)
          to[switch, l={$t{=}0$}] (1.5,1.8)
          to[R, l=$R$] (3.0,1.8)
          to[L, l=$L$, v=$v_L(t)$] (3.0,0)
          to[short] (0,0);
    \node at (-0.6,0.9) [font=\tiny\bfseries, unibblue] {$v_C(0){=}V_0$};
    \draw[->, >=stealth, thick, unibblue] (1.3,0.8) arc (160:-160:0.35);
    \node at (1.7,0.8) [unibblue, font=\tiny\bfseries] {$i(t)$};
  \end{circuitikz}""",
        "formula_ref": r"""\begin{itemize}[leftmargin=*, nosep]
  \item Persamaan Karakteristik RLC Seri: $s^2 + 2\alpha s + \omega_0^2 = 0$, dengan $\alpha = \frac{R}{2L}$ dan $\omega_0 = \frac{1}{\sqrt{LC}}$
  \item Ragam Solusi Fisis: Overdamped ($\alpha > \omega_0$), Critically Damped ($\alpha = \omega_0$), Underdamped ($\alpha < \omega_0$)
  \item Frekuensi Sudut Teredam: $\omega_d = \sqrt{\omega_0^2 - \alpha^2}$ \quad\textbar\quad Resistansi Kritis: $R_{\text{kritis}} = 2\sqrt{\frac{L}{C}}$
  \item Energi Total Sistem Bebas Redaman ($R=0$): $W_{\text{total}} = \frac{1}{2} L i^2(t) + \frac{1}{2} C v_C^2(t) = \text{konstan}$
\end{itemize}""",
        "c4_text": "Analisis Desain Rangkaian Snubber: Anda diminta merancang nilai resistansi $R$ agar rangkaian pada Soal 3 bertransisi tepat menjadi redaman kritis (\\textit{critically damped}, $\\zeta = 1$). (a) Hitung nilai resistansi kritis $R_{\\text{kritis}}$; (b) Turunkan ekspresi analitis arus pada kondisi tersebut; (c) Tentukan waktu saat arus mencapai nilai ekstremum maksimum pertamanya.",
        "c5_text": "Tinjau kasus osilasi tanpa redaman ($R=0$, rangkaian LC ideal). Buktikan secara matematis melalui solusi persamaan diferensial bahwa total energi medan elektromagnetik $W_{\\text{total}}(t) = \\frac{1}{2} L i^2(t) + \\frac{1}{2} C v_C^2(t)$ bernilai konstan sepanjang waktu tanpa ada disipasi.",
        "c6_text": "Rancang skrip program \\textbf{Julia} untuk menyelesaikan sistem persamaan diferensial ruang keadaan (*state-space*) RLC seri. Program harus memplot perbandingan kurva arus $i(t)$ untuk tiga variasi nilai $R$ ($R = 10\\,\\Omega$ underdamped, $R = R_{\\text{kritis}}$ critically damped, $R = 250\\,\\Omega$ overdamped) pada satu jendela grafik komparatif.",
    },
    5: {
        "title": "PDB Orde 2 Non-Homogen & Resonansi RLC Eksitasi AC",
        "subcpmk_num": "3",
        "subcpmk_text": "Mahasiswa mampu memecahkan PDB linier orde 2 non-homogen menggunakan metode koefisien tak tentu dan variasi parameter untuk menganalisis resonansi dan faktor kualitas rangkaian AC.",
        "c1_text": "Jelaskan prinsip superposisi solusi total PDB linier non-homogen $y(t) = y_h(t) + y_p(t)$, dan sebutkan aturan modifikasi bentuk tebakan solusi partikular jika fungsi eksitasi luar identik dengan salah satu solusi basis homogen.",
        "c2_text": "Jelaskan fenomena resonansi listrik seri secara fisis. Mengapa pada frekuensi resonansi sudut $\\omega_0 = 1/\\sqrt{LC}$, impedansi total rangkaian menjadi murni resistif dan tegangan induktor saling meniadakan tegangan kapasitor?",
        "c3_prompt": "Rangkaian RLC seri di samping dihubungkan ke sumber tegangan AC sinusoidal $v_s(t) = 120 \\cos(500 t)\\text{ V}$. Jika parameter rangkaian adalah $R = 15\\,\\Omega$, $L = 0{,}1\\text{ H}$, dan $C = 40\\,\\mu\\text{F}$, turunkan persamaan diferensial loop arus dan tentukan solusi partikular tunak (*steady-state*) arus $i_{\\text{ss}}(t)$.",
        "circuitikz": r"""\begin{circuitikz}[american, scale=0.68, transform shape]
    \draw (0,0) to[sV, l=$v_s(t)$] (0,1.8)
          to[R, l=$R$] (1.6,1.8)
          to[L, l=$L$] (3.0,1.8)
          to[C, l=$C$] (3.0,0)
          to[short] (0,0);
    \draw[->, >=stealth, thick, unibblue] (1.4,0.8) arc (160:-160:0.35);
    \node at (1.8,0.8) [unibblue, font=\tiny\bfseries] {$i(t)$};
  \end{circuitikz}""",
        "formula_ref": r"""\begin{itemize}[leftmargin=*, nosep]
  \item Impedansi RLC Seri Domain Frekuensi: $Z(j\omega) = R + j\left(\omega L - \frac{1}{\omega C}\right)$
  \item Kondisi Resonansi Listrik Seri: $\text{Im}\{Z(j\omega_0)\} = 0 \implies \omega_0 = \frac{1}{\sqrt{LC}}$, $f_0 = \frac{1}{2\pi\sqrt{LC}}$
  \item Faktor Kualitas ($Q$-Factor): $Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 R C} = \frac{1}{R}\sqrt{\frac{L}{C}}$
  \item Perbesaran Tegangan Resonansi: $V_{L,\text{maks}} = V_{C,\text{maks}} = Q \cdot V_s$ \quad\textbar\quad Bandwidth: $\Delta\omega = \frac{\omega_0}{Q} = \frac{R}{L}$
\end{itemize}""",
        "c4_text": "Analisis Faktor Kualitas ($Q$) dan Bahaya Resonansi: (a) Hitung frekuensi resonansi sudut $\\omega_0$ dan Faktor Kualitas $Q = \\frac{\\omega_0 L}{R}$ untuk rangkaian Soal 3; (b) Jika frekuensi sumber disetel tepat pada $\\omega = \\omega_0$, buktikan bahwa amplitudo tegangan pada kapasitor mencapai $V_{C,\\text{maks}} = Q \\cdot V_s$; (c) Jelaskan risiko isolasi tembus dielektrik akibat fenomena perbesaran tegangan ini.",
        "c5_text": "Gunakan Metode Variasi Parameter untuk memecahkan PDB osilasi dengan eksitasi tepat pada frekuensi alami tanpa redaman: $y'' + \\omega_0^2 y = F_0 \\sin(\\omega_0 t)$. Buktikan bahwa solusi partikular menghasilkan osilasi yang amplitudonya tumbuh linier terhadap waktu ($-\\frac{F_0}{2\\omega_0} t \\cos(\\omega_0 t)$) menuju resonansi destruktif.",
        "c6_text": "Rancang program simulasi sapuan frekuensi (\\textit{frequency sweep}) dalam bahasa \\textbf{Julia} untuk menghitung impedansi total $|Z(\\omega)|$ dan amplitudo arus $I_m(\\omega)$ pada rentang frekuensi $\\omega \\in [0{,}1\\omega_0, 3\\omega_0]$. Plot kurva respon frekuensi dan tandai frekuensi setengah daya (*half-power bandwidth* $\\Delta\\omega = R/L$).",
    },
    6: {
        "title": "Transformasi Laplace & Sinyal Transien Impuls Surja Petir",
        "subcpmk_num": "4",
        "subcpmk_text": "Mahasiswa mampu memetakan fungsi waktu ke domain frekuensi kompleks $s$ menggunakan Transformasi Laplace serta memodelkan respons sistem terhadap sinyal diskontinu (Heaviside & Dirac).",
        "c1_text": "Tuliskan definisi integral dari Transformasi Laplace unilateral $F(s) = \\int_0^\\infty f(t) e^{-st} dt$, dan tuliskan pasangan transformasi untuk tiga fungsi dasar: fungsi tangga satuan $u(t)$, fungsi impuls Dirac $\\delta(t)$, dan fungsi eksponensial $e^{-at}$.",
        "c2_text": "Jelaskan Teorema Pergeseran Frekuensi kompleks (*First Shifting Theorem*): $\\mathcal{L}\\{e^{-at} f(t)\\} = F(s+a)$. Bagaimana sifat pergeseran frekuensi ini menjelaskan redaman eksponensial pada respons transien rangkaian osilator teredam?",
        "c3_prompt": "Berdasarkan standar pengujian tegangan tinggi \\textbf{IEC 60060-1}, gelombang surja impuls petir standar $1{,}2/50\\,\\mu\\text{s}$ dinyatakan sebagai fungsi eksponensial ganda: $v(t) = V_0 (e^{-\\alpha t} - e^{-\\beta t}) u(t)$. Tentukan representasi aljabar domain Laplace $V(s) = \\mathcal{L}\\{v(t)\\}$ secara eksplisit.",
        "circuitikz": r"""\begin{circuitikz}[american, scale=0.68, transform shape]
    \draw (0,0) to[I, l=$I_0 \delta(t)$] (0,1.8)
          to[short] (1.5,1.8)
          to[R, l=$R_1$] (1.5,0)
          to[short] (0,0);
    \draw (1.5,1.8) to[R, l=$R_2$] (3.0,1.8)
          to[C, l=$C_2$, v=$v_{\text{impuls}}(t)$] (3.0,0)
          to[short] (1.5,0);
  \end{circuitikz}""",
        "formula_ref": r"""\begin{itemize}[leftmargin=*, nosep]
  \item Pasangan Transformasi Dasar: $\mathcal{L}\{u(t)\} = \frac{1}{s}$, $\mathcal{L}\{\delta(t)\} = 1$, $\mathcal{L}\{e^{-at}\} = \frac{1}{s+a}$, $\mathcal{L}\{\sin\omega t\} = \frac{\omega}{s^2+\omega^2}$
  \item Teorema Translasi Frekuensi \& Waktu: $\mathcal{L}\{e^{-at} f(t)\} = F(s+a)$ \quad\textbar\quad $\mathcal{L}\{f(t-T)u(t-T)\} = e^{-sT} F(s)$
  \item Teorema Nilai Awal \& Akhir: $\lim_{t\to 0^+} f(t) = \lim_{s\to\infty} s F(s)$ \quad\textbar\quad $\lim_{t\to\infty} f(t) = \lim_{s\to 0} s F(s)$
  \item Standar \textbf{IEC 60060-1}: Impuls Petir Standar $1{,}2/50\,\mu\text{s}$, $v(t) = V_0(e^{-\alpha t} - e^{-\beta t})$
\end{itemize}""",
        "c4_text": "Analisis respons transien rangkaian RL terhadap tegangan pulsa persegi berdurasi terbatas $T$: $v_s(t) = V_0 [u(t) - u(t-T)]$. Gunakan Teorema Pergeseran Waktu (*Second Shifting Theorem*) untuk menurunkan arus domain-$s$ $I(s)$, lalu rekonstruksi bentuk gelombang arus $i(t)$ untuk interval $0 \\le t < T$ dan interval $t \\ge T$.",
        "c5_text": "Evaluasi perilaku sistem domain frekuensi menggunakan Teorema Nilai Awal (IVT) dan Teorema Nilai Akhir (FVT): Diberikan fungsi transfer tegangan kapasitor $V_C(s) = \\frac{100}{s(s^2 + 6s + 25)}$. Tentukan nilai awal $v_C(0^+)$ dan nilai akhir tunak $v_C(\\infty)$ secara langsung dari domain-$s$, lalu validasi hasilnya dengan penyelesaian domain waktu.",
        "c6_text": "Rancang skrip program ilmiah berbasis \\textbf{Julia} untuk menghasilkan dan memplot gelombang impuls petir standar IEC 60060-1 ($V_0 = 250\\text{ kV}, \\alpha = 14658\\text{ s}^{-1}, \\beta = 2469135\\text{ s}^{-1}$) pada selang waktu mikrodetik $t \\in [0, 80\\,\\mu\\text{s}]$. Tandai titik waktu muka (*front time* $t_1 = 1{,}2\\,\\mu\\text{s}$) dan waktu paruh (*tail time* $t_2 = 50\\,\\mu\\text{s}$).",
    },
    7: {
        "title": "Invers Transformasi Laplace & Pemutus Tenaga (TRV)",
        "subcpmk_num": "4",
        "subcpmk_text": "Mahasiswa mampu merekonstruksi sinyal waktu melalui Invers Transformasi Laplace (pecahan parsial & integral konvolusi) serta menganalisis fenomena Transient Recovery Voltage (TRV) pada pemutus tenaga PMT.",
        "c1_text": "Tuliskan metode pecahan parsial (*partial fraction expansion*) untuk fungsi rasional $F(s) = \\frac{P(s)}{(s+a)(s^2 + \\omega^2)}$, dan tuliskan pasangan invers transformasi Laplace untuk suku linier dan suku kuadratik tersebut.",
        "c2_text": "Jelaskan definisi fisis *Transient Recovery Voltage* (TRV) pada Pemutus Tenaga (PMT / *Circuit Breaker*) menurut standar \\textbf{IEC 62271-100}. Mengapa sesaat setelah arus busur listrik terputus pada titik arus nol (*current zero*), tegangan melintasi kontak PMT berosilasi dengan frekuensi tinggi?",
        "c3_prompt": "Model domain-$s$ dari tegangan pemulihan transien PMT pada sistem transmisi 150 kV diberikan oleh $V_{\\text{TRV}}(s) = V_m \\left( \\frac{1}{s} - \\frac{s}{s^2 + \\omega_0^2} \\right)$. Gunakan invers transformasi Laplace untuk menurunkan fungsi waktu analitis $v_{\\text{TRV}}(t)$, dan tentukan amplitudo puncak tegangan pemulihannya!",
        "circuitikz": r"""\begin{circuitikz}[american, scale=0.68, transform shape]
    \draw (0,0) to[sV, l=$v_s(t)$] (0,1.8)
          to[L, l=$L_{\text{trafo}}$] (1.6,1.8)
          to[switch, l={PMT Buka}] (3.0,1.8)
          to[short] (3.0,0)
          to[short] (0,0);
    \draw (1.6,1.8) to[C, l=$C_{\text{bus}}$, v=$v_{\text{TRV}}$] (1.6,0);
  \end{circuitikz}""",
        "formula_ref": r"""\begin{itemize}[leftmargin=*, nosep]
  \item Ekspansi Pecahan Parsial: $\frac{P(s)}{(s-p_1)(s-p_2)} = \frac{A_1}{s-p_1} + \frac{A_2}{s-p_2}$ dengan $A_k = \lim_{s\to p_k}(s-p_k)F(s)$
  \item Teorema Konvolusi Domain Waktu: $\mathcal{L}^{-1}\{F(s)G(s)\} = (f * g)(t) = \int_0^t f(\tau) g(t-\tau) d\tau$
  \item Standar \textbf{IEC 62271-100}: Transient Recovery Voltage (TRV) pada Pemutus Tenaga (PMT)
  \item Laju Kenaikan Tegangan Pemulihan: $\text{RRRV} = \left. \frac{dv_{\text{TRV}}}{dt} \right|_{\text{maks}} = V_m \omega_0$
\end{itemize}""",
        "c4_text": "Analisis Laju Kenaikan Tegangan Pemulihan (\\textit{Rate of Rise of Recovery Voltage} / RRRV) yang didefinisikan sebagai $\\text{RRRV} = \\left. \\frac{dv_{\\text{TRV}}}{dt} \\right|_{\\text{maks}}$. Jika induktansi sumber hubung singkat $L = 5\\text{ mH}$, kapasitansi busbar $C = 20\\text{ nF}$, dan tegangan puncak sistem $V_m = 120\\text{ kV}$, hitung frekuensi osilasi alami $f_0$ dan nilai RRRV maksimum dalam satuan $\\text{kV/}\\mu\\text{s}$.",
        "c5_text": "Selesaikan Masalah Nilai Awal sistem eksitasi generator berikut secara tuntas menggunakan Transformasi Laplace: $y'' + 6y' + 25y = 50$, dengan nilai awal $y(0) = 1$ dan $y'(0) = -2$. Evaluasi apakah respons transien mengalami osilasi teredam, dan tentukan nilai tunak sistem saat $t \\to \\infty$.",
        "c6_text": "Rancang skrip numerik berbasis \\textbf{Julia} untuk menyelesaikan PDB TRV orde 2 non-homogen dengan paket \\texttt{DifferentialEquations.jl} serta memplot kurva $v_{\\text{TRV}}(t)$ bersama garis batas dielektrik PMT gas $\\text{SF}_6$. Tuliskan definisi fungsi ODE dan parameter simulasi lengkap.",
    },
    9: {
        "title": "Deret Fourier Trigonometrik & Analisis Harmonisa Beban",
        "subcpmk_num": "5",
        "subcpmk_text": "Mahasiswa mampu menguraikan sinyal periodik non-sinusoidal ke dalam Deret Fourier trigonometrik dan mengevaluasi Total Harmonic Distortion (THD) sesuai standar IEEE Std 519.",
        "c1_text": "Tuliskan bentuk umum Deret Fourier trigonometrik untuk suatu sinyal periodik $f(t)$ dengan periode $T$ dan frekuensi sudut dasar $\\omega_0 = 2\\pi/T$, beserta formulasi rumus integral Euler untuk koefisien $a_0$, $a_n$, dan $b_n$.",
        "c2_text": "Jelaskan mengapa beban non-linier industri (seperti konverter daya thyristor dan Variable Speed Drive) membangkitkan arus harmonisa pada sistem tenaga listrik. Bagaimana deret Fourier memisahkan komponen fundamental dari distorsi harmonisa?",
        "c3_prompt": "Tinjau arus beban penyearah gelombang penuh satu fasa tanpa filter yang menghasilkan gelombang pulsa persegi terpotong periodik pada gambar di samping dengan periode $T=20\\text{ ms}$ ($f_0 = 50\\text{ Hz}$) dan amplitudo puncak $I_m = 30\\text{ A}$. Turunkan koefisien deret Fourier $a_0$, $a_n$, dan $b_n$ secara analitis!",
        "circuitikz": r"""\begin{tikzpicture}[scale=0.75]
    \draw[->] (-0.5,0) -- (4.2,0) node[right, font=\tiny] {$t$};
    \draw[->] (0,-1.3) -- (0,1.6) node[above, font=\tiny] {$i(t)$};
    \draw[thick, unibblue] (0,1.2) -- (1.5,1.2) -- (1.5,-1.2) -- (3.0,-1.2) -- (3.0,1.2) -- (4.0,1.2);
    \node at (0.75,1.4) [font=\tiny\bfseries, unibblue] {$+I_m$};
    \node at (2.25,-1.4) [font=\tiny\bfseries, unibblue] {$-I_m$};
    \node at (3.0,-0.3) [font=\tiny] {$T$};
  \end{tikzpicture}""",
        "formula_ref": r"""\begin{itemize}[leftmargin=*, nosep]
  \item Deret Fourier Trigonometrik: $f(t) = a_0 + \sum_{n=1}^\infty \left( a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t) \right)$
  \item Koefisien Euler: $a_0 = \frac{1}{T}\int_0^T f(t) dt$, $a_n = \frac{2}{T}\int_0^T f(t)\cos(n\omega_0 t) dt$, $b_n = \frac{2}{T}\int_0^T f(t)\sin(n\omega_0 t) dt$
  \item Standar Batas Harmonisa \textbf{IEEE Std 519}: Batas Total Harmonic Distortion Arus $\text{THD}_i \le 5{,}0\%$
  \item Formulasi THD: $\text{THD}_i = \frac{\sqrt{\sum_{n=2}^\infty I_n^2}}{I_1} \times 100\%$
\end{itemize}""",
        "c4_text": "Berdasarkan deret Fourier arus Soal 3: (a) Hitung amplitudo komponen harmonisa ke-1 ($I_1$), ke-3 ($I_3$), dan ke-5 ($I_5$); (b) Hitung Total Harmonic Distortion arus ($\\text{THD}_i$) menggunakan 5 suku harmonisa pertama; (c) Analisis apakah nilai $\\text{THD}_i$ tersebut memenuhi ambang batas standar \\textbf{IEEE Std 519} (maksimal $5{,}0\\%$).",
        "c5_text": "Suatu sistem tenaga menyuplai tegangan sinusoidal murni $v(t) = 311 \\cos(100\\pi t)\\text{ V}$ ke beban non-linier yang menarik arus terdistorsi $i(t) = 15 \\cos(100\\pi t - 30^\\circ) + 5 \\cos(300\\pi t - 45^\\circ) + 2 \\cos(500\\pi t - 60^\\circ)\\text{ A}$. Evaluasi daya aktif total ($P$), daya distorsi ($D$), dan faktor daya sejati (*true power factor*) sistem!",
        "c6_text": "Rancang skrip program ilmiah dalam bahasa \\textbf{Julia} untuk merekonstruksi gelombang arus persegi Soal 3 melalui penjumlahan $N$ harmonisa pertama Deret Fourier. Program harus memplot perbandingan kurva rekonstruksi untuk $N \\in \\{1, 3, 7, 25\\}$ dan menunjukkan fenomena overshoot Gibbs di dekat titik diskontinuitas.",
    },
    10: {
        "title": "Deret Fourier Eksponensial & Kekekalan Daya Parseval",
        "subcpmk_num": "5",
        "subcpmk_text": "Mahasiswa mampu mentransformasikan deret Fourier ke dalam bentuk eksponensial kompleks serta menerapkan Teorema Parseval untuk menganalisis disipasi daya pada beban harmonisa.",
        "c1_text": "Tuliskan bentuk Deret Fourier eksponensial kompleks $f(t) = \\sum_{n=-\\infty}^{\\infty} c_n e^{j n \\omega_0 t}$ dan rumus integral untuk spektrum koefisien kompleks $c_n$. Bagaimana hubungan antara $c_n$ dengan koefisien trigonometrik $a_n$ dan $b_n$?",
        "c2_text": "Jelaskan makna fisis Teorema Parseval dalam konteks kekekalan energi dan daya listrik: mengapa total daya aktif rata-rata yang diserap beban linier merupakan jumlahan skalar dari daya masing-masing harmonisa tanpa adanya interaksi silang antar-frekuensi berbeda?",
        "c3_prompt": "Tinjau bentuk gelombang tegangan segitiga simetris bolak-balik pada gambar di samping dengan periode $T = 10\\text{ ms}$ dan nilai puncak $V_p = 100\\text{ V}$. Turunkan koefisien deret Fourier eksponensial $c_n$ secara tuntas untuk seluruh indeks bilangan bulat $n \\in \\mathbb{Z}$.",
        "circuitikz": r"""\begin{tikzpicture}[scale=0.75]
    \draw[->] (-0.5,0) -- (4.2,0) node[right, font=\tiny] {$t$};
    \draw[->] (0,-1.3) -- (0,1.6) node[above, font=\tiny] {$v(t)$};
    \draw[thick, unibblue] (0,0) -- (1.0,1.2) -- (2.0,0) -- (3.0,-1.2) -- (4.0,0);
    \node at (1.0,1.4) [font=\tiny\bfseries, unibblue] {$+V_p$};
    \node at (3.0,-1.4) [font=\tiny\bfseries, unibblue] {$-V_p$};
    \node at (2.0,-0.3) [font=\tiny] {$T/2$};
  \end{tikzpicture}""",
        "formula_ref": r"""\begin{itemize}[leftmargin=*, nosep]
  \item Simetri Fungsi: Genap ($f(-t) = f(t) \implies b_n = 0$), Ganjil ($f(-t) = -f(t) \implies a_n = 0$)
  \item Teorema Parseval (Kekekalan Daya): $P_{\text{avg}} = I_{\text{rms}}^2 R = R \left[ I_0^2 + \sum_{n=1}^\infty \frac{I_{n,\text{maks}}^2}{2} \right]$
  \item Nilai Efektif (RMS) Sinyal Terdistorsi: $I_{\text{rms}} = \sqrt{I_{\text{dc}}^2 + I_{1,\text{rms}}^2 + I_{2,\text{rms}}^2 + \dots}$
  \item Faktor Daya Sejati (*True Power Factor*): $\text{PF}_{\text{true}} = \frac{P}{S} = \frac{I_{1,\text{rms}}}{I_{\text{rms}}} \cos\theta_1$
\end{itemize}""",
        "c4_text": "Tegangan segitiga dari Soal 3 dihubungkan ke sebuah elemen pemanas berhambatan murni $R = 10\\,\\Omega$. (a) Hitung daya aktif rata-rata fundamental $P_1$; (b) Gunakan Teorema Parseval untuk menghitung persentase kontribusi daya harmonisa ke-3 dan ke-5 terhadap disipasi kalor total; (c) Analisis rugi daya tambahan akibat keberadaan harmonisa.",
        "c5_text": "Berdasarkan standar \\textbf{SPLN D3.022-1}, kabel bawah tanah saluran distribusi tegangan menengah mengalami pemanasan berlebih jika kandungan harmonisa tinggi. Evaluasi kenaikan rugi-rugi Joule ($I^2 R$) pada kabel tembaga jika dialiri arus beban dengan spektrum harmonisa $I_1 = 100\\text{ A}$, $I_3 = 30\\text{ A}$, $I_5 = 20\\text{ A}$ dibandingkan dengan arus sinusoidal murni $100\\text{ A}$.",
        "c6_text": "Rancang program ilmiah dalam bahasa \\textbf{Julia} untuk menghitung koefisien spektrum diskrit $|c_n|$ hingga harmonisa ke-30 dari gelombang Soal 3. Program harus memplot diagram spektrum garis magnitudo (\\textit{stem plot}) dan kurva akumulasi persentase daya Parseval terhadap indeks harmonisa $n$.",
    },
    11: {
        "title": "Transformasi Fourier Kontinu & Spektrum Sinyal Transien",
        "subcpmk_num": "5",
        "subcpmk_text": "Mahasiswa mampu mentransformasikan sinyal non-periodik ke domain frekuensi kontinu menggunakan Transformasi Fourier serta menganalisis respons frekuensi filter listrik.",
        "c1_text": "Tuliskan pasangan integral Transformasi Fourier kontinu $F(\\omega) = \\mathcal{F}\\{f(t)\\}$ dan Invers Transformasi Fourier $f(t) = \\mathcal{F}^{-1}\\{F(\\omega)\\}$, serta sebutkan syarat cukup Dirichlet agar suatu fungsi waktu dapat ditransformasikan ke domain Fourier.",
        "c2_text": "Jelaskan perbedaan konseptual mendasar antara Deret Fourier (sinyal periodik, spektrum diskrit harmonisa) dengan Transformasi Fourier (sinyal aperiodik/transien tunggal, spektrum kontinu kerapatan spektral).",
        "c3_prompt": "Sebuah sinyal pulsa eksponensial transien tunggal pemutus daya dinyatakan oleh $f(t) = V_0 e^{-a t} u(t)$ dengan konstanta redaman $a > 0$. Hitung spektrum kerapatan frekuensi kontinu $F(\\omega) = \\mathcal{F}\\{f(t)\\}$, lalu tentukan magnitudo spektrum $|F(\\omega)|$ dan sudut fasa $\\angle F(\\omega)$ secara analitis.",
        "circuitikz": r"""\begin{tikzpicture}[scale=0.75]
    \draw[->] (-0.5,0) -- (4.0,0) node[right, font=\tiny] {$t$};
    \draw[->] (0,-0.3) -- (0,1.8) node[above, font=\tiny] {$f(t)$};
    \draw[thick, unibblue, domain=0:3.8, samples=50] plot (\x, {1.5*exp(-1.0*\x)});
    \node at (0.4,1.6) [font=\tiny\bfseries, unibblue] {$V_0$};
    \node at (2.2,0.8) [font=\tiny] {$V_0 e^{-at}$};
  \end{tikzpicture}""",
        "formula_ref": r"""\begin{itemize}[leftmargin=*, nosep]
  \item Pasangan Transformasi Fourier Kontinu: $F(\omega) = \int_{-\infty}^\infty f(t) e^{-j\omega t} dt$ \quad\textbar\quad $f(t) = \frac{1}{2\pi}\int_{-\infty}^\infty F(\omega) e^{j\omega t} d\omega$
  \item Teorema Modulasi Frekuensi: $\mathcal{F}\{f(t)\cos(\omega_c t)\} = \frac{1}{2}\left[F(\omega - \omega_c) + F(\omega + \omega_c)\right]$
  \item Teorema Energi Rayleigh-Parseval: $\int_{-\infty}^\infty |f(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^\infty |F(\omega)|^2 d\omega$
  \item Respons Frekuensi Filter Pasif RC: $H(j\omega) = \frac{V_{\text{out}}(j\omega)}{V_{\text{in}}(j\omega)} = \frac{1}{1 + j\omega R C}$
\end{itemize}""",
        "c4_text": "Tinjau Teorema Energi Rayleigh-Parseval untuk sinyal transien: $\\int_{-\\infty}^\\infty |f(t)|^2 dt = \\frac{1}{2\\pi} \\int_{-\\infty}^\\infty |F(\\omega)|^2 d\\omega$. (a) Buktikan teorema ini untuk sinyal pulsa eksponensial Soal 3; (b) Tentukan bandwidth frekuensi $\\omega_B$ yang memuat tepat $90\\%$ dari total energi sinyal transien tersebut.",
        "c5_text": "Sinyal transien Soal 3 dilewatkan ke filter lolos-rendah (LPF) RC satu tingkat dengan fungsi alih $H(j\\omega) = \\frac{1}{1 + j\\omega/\\omega_c}$. Evaluasi energi spektral keluaran filter $E_{\\text{out}}$ dan analisis bagaimana pemilihan frekuensi cut-off $\\omega_c$ meredam komponen transien frekuensi tinggi yang merusak peralatan.",
        "c6_text": "Rancang skrip program dalam bahasa \\textbf{Julia} menggunakan paket \\texttt{FFTW.jl} untuk menghitung Fast Fourier Transform (FFT) dari pulsa persegi transien berdurasi $T = 2\\text{ ms}$. Program harus memplot spektrum kerapatan energi kontinu analitis (fungsi Sinc) berdampingan dengan hasil estimasi numerik FFT.",
    },
    12: {
        "title": "Persamaan Gelombang 1D & Persamaan Telegrafer Transmisi",
        "subcpmk_num": "6",
        "subcpmk_text": "Mahasiswa mampu memformulasikan dan memecahkan Persamaan Telegrafer Saluran Transmisi (PDP Hiperbolik) menggunakan metode pemisahan variabel dan solusi gelombang berjalan d'Alembert.",
        "c1_text": "Tuliskan sepasang Persamaan Telegrafer saluran transmisi untuk tegangan $v(x,t)$ dan arus $i(x,t)$ dengan parameter terdistribusi $R, L, G, C$, serta turunkan persamaan gelombang 1D orde 2 untuk tegangan pada saluran tanpa rugi-rugi (*lossless*).",
        "c2_text": "Jelaskan interpretasi fisis solusi umum d'Alembert $v(x,t) = f(x - vt) + g(x + vt)$ dalam konteks gelombang berjalan maju (*forward*) dan gelombang pantul (*backward*) sepanjang saluran transmisi.",
        "c3_prompt": "Saluran transmisi udara 150 kV sepanjang $L_s = 300\\text{ km}$ memiliki induktansi terdistribusi $L' = 1{,}2\\,\\mu\\text{H/m}$ dan kapasitansi $C' = 8{,}33\\text{ nF/km}$. Jika saluran dianggap tanpa rugi ($R'=G'=0$), hitung cepat rambat gelombang $v$ dan impedansi karakteristik saluran $Z_0$.",
        "circuitikz": r"""\begin{tikzpicture}[scale=0.75]
    \draw[thick] (0,1.2) -- (4.0,1.2);
    \draw[thick] (0,0) -- (4.0,0);
    \draw[dashed, red] (1.2,1.2) -- (1.2,0);
    \draw[dashed, red] (2.8,1.2) -- (2.8,0);
    \draw[<->, >=stealth] (1.2,-0.3) -- (2.8,-0.3) node[midway, below, font=\tiny] {$\Delta x$};
    \draw[->, >=stealth, thick, unibblue] (0.5,1.5) -- (1.5,1.5) node[right, font=\tiny] {$v(x,t)$};
    \node at (2.0,1.4) [font=\tiny] {$L'\Delta x, R'\Delta x$};
    \node at (2.0,0.4) [font=\tiny] {$C'\Delta x, G'\Delta x$};
  \end{tikzpicture}""",
        "formula_ref": r"""\begin{itemize}[leftmargin=*, nosep]
  \item Persamaan Telegrafer Saluran Transmisi: $\frac{\partial v}{\partial x} = -R' i - L' \frac{\partial i}{\partial t}$, \quad $\frac{\partial i}{\partial x} = -G' v - C' \frac{\partial v}{\partial t}$
  \item Persamaan Gelombang Saluran Tanpa Rugi ($R'=G'=0$): $\frac{\partial^2 v}{\partial x^2} = L' C' \frac{\partial^2 v}{\partial t^2} = \frac{1}{v_p^2} \frac{\partial^2 v}{\partial t^2}$
  \item Parameter Karakteristik Saluran: Kecepatan Rambat $v_p = \frac{1}{\sqrt{L'C'}}$, Impedansi Karakteristik $Z_0 = \sqrt{\frac{L'}{C'}}$
  \item Koefisien Refleksi Tegangan pada Beban $Z_L$: $\Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0}$
\end{itemize}""",
        "c4_text": "Analisis Refleksi Gelombang Surja Petir: Saluran transmisi Soal 3 dihubungkan ke transformator daya dengan impedansi surja beban $Z_L = 1200\\,\\Omega$. Ketika gelombang petir beramplitudo $V_0 = 400\\text{ kV}$ tiba di terminal trafo: (a) Hitung koefisien refleksi tegangan $\\Gamma_L$; (b) Hitung tegangan puncak total yang dialami isolasi transformator; (c) Analisis bahaya kegagalan dielektrik akibat fenomena pantulan tegangan ini.",
        "c5_text": "Gunakan Metode Pemisahan Variabel $v(x,t) = X(x) T(t)$ untuk memecahkan persamaan gelombang saluran tanpa rugi dengan syarat batas ujung terhubung singkat $v(0,t) = 0$ dan $v(L_s,t) = 0$. Buktikan bahwa frekuensi-frekuensi alami osilasi gelombang berdiri (*standing wave resonance*) bernilai $f_n = \\frac{n v}{2 L_s}$ untuk $n = 1, 2, 3, \\dots$.",
        "c6_text": "Rancang program simulasi gelombang berjalan dalam bahasa \\textbf{Julia} menggunakan skema beda hingga FDM (*Finite Difference Method*) untuk memvisualisasikan perambatan pulsa surja tegangan petir dari pangkal hingga memantul di ujung beban saluran transmisi. Buat animasi profil gelombang $v(x,t)$ terhadap posisi $x$.",
    },
    13: {
        "title": "Persamaan Laplace & Medan Potensial Elektrostatika 2D",
        "subcpmk_num": "6",
        "subcpmk_text": "Mahasiswa mampu menyelesaikan Persamaan Laplace 2D (PDP Eliptik) dengan metode pemisahan variabel koordinat Kartesian untuk menentukan distribusi potensial dan medan listrik pada geometri elektroda isolator.",
        "c1_text": "Tuliskan bentuk Persamaan Diferensial Parsial Laplace $\\nabla^2 V = 0$ dalam koordinat Kartesian 2D $\\frac{\\partial^2 V}{\\partial x^2} + \\frac{\\partial^2 V}{\\partial y^2} = 0$, dan sebutkan perbedaan fisis antara Persamaan Laplace (ruang bebas muatan) dan Persamaan Poisson (ruang bermuatan).",
        "c2_text": "Jelaskan prinsip fisis di balik Teorema Nilai Rata-Rata (*Mean Value Theorem*) untuk medan harmonik: mengapa nilai potensial listrik di sembarang titik selalu sama dengan rata-rata potensial pada permukaan bola/lingkaran yang melingkupinya, dan mengapa titik ekstremum lokal hanya dapat terjadi pada batas (*boundary*)?",
        "c3_prompt": "Tinjau alur celah isolator tegangan tinggi berdimensi persegi panjang semi-tak-hingga ($0 \\le x \\le a, y \\ge 0$) pada gambar di samping. Batas samping dan bawah dibumikan ($V(0,y) = 0, V(a,y) = 0, V(x,\\infty) = 0$), sedangkan batas pelat atas dipertahankan pada tegangan konstan $V(x,0) = V_0$. Gunakan pemisahan variabel untuk menurunkan fungsi potensial $V(x,y)$!",
        "circuitikz": r"""\begin{tikzpicture}[scale=0.75]
    \draw[thick] (0,2.5) -- (0,0) -- (3.0,0) -- (3.0,2.5);
    \draw[thick, unibblue] (0,0) -- (3.0,0) node[midway, below, font=\tiny\bfseries] {$V(x,0)=V_0$};
    \node at (-0.6,1.2) [font=\tiny] {$V=0$};
    \node at (3.6,1.2) [font=\tiny] {$V=0$};
    \node at (1.5,1.2) [font=\tiny, unibblue] {$\nabla^2 V = 0$};
    \draw[<->, >=stealth] (0,-0.6) -- (3.0,-0.6) node[midway, below, font=\tiny] {$a$};
  \end{tikzpicture}""",
        "formula_ref": r"""\begin{itemize}[leftmargin=*, nosep]
  \item Persamaan Laplace Elektrostatika Bebas Muatan ($\rho_v = 0$): $\nabla^2 V = \frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} = 0$
  \item Hubungan Medan Listrik dan Potensial Skalar: $\vec{E} = -\nabla V = -\left(\frac{\partial V}{\partial x}\hat{a}_x + \frac{\partial V}{\partial y}\hat{a}_y\right)$
  \item Metode Pemisahan Variabel (*Separation of Variables*): $V(x,y) = X(x) Y(y)$
  \item Kekuatan Dielektrik Udara (Tegangan Tembus Udara Kering): $E_{\text{kritis}} \approx 30\text{ kV/cm} = 3\text{ MV/m}$
\end{itemize}""",
        "c4_text": "Berdasarkan solusi potensial $V(x,y)$ dari Soal 3: (a) Turunkan ekspresi vektor medan listrik $\\vec{E}(x,y) = -\\nabla V = -\\left(\\frac{\\partial V}{\\partial x}\\hat{a}_x + \\frac{\\partial V}{\\partial y}\\hat{a}_y\\right)$; (b) Tentukan lokasi titik terjadinya stres medan listrik maksimum $\\vec{E}_{\\text{maks}}$; (c) Analisis potensi terjadinya lucutan korona (*corona discharge*) jika $V_0 = 100\\text{ kV}$ dan $a = 10\\text{ cm}$ (kuat dielektrik udara $30\\text{ kV/cm}$).",
        "c5_text": "Evaluasi distribusi kerapatan muatan induksi permukaan $\\sigma_s(x) = -\\epsilon_0 \\left. \\frac{\\partial V}{\\partial y} \\right|_{y=0}$ pada pelat konduktor batas. Buktikan bahwa muatan cenderung terkonsentrasi di sudut-sudut tajam elektroda (*edge effect*), dan jelaskan relevansi rekayasa penambahan cincin perata medan (*corona ring*) pada isolator gardu induk PLN.",
        "c6_text": "Rancang program ilmiah berbasis \\textbf{Julia} untuk menyelesaikan Persamaan Laplace 2D pada geometri Soal 3 menggunakan metode relaksasi beda hingga (FDM Jacobi / Gauss-Seidel). Program harus menghasilkan peta kontur garis ekuipotensial 2D berdampingan dengan panah medan vektor gradien $\\vec{E}$.",
    },
    14: {
        "title": "Fungsi Khusus: Persamaan Bessel & Fenomena Efek Kulit",
        "subcpmk_num": "6",
        "subcpmk_text": "Mahasiswa mampu memecahkan Persamaan Diferensial Bessel dalam koordinat silindris serta memodelkan fenomena Efek Kulit (Skin Effect) pada konduktor ACSR sesuai IEC 61089.",
        "c1_text": "Tuliskan bentuk baku Persamaan Diferensial Bessel berorde $n$: $x^2 \\frac{d^2 y}{dx^2} + x \\frac{dy}{dx} + (x^2 - n^2)y = 0$, dan sebutkan dua solusi basis bebas liniernya yaitu fungsi Bessel jenis pertama $J_n(x)$ dan jenis kedua $Y_n(x)$.",
        "c2_text": "Jelaskan sifat asimtotik fungsi Bessel $J_n(x)$ dan $Y_n(x)$ saat $x \\to 0$. Mengapa fungsi Bessel jenis kedua $Y_n(x)$ yang divergen menuju $-\\infty$ di titik pusat ($r = 0$) harus dieliminasi ($C_2 = 0$) pada pemodelan kawat konduktor silinder pejal?",
        "c3_prompt": "Pada kawat silindris padat beradius $a = 8\\text{ mm}$ yang dialiri arus bolak-balik $50\\text{ Hz}$, persamaan rapat arus radial dinyatakan oleh fungsi Bessel Kelvin: $J_z(r) = J_0 \\frac{J_0(k r)}{J_0(k a)}$. (a) Turunkan ekspresi analitis kedalaman kulit (*skin depth*) $\\delta = \\sqrt{\\frac{2}{\\omega \\mu \\sigma}}$; (b) Hitung kedalaman kulit $\\delta$ tembaga pada $f = 50\\text{ Hz}$ jika $\\sigma = 5{,}8 \\times 10^7\\text{ S/m}$ dan $\\mu = 4\\pi \\times 10^{-7}\\text{ H/m}$; (c) Bandingkan $\\delta$ terhadap radius fisik kawat $a$.",
        "circuitikz": r"""\begin{tikzpicture}[scale=0.75]
    \draw[thick, fill=gray!20] (0,0) circle (1.5);
    \draw[thick, fill=white] (0,0) circle (1.0);
    \pattern[pattern=north east lines] (0,0) circle (1.5);
    \fill[white] (0,0) circle (1.0);
    \draw[thick] (0,0) circle (1.0);
    \draw[->, >=stealth, thick] (0,0) -- (1.5,0) node[midway, above, font=\tiny] {$a$};
    \node at (0,0) [font=\tiny\bfseries] {Inti};
    \draw[<->, >=stealth, red, very thick] (1.0,0) -- (1.5,0) node[midway, below, font=\tiny\bfseries] {$\delta$};
  \end{tikzpicture}""",
        "formula_ref": r"""\begin{itemize}[leftmargin=*, nosep]
  \item Persamaan Diferensial Bessel Orde $n$: $x^2 \frac{d^2 y}{dx^2} + x \frac{dy}{dx} + (x^2 - n^2) y = 0$
  \item Solusi Umum Bessel: $y(x) = C_1 J_n(x) + C_2 Y_n(x)$ ($Y_n(x) \to -\infty$ saat $x \to 0$)
  \item Kedalaman Penetrasi Efek Kulit (*Skin Depth*): $\delta = \sqrt{\frac{2}{\omega \mu \sigma}} = \frac{1}{\sqrt{\pi f \mu \sigma}}$
  \item Standar \textbf{IEC 61089}: Rasio Resistansi AC/DC Konduktor Pejal: $\frac{R_{\text{ac}}}{R_{\text{dc}}} \approx \frac{a}{2\delta}$ untuk $a \gg \delta$
\end{itemize}""",
        "c4_text": "Analisis Rasio Kenaikan Resistansi AC Sesuai Standar \\textbf{IEC 61089}: Akibat efek kulit, arus terkonsentrasi di dekat permukaan luar kawat. (a) Turunkan aproksimasi kenaikan resistansi $R_{\\text{ac}}/R_{\\text{dc}} \\approx \\frac{a}{2\\delta}$ untuk $a \\gg \\delta$; (b) Analisis mengapa konduktor transmisi daya arus bolak-balik tegangan ekstra tinggi tidak menggunakan konduktor tembaga pejal berpenampang besar melainkan konduktor berkas berpilin (*bundled stranded conductor*).",
        "c5_text": "Evaluasi Desain Konduktor ACSR (*Aluminium Conductor Steel Reinforced*): Kawat ACSR menempatkan inti baja di lapisan terdalam dan untaian aluminium di lapisan terluar. Evaluasi keunggulan desain struktur ini secara terintegrasi dari sudut pandang elektromagnetika (rapat arus Bessel Kelvin) dan kekuatan mekanis bentangan antar-menara transmisi.",
        "c6_text": "Rancang skrip program ilmiah berbasis \\textbf{Julia} menggunakan paket \\texttt{SpecialFunctions.jl} untuk menghitung nilai fungsi Bessel $J_0(x)$ dan $J_1(x)$. Program harus memplot kurva distribusi rapat arus ternormalisasi $|J_z(r)/J_0|$ dari pusat kawat ($r = 0$) hingga tepi permukaan ($r = a$) pada tiga variasi frekuensi ($50\\text{ Hz}, 500\\text{ Hz}$, dan $50\\text{ kHz}$).",
    },
    15: {
        "title": "Polinomial Legendre & Persamaan Gelombang Elektromagnetik",
        "subcpmk_num": "6",
        "subcpmk_text": "Mahasiswa mampu memecahkan Persamaan Diferensial Legendre dalam koordinat bola serta menurunkan formulasi Persamaan Gelombang Elektromagnetik Helmholtz dari 4 Persamaan Maxwell.",
        "c1_text": "Tuliskan bentuk baku Persamaan Diferensial Legendre $(1 - x^2) \\frac{d^2 y}{dx^2} - 2x \\frac{dy}{dx} + n(n+1)y = 0$, dan sebutkan polinomial Legendre untuk tiga derajat pertama: $P_0(x)$, $P_1(x)$, dan $P_2(x)$.",
        "c2_text": "Jelaskan sifat ortogonalitas Polinomial Legendre $\\int_{-1}^1 P_m(x) P_n(x) dx = \\frac{2}{2n+1} \\delta_{mn}$. Bagaimana sifat ini dimanfaatkan untuk mengevaluasi koefisien ekspansi deret potensial elektrostatika pada sistem dengan simetri bola?",
        "c3_prompt": "Sebuah bola konduktor netral beradius $a = 15\\text{ cm}$ diletakkan di dalam medan listrik luar yang seragam $\\vec{E}_0 = E_0 \\hat{a}_z$ ($E_0 = 50\\text{ kV/m}$). Distribusi potensial di luar bola memenuhi persamaan Laplace koordinat bola dengan solusi umum $V(r,\\theta) = \\sum_{n=0}^\\infty (A_n r^n + B_n r^{-(n+1)}) P_n(\\cos\\theta)$. Tentukan fungsi analitis potensial $V(r,\\theta)$ secara tuntas!",
        "circuitikz": r"""\begin{tikzpicture}[scale=0.75]
    \draw[thick, fill=gray!20] (0,0) circle (1.2);
    \draw[->, >=stealth] (0,0) -- (0.85,0.85) node[midway, above, font=\tiny] {$a$};
    \node at (0,0) [font=\tiny\bfseries] {Bola};
    \foreach \y in {-1.2, -0.6, 0, 0.6, 1.2} {
      \draw[->, >=stealth, thick, unibblue] (-2.2,\y) -- (-1.5,\y);
      \draw[->, >=stealth, thick, unibblue] (1.5,\y) -- (2.2,\y);
    }
    \node at (1.5,1.5) [font=\tiny\bfseries, unibblue] {$\vec{E}_0 = E_0 \hat{a}_z$};
  \end{tikzpicture}""",
        "formula_ref": r"""\begin{itemize}[leftmargin=*, nosep]
  \item Persamaan Diferensial Legendre Orde $n$: $(1-x^2) \frac{d^2 y}{dx^2} - 2x \frac{dy}{dx} + n(n+1) y = 0$
  \item Polinomial Legendre: $P_0(x) = 1$, $P_1(x) = x$, $P_2(x) = \frac{1}{2}(3x^2 - 1)$, $P_3(x) = \frac{1}{2}(5x^3 - 3x)$
  \item Solusi Potensial Bola Konduktor: $V(r,\theta) = \sum_{n=0}^\infty \left( A_n r^n + \frac{B_n}{r^{n+1}} \right) P_n(\cos\theta)$
  \item Vektor Medan Listrik Koordinat Bola: $E_r = -\frac{\partial V}{\partial r}$, $E_\theta = -\frac{1}{r}\frac{\partial V}{\partial \theta}$, $E_\phi = -\frac{1}{r\sin\theta}\frac{\partial V}{\partial \phi}$
\end{itemize}""",
        "c4_text": "Analisis Penurunan Persamaan Gelombang Elektromagnetik 3D: Terapkan operator rotasi $\\nabla \\times (\\nabla \\times \\vec{E})$ pada Hukum Faraday $\\nabla \\times \\vec{E} = -\\frac{\\partial \\vec{B}}{\\partial t}$ di ruang bebas tanpa muatan dan arus ($\\rho=0, \\vec{J}=0$). Gunakan identitas vektor $\\nabla \\times (\\nabla \\times \\vec{E}) = \\nabla(\\nabla \\cdot \\vec{E}) - \\nabla^2 \\vec{E}$ untuk membuktikan bahwa medan listrik memenuhi persamaan gelombang 3D dengan kecepatan rambat $c = 1/\\sqrt{\\mu_0 \\epsilon_0} \\approx 3 \\times 10^8\\text{ m/s}$.",
        "c5_text": "Evaluasi Vektor Poynting $\\vec{S} = \\vec{E} \\times \\vec{H}$ dan Batas Paparan Publik \\textbf{IEEE Std C95.1}: Gelombang elektromagnetik transversal (TEM) memiliki amplitudo medan listrik $E = 50\\text{ V/m}$ di bawah koridor saluran transmisi SUTET 500 kV PLN. (a) Hitung magnitudo medan magnetik $H = E/\\eta_0$ di mana impedansi ruang bebas $\\eta_0 = \\sqrt{\\mu_0/\\epsilon_0} \\approx 377\\,\\Omega$; (b) Hitung densitas fluks daya rata-rata $S_{\\text{avg}} = \\frac{1}{2} E H$; (c) Evaluasi apakah nilai radiasi daya tersebut aman bagi masyarakat sekitar.",
        "c6_text": "Rancang skrip program ilmiah berbasis \\textbf{Julia} menggunakan pustaka \\texttt{Plots.jl} untuk memetakan garis-garis gaya medan listrik ekuipotensial dipol bola hasil penurunan Soal 3. Program harus menghitung vektor medan radial $E_r = -\\frac{\\partial V}{\\partial r}$ dan transversal $E_\\theta = -\\frac{1}{r}\\frac{\\partial V}{\\partial \\theta}$ serta menampilkan grafik vektor medan (*quiver plot*) di sekitar bola konduktor.",
    }
}

TEMPLATE_PS = r"""\documentclass[10pt,a4paper]{article}
\usepackage[top=1.4cm, bottom=1.4cm, left=1.6cm, right=1.6cm, headheight=14pt, footskip=18pt]{geometry}
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
\lfoot{\footnotesize\color{gray}Problem Set Tugas Terstruktur Berbasis OBE}
\cfoot{\footnotesize\color{gray}Hal. \thepage\ dari 2}
\rfoot{\footnotesize\color{unibblue}\textbf{Minggu __WEEK__: __TITLE_SHORT__}}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.4pt}

\begin{document}

% ==================== HALAMAN 1 ====================
\noindent\begin{minipage}[c]{0.68\textwidth}%
  {\large\textbf{\color{unibblue}PROBLEM SET (TUGAS MANDIRI TERSTRUKTUR)}}\\[1mm]
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

% Kotak Sub-CPMK & Pedoman Tugas Terstruktur
\begin{tcolorbox}[colback=boxbg,colframe=unibgold!90!black,boxrule=0.6pt,arc=2pt,left=5pt,right=5pt,top=3pt,bottom=3pt,title=\textbf{\scriptsize Capaian Pembelajaran (Sub-CPMK __SUBCPMK_NUM__) \& Pedoman Pengerjaan Tugas}]
  \scriptsize
  \textbf{Sub-CPMK __SUBCPMK_NUM__:} __SUBCPMK_TEXT__\\
  \textbf{Ketentuan Tugas:} Kerjakan secara mandiri pada kertas folio/A4 bergaris atau laporan digital rapi. Lampirkan penurunan rumus analitis lengkap dan cetak visualisasi kode program Julia (Soal C6). Kumpulkan pada awal perkuliahan minggu berikutnya.
\end{tcolorbox}

\vspace{1.5mm}

\noindent{\textbf{\color{unibblue}\large BAGIAN I: FONDASI KONSEPTUAL \& PENURUNAN MATEMATIS}}\par
\vspace{1mm}

% Soal C1
\noindent\textbf{1. (C1 - Mengingat \textbar\ Bobot: 10 Poin)}\par\vspace{0.8mm}
{\footnotesize __C1_TEXT__}\par

\vspace{2.5mm}

% Soal C2
\noindent\textbf{2. (C2 - Memahami \textbar\ Bobot: 15 Poin)}\par\vspace{0.8mm}
{\footnotesize __C2_TEXT__}\par

\vspace{2.5mm}

% Soal C3
\noindent\textbf{3. (C3 - Menerapkan \textbar\ Bobot: 20 Poin)}\par\vspace{0.8mm}
\noindent\begin{minipage}[t]{0.60\textwidth}%
  {\footnotesize __C3_PROMPT__}%
\end{minipage}%
\hfill%
\begin{minipage}[t]{0.37\textwidth}%
  \centering
  \resizebox{0.95\linewidth}{!}{%
  __CIRCUITIKZ__%
  }%
\end{minipage}\par

\vfill

% Kotak Formula Rujukan Teknis & Standar Industri
\begin{tcolorbox}[colback=unibblue!3,colframe=unibblue,colbacktitle=unibblue,coltitle=white,boxrule=0.6pt,arc=2pt,left=6pt,right=6pt,top=3pt,bottom=3pt,title=\textbf{\scriptsize FORMULA RUJUKAN TEKNIS \& STANDAR INDUSTRI TERKAIT}]
  \scriptsize
  __FORMULA_REF__
\end{tcolorbox}

\newpage
% ==================== HALAMAN 2 ====================

\noindent{\textbf{\color{unibblue}\large BAGIAN II: ANALISIS SISTEM, EVALUASI STANDAR, \& KOMPUTASI JULIA}}\par
\vspace{1mm}

% Soal C4
\noindent\textbf{4. (C4 - Menganalisis \textbar\ Bobot: 20 Poin)}\par\vspace{0.8mm}
{\footnotesize __C4_TEXT__}\par

\vspace{3.5mm}

% Soal C5
\noindent\textbf{5. (C5 - Mengevaluasi \textbar\ Bobot: 20 Poin)}\par\vspace{0.8mm}
{\footnotesize __C5_TEXT__}\par

\vspace{3.5mm}

% Soal C6
\noindent\textbf{6. (C6 - Merancang \& Komputasi Julia \textbar\ Bobot: 15 Poin)}\par\vspace{0.8mm}
{\footnotesize __C6_TEXT__}\par

\vfill

% Tabel Rekapitulasi Skor OBE & Lembar Catatan Umpan Balik Dosen
\noindent\begin{minipage}[b]{0.62\textwidth}%
  \centering
  \scriptsize
  \begin{tabular}{|c|c|c|c|c|c|c|}
    \hline
    \rowcolor{unibblue}
    \textbf{\color{white}C1} & \textbf{\color{white}C2} & \textbf{\color{white}C3} & \textbf{\color{white}C4} & \textbf{\color{white}C5} & \textbf{\color{white}C6} & \textbf{\color{white}Total} \\
    \rowcolor{unibblue!10}
    10 Pts & 15 Pts & 20 Pts & 20 Pts & 20 Pts & 15 Pts & 100 Pts \\
    \hline
    & & & & & & \\[3mm]
    \hline
  \end{tabular}%
\end{minipage}%
\hfill%
\begin{minipage}[b]{0.35\textwidth}%
  \centering
  \scriptsize
  \textbf{Verifikasi Dosen / Asisten:}\\[6mm]
  (\dotfill)\\[1mm]
  \tiny Tanggal: \dotfill
\end{minipage}\par

\vspace{2mm}
\begin{tcolorbox}[colback=white,colframe=unibblue!40!black,colbacktitle=unibblue!10,coltitle=unibblue,boxrule=0.5pt,arc=2pt,left=5pt,right=5pt,top=3pt,bottom=3pt,title=\textbf{\tiny Catatan Evaluasi \& Umpan Balik Dosen Pengampu}]
  \tiny
  \textbf{Rubrik Pemeriksaan Pengerjaan Tugas Mandiri:}\par\vspace{0.8mm}
  $\square$ Penurunan matematis langkah-demi-langkah runtut (C1--C4) \hfill $\square$ Validasi analitis \& standar industri IEEE/IEC/SPLN akurat (C5)\\[0.8mm]
  $\square$ Skrip program Julia mandiri \& grafik visualisasi terlampir (C6) \hfill $\square$ Kerapian format laporan \& ketepatan waktu pengumpulan\\[2.0mm]
  \textbf{Catatan / Koreksi Khusus Dosen:}\\[1.6cm]
\end{tcolorbox}

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

def generate_problem_set_tex(w_num):
    data = PROBLEM_SETS[w_num]
    content = TEMPLATE_PS
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
    content = content.replace("__C2_TEXT__", sanitize_latex(data["c2_text"]))
    content = content.replace("__C3_PROMPT__", sanitize_latex(data["c3_prompt"]))
    content = content.replace("__CIRCUITIKZ__", data["circuitikz"])
    content = content.replace("__FORMULA_REF__", data["formula_ref"])
    content = content.replace("__C4_TEXT__", sanitize_latex(data["c4_text"]))
    content = content.replace("__C5_TEXT__", sanitize_latex(data["c5_text"]))
    content = content.replace("__C6_TEXT__", sanitize_latex(data["c6_text"]))
    
    filename = f"problem_set{w_num}.tex"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filename}")

if __name__ == "__main__":
    for w in sorted(PROBLEM_SETS.keys()):
        generate_problem_set_tex(w)
