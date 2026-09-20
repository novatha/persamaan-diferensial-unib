# Ringkasan Sesi Perkuliahan: Perbaikan Menyeluruh Salindia Presentasi (ch1.tex s.d. ch15.tex)
**Tanggal & Waktu:** 20 September 2026, 11:22 WIB  
**Berkas:** `session_summary_20260920_1122.md`  
**Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Institusi:** Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika, Fakultas Teknik, Universitas Bengkulu  
**URL Portal Produksi:** [https://www.ndaratha.my.id/persamaan-diferensial/](https://www.ndaratha.my.id/persamaan-diferensial/)

---

## 1. Masalah yang Diidentifikasi pada Berkas Salindia Awal (`ch*.tex`)

1. **Overfull \hbox Berulang pada Seluruh Salindia:**
   - Karena ketiadaan opsi judul pendek dan nama pengampu pendek (`\author[...]{...}` dan `\title[...]{...}`), tema Beamer Madrid secara otomatis memasukkan string nama institusi multi-baris (`Program Studi Teknik Elektro\\Universitas Bengkulu`) ke dalam *footline* kiri (`\insertshortauthor`), menyebabkan galat *Overfull \hbox* sebesar 45–52 pt di setiap halaman pada seluruh berkas (`ch1.tex` hingga `ch15.tex`).
   - Format tanggal yang memuat baris baru manual (`2026 \\ \vspace{2mm}\small...`) meluber pada kotak navigasi kanan *footline*.
2. **Ketiadaan Mode `[plain]` pada Salindia Judul:**
   - Salindia judul awal memuat bilah navigasi atas dan bawah sehingga memicu peringatan `Overfull \vbox (12.75pt too high)`.
3. **Galat Tata Letak & Spasi Vertikal pada Salindia Tertentu:**
   - `ch2.tex`: Soal separabel memuat 4 baris rumus `$$...$$` bertingkat yang melampaui batas tinggi bingkai.
   - `ch4.tex`: Kuis redaman kritis meluap 0,96 pt secara vertikal.
   - `ch7.tex`: Diagram TikZ alur transformasi Laplace melebihi lebar bingkai (`8.9pt too wide`) dan blok pecahan parsial meluap secara vertikal.
   - `ch9.tex`: Tiga persamaan diferensial parsial dalam enumerasi blok meluap 20,28 pt secara vertikal.
   - `ch15.tex`: Empat blok persamaan Maxwell ditumpuk dalam satu salindia tunggal sehingga meluap 6,85 pt secara vertikal.

---

## 2. Solusi & Perbaikan yang Diterapkan

1. **Standardisasi Metadata & Branding Institusional UNIB:**
   - `\author[Novalio \& Arfan (UNIB)]{Ir. Novalio Daratha, S.T., M.Sc., Ph.D. \& Muhammad Arfan, S.T., M.T.}`
   - `\institute[Teknik Elektro UNIB]{Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro \& Informatika\\Fakultas Teknik, Universitas Bengkulu}`
   - `\title[Persamaan Diferensial (Minggu N)]{Persamaan Diferensial}`
   - `\date[2026]{Semester Genap 2026}`
   - Salindia judul kini menggunakan `\begin{frame}[plain]\titlepage\end{frame}`.
   - Palet warna Beamer resmi UNIB: Navy (`#002060`), Emas (`#C5A059`), dan Hijau (`#22703C`) diterapkan secara konsisten pada *palette primary, secondary, tertiary, structure, block, alertblock,* dan *exampleblock*.
2. **Resolusi Tata Letak Khusus:**
   - `ch2.tex`: Mengubah derivasi bertahap menjadi formula ringkas sehingga bebas luapan vertikal.
   - `ch4.tex`: Memperbaiki spasi kuis redaman kritis menjadi daftar ringkas.
   - `ch7.tex`: Membungkus diagram TikZ dengan `\resizebox{0.92\linewidth}{!}{...}` dan memadatkan dekomposisi pecahan parsial.
   - `ch9.tex`: Mengganti enumerasi persamaan klasik menjadi daftar item kompak.
   - `ch15.tex`: Membagi 4 Persamaan Maxwell ke dalam 2 salindia tematik (Salindia 1: Hukum Gauss Listrik & Magnet; Salindia 2: Hukum Faraday & Ampere-Maxwell).

---

## 3. Hasil Kompilasi & Verifikasi Menyeluruh

Semua 14 berkas salindia perkuliahan telah dikompilasi ulang dengan `pdflatex` (2 kali lintasan):

| Berkas Salindia | Pekan Perkuliahan | Status Kompilasi | Keterangan Luapan (*Overfull*) |
| :---: | :---: | :---: | :---: |
| `ch1.tex` | Minggu 1: Klasifikasi PDB/PDP, IVP, \& Pemodelan Fisik | **LULUS (0 Error)** | **0 Overfull (Sempurna)** |
| `ch2.tex` | Minggu 2: PDB Orde 1 (Separabel, Eksak, Faktor Integrasi) | **LULUS (0 Error)** | **0 Overfull (Sempurna)** |
| `ch3.tex` | Minggu 3: Aplikasi PDB Orde 1 (Transien RC, RL, \& Termal) | **LULUS (0 Error)** | **0 Overfull (Sempurna)** |
| `ch4.tex` | Minggu 4: PDB Linier Orde 2 Homogen Koefisien Konstan | **LULUS (0 Error)** | **0 Overfull (Sempurna)** |
| `ch5.tex` | Minggu 5: PDB Linier Orde 2 Non-Homogen \& Transien RLC | **LULUS (0 Error)** | **0 Overfull (Sempurna)** |
| `ch6.tex` | Minggu 6: Transformasi Laplace Dasar \& Teorema Geser | **LULUS (0 Error)** | **0 Overfull (Sempurna)** |
| `ch7.tex` | Minggu 7: Invers Laplace \& Solusi PDB Rangkaian Domain $s$ | **LULUS (0 Error)** | **0 Overfull (Sempurna)** |
| `ch9.tex` | Minggu 9: Pengantar PDP \& Analisis Deret Fourier | **LULUS (0 Error)** | **0 Overfull (Sempurna)** |
| `ch10.tex` | Minggu 10: Metode Pemisahan Variabel (*Separation of Variables*) | **LULUS (0 Error)** | **0 Overfull (Sempurna)** |
| `ch11.tex` | Minggu 11: Persamaan Gelombang 1D Saluran Transmisi | **LULUS (0 Error)** | **0 Overfull (Sempurna)** |
| `ch12.tex` | Minggu 12: Persamaan Panas 1D \& Manajemen Termal Kabel | **LULUS (0 Error)** | **0 Overfull (Sempurna)** |
| `ch13.tex` | Minggu 13: Persamaan Laplace 2D \& Potensial Elektrostatik | **LULUS (0 Error)** | **0 Overfull (Sempurna)** |
| `ch14.tex` | Minggu 14: Fungsi Bessel \& Efek Kulit (*Skin Effect*) Silinder | **LULUS (0 Error)** | **0 Overfull (Sempurna)** |
| `ch15.tex` | Minggu 15: Sintesis PDP dalam 4 Persamaan Maxwell | **LULUS (0 Error)** | **0 Overfull (Sempurna)** |

---

## 4. Sinkronisasi & Deployment Produksi (Vercel)

- Seluruh berkas PDF hasil kompilasi (`ch1.pdf` s.d. `ch15.pdf`) telah disinkronkan ke `./portal/public/pdf/` dan repositori utama `/Users/novaliodaratha/Documents/ndaratha.my.id/public/persamaan-diferensial/pdf/`.
- Portal web perkuliahan (Astro) berhasil dibangun ulang (`npm run build`).
- Sukses dideploy ke Vercel production: `https://www.ndaratha.my.id/persamaan-diferensial/`.
- Uji live via `curl -sI` mengonfirmasi status **HTTP/2 200 OK** untuk seluruh berkas salindia.
