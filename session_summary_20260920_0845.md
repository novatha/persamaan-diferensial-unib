# Ringkasan Sesi Perkuliahan: Standardisasi Penuh Portal & Materi Persamaan Diferensial Mengikuti Standar DSTL
**Waktu Eksekusi:** Minggu, 20 September 2026, Pukul 08:45 WIB  
**Mata Kuliah:** Persamaan Diferensial (Fokus Medan Elektromagnetika & Rangkaian Listrik)  
**Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Program Studi:** S1 Teknik Elektro, Fakultas Teknik, Universitas Bengkulu  

---

## 1. Latar Belakang & Instruksi Pengguna
Pengguna menginstruksikan: *"ikuti standar mata kuliah ini: https://www.ndaratha.my.id/dstl/materi"*.

Berdasarkan penelusuran arsitektur portal DSTL (Dasar-Dasar Sistem Tenaga Listrik), standar perkuliahan tersebut memiliki ekosistem **Astro Web Portal generasi terbaru** dengan fitur:
1. **Katalog 14 Modul Interaktif (`/materi`):**
   - *Filter Chips* kategori dinamis (*live filtering* tanpa reload).
   - *Live Search Bar* real-time (pencarian instan berdasarkan judul, topik, minggu, atau rumus).
   - *Kartu Modul Mingguan (Week Cards)* yang elegan dengan:
     - Badge minggu & kategori bertema.
     - Judul & Sub-judul bab.
     - Kotak Sub-CPMK OBE dengan ikon centang.
     - *Topic tags wrap*.
     - **Formulasi Matematis Preview** berlatar gelap yang dirender presisi menggunakan **KaTeX**.
     - **Kisi Unduhan 6 Tombol Aksi:** YouTube (Merah), Video MP4, Slide Beamer 16:9 (Emas), Solusi C1–C6 (Hijau Zamrud), Lembar Kerja Mahasiswa (Sian), dan Catatan Kuliah Monograf (Ungu).
2. **Navigasi Akademik Lengkap:**
   - `/` (Beranda: profil, CPMK, statistik ringkas, modul unggulan).
   - `/silabus` (RPS OBE SN-Dikti, matriks 16 minggu, tautan unduhan).
   - `/materi` (Katalog 14 Modul & Solved Problems).
   - `/tugas` (Bank Soal Bloom C1–C6 & Lembar Kerja Mahasiswa).
   - `/ujian` (Arsip resmi Soal & Solusi Lengkap UTS & UAS).

---

## 2. Pembangunan Portal Astro Persamaan Diferensial
Dibangun infrastruktur Astro lengkap di direktori `./portal`:
- **`portal/astro.config.mjs`:** Dikonfigurasi dengan `site: 'https://www.ndaratha.my.id'`, `base: '/persamaan-diferensial'`, integrasi MDX, Remark-Math, dan Rehype-KaTeX.
- **`portal/src/data/pdData.ts`:** Data model 14 pekan lengkap Persamaan Diferensial memuat Capaian Pembelajaran, 6 kategori mata kuliah (Fondasi PDB, Aplikasi Transien, Orde 2 & RLC, Transformasi Laplace, PDP & Fourier, Gelombang & Maxwell), formulasi matematis LaTeX, dan tautan berkas.
- **Komponen & Tata Letak:**
  - `PdWeekCard.astro`: Replikasi kartu DSTL disesuaikan untuk Persamaan Diferensial.
  - `Navbar.astro`: Navigasi sticky glassmorphic dengan logo integrasi $\int$, tautan portal, dan drawer mobile.
  - `Footer.astro`: Identitas pengampu, Prodi S1 Elektro UNIB, dan hak cipta 2026.
  - `Layout.astro`: Memuat tipografi Inter & Outfit, stylesheet KaTeX CDN, dan Lucide Icons.
- **Halaman Lengkap:**
  - `src/pages/index.astro`: Beranda resmi.
  - `src/pages/materi.astro`: Replikasi identik dari `https://www.ndaratha.my.id/dstl/materi`.
  - `src/pages/silabus.astro`: Matriks 16 pekan & unduhan RPS.
  - `src/pages/tugas.astro`: Bank soal solved problems & LKM.
  - `src/pages/ujian.astro`: Naskah & kunci jawaban UTS/UAS.

---

## 3. Kompilasi & Deployment Produksi Vercel
1. **Penyalinan Aset Digital:** Seluruh 60+ berkas PDF (`ch*.pdf`, `modul_*.pdf`, `worksheet*.pdf`, `problem_set*.pdf`, `uts.pdf`, `uas.pdf`) dan video MP4 disalin ke `portal/public/pdf/` dan `portal/public/video/`.
2. **Kompilasi Astro:** `npm run build` sukses mengkompilasi 5 rute statis dalam waktu **532 milidetik**.
3. **Sinkronisasi & Push:** Disinkronkan ke `/Users/novaliodaratha/Documents/ndaratha.my.id/public/persamaan-diferensial/`, dicommit ke git, dan dipush ke GitHub.
4. **Deploy Vercel Production:** Berhasil dideploy secara live dan dialiaskan ke domain utama:
   - 👉 **Katalog Modul Persamaan Diferensial:** [https://www.ndaratha.my.id/persamaan-diferensial/materi](https://www.ndaratha.my.id/persamaan-diferensial/materi)
   - 👉 **Beranda Portal:** [https://www.ndaratha.my.id/persamaan-diferensial/](https://www.ndaratha.my.id/persamaan-diferensial/)
   - 👉 **Silabus:** [https://www.ndaratha.my.id/persamaan-diferensial/silabus](https://www.ndaratha.my.id/persamaan-diferensial/silabus)
   - 👉 **Solved Problems:** [https://www.ndaratha.my.id/persamaan-diferensial/tugas](https://www.ndaratha.my.id/persamaan-diferensial/tugas)
   - 👉 **Arsip UTS/UAS:** [https://www.ndaratha.my.id/persamaan-diferensial/ujian](https://www.ndaratha.my.id/persamaan-diferensial/ujian)
   *(Seluruh rute telah diverifikasi menghasilkan HTTP/2 200 OK)*.
