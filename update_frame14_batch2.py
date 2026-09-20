import re

f14_content = {
    "ch9.tex": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
\begin{frame}{Kuis Konseptual Interaktif \& Evaluasi Bloom (C1--C6)}
  \begin{columns}[t]
    \column{0.52\textwidth}
    \begin{alertblock}{Peer Instruction: Uji Miskonsepsi Fisik}
      \footnotesize
      \textbf{Kasus Rekayasa:} Jika jumlah harmonisa deret Fourier gelombang kotak dinaikkan dari $N = 25$ hingga $N = 1.000.000$ suku, apakah lonjakan overshoot di sudut diskontinuitas akan hilang ke $0\%$?
      \vspace{0.05cm}
      \begin{itemize}\setlength{\itemsep}{1pt}
        \item \textbf{[A]} Ya, karena deret Fourier konvergen sempurna ke fungsi.
        \item \textbf{[B]} **Tidak**, lecutan overshoot tetap bertengger konstan sebesar $\approx 8{,}95\%$ (Fenomena Gibbs) dan lebarnya menyempit menuju nol!
        \item \textbf{[C]} Ya, tetapi membutuhkan komponen resistor fisik.
        \item \textbf{[D]} Tidak, lecutan justru membesar menjadi $50\%$.
      \end{itemize}
    \end{alertblock}

    \column{0.46\textwidth}
    \begin{block}{Tantangan Analisis \& Desain (C4--C6)}
      \footnotesize
      \begin{itemize}\setlength{\itemsep}{2pt}
        \item \textbf{C4 (Analisis):} Hitung Total Harmonic Distortion (THD) tegangan inverter PLTS sesuai batas aman IEEE Std 519 ($<5\%$).
        \item \textbf{C5 (Evaluasi):} Buktikan teorema ortogonalitas fungsi trigonometri pada interval simetris $[-L, L]$.
        \item \textbf{C6 (Desain):} Rancang spektrum filter harmonisa aktif untuk meredam harmonisa ke-3 dan ke-5 beban non-linier!
      \end{itemize}
    \end{block}
  \end{columns}
\end{frame}""",

    "ch10.tex": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
\begin{frame}{Kuis Konseptual Interaktif \& Evaluasi Bloom (C1--C6)}
  \begin{columns}[t]
    \column{0.52\textwidth}
    \begin{alertblock}{Peer Instruction: Uji Miskonsepsi Fisik}
      \footnotesize
      \textbf{Kasus Rekayasa:} Pada pemisahan variabel $u(x,t) = X(x)T(t)$ untuk persamaan termal, mengapa konstanta pemisah $k$ wajib dipilih bernilai negatif ($-\lambda^2$)?
      \vspace{0.05cm}
      \begin{itemize}\setlength{\itemsep}{1pt}
        \item \textbf{[A]} Konstanta positif dilarang dalam kalkulus diferensial.
        \item \textbf{[B]} Konstanta positif menghasilkan solusi $T(t) = C e^{+\lambda^2 t} \to \infty$, yang melanggar hukum termodinamika bahwa panas harus meluruh stabil!
        \item \textbf{[C]} Konstanta negatif mempercepat perhitungan determinan.
        \item \textbf{[D]} Nilai positif hanya berlaku untuk gelombang suara.
      \end{itemize}
    \end{alertblock}

    \column{0.46\textwidth}
    \begin{block}{Tantangan Analisis \& Desain (C4--C6)}
      \footnotesize
      \begin{itemize}\setlength{\itemsep}{2pt}
        \item \textbf{C4 (Analisis):} Turunkan fungsi eigen spasial untuk syarat batas terisolasi adiabatic Neumann ($X'(0)=X'(L)=0$).
        \item \textbf{C5 (Evaluasi):} Evaluasi konvergensi deret Fourier solusi transien terhadap kondisi awal tak rata.
        \item \textbf{C6 (Desain):} Rancang panjang busbar gardu induk agar kenaikan suhu akibat arus nominal $3000\text{ A}$ tidak melampaui $90^\circ\text{C}$!
      \end{itemize}
    \end{block}
  \end{columns}
\end{frame}""",

    "ch11.tex": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
\begin{frame}{Kuis Konseptual Interaktif \& Evaluasi Bloom (C1--C6)}
  \begin{columns}[t]
    \column{0.52\textwidth}
    \begin{alertblock}{Peer Instruction: Uji Miskonsepsi Fisik}
      \footnotesize
      \textbf{Kasus Rekayasa:} Saluran transmisi $150\text{ kV}$ memiliki ujung terbuka (*open circuit*, $Z_L \to \infty$). Ketika surja petir $V^+$ menabrak ujung saluran tersebut, tegangan sesaat pada isolator ujung saluran menjadi:
      \vspace{0.05cm}
      \begin{itemize}\setlength{\itemsep}{1pt}
        \item \textbf{[A]} Nol karena arus tidak dapat mengalir ke luar kawat.
        \item \textbf{[B]} **Dua kali lipat** ($2V^+$) akibat pemantulan sefasa penuh ($\Gamma_L = +1$)!
        \item \textbf{[C]} Setengahnya ($V^+/2$) karena pembagian tegangan.
        \item \textbf{[D]} Berkurang drastis terserap ke udara bebas.
      \end{itemize}
    \end{alertblock}

    \column{0.46\textwidth}
    \begin{block}{Tantangan Analisis \& Desain (C4--C6)}
      \footnotesize
      \begin{itemize}\setlength{\itemsep}{2pt}
        \item \textbf{C4 (Analisis):} Susun diagram kisi Bewley untuk melacak pantulan berulang surja pada saluran transmisi terhubung trafo.
        \item \textbf{C5 (Evaluasi):} Evaluasi nilai Voltage Standing Wave Ratio (VSWR) pada ketidakcocokan beban $Z_L \ne Z_0$.
        \item \textbf{C6 (Desain):} Rancang koordinasi isolasi lightning arrester (LA) IEC 60071-1 agar tegangan pantul tidak merusak trafo!
      \end{itemize}
    \end{block}
  \end{columns}
\end{frame}""",

    "ch12.tex": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
\begin{frame}{Kuis Konseptual Interaktif \& Evaluasi Bloom (C1--C6)}
  \begin{columns}[t]
    \column{0.52\textwidth}
    \begin{alertblock}{Peer Instruction: Uji Miskonsepsi Fisik}
      \footnotesize
      \textbf{Kasus Rekayasa:} Mengapa kabel tanah XLPE 20 kV yang ditanam memiliki batas kuat hantar arus (*ampacity*) jauh lebih rendah dibanding kawat ACSR berdiameter sama di udara terbuka?
      \vspace{0.05cm}
      \begin{itemize}\setlength{\itemsep}{1pt}
        \item \textbf{[A]} Tembaga kabel tanah memiliki konduktivitas lebih rendah.
        \item \textbf{[B]} Lapisan isolasi padat polimer XLPE dan timbunan tanah memiliki resistansi termal jauh lebih besar dibanding konveksi udara bebas!
        \item \textbf{[C]} Medan gravitasi bumi menahan aliran arus listrik.
        \item \textbf{[D]} Kabel tanah rentan kehilangan tegangan akibat induksi.
      \end{itemize}
    \end{alertblock}

    \column{0.46\textwidth}
    \begin{block}{Tantangan Analisis \& Desain (C4--C6)}
      \footnotesize
      \begin{itemize}\setlength{\itemsep}{2pt}
        \item \textbf{C4 (Analisis):} Turunkan dekomposisi solusi tunak dan transien pada persamaan difusi panas non-homogen dengan pembangkitan internal.
        \item \textbf{C5 (Evaluasi):} Evaluasi bahaya *thermal runaway* pada isolasi XLPE jika suhu inti melampaui $90^\circ\text{C}$.
        \item \textbf{C6 (Desain):} Rancang kedalaman parit penanaman kabel tanah dan material timbunan pasir termal sesuai IEC 60287!
      \end{itemize}
    \end{block}
  \end{columns}
\end{frame}""",

    "ch13.tex": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
\begin{frame}{Kuis Konseptual Interaktif \& Evaluasi Bloom (C1--C6)}
  \begin{columns}[t]
    \column{0.52\textwidth}
    \begin{alertblock}{Peer Instruction: Uji Miskonsepsi Fisik}
      \footnotesize
      \textbf{Kasus Rekayasa:} Teorema nilai rata-rata Gauss untuk persamaan Laplace $\nabla^2 V = 0$ membuktikan bahwa potensial di setiap titik sama dengan rata-rata sekelilingnya. Konsekuensi fisis pentingnya:
      \vspace{0.05cm}
      \begin{itemize}\setlength{\itemsep}{1pt}
        \item \textbf{[A]} Medan listrik bernilai nol di seluruh titik ruang bebas.
        \item \textbf{[B]} Potensial elektrostatika **tidak pernah memiliki titik ekstremum lokal** (maksimum/minimum selalu terletak di elektroda batas)!
        \item \textbf{[C]} Partikel bermuatan dapat melayang stabil di ruang hampa.
        \item \textbf{[D]} Kapasitansi selalu bernilai konstan independen geometri.
      \end{itemize}
    \end{alertblock}

    \column{0.46\textwidth}
    \begin{block}{Tantangan Analisis \& Desain (C4--C6)}
      \footnotesize
      \begin{itemize}\setlength{\itemsep}{2pt}
        \item \textbf{C4 (Analisis):} Buktikan Teorema Ketunggalan (*Uniqueness Theorem*) solusi persamaan Poisson/Laplace dengan identitas Green.
        \item \textbf{C5 (Evaluasi):} Evaluasi laju konvergensi metode Jacobi vs Gauss-Seidel vs Suksesif Over-Relaksasi (SOR).
        \item \textbf{C6 (Desain):} Rancang geometri cincin korona (*corona ring*) pada isolator 150 kV untuk meratakan gradien medan listrik!
      \end{itemize}
    \end{block}
  \end{columns}
\end{frame}""",

    "ch14.tex": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
\begin{frame}{Kuis Konseptual Interaktif \& Evaluasi Bloom (C1--C6)}
  \begin{columns}[t]
    \column{0.52\textwidth}
    \begin{alertblock}{Peer Instruction: Uji Miskonsepsi Fisik}
      \footnotesize
      \textbf{Kasus Rekayasa:} Pada saluran transmisi daya tinggi PLN, mengapa kabel konduktor dibuat dari aluminium di luar dan baja pejal di inti tengah (kawat ACSR IEC 61089), bukan sebaliknya?
      \vspace{0.05cm}
      \begin{itemize}\setlength{\itemsep}{1pt}
        \item \textbf{[A]} Baja lebih tahan terhadap korosi kimia dibanding aluminium.
        \item \textbf{[B]} Efek kulit mendesak arus AC mengalir di lapisan luar (aluminium konduktif), sehingga inti tengah yang sepi arus diisi baja kuat penahan beban tarikan mekanis!
        \item \textbf{[C]} Aluminium memiliki densitas massa lebih tinggi dari baja.
        \item \textbf{[D]} Baja menghalangi induksi medan petir masuk ke fasa.
      \end{itemize}
    \end{alertblock}

    \column{0.46\textwidth}
    \begin{block}{Tantangan Analisis \& Desain (C4--C6)}
      \footnotesize
      \begin{itemize}\setlength{\itemsep}{2pt}
        \item \textbf{C4 (Analisis):} Hitung frekuensi pancung pandu gelombang silindris berongga melalui akar pertama fungsi Bessel $J_0(\alpha_{0,1}) = 0$.
        \item \textbf{C5 (Evaluasi):} Evaluasi kenaikan resistansi efektif AC terhadap DC ($R_{\text{ac}}/R_{\text{dc}}$) pada frekuensi switching inverter $20\text{ kHz}$.
        \item \textbf{C6 (Desain):} Rancang dimensi rel busbar tubular berongga gardu induk GITET 500 kV menghemat biaya material $40\%$!
      \end{itemize}
    \end{block}
  \end{columns}
\end{frame}"""
}

for fname, new_f14 in f14_content.items():
    with open(fname, "r") as f:
        text = f.read()

    # Pattern matches \begin{frame}{Kuis Evaluasi Taksonomi Bloom Berjenjang (C1--C6)} ... \end{frame}
    patt = re.compile(r"\\begin\{frame\}\{Kuis Evaluasi Taksonomi Bloom Berjenjang \(C1--C6\)\}.*?\\end\{frame\}", re.DOTALL)
    if patt.search(text):
        text = patt.sub(lambda m: new_f14, text, count=1)
        with open(fname, "w") as f:
            f.write(text)
        print(f"Successfully replaced Frame 14 in {fname}")
    else:
        print(f"Pattern not found in {fname}")
