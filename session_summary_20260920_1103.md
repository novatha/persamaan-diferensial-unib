# Ringkasan Sesi Perkuliahan: Finalisasi Monograf Lengkap Modul 1--15 Persamaan Diferensial Teknik Elektro UNIB
**Tanggal & Waktu:** 20 September 2026, 11:03 WIB  
**Berkas:** `session_summary_20260920_1103.md`  
**Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Institusi:** Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika, Fakultas Teknik, Universitas Bengkulu  
**URL Portal Produksi:** [https://www.ndaratha.my.id/persamaan-diferensial/](https://www.ndaratha.my.id/persamaan-diferensial/)

---

## 1. Ikhtisar Pencapaian Utama

Pada sesi ini, telah dituntaskan secara menyeluruh pembuatan, standardisasi, kompilasi bebas galat (*zero overfull hbox*), pengujian jumlah kata (*$\ge 1.200$ kata substansi*), integrasi visualisasi komputasi ilmiah terbuka berbasis bahasa **Julia**, sinkronisasi aset, pembuatan aplikasi web portal perkuliahan Astro, serta deployment langsung ke peladen produksi Vercel untuk **seluruh pekan perkuliahan (Minggu 1 s.d. 15)**.

---

## 2. Inventaris Lengkap Monograf Modul Ajar (Minggu 1 s.d. 15)

Seluruh modul mengacu pada **Kerangka 4-Pilar Pedagogis Berbasis OBE**:
1. **Intuisi Fisika Rekayasa (*Physical Intuition*):** Dinamika energi elemen $R, L, C$, garis medan $\vec{E}$ dan $\vec{B}$, serta perambatan gelombang.
2. **Derivasi Eksplisit (*First-Principles*):** Penurunan analitis bertahap tanpa lompatan baris (*no skipped steps*).
3. **Komputasi Numerik Terbuka (*Open-Source Scientific Computing*):** Menggunakan bahasa **Julia** (`DifferentialEquations.jl` & `Plots.jl`).
4. **Standar Industri Rekayasa Elektro:** Mengacu pada standar operasional PLN, IEEE (Std 142, Std 605, Std 18, Std 738), dan IEC (60502, 61089, 62271, 60871).

| Berkas Modul | Pekan | Topik Utama & Ruang Lingkup | Jumlah Kata | Halaman | Status Kompilasi |
| :--- | :---: | :--- | :---: | :---: | :---: |
| `modul_1.tex` | W1 | Klasifikasi PD, Nilai Awal (IVP), Kontinuitas Energi \& Pemodelan Rangkaian RL | 2.572 kata | 17 hal | **Zero Overfull \hbox** |
| `modul_2.tex` | W2 | PDB Orde 1: Metode Separabel \& Faktor Integrasi Rangkaian Listrik | 2.521 kata | 19 hal | **Zero Overfull \hbox** |
| `modul_3.tex` | W3 | Aplikasi Rekayasa: Transien Pengisian RC, Pengosongan RL, \& Batas Termal Konduktor | 2.724 kata | 17 hal | **Zero Overfull \hbox** |
| `modul_4.tex` | W4 | PDB Linier Orde 2 Homogen, Determinan Wronskian, \& Dinamika Tangki Osilator LC | 1.941 kata | 16 hal | **Zero Overfull \hbox** |
| `modul_5.tex` | W5 | PDB Linier Orde 2 Non-Homogen, Koefisien Tak Tentu, \& Resonansi RLC Seri AC | 1.744 kata | 14 hal | **Zero Overfull \hbox** |
| `modul_6.tex` | W6 | Transformasi Laplace Dasar, Sifat Linieritas, Teorema Translasi/Geser Waktu | 1.589 kata | 14 hal | **Zero Overfull \hbox** |
| `modul_7.tex` | W7 | Invers Laplace, Pecahan Parsial, Konvolusi, \& Analisis Transien Rangkaian Domain $s$ | 2.811 kata | 17 hal | **Zero Overfull \hbox** |
| `modul_uts` | W8 | *Evaluasi Tengah Semester: Ujian Tengah Semester (UTS)* | -- | -- | *Terjadwal* |
| `modul_9.tex` | W9 | Pengantar Persamaan Diferensial Parsial (PDP) \& Analisis Spektrum Deret Fourier AC | 2.223 kata | 14 hal | **Zero Overfull \hbox** |
| `modul_10.tex` | W10 | Solusi PDP Metode Pemisahan Variabel, Masalah Nilai Batas \& Nilai Eigen Spasial | 2.080 kata | 13 hal | **Zero Overfull \hbox** |
| `modul_11.tex` | W11 | Persamaan Gelombang 1D (Hiperbolik): Persamaan Telegrafer Saluran Transmisi & Surja Petir | 1.745 kata | 12 hal | **Zero Overfull \hbox** |
| `modul_12.tex` | W12 | Persamaan Panas/Difusi 1D (Parabolik): Disipasi Termal Konduktor & Kabel Bawah Tanah | 1.873 kata | 12 hal | **Zero Overfull \hbox** |
| `modul_13.tex` | W13 | Persamaan Laplace 2D Kartesian (Eliptik): Pemetaan Potensial Elektrostatik \& Pembumian | 2.042 kata | 14 hal | **Zero Overfull \hbox** |
| `modul_14.tex` | W14 | PD Koefisien Variabel, Metode Frobenius, Fungsi Bessel \& Efek Kulit (*Skin Effect*) ACSR | 1.741 kata | 12 hal | **Zero Overfull \hbox** |
| `modul_15.tex` | W15 | Polinomial Legendre, Koordinat Bola, 4 Persamaan Maxwell Diferensial \& Sintesis Kurikulum | 2.664 kata | 16 hal | **Zero Overfull \hbox** |
| `modul_uas` | W16 | *Evaluasi Akhir Semester: Ujian Akhir Semester (UAS)* | -- | -- | *Terjadwal* |

---

## 3. Komputasi Ilmiah Terbuka (Julia 1.12+)

Setiap modul ajar dilengkapi modul praktikum numerik dengan kode sumber program Julia yang siap dieksekusi:
- **Minggu 1 s.d. 5:** Solusi dinamika transien rangkaian $RL, RC, LC, RLC$ menggunakan paket standar dunia `DifferentialEquations.jl` (`OrdinaryDiffEq.jl`).
- **Minggu 6 s.d. 7:** Transformasi Laplace dan respon frekuensi impuls/step domain waktu vs domain $s$.
- **Minggu 9 s.d. 13:** Analisis harmonisa deret Fourier, animasi gelombang berjalan d'Alembert saluran transmisi, difusi panas kabel tanah, dan kontur 2D potensial Laplace grid elektrostatika.
- **Minggu 14 s.d. 15:** Evaluasi fungsi Bessel $J_0(x), J_1(x), Y_0(x)$, pemetaan kerapatan arus frekuensi tinggi (*skin effect*), Polinomial Legendre $P_n(x)$ orde $0$ s.d. $4$, dan pemetaan kontur potensial ekipotensial bola konduktor terbumikan di bawah medan eksternal $E_0 \hat{a}_z$.

---

## 4. Sinkronisasi & Deployment Produksi (Vercel)

1. **Aplikasi Portal Web Perkuliahan (Astro 7.2.0):**
   - Berhasil dikompilasi menggunakan `npm run build` di direktori `./portal`.
   - Mengintegrasikan rute `/materi`, `/silabus`, `/tugas`, dan `/ujian` dengan tautan langsung ke berkas PDF monograf, salindia presentasi, lembar kerja (*worksheet*), dan bank soal (*problem set*).
2. **Sinkronisasi Multi-Repositori:**
   - Direktori lokal: `./portal/public/pdf/`
   - Direktori build: `./portal/dist/`
   - Direktori web utama: `/Users/novaliodaratha/Documents/ndaratha.my.id/public/persamaan-diferensial/`
3. **Penyebaran Produksi (*Production Deployment*):**
   - Diluncurkan melalui perintah `npx vercel --prod --yes` di repositori web `ndaratha.my.id`.
   - Domain resmi: `https://www.ndaratha.my.id/persamaan-diferensial/`
   - Pengujian live via `curl -sI` memastikan status **HTTP/2 200 OK** untuk seluruh berkas monograf yang baru diunggah (`modul_14.pdf`, `modul_15.pdf`, dan halaman `/materi`).
