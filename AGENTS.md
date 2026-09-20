# Panduan & Standar Pedoman Pembelajaran (AGENTS.md)
Mata Kuliah: Persamaan Diferensial (Fokus Persiapan Medan Elektromagnetika & Rangkaian Listrik)
Dosen Pengampu: Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.
Institusi: Program Studi Teknik Elektro, Jurusan Teknik Elektro & Informatika, Fakultas Teknik, Universitas Bengkulu

---

## 1. Prinsip Utama: Model 4-Pilar Pedagogis Berbasis OBE

Setiap penyusunan modul ajar, salindia presentasi, lembar kerja, problem set, maupun video perkuliahan untuk mata kuliah ini WAJIB mengacu pada **Kerangka 4-Pilar Pedagogis**:

1. **Pilar 1: Intuisi Fisika Rekayasa (*Engineering Physics & Physical Intuition*)**
   - Menguraikan fenomena fisis nyata sebelum masuk ke perumusan matematika abstrak.
   - Mengaitkan persamaan diferensial dengan dinamika energi pada elemen rangkaian terpusat (resistor disipatif, induktor penyimpan medan magnet $\frac{1}{2} L i^2$, kapasitor penyimpan medan listrik $\frac{1}{2} C v^2$) serta hukum kekekalan muatan dan fluks.
   - Pada tingkat lanjut (PDP), menjelaskan fenomena gelombang berjalan dan gelombang berdiri pada saluran transmisi, distribusi potensial elektrostatika pada ruang bebas muatan, dan difusi medan elektromagnetik (efek kulit / *skin effect*).

2. **Pilar 2: Derivasi Matematis Eksplisit (*First-Principles Derivations*)**
   - Menurunkan solusi persamaan secara analitis langkah demi langkah tanpa melompati baris (*no skipped steps*).
   - Menjelaskan makna fisis setiap konstanta integrasi yang ditentukan oleh Masalah Nilai Awal (*Initial Value Problem* / IVP) maupun Masalah Nilai Batas (*Boundary Value Problem* / BVP).
   - Menguasai metode-metode standar: PDB orde 1 (Separabel, Eksak, Faktor Integrasi), PDB orde 2 koefisien konstan (akar karakteristik real berbeda, real kembar, kompleks konjugat), Transformasi Laplace dan Invers Laplace, Deret Fourier, serta Pemisahan Variabel (*Separation of Variables*) pada sistem koordinat Kartesian, Silinder (Fungsi Bessel), dan Bola (Polinomial Legendre).

3. **Pilar 3: Komputasi Numerik Terbuka Berbasis Julia (DifferentialEquations.jl, Plots.jl & Pluto Notebooks)**
   - Menggunakan bahasa pemrograman ilmiah modern berkecepatan tinggi dan bebas lisensi (*open-source*): **Julia** (didukung oleh pustaka ekosistem terbaik dunia untuk pemodelan dinamika sistem seperti \texttt{DifferentialEquations.jl}, \texttt{OrdinaryDiffEq.jl}, dan visualisasi grafik dengan \texttt{Plots.jl}).
   - Menyediakan visualisasi interaktif berupa kurva transien respon waktu (overdamped, critically damped, underdamped), animasi perambatan gelombang 1D, serta kontur garis medan dan potensial elektrostatika 2D/3D (Laplace/Poisson).
   - Skrip harus terdokumentasi rapi, modular, efisien (type-stable), dan siap dijalankan secara mandiri oleh mahasiswa di laptop masing-masing tanpa hambatan lisensi berbayar.

4. **Pilar 4: Aplikasi Nyata Bidang Teknik Elektro & Standar Industri**
   - Mengintegrasikan aplikasi riil keteknikan: saluran transmisi daya tegangan tinggi (persamaan telegrafer), kabel koaksial, pembumian transformator gardu induk, fenomena transien switching, serta landasan matematis menuju 4 Persamaan Maxwell (Gauss, Faraday, Ampere-Maxwell).

---

## 2. Standar Modul Ajar (Diktat / Monograf Perkuliahan)

Setiap penyusunan modul ajar mingguan wajib mematuhi standar monograf berikut:
1. **Panjang Teks Minimum:** Wajib memiliki panjang teks minimal **1.200 kata** substansi pedagogis akademis (tidak termasuk kode program, tabel, dan caption).
2. **Struktur Standar 12 Bagian:** Mengikuti blueprint modul standar institusi:
   - Sub-CPMK OBE dalam `tcolorbox` (C1 s.d. C6)
   - Peta Konsep & Posisi Modul dalam Kurikulum (diagram alir TikZ skala penuh responsif)
   - Pendahuluan & Filosofi Fisika Rekayasa Elektro
   - Taksonomi, Definisi Formal & Teorema Matematis Eksplisit
   - Masalah Nilai Awal (IVP) / Masalah Nilai Batas (BVP) & Prinsip Kontinuitas Energi
   - Pemodelan Fisis Rangkaian / Medan dari Prinsip Dasar (*First-Principles*)
   - Dinamika Transien & Skala Waktu Alami
   - Studi Kasus Nyata Bidang Teknik Elektro & Standar Industri (PLN, IEEE)
   - Contoh Soal Terhitung Numerik Langkah demi Langkah (*Worked Examples*)
   - Praktikum Komputasi Numerik Terbuka Berbasis **Julia** (\texttt{DifferentialEquations.jl} \& \texttt{Plots.jl})
   - Evaluasi & Bank Soal Terstruktur Taksonomi Bloom (C1 s.d. C6)
   - Rangkuman, Glosarium Istilah Teknis, dan Referensi Standar Industri
3. **Bahasa Pemrograman Komputasi:** Wajib menggunakan **Julia** sebagai bahasa komputasi ilmiah utama.
4. **Kualitas Tipografi & Tata Letak:** Bebas kesalahan tumpukan teks atau pemotongan batas halaman (Zero `Overfull \hbox`). Diagram TikZ wajib dibungkus `\resizebox{\linewidth}{!}{...}` agar presisi dengan lebar kolom teks.

---

## 3. Standar Lembar Kerja Mahasiswa (Worksheet) & Problem Set

Setiap instrumen evaluasi dan latihan mingguan harus:
1. **Mencakup Ranah Kognitif Taksonomi Bloom Berjenjang (C1 s.d. C6):**
   - **C1 (Mengingat):** Definisi, klasifikasi orde, derajat, linearitas, kondisi homogen/non-homogen.
   - **C2 (Memahami):** Penjelasan konsep fisis konstanta waktu $\tau$, rasio redaman $\zeta$, frekuensi alami $\omega_n$, syarat batas Dirichlet dan Neumann.
   - **C3 (Menerapkan):** Penurunan analitis dan perhitungan manual solusi khusus dengan nilai awal/batas yang diberikan.
   - **C4 (Menganalisis):** Analisis transien terhadap variasi nilai $R, L, C$, perbandingan respon undamped vs underdamped, spektrum harmonisa deret Fourier.
   - **C5 (Mengevaluasi):** Evaluasi kestabilan sistem transien, validasi solusi numerik (FDM/Euler/RK4) terhadap solusi eksak analitik.
   - **C6 (Menciptakan/Merancang):** Perancangan parameter rangkaian filter transien, perancangan geometri pelat elektroda untuk profil medan listrik yang seragam.
2. **Estetika LaTeX Profesional:**
   - Menggunakan paket `tcolorbox`, `amsmath`, `amssymb`, dan diagram `tikz` / `circuitikz`.
   - Menampilkan kotak Sub-CPMK berbasis OBE di awal lembar kerja.

---

## 3. Standar Pabrikasi Video Perkuliahan & YouTube

1. **Format Salindia Presentasi (Beamer 16:9):**
   - Rasio layar lebar: `\documentclass[aspectratio=169,10pt]{beamer}`.
   - Tata letak konsisten, bebas tumpang tindih teks, tipografi bersih, dan palet warna institusi UNIB (Navy, Gold, Green).
2. **Sintesis Audio & Video:**
   - Sintesis suara bahasa Indonesia alami menggunakan Microsoft Edge TTS (`id-ID-ArdiNeural`).
   - Jeda pergantian salindia 1,0 s.d. 1,2 detik (*audio padding*) untuk artikulasi yang elegan dan mudah dipahami.
   - Kualitas video 1080p Full HD ($1920 \times 1080$), kompresi video `libx264` (preset `faster`, CRF 20), audio AAC 192 kbps.
   - Sinkronisasi sempurna antar klip (0 ms *audio-video drift*).
3. **Standar Metadata YouTube (SEO Optimized):**
   - Setiap pekan dilengkapi berkas naskah Markdown: `video_script_pd_w*.md`.
   - Judul resmi: `[Minggu XX] <Topik Kuliah> - Persamaan Diferensial | Teknik Elektro UNIB`.
   - Deskripsi memuat ringkasan perkuliahan, CPMK, tautan portal modul, daftar bab & linimasa (*timestamps/chapters*), referensi buku acuan (Kreyszig, Zill, Hayt), dan tagar relevan.
   - Unggah otomatis ke kanal resmi **Novalio Daratha** menggunakan YouTube API v3 dan dikelompokkan ke dalam playlist resmi.

---

## 4. Standar Web Portal & Deployment
1. Seluruh PDF hasil kompilasi salindia, diktat modul, lembar kerja, problem set, dan buku ajar harus disinkronkan ke direktori aset portal perkuliahan.
2. Portal perkuliahan menyediakan akses satu pintu (*single-entry academic hub*) bagi mahasiswa untuk membaca modul, mengunduh PDF, menyimak video YouTube perkuliahan, dan menguji simulasi kode terbuka.
3. Portal dideploy secara live di bawah domain resmi pengampu: `https://www.ndaratha.my.id/persamaan-diferensial/`.
4. Setiap sesi pengerjaan wajib diakhiri dengan pembuatan berkas ringkasan Markdown terstempel waktu (`session_summary_YYYYMMDD_HHMM.md`).
