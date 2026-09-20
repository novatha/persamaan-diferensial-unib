# Rangkuman Sesi Perkuliahan: Integrasi Tautan YouTube & Sinkronisasi Seluruh Dokumen Pembelajaran
**Tanggal & Waktu:** Minggu, 20 September 2026, 20:50 WIB  
**Mata Kuliah:** Persamaan Diferensial (TEE-203) — S1 Teknik Elektro UNIB  
**Dosen Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Domain Portal:** [https://pd.ndaratha.my.id](https://pd.ndaratha.my.id)  
**Playlist YouTube Resmi:** [https://www.youtube.com/playlist?list=PLS5oOZWXZeTw](https://www.youtube.com/playlist?list=PLS5oOZWXZeTw)

---

## 1. Sasaran & Capaian Pekerjaan
Sesuai instruksi pengguna: *"Tambahkan link youtube ke protal mata kuliah. Update juga slide, probelm set, catatan kuliah dan lembar kerja mahasiswa."*, seluruh materi ajar dan portal web perkuliahan telah diperbarui secara komprehensif:

1. **Pembaruan Portal Web (`pd.ndaratha.my.id`):**
   - **Bilah Navigasi (`Navbar.astro`):** Menambahkan tombol aksi khusus **"YouTube Playlist"** dengan ikon YouTube, tautan langsung ke playlist resmi, serta efek cahaya merah (*red glow*) yang serasi dengan tema *glassmorphism* portal. Menu navigasi *mobile drawer* juga dilengkapi tautan YouTube.
   - **Halaman Materi (`materi.astro`):** Menyematkan tombol akses cepat ke Playlist Resmi YouTube di area tajuk utama (*lead header*).
   - **Kartu Pembelajaran (`PdWeekCard.astro`):** Memastikan seluruh 14 kartu minggu pembelajaran menampilkan tombol langsung **"YouTube"** (`doc-btn-yt`) yang mengarah ke rekaman video kuliah per pekan.
   - **Halaman Tugas & Solved Problems (`tugas.astro`):** Menambahkan tombol **"Video Kuliah"** (`btn-yt`) pada setiap kartu tugas terstruktur sehingga mahasiswa dapat langsung menyimak penjelasan dosen sebelum mengerjakan soal.

2. **Pembaruan Seluruh Dokumen Materi Perkuliahan (56 Dokumen LaTeX):**
   - **14 Salindia Beamer (`ch1.tex` s.d. `ch15.tex`, tanpa pekan 8):**
     - Pada Salindia Judul (Frame 1): Ditambahkan tautan video spesifik pekan tersebut dan tautan playlist lengkap di bawah tanggal perkuliahan.
     - Pada Salindia Penutup (Frame 15): Ditambahkan kotak/baris tautan video kuliah YouTube, playlist resmi, dan portal web perkuliahan.
   - **14 Diktat / Catatan Kuliah Monograf (`modul_1.tex` s.d. `modul_15.tex`):**
     - Disisipkan kotak resmi bergaris tepi merah (*official YouTube banner tcolorbox*) tepat di bawah `\maketitle` sebelum kotak Sub-CPMK, memuat tautan video kuliah resmi, playlist lengkap, dan portal akademik.
   - **14 Problem Set Tugas Terstruktur (`problem_set1.tex` s.d. `problem_set15.tex`):**
     - Ditambahkan tautan video kuliah spesifik dan *shortlink* playlist di dalam kotak Sub-CPMK dan pedoman tugas.
     - Ditambahkan tautan video pada *footer* halaman kiri (`\lfoot`).
   - **14 Lembar Kerja Mahasiswa / LKM (`worksheet1.tex` s.d. `worksheet15.tex`):**
     - Ditambahkan tautan video panduan dan playlist pada kotak informasi Sub-CPMK & Alokasi Waktu.
     - Ditambahkan tautan video pada *footer* halaman kiri (`\lfoot`).

---

## 2. Tabel Pemetaan Tautan YouTube Resmi per Pekan

| Pekan | Topik Perkuliahan | ID Video | Tautan YouTube Resmi | Status Dokumen (Slide, Modul, PS, LKM) |
| :---: | :--- | :---: | :---: | :---: |
| **01** | Pengantar & Klasifikasi PD, Dinamika Energi RL | `Zq6IbzuVLBw` | [youtu.be/Zq6IbzuVLBw](https://youtu.be/Zq6IbzuVLBw) | **Diperbarui & Kompilasi Sempurna** |
| **02** | PDB Orde 1: Separabel, Eksak & Faktor Integrasi RC | `5GQHKrvaSwg` | [youtu.be/5GQHKrvaSwg](https://youtu.be/5GQHKrvaSwg) | **Diperbarui & Kompilasi Sempurna** |
| **03** | Aplikasi PDB Orde 1: Transien & Termal Trafo | `_JZ7kBkgxlk` | [youtu.be/_JZ7kBkgxlk](https://youtu.be/_JZ7kBkgxlk) | **Diperbarui & Kompilasi Sempurna** |
| **04** | PDB Linier Orde 2 Homogen: 3 Ragam Redaman & LC | `be3FdcQkq6o` | [youtu.be/be3FdcQkq6o](https://youtu.be/be3FdcQkq6o) | **Diperbarui & Kompilasi Sempurna** |
| **05** | PDB Orde 2 Non-Homogen & Resonansi RLC Seri AC | `x15SuJBvZQE` | [youtu.be/x15SuJBvZQE](https://youtu.be/x15SuJBvZQE) | **Diperbarui & Kompilasi Sempurna** |
| **06** | Transformasi Laplace Dasar & Teorema Pergeseran | `iIYM-WRaTiU` | [youtu.be/iIYM-WRaTiU](https://youtu.be/iIYM-WRaTiU) | **Diperbarui & Kompilasi Sempurna** |
| **07** | Invers Laplace & Rangkaian Domain Frekuensi s | `crWRyniSoi0` | [youtu.be/crWRyniSoi0](https://youtu.be/crWRyniSoi0) | **Diperbarui & Kompilasi Sempurna** |
| **09** | Pengantar PDP & Analisis Deret Fourier SPWM | `VaRiwphPnaw` | [youtu.be/VaRiwphPnaw](https://youtu.be/VaRiwphPnaw) | **Diperbarui & Kompilasi Sempurna** |
| **10** | Solusi PDP: Metode Pemisahan Variabel | `oEBvpt86fvI` | [youtu.be/oEBvpt86fvI](https://youtu.be/oEBvpt86fvI) | **Diperbarui & Kompilasi Sempurna** |
| **11** | Persamaan Gelombang 1D & Telegrafer Transmisi | `RxoN7UaK3OI` | [youtu.be/RxoN7UaK3OI](https://youtu.be/RxoN7UaK3OI) | **Diperbarui & Kompilasi Sempurna** |
| **12** | Persamaan Panas 1D & Batas Ampacity Konduktor | `piBpNjXaKpQ` | [youtu.be/piBpNjXaKpQ](https://youtu.be/piBpNjXaKpQ) | **Diperbarui & Kompilasi Sempurna** |
| **13** | Persamaan Laplace 2D & Relaksasi Beda Hingga | `JgFsCfTgg4U` | [youtu.be/JgFsCfTgg4U](https://youtu.be/JgFsCfTgg4U) | **Diperbarui & Kompilasi Sempurna** |
| **14** | Fungsi Bessel Silinder & Efek Kulit (Skin Effect) | `VidTzwMhRDo` | [youtu.be/VidTzwMhRDo](https://youtu.be/VidTzwMhRDo) | **Diperbarui & Kompilasi Sempurna** |
| **15** | Sintesis 4 Persamaan Maxwell & Gelombang EM 3D | `J4XziBcVtfk` | [youtu.be/J4XziBcVtfk](https://youtu.be/J4XziBcVtfk) | **Diperbarui & Kompilasi Sempurna** |

---

## 3. Verifikasi Mutu & Kepatuhan Standar Dokumen
- **Zero Compilation Errors:** Seluruh 56 berkas LaTeX berhasil dikompilasi secara paralel menggunakan `pdflatex` dengan kode keluar 0 (*Exit Code: 0*).
- **Penanganan Khusus Karakter URL:** Menggunakan perintah LaTeX `\url{...}` untuk menghindari kendala karakter khusus seperti garis bawah (`_`) pada video Minggu 3 (`_JZ7kBkgxlk`).
- **Kepatuhan Ketat 2 Halaman:** Seluruh 14 berkas `worksheet*.pdf` dan 14 berkas `problem_set*.pdf` diverifikasi otomatis menggunakan utilitas `pdfinfo`. Seluruh berkas tepat **2 halaman** (100% patuh, tanpa halaman yatim / *orphan pages*).
- **Sinkronisasi Berkas Publik:** Seluruh berkas PDF yang telah diperbarui disinkronkan ke:
  - `docs/files/*.pdf`
  - `portal/public/pdf/*.pdf`
  - `portal/dist/pdf/*.pdf`
  - `/Users/novaliodaratha/Documents/ndaratha.my.id/public/persamaan-diferensial/pdf/*.pdf`

---

## 4. Penggelaran & Verifikasi Produksi
- **Build Astro Portal:** Berhasil dikompilasi ke static bundle (`portal/dist/`) dalam 1,13 detik.
- **Build MkDocs:** Berhasil dibersihkan dan dibangun ulang dalam 0,67 detik.
- **Penggelaran Vercel Production:** Berhasil digelarkan (*Aliased to `https://pd.ndaratha.my.id`*).
- **Pemeriksaan HTTP Live:**
  ```http
  HTTP/2 200 
  server: Vercel
  content-type: text/html; charset=utf-8
  date: Sun, 20 Sep 2026 13:47:36 GMT
  ```
