import re

with open("modul_1.tex", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Preamble adjustments
julia_listing_def = r"""% Pengaturan kode Julia
\lstdefinelanguage{Julia}%
  {morekeywords={abstract,break,case,catch,const,continue,do,else,elseif,%
      end,export,false,for,function,global,if,import,%
      let,local,macro,module,mutable,primitive,quote,return,struct,%
      true,try,type,using,var,while},%
   sensitive=true,%
   morecomment=[l]{\#},%
   morecomment=[n]{\#=}{=\#},%
   morestring=[b]',%
   morestring=[b]"%
  }[keywords,comments,strings]

\lstdefinestyle{juliastyle}{
    language=Julia,
    basicstyle=\footnotesize\ttfamily,
    keywordstyle=\color{blue!80!black}\bfseries,
    commentstyle=\color{green!50!black}\itshape,
    stringstyle=\color{red!80!black},
    numbers=left,
    numberstyle=\tiny\color{gray},
    breaklines=true,
    showstringspaces=false,
    frame=single,
    backgroundcolor=\color{gray!6},
    captionpos=b,
    xleftmargin=10pt,
    tabsize=4
}"""

text = text.replace(r"""\fancyhead[L]{\textbf{Persamaan Diferensial 2026} -- Teknik Elektro Universitas Bengkulu}
\fancyhead[R]{Modul Ajar Minggu 1: Pengantar \& Klasifikasi PD}""",
r"""\fancyhead[L]{\small\textbf{Persamaan Diferensial 2026} -- Teknik Elektro UNIB}
\fancyhead[R]{\small Modul 1: Pengantar \& Klasifikasi PD}""")

# Replace octave style with julia style in preamble
octave_preamble_pattern = r"% Pengaturan kode GNU Octave[\s\S]*?\\captionpos=b\s*\}"
text = re.sub(octave_preamble_pattern, lambda m: julia_listing_def, text)

# Title
text = text.replace(
    r"\textbf{\LARGE PENGANTAR PERSAMAAN DIFERENSIAL: KLASIFIKASI PDB/PDP, MASALAH NILAI AWAL (IVP), FISIKA DINAMIKA ENERGI RANGKAIAN ELEKTRIK \& KOMPUTASI GNU OCTAVE}}",
    r"\textbf{\LARGE PENGANTAR PERSAMAAN DIFERENSIAL: KLASIFIKASI PDB/PDP, MASALAH NILAI AWAL (IVP), FISIKA DINAMIKA ENERGI RANGKAIAN ELEKTRIK \& KOMPUTASI NUMERIK BERBASIS JULIA}}"
)

# Sub-CPMK C6
text = text.replace(
    r"\item \textbf{C6 (Menciptakan/Komputasi):} Mengembangkan skrip modular berbasis \textbf{GNU Octave} untuk mensimulasikan respon transien arus pengisian induktor, memvalidasi solusi eksak analitik terhadap solusi numerik integrasi Runge-Kutta (\texttt{ode45}), serta memvisualisasikan medan arah (\textit{slope field}).",
    r"\item \textbf{C6 (Menciptakan/Komputasi):} Mengembangkan skrip modular berbasis bahasa pemrograman ilmiah \textbf{Julia} (menggunakan pustaka \texttt{DifferentialEquations.jl} dan pemecah adaptif \texttt{Tsit5()}) untuk mensimulasikan respon transien arus pengisian induktor, memvalidasi solusi eksak analitik terhadap solusi numerik, serta memvisualisasikan kurva dinamika sistem."
)

# Gambar 1 (Peta Jalan)
fig1_pattern = r"\\begin\{figure\}\[htbp\]\s*\\centering\s*\\resizebox\{.*?\}\{.*?\}\s*\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}%?\s*\}\s*\\caption\{Peta jalan kurikulum perkuliahan Persamaan Diferensial Teknik Elektro 2026\.\}\s*\\label\{fig:peta_jalan_pd\}\s*\\end\{figure\}"

fig1_new = r"""\begin{figure}[htbp]
\centering
\resizebox{\linewidth}{!}{%
\begin{tikzpicture}[
    node distance=0.85cm and 0.45cm,
    block/.style={rectangle, draw=headercolor, fill=blue!8, thick, rounded corners=3pt, align=center, text width=3.35cm, minimum height=1.05cm, font=\scriptsize},
    highlight/.style={rectangle, draw=red!80!black, fill=red!15, very thick, rounded corners=3pt, align=center, text width=3.35cm, minimum height=1.05cm, font=\scriptsize\bfseries},
    midblock/.style={rectangle, draw=orange!80!black, fill=orange!15, thick, rounded corners=3pt, align=center, text width=3.35cm, minimum height=1.05cm, font=\scriptsize\bfseries},
    arrow/.style={->, >=stealth, line width=1.1pt, headercolor}
]
    % Paruh 1: PDB & Rangkaian Listrik
    \node[highlight] (w1) {Minggu 1: Klasifikasi PD, IVP\\\& Pemodelan Fisis RL};
    \node[block, right=of w1] (w2) {Minggu 2: PDB Orde 1\\(Separabel \& Faktor Integrasi)};
    \node[block, right=of w2] (w3) {Minggu 3: Aplikasi Rekayasa\\(Transien RC, RL, Termal)};
    \node[block, right=of w3] (w4) {Minggu 4: PDB Orde 2 Homogen\\(Wronskian \& Tangki LC)};
    
    \node[block, below=of w4] (w5) {Minggu 5: PDB Orde 2 Non-Homogen\\\& Transien RLC Seri AC};
    \node[block, left=of w5] (w6) {Minggu 6: Transformasi Laplace\\Dasar \& Teorema Geser};
    \node[block, left=of w6] (w7) {Minggu 7: Invers Laplace \&\\Solusi PDB Domain $s$};
    \node[midblock, left=of w7] (w8) {Minggu 8: Evaluasi Capaian\\Ujian Tengah Semester (UTS)};
    
    % Paruh 2: PDP & Medan Elektromagnetika
    \node[block, below=of w8] (w9) {Minggu 9: Pengantar PDP \&\\Analisis Deret Fourier};
    \node[block, right=of w9] (w10) {Minggu 10: Solusi PDP Metode\\Pemisahan Variabel};
    \node[block, right=of w10] (w11) {Minggu 11: Persamaan Gelombang\\1D (Telegrafer Transmisi)};
    \node[block, right=of w11] (w12) {Minggu 12: Persamaan Panas 1D\\\& Manajemen Termal Kabel};
    
    \node[block, below=of w12] (w13) {Minggu 13: Persamaan Laplace 2D\\Potensial Elektrostatik};
    \node[block, left=of w13] (w14) {Minggu 14: Fungsi Bessel \&\\Efek Kulit (\textit{Skin Effect})};
    \node[block, left=of w14] (w15) {Minggu 15: 4 Persamaan Maxwell\\Diferensial \& Sintesis PDP};
    \node[midblock, left=of w15] (w16) {Minggu 16: Evaluasi Akhir\\Ujian Akhir Semester (UAS)};
    
    \draw[arrow] (w1) -- (w2);
    \draw[arrow] (w2) -- (w3);
    \draw[arrow] (w3) -- (w4);
    \draw[arrow] (w4) -- (w5);
    \draw[arrow] (w5) -- (w6);
    \draw[arrow] (w6) -- (w7);
    \draw[arrow] (w7) -- (w8);
    \draw[arrow] (w8) -- (w9);
    \draw[arrow] (w9) -- (w10);
    \draw[arrow] (w10) -- (w11);
    \draw[arrow] (w11) -- (w12);
    \draw[arrow] (w12) -- (w13);
    \draw[arrow] (w13) -- (w14);
    \draw[arrow] (w14) -- (w15);
    \draw[arrow] (w15) -- (w16);
\end{tikzpicture}%
}
\caption{Peta jalan kurikulum perkuliahan Persamaan Diferensial Teknik Elektro 2026.}
\label{fig:peta_jalan_pd}
\end{figure}"""

text = re.sub(fig1_pattern, lambda m: fig1_new, text)

# Section overfull headers
text = text.replace(
    r"\section{Pendahuluan \& Filosofi Dinamika Sistem dalam Rekayasa Elektro}",
    r"\section{Pendahuluan \& Filosofi Dinamika dalam Rekayasa Elektro}"
)
text = text.replace(
    r"\section{Praktikum Komputasi Matematika Terbuka dengan GNU Octave}",
    r"\section{Praktikum Komputasi Terbuka Berbasis Julia}"
)
text = text.replace(
    r"\section{Contoh Soal Terhitung Langkah demi Langkah (*Worked Numerical Examples*)}",
    r"\section{Contoh Soal Terhitung Langkah demi Langkah (\textit{Worked Numerical Examples})}"
)

# Heading math tokens
text = text.replace(
    r"\subsection{Prinsip Fisika Kontinuitas Energi: Mengapa $i_L(0^-) = i_L(0^+)$ dan $v_C(0^-) = v_C(0^+)$?}",
    r"\subsection{Prinsip Fisika Kontinuitas Energi: Mengapa \texorpdfstring{$i_L(0^-) = i_L(0^+)$ dan $v_C(0^-) = v_C(0^+)$}{i_L(0-) = i_L(0+) dan v_C(0-) = v_C(0+)}?}"
)
text = text.replace(
    r"\subsection{Dinamika Transien: Evaluasi Berbasis Kelipatan Konstanta Waktu $\tau$}",
    r"\subsection{Dinamika Transien: Evaluasi Berbasis Kelipatan Konstanta Waktu \texorpdfstring{$\tau$}{tau}}"
)

# Section 9: Julia script and description
julia_section = r"""\section{Praktikum Komputasi Terbuka Berbasis Julia}

Dalam dunia komputasi sains dan rekayasa modern, bahasa pemrograman \textbf{Julia} telah menjadi standar baru karena memecahkan masalah \textit{two-language problem} (menawarkan sintaks ekspresif semudah Python/MATLAB namun berkecepatan tinggi setara C/Fortran). Khusus untuk pemodelan persamaan diferensial, ekosistem \texttt{DifferentialEquations.jl} diakui secara internasional sebagai salah satu paket pemecah persamaan diferensial tercepat dan paling komprehensif di dunia ilmiah.

Untuk memverifikasi solusi analitik dan mengamati dinamika transien secara visual, mahasiswa wajib menjalankan skrip modular berbasis \textbf{Julia} berikut.

\begin{lstlisting}[style=juliastyle, caption={Skrip Julia: Simulasi Transien Rangkaian RL dan Verifikasi Numerik Menggunakan DifferentialEquations.jl.}]
# =========================================================================
# MODUL AJAR PERSAMAAN DIFERENSIAL - JURUSAN TEKNIK ELEKTRO UNIB
# Praktikum Minggu 1: Respon Transien Rangkaian RL (Analitik vs Numerik)
# Dosen: Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.
# Bahasa Pemrograman: Julia 1.12+ (DifferentialEquations.jl & Plots.jl)
# =========================================================================

using DifferentialEquations
using Plots

# 1. Parameter Fisik Sistem Rangkaian RL
const V0  = 125.0       # Tegangan Sumber DC [Volt]
const R   = 2.5         # Resistansi Kumparan [Ohm]
const L   = 0.050       # Induktansi Kumparan [Henry]
const tau = L / R       # Konstanta Waktu [detik] (20 ms)
const Iss = V0 / R      # Arus Keadaan Mantap [Ampere] (50 A)

println("="^65)
println("  SIMULASI TRANSIEN RANGKAIAN RL BERBASIS JULIA")
println("="^65)
println("Tegangan Sumber (V0)   : $V0 Volt")
println("Resistansi Kumparan (R): $R Ohm")
println("Induktansi (L)         : $L Henry")
println("Konstanta Waktu (tau)  : $tau detik ($(tau*1000) ms)")
println("Arus Mantap (Iss)      : $Iss Ampere")
println("-"^65)

# 2. Formulasi Masalah Nilai Awal (IVP) untuk DifferentialEquations.jl
# Bentuk PDB eksplisit: di/dt = f(i, p, t) = (V0 - R*i) / L
function rl_ode!(di, i, p, t)
    V0_val, R_val, L_val = p
    di[1] = (V0_val - R_val * i[1]) / L_val
end

# Parameter sistem, Kondisi Awal i(0) = 0 A, dan Rentang Waktu (0 s.d. 6 tau)
p = (V0, R, L)
i0 = [0.0]
tspan = (0.0, 6.0 * tau)

# Definisi ODEProblem dan Penyelesaian dengan Algoritma Tsit5 (Tsitouras 5/4)
prob = ODEProblem(rl_ode!, i0, tspan, p)
sol = solve(prob, Tsit5(), reltol=1e-8, abstol=1e-8)

# 3. Solusi Eksak Analitik & Evaluasi Presisi Numerik
t_eval = range(0.0, 6.0 * tau, length=500)
i_exact = [Iss * (1.0 - exp(-t / tau)) for t in t_eval]
v_induktor = [V0 * exp(-t / tau) for t in t_eval]

# Interpolasi solusi numerik pada grid evaluasi
i_num = [sol(t)[1] for t in t_eval]
error_abs = abs.(i_exact .- i_num)
max_error = maximum(error_abs)
println("Maksimum Error Mutlak Numerik vs Analitik: $max_error Ampere")
println("-"^65)

# 4. Visualisasi Grafik Resolusi Tinggi
p1 = plot(t_eval .* 1000, i_exact, label="Solusi Analitik Eksak",
          lw=2.5, color=:blue, legend=:bottomright)
scatter!(p1, sol.t .* 1000, [u[1] for u in sol.u],
         label="Simulasi Tsit5() Numerik", ms=3.5, color=:red, shape=:circle)
hline!(p1, [Iss], label="Keadaan Mantap (Iss = 50 A)",
       ls=:dash, lw=1.2, color=:black)
vline!(p1, [tau * 1000], label="1 tau = 20 ms (63.2%)",
       ls=:dash, lw=1.2, color=:green)
vline!(p1, [5 * tau * 1000], label="5 tau = 100 ms (99.3%)",
       ls=:dash, lw=1.2, color=:purple)
plot!(p1, title="Respon Transien Pengisian Arus Induktor: i(t) vs Waktu",
      xlabel="Waktu (milidetik)", ylabel="Arus Induktor i(t) [Ampere]", grid=true)

p2 = plot(t_eval .* 1000, v_induktor, label="Tegangan Induktor v_L(t)",
          lw=2.0, color=:red, legend=:topright)
plot!(p2, t_eval .* 1000, (i_exact.^2 .* R) ./ 1000,
      label="Disipasi Daya Resistor [kW]", lw=2.0, color=:darkgreen)
plot!(p2, title="Tegangan Induktor dan Disipasi Daya Termal",
      xlabel="Waktu (milidetik)", ylabel="Tegangan [V] / Daya [kW]", grid=true)

final_plot = plot(p1, p2, layout=(2, 1), size=(850, 650))
savefig(final_plot, "simulasi_transien_rl_julia.png")
println("Simulasi Julia selesai! Grafik disimpan sebagai 'simulasi_transien_rl_julia.png'.")
\end{lstlisting}"""

octave_section_pattern = r"\\section\{Praktikum Komputasi.*?\}[\s\S]*?\\end\{lstlisting\}"
text = re.sub(octave_section_pattern, lambda m: julia_section, text)

# Bloom C6 question
text = text.replace(
    r"Rancanglah suatu fungsi skrip di **GNU Octave** bernama \texttt{simulasi\_transien\_rc(R, C, V0)} yang secara otomatis menerima input parameter $R, C, V_0$, menghitung konstanta waktu $\tau$, menyelesaikan IVP pengisian kapasitor dengan integrasi numerik, dan memplot kurva tegangan $v_C(t)$ serta arus pengisian $i(t)$ lengkap dengan garis penanda $1\tau$ hingga $5\tau$!",
    r"Rancanglah suatu fungsi skrip di bahasa pemrograman \textbf{Julia} bernama \texttt{simulasi_transien_rc(R, C, V0)} yang secara otomatis menerima parameter $R, C, V_0$, mendefinisikan \texttt{ODEProblem} untuk pengisian kapasitor transien RC, menyelesaikan IVP menggunakan algoritma \texttt{Tsit5()}, dan memplot kurva tegangan $v_C(t)$ serta arus pengisian $i(t)$ lengkap dengan garis penanda $1\tau$ hingga $5\tau$!"
)

# Clean Markdown markers outside listings
lines = text.splitlines()
cleaned_lines = []
in_listing = False

for line in lines:
    stripped = line.strip()
    if r"\begin{lstlisting}" in line:
        in_listing = True
    elif r"\end{lstlisting}" in line:
        in_listing = False
        cleaned_lines.append(line)
        continue

    if in_listing:
        cleaned_lines.append(line)
        continue

    if stripped == "---":
        continue

    # Replace **bold** with \textbf{bold}
    line = re.sub(r"\*\*([^\*]+?)\*\*", r"\\textbf{\1}", line)
    # Specific italics
    line = line.replace("(*Skin Effect*)", r"(\textit{Skin Effect})")
    line = line.replace("*first-principles*", r"\textit{first-principles}")
    line = line.replace("(*relay 87T*)", r"(\textit{relay 87T})")
    line = line.replace("(*nuisance tripping*)", r"(\textit{nuisance tripping})")
    line = line.replace("(*energized*)", r"(\textit{energized})")
    line = line.replace("(*Circuit Breaker*)", r"(\textit{Circuit Breaker})")
    line = line.replace("(*steady state*)", r"(\textit{steady state})")

    cleaned_lines.append(line)

new_text = "\n".join(cleaned_lines)

with open("modul_1.tex", "w", encoding="utf-8") as f:
    f.write(new_text)

print("Successfully transformed modul_1.tex with Julia and zero overflow!")
