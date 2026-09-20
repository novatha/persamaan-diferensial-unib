# Ringkasan Sesi Kerja: Perbaikan Gambar 1, Standar Modul 1200 Kata & Integrasi Julia
**Waktu Pelaksanaan:** Minggu, 20 September 2026, 09:07 WIB  
**Mata Kuliah:** Persamaan Diferensial (TEE-203) - S1 Teknik Elektro Universitas Bengkulu  
**Dosen Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  

---

## 1. Pemenuhan Instruksi & Permintaan Pengguna

### A. Perbaikan Overflow Gambar 1 pada Modul 1 (`modul_1.tex` & `modul_1.pdf`)
- **Akar Masalah:**
  - Pada versi awal, diagram TikZ 16 minggu pada Gambar 1 melebihi batas margin halaman kanan (`Overfull \hbox (127.6pt too wide)`), menyebabkan kolom Minggu 4, 5, 12, dan 13 terpotong saat diekspor ke PDF.
  - Selain itu, header `fancyhdr` mengalami tumpang tindih teks di bagian tengah antara judul mata kuliah dan judul modul ajar.
- **Solusi Komprehensif yang Diterapkan:**
  1. **Geometri TikZ & Skala Penuh:** Diagram dibungkus dengan `\resizebox{\linewidth}{!}{% ... %}` dengan styling seragam (`text width=3.35cm, minimum height=1.05cm`), memastikan 4 kolom tersusun presisi dalam batas margin A4 tanpa terpotong (0 pt overflow).
  2. **Perbaikan Header `fancyhdr`:** Mengubah teks header kiri dan kanan menjadi ringkas dan elegan:
     - Header Kiri: `\small\textbf{Persamaan Diferensial 2026} -- Teknik Elektro UNIB`
     - Header Kanan: `\small Modul 1: Pengantar \& Klasifikasi PD`
  3. **Pembersihan Tipografi:** Menghilangkan seluruh artefak markdown mentah (`**`, `*`, `---`), memperbaiki judul bab agar pas satu baris, dan menambahkan `\texorpdfstring` pada judul subbab yang memuat simbol matematika.
  4. **Kompilasi Sukses:** Dua putaran kompilasi `pdflatex` menghasilkan 17 halaman PDF bersih tanpa error dan tanpa `Overfull \hbox`.

---

### B. Adopsi Bahasa Pemrograman Julia sebagai Standar Komputasi Mata Kuliah
- Berdasarkan arahan resmi: *"Untuk programming pada mata kuliah persamaan diferensial, gunakan Julia."*
- **Tindakan Pembaruan:**
  1. **Pembaruan Pedoman Pedagogis ([`AGENTS.md`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/AGENTS.md)):**
     - Memperbarui Pilar 3 menjadi: **Komputasi Numerik Terbuka Berbasis Julia (`DifferentialEquations.jl`, `Plots.jl` & Pluto Notebooks)**.
  2. **Pembaruan Modul 1 ([`modul_1.tex`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/modul_1.tex)):**
     - Mengganti bagian praktikum komputasi dengan skrip modular **Julia 1.12+**.
     - Menggunakan pustaka standar ilmiah global `DifferentialEquations.jl` dengan algoritma adaptif `Tsit5()` (Tsitouras 5/4 Runge-Kutta) untuk memvalidasi Masalah Nilai Awal (IVP) pengisian transien rangkaian RL terhadap solusi eksak analitik.
     - Menyertakan visualisasi resolusi tinggi menggunakan pustaka `Plots.jl`.
     - Menyesuaikan Sub-CPMK C6 dan soal evaluasi perancangan C6 ke bahasa Julia.
  3. **Pembaruan Basis Data Portal ([`portal/src/data/pdData.ts`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/portal/src/data/pdData.ts)):**
     - Menyelaraskan seluruh 14 pekan topik praktikum komputasi ke ekosistem Julia (`DifferentialEquations.jl`, `Symbolics.jl`, `SpecialFunctions.jl`, dan Pluto Notebooks).

---

### C. Pemenuhan Standar Panjang Modul Minimal 1.200 Kata
- Berdasarkan arahan resmi: *"Untuk modul, jumlah kata minimal adalah 1200 kata."*
- **Verifikasi Pengukuran Kata (`texcount`):**
  - **Jumlah Kata Teks Substantif:** **2.572 kata** (lebih dari dua kali lipat syarat minimum 1.200 kata).
  - **Jumlah Kata Judul/Header:** 205 kata.
  - **Total Kata Keseluruhan:** ~2.824 kata dalam 17 halaman monograf.
- Aturan ini telah dibakukan secara eksplisit pada Bab 2 dokumen [`AGENTS.md`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/AGENTS.md) sebagai acuan baku wajib untuk penyusunan Modul 2 hingga Modul 15.

---

## 2. Sinkronisasi Aset & Deployment Produksi
1. **Pembaruan Berkas PDF:**
   - [`modul_1.pdf`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/modul_1.pdf) (421 KB, 17 halaman) disalin ke:
     - `portal/public/pdf/modul_1.pdf`
     - `docs/files/modul_1.pdf`
     - `/Users/novaliodaratha/Documents/ndaratha.my.id/public/persamaan-diferensial/pdf/modul_1.pdf`
2. **Kompilasi Portal Astro:**
   - Menjalankan `npm run build` di direktori `./portal`, sukses membuat rute statis `dist/` dalam 582 ms.
   - Melakukan sinkronisasi `rsync` ke repositori produksi `ndaratha.my.id`.
3. **Pembaruan Git & Vercel:**
   - Melakukan commit dan push ke cabang `main` di GitHub (`novatha/ndaratha.my.id`).
   - Memicu deployment produksi Vercel (`https://www.ndaratha.my.id/persamaan-diferensial/materi`).

---

## 3. Rencana Langkah Selanjutnya
1. Melanjutkan penulisan monograf **Modul 2** (`modul_2.tex`): PDB Orde 1 (Separabel, Eksak, Faktor Integrasi) dengan standar monograf >1.200 kata, skema 12 bagian, dan skrip komputasi berbasis Julia (`Symbolics.jl` dan `DifferentialEquations.jl`).
2. Melanjutkan pembuatan video perkuliahan otomatis untuk Minggu 3 menggunakan pipeline Beamer, Microsoft Edge TTS (`id-ID-ArdiNeural`), dan ffmpeg 1080p.
