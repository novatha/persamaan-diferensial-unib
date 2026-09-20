# Ringkasan Sesi Kerja: Transformasi Modul Ajar Persamaan Diferensial (Minggu 2 s.d. 5)
**Tanggal & Waktu:** 20 September 2026, 10:15 WIB  
**Mata Kuliah:** Persamaan Diferensial (TEE-203)  
**Institusi:** Jurusan Teknik Elektro, Fakultas Teknik, Universitas Bengkulu  
**Dosen Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  

---

## 1. Capaian & Pekerjaan yang Diselesaikan

Pada sesi ini, dilakukan pembenahan dan transformasi menyeluruh modul-modul perkuliahan mingguan untuk mata kuliah **Persamaan Diferensial** sesuai standar monograf buku ajar bereputasi, blueprint 12 bagian, dan Kerangka 4-Pilar Pedagogis OBE (mengikuti standar kurikulum DSTL di portal `https://www.ndaratha.my.id/dstl/materi`).

### A. Modul 2 (Minggu 2): PDB Orde 1 Separabel, Eksak, Faktor Integrasi \& Rangkaian RC
- **File:** `modul_2.tex` $\to$ `modul_2.pdf` (19 halaman).
- **Jumlah Kata Substantif:** **2.521 kata** (melampaui syarat minimum 1.200 kata).
- **Status Kompilasi:** **Zero Overfull \hbox**.
- **Materi Utama:**
  - Bentuk umum separabel, keeksakan Euler-Clairaut ($\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$), fungsi potensial skalar $F(x,y)$, dan faktor pengintegrasi $\mu(x), \mu(y)$.
  - Pembuktian kontinuitas tegangan kapasitor ($v_C(0^-) = v_C(0^+)$).
  - Paradoks efisiensi pengisian kapasitor (disipasi termal 50\% pada resistor).
  - Studi kasus industri: perancangan *snubber RC* peredam lonjakan $dv/dt$ pada sakelar semikonduktor daya IGBT.
  - Praktikum Julia 1.12+: `DifferentialEquations.jl` (solver `Tsit5()`) dan `Plots.jl`.
  - 3 Worked Examples dan Bank Soal Bloom C1--C6.

### B. Modul 3 (Minggu 3): Aplikasi Transien RC-RL, Inductive Kickback \& Dinamika Termal Trafo Daya
- **File:** `modul_3.tex` $\to$ `modul_3.pdf` (17 halaman).
- **Jumlah Kata Substantif:** **2.724 kata** (melampaui syarat minimum 1.200 kata).
- **Status Kompilasi:** **Zero Overfull \hbox**.
- **Materi Utama:**
  - Kontinuitas arus induktor ($i_L(0^-) = i_L(0^+)$) dan penurunan KVL respon langkah rangkaian RL.
  - Fenomena fisis bahaya lonjakan tegangan induktif (*inductive kickback* $v_L = -L \frac{di}{dt}$) saat sakelar dibuka mendadak dan sirkuit mitigasi dioda *freewheeling* anti-paralel.
  - Transien sakelar multi-interval pada rangkaian RC.
  - Penurunan model diferensial termal transformator daya gardu induk dari prinsip pertama (Hukum Pendinginan Newton dan kesetimbangan energi kalor internal):
    $$\frac{dT(t)}{dt} + \frac{1}{\tau_{\text{th}}} T(t) = \frac{T_{\text{amb}}}{\tau_{\text{th}}} + \frac{P_{\text{loss}}}{C_{\text{th}}}$$
  - Standar industri IEEE Std C57.91 untuk estimasi umur isolasi termal (persamaan Arrhenius $V = 2^{(\Theta_{\text{H}} - 110)/6}$).
  - Praktikum Julia 1.12+: Simulasi simultan transien elektrik RL dan profil suhu minyak trafo 60 MVA dengan ambang alarm $85^\circ$C dan trip $95^\circ$C.
  - 3 Worked Examples terhitung numerik dan Bank Soal Bloom C1--C6.

### C. Modul 4 (Minggu 4): PDB Linier Orde 2 Homogen Koefisien Konstan \& Tangki LC
- **File:** `modul_4.tex` $\to$ `modul_4.pdf` (16 halaman).
- **Jumlah Kata Substantif:** **1.941 kata** (melampaui syarat minimum 1.200 kata).
- **Status Kompilasi:** **Zero Overfull \hbox**.
- **Materi Utama:**
  - Persamaan karakteristik kuadrat $a r^2 + b r + c = 0$ dan diskriminan $D = b^2 - 4ac$.
  - Uji kebebasan linier Determinan Wronskian $W(y_1, y_2) \neq 0$ dan Teorema Identitas Abel.
  - Pembuktian analitis kemunculan suku $x e^{rx}$ pada akar kembar melalui Metode Reduksi Orde d'Alembert.
  - Tiga ragam redaman RLC seri bebas sumber: *Overdamped* ($\zeta > 1$), *Critically Damped* ($\zeta = 1$), dan *Underdamped* ($0 < \zeta < 1$).
  - Kekekalan energi total pada tangki osilator LC murni ($R = 0$) frekuensi radio (RF).
  - Trajektori ruang fasa (*phase portrait*) dan klasifikasi titik ekuilibrium (pusat eliptik, fokus stabil, simpul stabil).
  - Praktikum Julia 1.12+: Simulasi perbandingan ketiga respon redaman dan plot ruang fasa menuju titik ekuilibrium $(0,0)$.
  - 3 Worked Examples dan Bank Soal Bloom C1--C6.

### D. Modul 5 (Minggu 5): PDB Linier Orde 2 Non-Homogen \& RLC Seri AC
- **File:** `modul_5.tex` $\to$ `modul_5.pdf` (14 halaman).
- **Jumlah Kata Substantif:** **1.744 kata** (melampaui syarat minimum 1.200 kata).
- **Status Kompilasi:** **Zero Overfull \hbox**.
- **Materi Utama:**
  - Struktur solusi lengkap $y(x) = y_h(x) + y_p(x)$ (respon transien dan respon tunak).
  - Metode Koefisien Tak Tentu dan aturan modifikasi perkalian $x^s$ saat terjadi resonansi matematis.
  - Penurunan analitik respon arus rangkaian RLC seri tereksitasi sumber sinusoidal AC $v_s(t) = V_m \cos(\omega t)$ (pembuktian Hukum Ohm AC dan impedansi $Z = \sqrt{R^2 + X^2}$).
  - Resonansi tegangan seri pada $\omega_0 = \frac{1}{\sqrt{LC}}$, faktor kualitas $Q = \frac{\omega_0 L}{R}$, dan bahaya amplifikasi tegangan reaktif $v_C = Q V_m$.
  - Fenomena layangan (*beats*) saat frekuensi eksitasi mendekati frekuensi alami ($\omega \approx \omega_0$).
  - Praktikum Julia 1.12+: Simulasi transien arus, kurva amplifikasi tegangan kapasitor, dan kurva respon frekuensi resonansi arus.
  - 3 Worked Examples dan Bank Soal Bloom C1--C6.

---

## 2. Sinkronisasi \& Distribusi Portal Web

1. **Kompilasi PDF:** Seluruh berkas PDF hasil kompilasi (`modul_2.pdf`, `modul_3.pdf`, `modul_4.pdf`, `modul_5.pdf`) telah dikompilasi ulang dengan dua pass `pdflatex` dan diverifikasi menghasilkan **Zero Overfull \hbox**.
2. **Distribusi Aset:** Seluruh PDF disalin ke `portal/public/pdf/` dan direktori publik situs utama pengampu di `/Users/novaliodaratha/Documents/ndaratha.my.id/public/persamaan-diferensial/pdf/`.
3. **Build Portal:** Astro build (`npm run build`) pada portal perkuliahan berhasil 100\% tanpa eror.
4. **Deploy:** Hasil build statis disinkronkan menggunakan `rsync` dan dideploy ke Vercel production untuk domain resmi `https://www.ndaratha.my.id/persamaan-diferensial/`.

---

## 3. Rencana Kerja Selanjutnya

1. Melanjutkan transformasi serupa untuk paruh pertama semester berikutnya:
   - **Modul 6 (Minggu 6):** Transformasi Laplace Dasar \& Teorema Pergeseran.
   - **Modul 7 (Minggu 7):** Invers Transformasi Laplace \& Solusi PDB Rangkaian Domain $s$.
2. Melanjutkan ke paruh kedua semester (PDP \& Medan Elektromagnetika):
   - **Modul 9 s.d. 15:** Deret Fourier, Pemisahan Variabel, Persamaan Gelombang 1D (Telegrafer), Persamaan Panas 1D, Persamaan Laplace 2D, Fungsi Bessel, dan 4 Persamaan Maxwell.
