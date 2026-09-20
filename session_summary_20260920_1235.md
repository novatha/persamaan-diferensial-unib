# Ringkasan Sesi Perkuliahan: Revitalisasi Total Salindia Beamer (Minggu 1–7 & Minggu 9–15)
Tanggal & Waktu: **20 September 2026, 12:35 WIB**  
Mata Kuliah: **Persamaan Diferensial (Fokus Teknik Elektro)**  
Dosen Pengampu: **Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.**  
Institusi: **Jurusan Teknik Elektro, Fakultas Teknik, Universitas Bengkulu**

---

## 1. Latar Belakang & Tujuan
Sesi kerja ini berfokus pada pemenuhan permintaan pengguna untuk merevitalisasi seluruh salindia Beamer perkuliahan (`ch*.tex`, `ch*.pdf`) agar berstandar tinggi, profesional, dan siap saji bagi mahasiswa S1 Teknik Elektro. Salindia lama memiliki kekurangan berupa jumlah frame yang terlalu sedikit (3–5 frame per deck), tidak mencakup model 4-Pilar Pedagogis, dan belum mengintegrasikan komputasi modern berbasis bahasa Julia.

---

## 2. Rincian Capaian Kerja

### A. Rekonstruksi Penuh 14 Salindia Beamer (15 Frame / Deck)
Seluruh 14 deck materi perkuliahan telah ditulis ulang dan dikompilasi ke format layar lebar 16:9 (`[aspectratio=169,10pt]{beamer}`) dengan palet warna resmi Universitas Bengkulu:
1. **Week 1 (`ch1.tex` / `ch1.pdf`):** Klasifikasi PDB/PDP, Orde, Derajat, Linearitas, Masalah Nilai Awal (IVP), KVL RL, Solusi Eksak & Solver Julia `Tsit5()`.
2. **Week 2 (`ch2.tex` / `ch2.pdf`):** PDB Orde 1 Separabel, Eksak, Faktor Integrasi, Rangkaian RC Pengisian Kapasitor, Snubber IGBT Inverter Surya.
3. **Week 3 (`ch3.tex` / `ch3.pdf`):** Transien RL/RC, Inductive Kickback Dioda Freewheeling, Pemodelan Termal Hotspot Trafo Tenaga 60 MVA IEEE C57.91.
4. **Week 4 (`ch4.tex` / `ch4.pdf`):** PDB Orde 2 Homogen, Persamaan Karakteristik, Wronskian, Tiga Ragam Redaman RLC Seri (Overdamped, Critically Damped, Underdamped), Tangki Osilator LC.
5. **Week 5 (`ch5.tex` / `ch5.pdf`):** PDB Orde 2 Non-Homogen, Metode Koefisien Tak Tentu, Resonansi Seri, Faktor Kualitas $Q$, Fenomena Sub-Synchronous Resonance (SSR) Turbin Generator PLN.
6. **Week 6 (`ch6.tex` / `ch6.pdf`):** Transformasi Laplace, Pasangan Transformasi Dasar, Fungsi Tangga Satuan Heaviside, Impuls Dirac, Teorema Geser, Pemodelan Gelombang Surja Petir Standar IEC 60060-1 ($1{,}2/50\,\mu\text{s}$).
7. **Week 7 (`ch7.tex` / `ch7.pdf`):** Invers Laplace, Dekomposisi Pecahan Parsial (Akar Real, Kembar, Kompleks Konjugat), Respon Masukan Nol (ZIR) \& Status Nol (ZSR), Transient Recovery Voltage (TRV) Pemutus Tenaga IEC 62271-100.
8. **Week 9 (`ch9.tex` / `ch9.pdf`):** Pengantar Persamaan Diferensial Parsial (PDP), Taksonomi Orde Dua (Eliptik, Parabolik, Hiperbolik), Deret Fourier Trigonometrik, Fenomena Gibbs ($8{,}95\%$), Total Harmonic Distortion (THD) Inverter PLTS IEEE Std 519-2022.
9. **Week 10 (`ch10.tex` / `ch10.pdf`):** Metode Pemisahan Variabel, Teori Masalah Nilai Batas Sturm-Liouville, Nilai Eigen \& Fungsi Eigen, Syarat Batas Dirichlet \& Neumann, Distribusi Suhu Busbar GITET 500 kV IEEE Std 738.
10. **Week 11 (`ch11.tex` / `ch11.pdf`):** Persamaan Gelombang 1D, Penurunan Persamaan Telegrafer dari Elemen Saluran $\Delta x$, Solusi d'Alembert, Koefisien Refleksi Beban $\Gamma_L$, Rasio Gelombang Berdiri (VSWR), Gelombang Berjalan Surja Petir SUTT 150 kV IEC 60071-1.
11. **Week 12 (`ch12.tex` / `ch12.pdf`):** Persamaan Difusi/Panas 1D, Pemanasan Joule $I^2 R$, Dekomposisi Solusi Tunak \& Transien, Konstanta Waktu Termal $\tau$, Perhitungan Kuat Hantar Arus (*Ampacity*) Kabel Tanah XLPE 20 kV Standar IEC 60287 / IEEE 835.
12. **Week 13 (`ch13.tex` / `ch13.pdf`):** Persamaan Laplace 2D Elektrostatika, Teorema Nilai Rata-rata Gauss, Diskritisasi FDM 5-Titik, Algoritma Relaksasi SOR, Gradien Medan Listrik \& Mitigasi Pelepasan Korona Isolator Tumpu 150 kV IEC 60060-1.
13. **Week 14 (`ch14.tex` / `ch14.pdf`):** Persamaan Diferensial Bessel Koordinat Silinder, Deret Frobenius, Fungsi Bessel Orde Pertama $J_\nu(x)$ \& Kedua $Y_\nu(x)$, Frekuensi Pancung Pandu Gelombang $\text{TM}_{01}$, Mekanisme Fisika Efek Kulit (*Skin Effect*), Solusi Kawat ACSR IEC 61089 \& Busbar Tubular Gardu Induk.
14. **Week 15 (`ch15.tex` / `ch15.pdf`):** Persamaan Laplace Koordinat Bola, Polinomial Legendre $P_n(\cos\theta)$, Potensial Bola Konduktor dalam Medan Seragam, 4 Persamaan Diferensial Maxwell, Arus Pergeseran Maxwell $\partial\vec{D}/\partial t$, Penurunan Kecepatan Cahaya $c = 1/\sqrt{\mu_0\epsilon_0}$, Vektor Poynting $\vec{S} = \vec{E}\times\vec{H}$, Standar Paparan Medan SUTET 500 kV IEEE C95.1 / Permen ESDM, dan Matriks Sintesis Akhir Kurikulum.

---

### B. Hasil Verifikasi Kualitas
Skrip verifikasi otomatis Python mengonfirmasi status sempurna untuk seluruh 14 salindia:
- **Tepat 15 frame/halaman per berkas** (tidak kurang dan tidak lebih).
- **Nol Overfull Warning** (0 `Overfull \hbox` dan 0 `Overfull \vbox` pada seluruh berkas log TeX).
- Seluruh diagram TikZ dan Circuitikz diskalakan secara responsif dengan `\resizebox{\linewidth}{!}{...}` atau `\resizebox{!}{0.38\textheight}{...}`.
- Seluruh kode komputasi numerik disajikan secara eksklusif dalam bahasa **Julia 1.12+** menggunakan pustaka `Plots.jl` dan `DifferentialEquations.jl`.
- Seluruh lembar evaluasi menyertakan soal berjenjang Taksonomi Bloom C1 s.d. C6.

---

### C. Sinkronisasi Portal & Deployment
1. Seluruh 14 file `ch*.pdf` telah disinkronkan ke:
   - `portal/public/pdf/`
   - `/Users/novaliodaratha/Documents/ndaratha.my.id/public/persamaan-diferensial/pdf/`
2. Pembangunan situs statis portal Astro (`npm run build`) berhasil 100% tanpa galat.
3. Sinkronisasi direktori `dist/` ke repositori web utama `ndaratha.my.id` berhasil ditransfer.
4. **Deployment Produksi Vercel:** Berhasil dipublikasikan secara langsung (*live*) ke domain utama `https://www.ndaratha.my.id/persamaan-diferensial/` dengan respons HTTP 200 untuk seluruh berkas PDF perkuliahan.

---

## 3. Status Akhir
Seluruh target perbaikan salindia mata kuliah Persamaan Diferensial telah diselesaikan dengan kualitas akademis profesional tanpa kompromi.
