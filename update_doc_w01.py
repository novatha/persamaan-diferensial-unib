# -*- coding: utf-8 -*-

md_content = """# 📘 Modul Ajar Kuliah Minggu 1: Pengantar Persamaan Diferensial
**Klasifikasi PDB/PDP, Masalah Nilai Awal (IVP), Dinamika Energi Rangkaian Elektrik & Komputasi GNU Octave**

---

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; border-radius: 8px; margin: 1.5rem 0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
  <iframe src="https://www.youtube-nocookie.com/embed/umcAHSZyhCE" title="Video Perkuliahan Minggu 01 - Persamaan Diferensial | Teknik Elektro UNIB" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

???+ info "📥 Pusat Unduhan Berkas Pembelajaran Minggu 1"
    - 📄 [**Diktat / Modul Monograf Lengkap (16 Halaman PDF)**](files/modul_1.pdf)
    - 📽️ [**Slide Presentasi Beamer 16:9 (PDF)**](files/ch1.pdf)
    - 📝 [**Lembar Kerja Mahasiswa (Worksheet C1–C6 PDF)**](files/worksheet1.pdf)
    - 📐 [**Problem Set Latihan Mandiri & Kunci Jawaban (PDF)**](files/problem_set1.pdf)
    - 💻 [**Simulasi Transien RC & RL (.ipynb)**](files/Simulasi_Transien_RC_RL.ipynb)
    - 📺 [**Tonton di Kanal YouTube Resmi Novalio Daratha (12:19)**](https://youtu.be/umcAHSZyhCE)

---

???+ abstract "🎯 Capaian Pembelajaran Khusus (Sub-CPMK 1)"
    Setelah menyelesaikan pembelajaran pada Modul Ajar Minggu 1 ini, mahasiswa diharapkan mampu:
    
    1. **C1 (Mengingat):** Mendefinisikan persamaan diferensial, membedakan secara tegas antara Persamaan Diferensial Biasa (PDB) dan Persamaan Diferensial Parsial (PDP), serta mengidentifikasi orde, derajat, linieritas, dan sifat homogenitas suatu persamaan diferensial.
    2. **C2 (Memahami):** Menjelaskan makna fisis laju perubahan seketika ($dx/dt$), perbedaan fundamental antara solusi umum (keluarga kurva integral kontinu) dan solusi khusus unik, serta peranan krusial Masalah Nilai Awal (*Initial Value Problem* - IVP) dalam menentukan lintasan dinamika sistem fisik.
    3. **C3 (Menerapkan):** Menyelesaikan persamaan diferensial biasa orde satu linier/separabel sederhana secara analitis dan menentukan nilai konstanta integrasi $C$ berdasarkan kondisi batas awal pada rangkaian transien listrik.
    4. **C4 (Menganalisis):** Menurunkan model persamaan diferensial dari hukum-hukum fundamental fisika elektro (Hukum Kirchhoff Tegangan/Arus, Hukum Induksi Faraday $v_L = L \frac{di}{dt}$, dan Arus Perpindahan Kapasitor $i_C = C \frac{dv}{dt}$) serta membuktikan prinsip kontinuitas energi medan magnet dan medan listrik pada saat pensaklaran (*switching*).
    5. **C5 (Mengevaluasi):** Mengkaji keabsahan model matematis linier ideal terhadap fenomena non-linier riil (seperti saturasi magnetik inti besi induktor dan resistansi parasitik kapasitor) pada aplikasi jaringan kelistrikan modern.
    6. **C6 (Menciptakan/Komputasi):** Mengembangkan skrip modular berbasis **GNU Octave** untuk mensimulasikan respon transien arus pengisian induktor, memvalidasi solusi eksak analitik terhadap solusi numerik integrasi Runge-Kutta (`ode45`), serta memvisualisasikan medan arah (*slope field*).

---

## 1. Peta Konsep dan Posisi Modul dalam Kurikulum

Mata kuliah Persamaan Diferensial di Jurusan Teknik Elektro dirancang secara khusus untuk membangun landasan analitik dan intuisi fisika yang kokoh bagi dua pilar utama rekayasa elektro:
1. **Paruh Pertama (Minggu 1 – 7):** Analisis Transien Rangkaian Listrik berbasis Persamaan Diferensial Biasa (PDB).
2. **Paruh Kedua (Minggu 9 – 15):** Teori Medan Elektromagnetika & Gelombang berbasis Persamaan Diferensial Parsial (PDP).

```mermaid
flowchart LR
    subgraph Paruh1["Paruh 1: PDB & Rangkaian Listrik"]
        W1["<b>W1: Klasifikasi PD & Pemodelan RL</b>"] --> W2["W2: PDB Orde 1 Separabel"]
        W2 --> W3["W3: Aplikasi Transien RC/RL"]
        W3 --> W4["W4: PDB Orde 2 Homogen LC"]
        W4 --> W5["W5: Transien RLC AC"]
        W5 --> W6["W6: Transformasi Laplace"]
        W6 --> W7["W7: Invers Laplace Domain s"]
    end
    
    subgraph Paruh2["Paruh 2: PDP & Medan Elektromagnetika"]
        W9["W9: Deret Fourier"] --> W10["W10: Pemisahan Variabel"]
        W10 --> W11["W11: Gelombang 1D Telegrafer"]
        W11 --> W12["W12: Panas 1D Termal Kabel"]
        W12 --> W13["W13: Laplace 2D Potensial"]
        W13 --> W14["W14: Bessel & Efek Kulit"]
        W14 --> W15["W15: 4 Persamaan Maxwell"]
    end
    
    W7 --> UTS["Minggu 8: UTS"]
    UTS --> W9
    W15 --> UAS["Minggu 16: UAS"]

    style W1 fill:#ffcccc,stroke:#cc0000,stroke-width:2px;
```

---

## 2. Pendahuluan & Filosofi Fisika Dinamika Sistem Elektro

Hukum-hukum fundamental fisika elektro tidak pernah menyatakan besaran fisik secara statis, melainkan menyatakan **laju perubahan seketika** (*rate of change*):

1. **Hukum Arus Kapasitor (Arus Perpindahan):**
   $$ i(t) = \frac{dq(t)}{dt} = C \frac{dv(t)}{dt} $$
   Kapasitor berlaku sebagai sirkuit terbuka pada tegangan konstan DC ($\frac{dv}{dt} = 0$), namun mengalirkan arus sangat besar jika tegangan berubah cepat.
2. **Hukum Tegangan Induktor (Hukum Induksi Faraday):**
   $$ v(t) = \frac{d\lambda(t)}{dt} = L \frac{di(t)}{dt} $$
   Induktor berlaku sebagai kawat hubung singkat pada arus mantap DC ($\frac{di}{dt} = 0$), namun memunculkan tegangan lawan induksi yang sangat tinggi ketika arus diputus tiba-tiba.
3. **Kekekalan Energi pada Elemen Terpusat:**
   - Resistor mendisipasikan kalor: $p_R(t) = R \cdot i(t)^2$
   - Induktor menyimpan energi medan magnet: $E_L(t) = \frac{1}{2} L i(t)^2$
   - Kapasitor menyimpan energi medan listrik: $E_C(t) = \frac{1}{2} C v(t)^2$

---

## 3. Taksonomi & Klasifikasi Persamaan Diferensial

| Atribut Klasifikasi | Definisi & Kriteria | Contoh di Bidang Teknik Elektro |
| :--- | :--- | :--- |
| **Tipe: PDB (ODE)** | Satu variabel bebas tunggal (waktu $t$) | $L \frac{di}{dt} + Ri = V_0$ (Transien RL) |
| **Tipe: PDP (PDE)** | Dua atau lebih variabel bebas ($x, t$) | $\frac{\partial^2 v}{\partial x^2} = LC \frac{\partial^2 v}{\partial t^2}$ (Telegrafer transmisi) |
| **Orde** | Tingkat turunan paling tinggi | Orde 1 ($di/dt$), Orde 2 ($d^2q/dt^2$) |
| **Derajat** | Pangkat aljabar dari turunan tertinggi | $\left(\frac{di}{dt}\right)^1 \implies \text{Derajat 1}$ |
| **Linieritas** | Derajat satu untuk $y$ & $y'$, tanpa perkalian $y \cdot y'$ atau non-linier $\sin(y)$ | Memenuhi prinsip superposisi $L[c_1 y_1 + c_2 y_2] = c_1 L[y_1] + c_2 L[y_2]$ |
| **Homogenitas** | Suku pemaksa $g(t) = 0$ vs $g(t) \neq 0$ | Homogen = Respon Alami; Non-Homogen = Respon Paksa |

---

## 4. Konsep Solusi & Medan Arah (*Slope Field*)

Solusi umum PDB orde $n$ memuat $n$ buah konstanta sembarang ($C$), yang merepresentasikan keluarga tak hingga dari kurva integral di bidang $(t, y)$.

Untuk persamaan yang sulit diintegrasikan secara analitik, **Medan Arah** (*Direction / Slope Field*) menggambarkan segmen gradien kemiringan garis singgung $m = \frac{dy}{dt} = f(t,y)$ pada setiap titik koordinat. Seluruh kurva solusi pengisian arus induktor dari mana pun titik awal dimulai akan berkonvergensi secara asimtotik menuju nilai keadaan mantap (*steady-state*):
$$ I_{\text{ss}} = \lim_{t \to \infty} i(t) = \frac{V_0}{R} $$

---

## 5. Masalah Nilai Awal (IVP) & Prinsip Kontinuitas Energi

Kondisi awal pada saat penyaklaran ($t = 0^+$) diatur secara mutlak oleh hukum kekekalan energi alam semesta:

!!! warning "Prinsip Kontinuitas Energi Rangkaian"
    - **Arus Induktor Tidak Boleh Berubah Seketika:**
      $$ i_L(0^-) = i_L(0^+) $$
      Jika arus melompat seketika, laju perubahan $\frac{di}{dt} \to \infty$, yang menuntut daya tak hingga ($p_L = L i \frac{di}{dt} \to \infty$), suatu hal yang mustahil secara fisik.
    - **Tegangan Kapasitor Tidak Boleh Berubah Seketika:**
      $$ v_C(0^-) = v_C(0^+) $$
      Lonjakan tegangan seketika menuntut arus perpindahan tak hingga ($i_C = C \frac{dv}{dt} \to \infty$).

---

## 6. Pemodelan Rangkaian RL Seri & Derivasi Analitik

Tinjau loop tertutup rangkaian seri resistor $R$, induktor $L$, dan sumber tegangan DC $V_0$. Hukum Tegangan Kirchhoff (KVL) menyatakan:
$$ v_R(t) + v_L(t) = V_0 \implies L \frac{di(t)}{dt} + R i(t) = V_0 $$

### Penurunan Solusi Lengkap:
Pisahkan variabel:
$$ \frac{di}{V_0 - R i} = \frac{1}{L} dt $$
Integralkan kedua ruas:
$$ -\frac{1}{R} \ln|V_0 - R i| = \frac{t}{L} + C_1 \implies i(t) = \frac{V_0}{R} + K e^{-\frac{R}{L} t} $$

Terapkan kondisi awal $i(0) = 0$:
$$ 0 = \frac{V_0}{R} + K \implies K = -\frac{V_0}{R} $$

Diperoleh **Solusi Khusus Arus Pengisian**:
$$ i(t) = \frac{V_0}{R} \left( 1 - e^{-\frac{t}{\tau}} \right), \quad \text{di mana } \tau = \frac{L}{R} \text{ [detik]} $$

| Kelipatan Waktu | Faktor $e^{-t/\tau}$ | Persentase Arus $i(t)$ | Status Operasi |
| :---: | :---: | :---: | :--- |
| **$0$** | $1{,}0000$ | $0{,}0\%$ | Sakelar baru menutup; induktor menahan arus secara total |
| **$1\tau$** | $0{,}3679$ | $63{,}2\%$ | Konstanta waktu: transien berlangsung cepat |
| **$2\tau$** | $0{,}1353$ | $86{,}5\%$ | Respon mulai melambat |
| **$3\tau$** | $0{,}0498$ | $95{,}0\%$ | Mendekati keadaan mantap |
| **$5\tau$** | $0{,}0067$ | $99{,}3\%$ | Secara konvensi rekayasa, transien dinyatakan **selesai** |

---

## 7. Studi Kasus Industri: Transien Penyalaan Trafo Gardu Induk

Transformator daya besar (seperti di Gardu Induk Pulau Baai 150 kV atau GI Curup) memiliki rasio reaktansi terhadap resistansi yang sangat tinggi ($X/R \approx 30$). Konstanta waktu transien mencapai:
$$ \tau = \frac{X/R}{\omega} = \frac{30}{2\pi \times 50} \approx 95\text{ ms} $$

Waktu peluruhan transien mencapai $5\tau \approx 475\text{ ms} \approx 0{,}5\text{ detik}$. Selama periode transien ini, inti besi transformator mengalami kejenuhan magnetik yang memicu **inrush current** hingga $6 - 10 \times$ arus nominal. Insinyur proteksi wajib menyetel relai diferensial (*relay 87T*) dengan penahan harmonisa kedua (*second-harmonic restraint*) agar transformator tidak trip secara keliru.

---

## 8. Contoh Soal Terhitung Langkah demi Langkah

!!! example "Kasus Solenoida Pemutus Tenaga (Circuit Breaker)"
    Sebuah kumparan trip pemutus tenaga memiliki $R = 2{,}5\ \Omega$, $L = 50\text{ mH}$, dipasok baterai gardu induk $V_0 = 125\text{ V}$.
    
    1. **Konstanta Waktu:**
       $$ \tau = \frac{L}{R} = \frac{0{,}05}{2{,}5} = 0{,}02\text{ s} = 20\text{ ms} $$
    2. **Arus Keadaan Mantap:**
       $$ I_{\text{ss}} = \frac{125}{2{,}5} = 50\text{ A} $$
    3. **Arus pada $t = 20\text{ ms}$ ($1\tau$):**
       $$ i(20\text{ ms}) = 50(1 - e^{-1}) = 31{,}61\text{ A} $$
    4. **Arus pada $t = 100\text{ ms}$ ($5\tau$):**
       $$ i(100\text{ ms}) = 50(1 - e^{-5}) = 49{,}66\text{ A} $$
    5. **Energi Medan Magnet Mantap:**
       $$ E_L = \frac{1}{2} L I_{\text{ss}}^2 = \frac{1}{2} (0{,}05) (50)^2 = 62{,}5\text{ Joule} $$

---

## 9. Praktikum Komputasi Matematika Terbuka (GNU Octave)

Berikut adalah skrip lengkap GNU Octave untuk memvalidasi respon transien analitik terhadap integrasi numerik `ode45`:

```matlab
% =========================================================================
% Skrip Praktikum Minggu 1: Respon Transien RL (Analitik vs ODE45)
% =========================================================================
clear all; close all; clc;

V0 = 125.0; R = 2.5; L = 0.050;
tau = L / R; Iss = V0 / R;

t_end = 6 * tau;
t_exact = linspace(0, t_end, 500);
i_exact = Iss * (1 - exp(-t_exact / tau));

% Solusi Numerik ODE45
f_ode = @(t, i) (V0 - R * i) / L;
[t_num, i_num] = ode45(f_ode, [0, t_end], 0.0);

% Plotting
figure('Name', 'Respon Transien Rangkaian RL');
subplot(2,1,1);
plot(t_exact*1000, i_exact, 'b-', 'LineWidth', 2.2); hold on;
plot(t_num*1000, i_num, 'ro', 'MarkerSize', 4);
yline(Iss, 'k--'); xline(tau*1000, 'g--'); xline(5*tau*1000, 'm--');
grid on;
title('Respon Transien Arus Induktor: i(t) vs Waktu');
xlabel('Waktu (ms)'); ylabel('Arus i(t) [A]');
legend('Solusi Analitik Eksak', 'Solusi Numerik ODE45', 'Keadaan Mantap', '1 Tau (63.2%)', '5 Tau (99.3%)');

subplot(2,1,2);
v_L = V0 * exp(-t_exact / tau);
plot(t_exact*1000, v_L, 'r-', 'LineWidth', 2.0); grid on;
title('Dinamika Tegangan Induktor v_L(t)');
xlabel('Waktu (ms)'); ylabel('Tegangan (Volt)');
```

---

## 10. Evaluasi & Bank Soal Terstruktur (Taksonomi Bloom C1 – C6)

1. **C1 (Mengingat):** Tentukan orde, derajat, dan linieritas dari persamaan diferensial:
   $$ \frac{d^2 v}{dt^2} + 5 \left(\frac{dv}{dt}\right)^3 + 9 v = 0 $$
2. **C2 (Memahami):** Mengapa saat sakelar ditutup mendadak, induktor bertindak sebagai *open circuit* sedangkan kapasitor bertindak sebagai *short circuit*? Buktikan dari $v_L = L \frac{di}{dt}$ dan $i_C = C \frac{dv}{dt}$.
3. **C3 (Menerapkan):** Selesaikan IVP: $\frac{dy}{dx} = \frac{x^2}{y}, \quad y(0) = -4$, dan tentukan domain validitasnya!
4. **C4 (Menganalisis):** Buktikan bahwa seluruh energi awal kapasitor $E_C = \frac{1}{2} C V_0^2$ yang dikosongkan ke resistor $R$ akan terdisipasi secara tepat menjadi energi kalor $\int_0^\infty i^2 R dt$!
5. **C5 (Mengevaluasi):** Evaluasi distorsi harmonisa arus yang timbul jika induktor inti besi mengalami saturasi $\lambda(i) = a \arctan(b i)$ saat dipasok tegangan sinusoidal!
6. **C6 (Menciptakan/Perancangan):** Rancang fungsi GNU Octave `simulasi_transien_rc(R, C, V0)` yang menerima parameter fisik rangkaian RC dan menghasilkan kurva respon waktu pengisian secara otomatis!

---

## 11. Referensi Rujukan Standar
1. Erwin Kreyszig, *Advanced Engineering Mathematics*, 10th Edition, John Wiley & Sons, 2020.
2. Dennis G. Zill, *A First Course in Differential Equations with Modeling Applications*, 11th Edition, Cengage Learning, 2018.
3. William H. Hayt, Jack E. Kemmerly, Jamie D. Phillips, dan Steven M. Durbin, *Engineering Circuit Analysis*, 9th Edition, McGraw-Hill, 2019.
4. IEEE Std C37.010-2016, *IEEE Application Guide for AC High-Voltage Circuit Breakers*.
"""

with open("docs/01_modul_1.md", "w") as f:
    f.write(md_content)

print("docs/01_modul_1.md updated successfully!")
