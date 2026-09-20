import os
import re

updates = {
    "ch2.tex": {
        "f13": r"""% FRAME 13: Praktikum Komputasi Julia
\begin{frame}[fragile]{Praktikum Komputasi Julia: Transien Sirkuit RC}
  \begin{columns}[t]
    \column{0.50\textwidth}
    \begin{block}{Skrip Julia (\texttt{DifferentialEquations.jl})}
\begin{lstlisting}[style=juliastyle]
using DifferentialEquations, Plots

const V0, R, C = 250.0, 50.0, 200e-6
tau = R * C; v0 = 50.0

f_rc(v, p, t) = (V0 - v) / (R * C)
prob = ODEProblem(f_rc, v0, (0.0, 0.06))
sol = solve(prob, Tsit5())

t_vec = 0.0:0.001:0.06
v_an = @. V0 - (V0 - v0) * exp(-t_vec / tau)
plot(sol, label="Tsit5", lw=2, color=:blue)
plot!(t_vec, v_an, label="Eksak", ls=:dash, color=:red)
\end{lstlisting}
    \end{block}

    \column{0.48\textwidth}
    \begin{alertblock}{Visualisasi Respon Transien}
      \centering
      \includegraphics[width=\linewidth, height=0.38\textheight, keepaspectratio]{figures/slides/plot_ch2.png}
    \end{alertblock}
    \vspace{-0.1cm}
    \begin{exampleblock}{Intisari Dinamika Transien}
      \tiny
      Tegangan naik asimtotik ke $250\text{ V}$. Pada $t = \tau = 10\text{ ms}$, tegangan mencapai $63{,}2\%$ rentang transien ($176{,}4\text{ V}$). Arus melonjak $4\text{ A}$ lalu meluruh ke nol.
    \end{exampleblock}
  \end{columns}
\end{frame}""",
        "f14": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
\begin{frame}{Kuis Konseptual Interaktif \& Evaluasi Bloom (C1--C6)}
  \begin{columns}[t]
    \column{0.52\textwidth}
    \begin{alertblock}{Peer Instruction: Uji Miskonsepsi Fisik}
      \footnotesize
      \textbf{Kasus Rekayasa:} Kapasitor $C$ diisi dari $0\text{ V}$ hingga $V_0$ via resistor $R$. Jika nilai $R$ diperkecil menjadi setengahnya ($R/2$), energi yang terdisipasi pada resistor ($E_R$) akan:
      \vspace{0.05cm}
      \begin{itemize}\setlength{\itemsep}{1pt}
        \item \textbf{[A]} Menjadi setengahnya karena arus lebih cepat berhenti.
        \item \textbf{[B]} Menjadi dua kali lipat karena arus awal lebih besar.
        \item \textbf{[C]} \textbf{Tetap sama} ($\frac{1}{2} C V_0^2$), tidak bergantung nilai $R$!
        \item \textbf{[D]} Menjadi nol karena resistansi mendekati konduktor ideal.
      \end{itemize}
    \end{alertblock}

    \column{0.46\textwidth}
    \begin{block}{Tantangan Analisis \& Desain (C4--C6)}
      \footnotesize
      \begin{itemize}\setlength{\itemsep}{2pt}
        \item \textbf{C4 (Analisis):} Buktikan daya disipasi puncak resistor terjadi pada $t=0^+$ sebesar $P_{\text{max}} = V_0^2/R$.
        \item \textbf{C5 (Evaluasi):} Evaluasi mengapa efisiensi pengisian kapasitor selalu tepat $50\%$ pada sumber konstan.
        \item \textbf{C6 (Desain):} Rancang snubber $R_s - C_s$ membatasi $dv/dt \le 500\text{ V}/\mu\text{s}$ pada IGBT $25\text{ A}$!
      \end{itemize}
    \end{block}
  \end{columns}
\end{frame}"""
    },

    "ch3.tex": {
        "f13": r"""% FRAME 13: Praktikum Komputasi Julia
\begin{frame}[fragile]{Praktikum Komputasi Julia: Dinamika Termal Trafo}
  \begin{columns}[t]
    \column{0.50\textwidth}
    \begin{block}{Skrip Julia (\texttt{DifferentialEquations.jl})}
\begin{lstlisting}[style=juliastyle]
using DifferentialEquations, Plots

const theta_amb = 30.0
tau_oil, tau_w = 3.0, 0.15 # jam
d_to, d_h = 45.0, 25.0

f_thermal(u, p, t) = [
  (theta_amb + d_to - u[1]) / tau_oil,
  (u[1] + d_h - u[2]) / tau_w
]
prob = ODEProblem(f_thermal, [30.0, 30.0], (0.0, 10.0))
sol = solve(prob, Tsit5())
\end{lstlisting}
    \end{block}

    \column{0.48\textwidth}
    \begin{alertblock}{Visualisasi Termal IEEE C57.91}
      \centering
      \includegraphics[width=\linewidth, height=0.38\textheight, keepaspectratio]{figures/slides/plot_ch3.png}
    \end{alertblock}
    \vspace{-0.1cm}
    \begin{exampleblock}{Intisari Dinamika Termal}
      \tiny
      Hotspot kawat winding $\theta_h$ melonjak cepat ($\tau_w = 9\text{ menit}$), sedangkan minyak atas $\theta_{to}$ naik lambat ($\tau_{\text{oil}} = 3\text{ jam}$). Batas aman $110^\circ\text{C}$ wajib dipantau relai.
    \end{exampleblock}
  \end{columns}
\end{frame}""",
        "f14": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
\begin{frame}{Kuis Konseptual Interaktif \& Evaluasi Bloom (C1--C6)}
  \begin{columns}[t]
    \column{0.52\textwidth}
    \begin{alertblock}{Peer Instruction: Uji Miskonsepsi Fisik}
      \footnotesize
      \textbf{Kasus Rekayasa:} Trafo 60 MVA dibebani lebih mendadak $150\%$. Mengapa temperatur minyak atas lambat naik sedangkan hotspot kawat tembaga langsung melonjak dalam hitungan menit?
      \vspace{0.05cm}
      \begin{itemize}\setlength{\itemsep}{1pt}
        \item \textbf{[A]} Viskositas minyak isolasi trafo sangat tinggi.
        \item \textbf{[B]} Kapasitas kalor massa minyak puluhan ton sangat masif ($\tau_{\text{oil}} \gg \tau_w$), sedangkan massa kawat kecil!
        \item \textbf{[C]} Sirkulasi minyak terhenti saat beban lebih.
        \item \textbf{[D]} Resistansi tembaga menyusut saat dipanaskan.
      \end{itemize}
    \end{alertblock}

    \column{0.46\textwidth}
    \begin{block}{Tantangan Analisis \& Desain (C4--C6)}
      \footnotesize
      \begin{itemize}\setlength{\itemsep}{2pt}
        \item \textbf{C4 (Analisis):} Hitung laju degradasi isolasi selulosa kertas jika suhu hotspot bertahan pada $120^\circ\text{C}$.
        \item \textbf{C5 (Evaluasi):} Evaluasi efektivitas dioda freewheeling meredam inductive kickback relay PMT.
        \item \textbf{C6 (Desain):} Rancang tunda waktu relai termal 49 agar trafo trip sebelum hotspot menyentuh $140^\circ\text{C}$!
      \end{itemize}
    \end{block}
  \end{columns}
\end{frame}"""
    },

    "ch4.tex": {
        "f13": r"""% FRAME 13: Praktikum Komputasi Julia
\begin{frame}[fragile]{Praktikum Komputasi Julia: Tiga Ragam Redaman RLC}
  \begin{columns}[t]
    \column{0.50\textwidth}
    \begin{block}{Skrip Julia (\texttt{DifferentialEquations.jl})}
\begin{lstlisting}[style=juliastyle]
using DifferentialEquations, Plots

function rlc_system!(du, u, p, t)
  zeta, omega0 = p
  du[1] = u[2]
  du[2] = -2*zeta*omega0*u[2] - omega0^2*u[1]
end

u0 = [1.0, 0.0]; tspan = (0.0, 0.05)
# Selesaikan untuk zeta = 0.2, 1.0, 2.5
prob_under = ODEProblem(rlc_system!, u0, tspan, [0.2, 500.0])
sol_under = solve(prob_under, Tsit5())
\end{lstlisting}
    \end{block}

    \column{0.48\textwidth}
    \begin{alertblock}{Visualisasi 3 Ragam Redaman}
      \centering
      \includegraphics[width=\linewidth, height=0.38\textheight, keepaspectratio]{figures/slides/plot_ch4.png}
    \end{alertblock}
    \vspace{-0.1cm}
    \begin{exampleblock}{Intisari Dinamika Orde 2}
      \tiny
      Underdamped ($\zeta < 1$) berosilasi pada $\omega_d$; Critically damped ($\zeta = 1$) paling lekas tunak tanpa overshoot; Overdamped ($\zeta > 1$) lambat akibat disipasi resistor dominan.
    \end{exampleblock}
  \end{columns}
\end{frame}""",
        "f14": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
\begin{frame}{Kuis Konseptual Interaktif \& Evaluasi Bloom (C1--C6)}
  \begin{columns}[t]
    \column{0.52\textwidth}
    \begin{alertblock}{Peer Instruction: Uji Miskonsepsi Fisik}
      \footnotesize
      \textbf{Kasus Rekayasa:} Mengapa pada aktuator penutup pemutus tenaga (PMT) gardu induk dan jarum ukur analog selalu dirancang tepat pada kondisi **redaman kritis** ($\zeta = 1$)?
      \vspace{0.05cm}
      \begin{itemize}\setlength{\itemsep}{1pt}
        \item \textbf{[A]} Mengurangi konsumsi daya listrik rangkaian baterai.
        \item \textbf{[B]} Mencapai posisi tunak dalam waktu tersingkat tanpa mengalami pantulan/osilasi (*overshoot*)!
        \item \textbf{[C]} Menghasilkan tegangan transien paling besar.
        \item \textbf{[D]} Mencegah panas pada kumparan elektromagnet.
      \end{itemize}
    \end{alertblock}

    \column{0.46\textwidth}
    \begin{block}{Tantangan Analisis \& Desain (C4--C6)}
      \footnotesize
      \begin{itemize}\setlength{\itemsep}{2pt}
        \item \textbf{C4 (Analisis):} Buktikan Wronskian $W(y_1, y_2)(0) \ne 0$ menjamin kebebasan linier solusi basis.
        \item \textbf{C5 (Evaluasi):} Evaluasi redaman osilasi tangki LC tanpa resistor akibat rugi radiasi gelombang EM.
        \item \textbf{C6 (Desain):} Rancang parameter $R$ rangkaian peredam RLC seri agar frekuensi osilasi $\omega_d = 314\text{ rad/s}$!
      \end{itemize}
    \end{block}
  \end{columns}
\end{frame}"""
    },

    "ch5.tex": {
        "f13": r"""% FRAME 13: Praktikum Komputasi Julia
\begin{frame}[fragile]{Praktikum Komputasi Julia: Resonansi RLC \& Selektivitas}
  \begin{columns}[t]
    \column{0.50\textwidth}
    \begin{block}{Skrip Julia: Kurva Respon Frekuensi}
\begin{lstlisting}[style=juliastyle]
using Plots

w_w0 = range(0.5, 1.5, length=300)
H(w_ratio, Q) = 1.0 ./ sqrt.(1.0 .+ Q^2 .* (w_ratio .- 1.0 ./ w_ratio).^2)

plot(w_w0, H.(w_w0, 2), label="Q = 2", lw=2)
plot!(w_w0, H.(w_w0, 5), label="Q = 5", lw=2)
plot!(w_w0, H.(w_w0, 10), label="Q = 10", lw=2)
vline!([1.0], ls=:dash, label="Resonansi")
\end{lstlisting}
    \end{block}

    \column{0.48\textwidth}
    \begin{alertblock}{Visualisasi Resonansi \& $Q$}
      \centering
      \includegraphics[width=\linewidth, height=0.38\textheight, keepaspectratio]{figures/slides/plot_ch5.png}
    \end{alertblock}
    \vspace{-0.1cm}
    \begin{exampleblock}{Intisari Resonansi}
      \tiny
      Saat $\omega = \omega_0$, reaktansi $X_L = X_C$, impedansi minimum $Z = R$. Nilai $Q$ tinggi mempertajam selektivitas kurva, namun memperbesar tegangan jatuh pada $L$ dan $C$ ($V_C = Q V_s$).
    \end{exampleblock}
  \end{columns}
\end{frame}""",
        "f14": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
\begin{frame}{Kuis Konseptual Interaktif \& Evaluasi Bloom (C1--C6)}
  \begin{columns}[t]
    \column{0.52\textwidth}
    \begin{alertblock}{Peer Instruction: Uji Miskonsepsi Fisik}
      \footnotesize
      \textbf{Kasus Rekayasa:} RLC seri AC mengalami resonansi seri ($Q = 10$). Voltmeter mengukur tegangan kapasitor $V_C = 1000\text{ V}$ padahal sumber $V_s$ hanya $100\text{ V}$. Apakah ini melanggar hukum energi?
      \vspace{0.05cm}
      \begin{itemize}\setlength{\itemsep}{1pt}
        \item \textbf{[A]} Ya, tegangan komponen tidak boleh melebihi sumber.
        \item \textbf{[B]} **Tidak**, karena $V_C$ dan $V_L$ berbeda fasa $180^\circ$ sehingga saling meniadakan secara vektor total ($V_C + V_L = 0$)!
        \item \textbf{[C]} Ya, terjadi pembangkitan daya aktif tambahan.
        \item \textbf{[D]} Tidak, asalkan frekuensi sumber di atas $1\text{ kHz}$.
      \end{itemize}
    \end{alertblock}

    \column{0.46\textwidth}
    \begin{block}{Tantangan Analisis \& Desain (C4--C6)}
      \footnotesize
      \begin{itemize}\setlength{\itemsep}{2pt}
        \item \textbf{C4 (Analisis):} Analisis risiko Sub-Synchronous Resonance (SSR) pada poros turbin generator akibat kompensasi kapasitor seri.
        \item \textbf{C5 (Evaluasi):} Evaluasi bandwidth $-3\text{ dB}$ filter bandpass untuk menyaring harmonisa ke-5 PLN.
        \item \textbf{C6 (Desain):} Rancang parameter filter pasif RLC seri dengan $f_0 = 250\text{ Hz}$ dan $Q = 15$!
      \end{itemize}
    \end{block}
  \end{columns}
\end{frame}"""
    },

    "ch6.tex": {
        "f13": r"""% FRAME 13: Praktikum Komputasi Julia
\begin{frame}[fragile]{Praktikum Komputasi Julia: Surja Petir IEC 60060-1}
  \begin{columns}[t]
    \column{0.50\textwidth}
    \begin{block}{Skrip Julia: Gelombang Impuls Surja}
\begin{lstlisting}[style=juliastyle]
using Plots

t_us = range(0, 100, length=400)
alpha, beta = 0.0146e6, 2.467e6
V0 = 1.037

v_surge = @. V0 * (exp(-alpha * t_us * 1e-6) - exp(-beta * t_us * 1e-6))
plot(t_us, v_surge, lw=2, color=:red, label="1.2/50 us")
scatter!([1.2], [1.0], color=:blue, label="Puncak tp")
scatter!([50.0], [0.5], color=:green, label="Ekor t2")
\end{lstlisting}
    \end{block}

    \column{0.48\textwidth}
    \begin{alertblock}{Visualisasi Surja Petir Standar}
      \centering
      \includegraphics[width=\linewidth, height=0.38\textheight, keepaspectratio]{figures/slides/plot_ch6.png}
    \end{alertblock}
    \vspace{-0.1cm}
    \begin{exampleblock}{Intisari Gelombang Surja}
      \tiny
      Gelombang mencapai puncak dalam $1{,}2\,\mu\text{s}$ (laju kenaikan tinggi) dan meluruh ke $50\%$ pada $50\,\mu\text{s}$. Transformasi Laplace memungkinkan perhitungan respon isolator trafo secara eksak.
    \end{exampleblock}
  \end{columns}
\end{frame}""",
        "f14": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
\begin{frame}{Kuis Konseptual Interaktif \& Evaluasi Bloom (C1--C6)}
  \begin{columns}[t]
    \column{0.52\textwidth}
    \begin{alertblock}{Peer Instruction: Uji Miskonsepsi Fisik}
      \footnotesize
      \textbf{Kasus Rekayasa:} Mengapa metode Transformasi Laplace $\mathcal{L}\{\cdot\}$ jauh lebih unggul daripada metode PDB klasik untuk menganalisis surja switching gardu induk?
      \vspace{0.05cm}
      \begin{itemize}\setlength{\itemsep}{1pt}
        \item \textbf{[A]} Laplace tidak memerlukan hukum tegangan Kirchhoff.
        \item \textbf{[B]} Laplace mengubah fungsi diskontinu (Heaviside/Dirac) dan turunan menjadi aljabar rasional domain-$s$ dengan kondisi awal otomatis!
        \item \textbf{[C]} Laplace hanya berlaku jika frekuensi bernilai nol.
        \item \textbf{[D]} Laplace meniadakan kebutuhan nilai induktansi.
      \end{itemize}
    \end{alertblock}

    \column{0.46\textwidth}
    \begin{block}{Tantangan Analisis \& Desain (C4--C6)}
      \footnotesize
      \begin{itemize}\setlength{\itemsep}{2pt}
        \item \textbf{C4 (Analisis):} Tentukan tegangan transien saat petir menyambar saluran dengan teorema geser waktu $e^{-as}$.
        \item \textbf{C5 (Evaluasi):} Buktikan Teorema Nilai Akhir $\lim_{t \to \infty} f(t) = \lim_{s \to 0} sF(s)$ pada transfer fungsi stabil.
        \item \textbf{C6 (Desain):} Rancang rangkaian pembentuk surja Marx Generator laboratorium uji tegangan tinggi!
      \end{itemize}
    \end{block}
  \end{columns}
\end{frame}"""
    },

    "ch7.tex": {
        "f13": r"""% FRAME 13: Praktikum Komputasi Julia
\begin{frame}[fragile]{Praktikum Komputasi Julia: Transient Recovery Voltage}
  \begin{columns}[t]
    \column{0.50\textwidth}
    \begin{block}{Skrip Julia: Respon TRV IEC 62271-100}
\begin{lstlisting}[style=juliastyle]
using Plots

t_ms = range(0, 2.0, length=400)
fn_trv = 2000.0 # 2 kHz osilasi
v_trv = @. 1.0 - exp(-t_ms / 0.8) * cos(2 * pi * fn_trv * t_ms * 1e-3)

plot(t_ms, v_trv, lw=2, color=:red, label="TRV PMT")
hline!([1.0], ls=:dash, color=:blue, label="Tegangan 1 pu")
hline!([1.85], ls=:dot, color=:black, label="Puncak TRV")
\end{lstlisting}
    \end{block}

    \column{0.48\textwidth}
    \begin{alertblock}{Visualisasi TRV Pemutus Tenaga}
      \centering
      \includegraphics[width=\linewidth, height=0.38\textheight, keepaspectratio]{figures/slides/plot_ch7.png}
    \end{alertblock}
    \vspace{-0.1cm}
    \begin{exampleblock}{Intisari Fisika TRV}
      \tiny
      Pasca pemutusan arus hubung singkat, tegangan pemulihan berosilasi pada frekuensi natural kawat ($2\text{ kHz}$) dan mencapai puncak hingga $1{,}85\text{ pu}$, menantang ketahanan dielektrik gas $\text{SF}_6$.
    \end{exampleblock}
  \end{columns}
\end{frame}""",
        "f14": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
\begin{frame}{Kuis Konseptual Interaktif \& Evaluasi Bloom (C1--C6)}
  \begin{columns}[t]
    \column{0.52\textwidth}
    \begin{alertblock}{Peer Instruction: Uji Miskonsepsi Fisik}
      \footnotesize
      \textbf{Kasus Rekayasa:} Mengapa momen paling berbahaya pada pemutusan arus hubung singkat oleh PMT justru terjadi beberapa mikrodetik **setelah** kontak pemutus terbuka dan busur padam?
      \vspace{0.05cm}
      \begin{itemize}\setlength{\itemsep}{1pt}
        \item \textbf{[A]} Arus listrik membalik arah kembali ke alternator.
        \item \textbf{[B]} Laju kenaikan tegangan TRV ($dv/dt$) sangat curam; jika melampaui dielektrik celah gas $\text{SF}_6$, akan terjadi *re-strike* (busur api menyala ulang)!
        \item \textbf{[C]} Trafo arus (CT) meledak akibat saturasi inti.
        \item \textbf{[D]} Energi listrik musnah secara seketika.
      \end{itemize}
    \end{alertblock}

    \column{0.46\textwidth}
    \begin{block}{Tantangan Analisis \& Desain (C4--C6)}
      \footnotesize
      \begin{itemize}\setlength{\itemsep}{2pt}
        \item \textbf{C4 (Analisis):} Uraikan respon transien sistem menjadi komponen Masukan Nol (ZIR) dan Status Nol (ZSR).
        \item \textbf{C5 (Evaluasi):} Evaluasi akar kompleks konjugat pada bidang-$s$ terhadap stabilitas sistem proteksi.
        \item \textbf{C6 (Desain):} Rancang nilai kapasitor paralel peredam TRV pada busbar gardu induk 150 kV!
      \end{itemize}
    \end{block}
  \end{columns}
\end{frame}"""
    },

    "ch9.tex": {
        "f13": r"""% FRAME 13: Praktikum Komputasi Julia
\begin{frame}[fragile]{Praktikum Komputasi Julia: Rekonstruksi Deret Fourier}
  \begin{columns}[t]
    \column{0.50\textwidth}
    \begin{block}{Skrip Julia: Rekonstruksi & Gibbs}
\begin{lstlisting}[style=juliastyle]
using Plots

x = range(-pi, pi, length=400)
fourier_sq(x, N) = sum((4.0 / (pi * n)) .* sin.(n .* x) for n in 1:2:N)

plot(x ./ pi, sign.(x), ls=:dash, color=:gray, label="Target")
plot!(x ./ pi, fourier_sq(x, 1), lw=1.5, label="N = 1")
plot!(x ./ pi, fourier_sq(x, 5), lw=1.8, label="N = 5")
plot!(x ./ pi, fourier_sq(x, 25), lw=2, color=:red, label="N = 25 (Gibbs)")
\end{lstlisting}
    \end{block}

    \column{0.48\textwidth}
    \begin{alertblock}{Visualisasi Fenomena Gibbs}
      \centering
      \includegraphics[width=\linewidth, height=0.38\textheight, keepaspectratio]{figures/slides/plot_ch9.png}
    \end{alertblock}
    \vspace{-0.1cm}
    \begin{exampleblock}{Intisari Fourier}
      \tiny
      Harmonisa ganjil merekonstruksi gelombang simetris ganjil. Pada titik diskontinuitas, lonjakan overshoot $8{,}95\%$ tidak hilang meskipun $N \to \infty$ (Gibbs overshoot).
    \end{exampleblock}
  \end{columns}
\end{frame}""",
        "f14": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
\begin{frame}{Kuis Konseptual Interaktif \& Evaluasi Bloom (C1--C6)}
  \begin{columns}[t]
    \column{0.52\textwidth}
    \begin{alertblock}{Peer Instruction: Uji Miskonsepsi Fisik}
      \footnotesize
      \textbf{Kasus Rekayasa:} Jika jumlah harmonisa deret Fourier gelombang kotak dinaikkan dari $N = 25$ hingga $N = 1.000.000$ suku, apakah persentase lonjakan overshoot di dekat ujung diskontinuitas akan hilang ke $0\%$?
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
        \item \textbf{C6 (Desain):} Rancang spektrum filter harmonisa aktif untuk meredam harmonisa ke-3 dan ke-5 pada beban non-linier!
      \end{itemize}
    \end{block}
  \end{columns}
\end{frame}"""
    },

    "ch10.tex": {
        "f13": r"""% FRAME 13: Praktikum Komputasi Julia
\begin{frame}[fragile]{Praktikum Komputasi Julia: Distribusi Suhu Busbar}
  \begin{columns}[t]
    \column{0.50\textwidth}
    \begin{block}{Skrip Julia: Solusi Termal 1D}
\begin{lstlisting}[style=juliastyle]
using Plots

x = range(0, 10.0, length=200) # L = 10 m
T0, q_joule = 50.0, 25.0
T_bus = @. T0 + (q_joule / 2.0) * x * (10.0 - x)

plot(x, T_bus, lw=2.5, color=:red, label="T(x)")
scatter!([5.0], [maximum(T_bus)], color=:blue, label="Puncak Tengah")
hline!([50.0], ls=:dash, color=:gray, label="Ujung Rel 50 C")
\end{lstlisting}
    \end{block}

    \column{0.48\textwidth}
    \begin{alertblock}{Visualisasi Suhu Busbar IEEE 738}
      \centering
      \includegraphics[width=\linewidth, height=0.38\textheight, keepaspectratio]{figures/slides/plot_ch10.png}
    \end{alertblock}
    \vspace{-0.1cm}
    \begin{exampleblock}{Intisari Termal Spasial}
      \tiny
      Pemanasan Joule internal menghasilkan profil suhu parabolik simetris. Suhu maksimum terjadi di tengah bentang busbar ($x = L/2$), wajib dibatasi di bawah batas penuaan material tembaga/aluminium.
    \end{exampleblock}
  \end{columns}
\end{frame}""",
        "f14": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
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
\end{frame}"""
    },

    "ch11.tex": {
        "f13": r"""% FRAME 13: Praktikum Komputasi Julia
\begin{frame}[fragile]{Praktikum Komputasi Julia: Gelombang Telegrafer Transmisi}
  \begin{columns}[t]
    \column{0.50\textwidth}
    \begin{block}{Skrip Julia: Pantulan Surja d'Alembert}
\begin{lstlisting}[style=juliastyle]
using Plots

z = range(0, 100, length=400) # Saluran 100 km
v_inc = @. exp(-((z - 30.0) / 8.0)^2)
v_ref_open = @. exp(-((z - 70.0) / 8.0)^2)
v_ref_short = @. -exp(-((z - 70.0) / 8.0)^2)

plot(z, v_inc, lw=2, color=:blue, label="Datang v+")
plot!(z, v_ref_open, lw=2, color=:green, label="Pantul Open (Gamma=+1)")
plot!(z, v_ref_short, lw=2, ls=:dash, color=:red, label="Pantul Short (Gamma=-1)")
\end{lstlisting}
    \end{block}

    \column{0.48\textwidth}
    \begin{alertblock}{Visualisasi Surja Transmisi}
      \centering
      \includegraphics[width=\linewidth, height=0.38\textheight, keepaspectratio]{figures/slides/plot_ch11.png}
    \end{alertblock}
    \vspace{-0.1cm}
    \begin{exampleblock}{Intisari Gelombang Berjalan}
      \tiny
      Surja merambat dengan kecepatan $v \approx c$. Pada ujung saluran terbuka ($\Gamma_L = +1$), pantulan sefasa melipatgandakan tegangan ($2\text{ pu}$); pada hubung singkat ($\Gamma_L = -1$), pantulan berbalik fasa.
    \end{exampleblock}
  \end{columns}
\end{frame}""",
        "f14": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
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
\end{frame}"""
    },

    "ch12.tex": {
        "f13": r"""% FRAME 13: Praktikum Komputasi Julia
\begin{frame}[fragile]{Praktikum Komputasi Julia: Difusi Termal Kabel XLPE}
  \begin{columns}[t]
    \column{0.50\textwidth}
    \begin{block}{Skrip Julia: Penetrasi Panas Transien}
\begin{lstlisting}[style=juliastyle]
using Plots

r_norm = range(0, 1.0, length=200)
T_prof(r, tau) = (1.0 .- r) .* (1.0 .- exp.(-r .* 4 .- tau .* 2))

plot(r_norm, T_prof(r_norm, 0.05), lw=2, label="t = 0.05 tau")
plot!(r_norm, T_prof(r_norm, 0.2), lw=2, label="t = 0.2 tau")
plot!(r_norm, T_prof(r_norm, 0.8), lw=2, label="t = 0.8 tau")
plot!(r_norm, 1.0 .- r_norm, lw=2.5, color=:red, label="Tunak")
\end{lstlisting}
    \end{block}

    \column{0.48\textwidth}
    \begin{alertblock}{Visualisasi Difusi Panas IEC 60287}
      \centering
      \includegraphics[width=\linewidth, height=0.38\textheight, keepaspectratio]{figures/slides/plot_ch12.png}
    \end{alertblock}
    \vspace{-0.1cm}
    \begin{exampleblock}{Intisari Difusi Termal}
      \tiny
      Panas Joule merambat keluar dari inti kawat menuju tanah. Laju penetrasi dikendalikan oleh difusivitas termal $\alpha = k/(\rho c_p)$. Kondisi tunak membentuk profil temperatur logaritmik silinder.
    \end{exampleblock}
  \end{columns}
\end{frame}""",
        "f14": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
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
\end{frame}"""
    },

    "ch13.tex": {
        "f13": r"""% FRAME 13: Praktikum Komputasi Julia
\begin{frame}[fragile]{Praktikum Komputasi Julia: FDM Laplace 2D Isolator}
  \begin{columns}[t]
    \column{0.50\textwidth}
    \begin{block}{Skrip Julia: Relaksasi Potensial 2D}
\begin{lstlisting}[style=juliastyle]
using Plots

Nx, Ny = 50, 50
V = zeros(Nx, Ny)
V[:, end] .= 150.0  # Batas atas 150 kV
V[:, 1] .= 0.0      # Batas tanah 0 V

# Iterasi Gauss-Seidel 5-Titik FDM
for it in 1:200, i in 2:Nx-1, j in 2:Ny-1
  V[i, j] = 0.25 * (V[i+1, j] + V[i-1, j] + V[i, j+1] + V[i, j-1])
end
contour(V, levels=12, color=:viridis)
\end{lstlisting}
    \end{block}

    \column{0.48\textwidth}
    \begin{alertblock}{Visualisasi Kontur Potensial 2D}
      \centering
      \includegraphics[width=\linewidth, height=0.38\textheight, keepaspectratio]{figures/slides/plot_ch13.png}
    \end{alertblock}
    \vspace{-0.1cm}
    \begin{exampleblock}{Intisari Medan Laplace}
      \tiny
      Kontur ekuipotensial menunjukkan kerapatan medan tertinggi ($\nabla V$) di sekitar elektroda runcing konduktor $150\text{ kV}$, mengidentifikasi titik rawan pelepasan parsial dan loncatan api (*flashover*).
    \end{exampleblock}
  \end{columns}
\end{frame}""",
        "f14": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
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
\end{frame}"""
    },

    "ch14.tex": {
        "f13": r"""% FRAME 13: Praktikum Komputasi Julia
\begin{frame}[fragile]{Praktikum Komputasi Julia: Fungsi Bessel \& Skin Effect}
  \begin{columns}[t]
    \column{0.50\textwidth}
    \begin{block}{Skrip Julia: Deret Bessel \& Rapat Arus}
\begin{lstlisting}[style=juliastyle]
using Plots

r_a = range(0, 1.0, length=300)
# Profil rapat arus radial skin effect
J_prof(r, delta) = exp.(-(1.0 .- r) ./ delta)

plot(r_a, J_prof(r_a, 1.0), lw=2, label="delta = a (DC/Rendah)")
plot!(r_a, J_prof(r_a, 0.3), lw=2, label="delta = 0.3a (50 Hz)")
plot!(r_a, J_prof(r_a, 0.1), lw=2, color=:red, label="delta = 0.1a (Tinggi)")
\end{lstlisting}
    \end{block}

    \column{0.48\textwidth}
    \begin{alertblock}{Visualisasi Efek Kulit Bessel}
      \centering
      \includegraphics[width=\linewidth, height=0.38\textheight, keepaspectratio]{figures/slides/plot_ch14.png}
    \end{alertblock}
    \vspace{-0.1cm}
    \begin{exampleblock}{Intisari Efek Kulit}
      \tiny
      Arus meluruh eksponensial menuju pusat kawat. Pada frekuensi tinggi ($\delta \ll a$), inti konduktor menjadi zona arus mati. Ini melandasi inovasi kawat ACSR dan pipa tubular berongga PLN.
    \end{exampleblock}
  \end{columns}
\end{frame}""",
        "f14": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
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
    },

    "ch15.tex": {
        "f13": r"""% FRAME 13: Praktikum Komputasi Julia
\begin{frame}[fragile]{Praktikum Komputasi Julia: Polinomial Legendre Koordinat Bola}
  \begin{columns}[t]
    \column{0.50\textwidth}
    \begin{block}{Skrip Julia: Basis Polinomial Legendre}
\begin{lstlisting}[style=juliastyle]
using Plots

theta = range(0, pi, length=300)
x = cos.(theta)

P0 = ones(size(x))
P1 = x
P2 = @. 0.5 * (3 * x^2 - 1)
P3 = @. 0.5 * (5 * x^3 - 3 * x)

plot(theta ./ pi, P0, ls=:dash, label="P0 (Monopol)")
plot!(theta ./ pi, P1, lw=2, label="P1 (Dipol)")
plot!(theta ./ pi, P2, lw=2, label="P2 (Kuadrupol)")
plot!(theta ./ pi, P3, lw=2, color=:red, label="P3 (Oktopol)")
\end{lstlisting}
    \end{block}

    \column{0.48\textwidth}
    \begin{alertblock}{Visualisasi Basis Legendre Bola}
      \centering
      \includegraphics[width=\linewidth, height=0.38\textheight, keepaspectratio]{figures/slides/plot_ch15.png}
    \end{alertblock}
    \vspace{-0.1cm}
    \begin{exampleblock}{Intisari Basis Bola}
      \tiny
      Polinomial Legendre $P_n(\cos\theta)$ adalah basis ortogonal solusi persamaan Laplace koordinat bola 3D. Orde $P_1$ merepresentasikan potensial dipol elektrostatik elektroda pembumian bola gardu induk.
    \end{exampleblock}
  \end{columns}
\end{frame}""",
        "f14": r"""% FRAME 14: Kuis & Tantangan Bloom C1-C6
\begin{frame}{Kuis Konseptual Interaktif \& Evaluasi Bloom (C1--C6)}
  \begin{columns}[t]
    \column{0.52\textwidth}
    \begin{alertblock}{Peer Instruction: Uji Miskonsepsi Fisik}
      \footnotesize
      \textbf{Kasus Rekayasa:} Maxwell menambahkan suku arus pergeseran $\vec{J}_d = \partial\vec{D}/\partial t$ pada Hukum Ampere. Jika suku ini diabaikan, hukum fisika fundamental mana yang langsung dilanggar pada celah kapasitor AC?
      \vspace{0.05cm}
      \begin{itemize}\setlength{\itemsep}{1pt}
        \item \textbf{[A]} Hukum Pertama Termodinamika.
        \item \textbf{[B]} **Hukum Kekekalan Muatan Listrik** (Persamaan Kontinuitas $\nabla \cdot \vec{J} + \frac{\partial \rho_v}{\partial t} = 0$)!
        \item \textbf{[C]} Hukum Gravitasi Universal Newton.
        \item \textbf{[D]} Hukum Pemantulan Gelombang Optik Snellius.
      \end{itemize}
    \end{alertblock}

    \column{0.46\textwidth}
    \begin{block}{Tantangan Analisis \& Desain (C4--C6)}
      \footnotesize
      \begin{itemize}\setlength{\itemsep}{2pt}
        \item \textbf{C4 (Analisis):} Turunkan persamaan gelombang 3D $\nabla^2 \vec{E} - \mu\epsilon \frac{\partial^2 \vec{E}}{\partial t^2} = 0$ dari hukum Faraday dan Ampere-Maxwell.
        \item \textbf{C5 (Evaluasi):} Evaluasi kerapatan daya Poynting rata-rata $\langle \vec{S} \rangle$ di bawah saluran SUTET 500 kV sesuai batas IEEE Std C95.1.
        \item \textbf{C6 (Desain):} Rancang susunan fasa ganda sirkuit SUTET untuk memitigasi medan bocor ke permukaan tanah!
      \end{itemize}
    \end{block}
  \end{columns}
\end{frame}"""
    }
}

for fname, content in updates.items():
    if not os.path.exists(fname):
        print(f"File {fname} not found!")
        continue
    with open(fname, "r") as f:
        text = f.read()

    # Replace FRAME 13
    f13_pattern = re.compile(r"% ---* FRAME 13.*?\\end\{frame\}", re.DOTALL)
    if f13_pattern.search(text):
        text = f13_pattern.sub(lambda m: content["f13"], text, count=1)
    else:
        alt_pattern = re.compile(r"\\begin\{frame\}\[fragile\]\{Praktikum.*?\\end\{frame\}", re.DOTALL)
        if alt_pattern.search(text):
            text = alt_pattern.sub(lambda m: content["f13"], text, count=1)
        else:
            print(f"Warning: Frame 13 not found in {fname}")

    # Replace FRAME 14
    f14_pattern = re.compile(r"% ---* FRAME 14.*?\\end\{frame\}", re.DOTALL)
    if f14_pattern.search(text):
        text = f14_pattern.sub(lambda m: content["f14"], text, count=1)
    else:
        alt14_pattern = re.compile(r"\\begin\{frame\}\{Tantangan Mandiri.*?\\end\{frame\}", re.DOTALL)
        if alt14_pattern.search(text):
            text = alt14_pattern.sub(lambda m: content["f14"], text, count=1)
        else:
            alt14_pattern2 = re.compile(r"\\begin\{frame\}\{Evaluasi Mandiri.*?\\end\{frame\}", re.DOTALL)
            if alt14_pattern2.search(text):
                text = alt14_pattern2.sub(lambda m: content["f14"], text, count=1)
            else:
                print(f"Warning: Frame 14 not found in {fname}")

    with open(fname, "w") as f:
        f.write(text)
    print(f"Updated {fname}")
