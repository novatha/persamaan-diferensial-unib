# Ringkasan Sesi Perkuliahan: Deployment Sukses ke Situs Produksi pd.ndaratha.my.id
**Tanggal & Waktu:** 20 September 2026, 17:48 WIB  
**Berkas:** `session_summary_20260920_1748.md`  
**Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Institusi:** Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika, Fakultas Teknik, Universitas Bengkulu  
**URL Produksi:** [https://pd.ndaratha.my.id](https://pd.ndaratha.my.id)

---

## 1. Ikhtisar Deployment
Situs perkuliahan dan pusat dokumentasi digital mata kuliah **Persamaan Diferensial** telah berhasil dikompilasi, disinkronkan, dan dideploy ke peladen produksi Vercel di bawah domain resmi **`pd.ndaratha.my.id`**.

---

## 2. Aset & Pembaruan yang Disinkronkan
1. **Modul Ajar Monograf Lengkap (Minggu 1 s.d. 15):**
   - Seluruh modul PDF (`modul_1.pdf` s.d. `modul_15.pdf`) yang telah distandardisasi dengan Kerangka 4-Pilar OBE, $\ge 1.200$ kata substansi, diagram TikZ responsif, dan kode praktikum komputasi terbuka Julia.
2. **Salindia Presentasi Beamer (Ch 1 s.d. Ch 15):**
   - Seluruh berkas presentasi Beamer (`ch1.pdf` s.d. `ch15.pdf`) format 16:9, palet warna institusi, dan integrasi Sub-CPMK C1 s.d. C6.
3. **Lembar Kerja Mahasiswa (Worksheet 1 s.d. 15):**
   - Instrumen LKM berjenjang Taksonomi Bloom C1 s.d. C6 (`worksheet1.pdf` s.d. `worksheet15.pdf`).
4. **Problem Set Terstruktur (Problem Set 1 s.d. 15):**
   - Bank soal latihan analitis dan rekayasa elektro berjenjang Bloom C1 s.d. C6 (`problem_set1.pdf` s.d. `problem_set15.pdf`).
5. **Jupyter / Julia Notebooks:**
   - Notebook simulasi komputasi dinamika transien RC/RL, RLC, gelombang 1D, difusi panas 1D, dan pemetaan Laplace 2D.
6. **Optimasi Payload Vercel:**
   - Dibuat berkas `.vercelignore` dan pembaruan `.gitignore` untuk mengeliminasi berkas video biner berat dan cache pembangun lokal sehingga payload deployment tetap ramping, cepat (< 35 detik), dan aman dari kebocoran berkas sensitif.

---

## 3. Hasil Pengujian Live (Production Verification)
Pengujian langsung ke peladen produksi melalui protokol HTTP/2:
- **Halaman Utama:** `https://pd.ndaratha.my.id` $\to$ **HTTP/2 200 OK**
- **Slide Presentasi W1:** `https://pd.ndaratha.my.id/files/ch1.pdf` $\to$ **HTTP/2 200 OK**
- **Monograf Lengkap W15:** `https://pd.ndaratha.my.id/files/modul_15.pdf` $\to$ **HTTP/2 200 OK**
- **Lembar Kerja W15:** `https://pd.ndaratha.my.id/files/worksheet15.pdf` $\to$ **HTTP/2 200 OK**
- **Sinkronisasi Git:** Berhasil di-*commit* (`6aad595`) dan di-*push* ke remote GitHub `novatha/persamaan-diferensial-unib:main`.
