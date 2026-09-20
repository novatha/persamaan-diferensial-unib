# Ringkasan Sesi Perkuliahan: Penyesuaian Narasi Audio Sub-CPMK Minggu 15, Re-Render Video & Re-Upload YouTube
**Tanggal & Waktu:** 20 September 2026, 19:00 WIB  
**Berkas:** `session_summary_20260920_1900.md`  
**Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Institusi:** Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika, Fakultas Teknik, Universitas Bengkulu  
**URL Video YouTube Baru:** [https://youtu.be/J4XziBcVtfk](https://youtu.be/J4XziBcVtfk)  
**URL Web Produksi:** [https://pd.ndaratha.my.id](https://pd.ndaratha.my.id)

---

## 1. Masalah yang Diidentifikasi
Terdapat ketidakcocokan antara teks Capaian Pembelajaran Modul (Sub-CPMK 15 C1 s.d. C6 Taksonomi Bloom) yang ditampilkan pada Salindia 2 Beamer `ch15.tex` dengan narasi audio yang disuarakan oleh model TTS pada video Minggu 15 sebelumnya:
- C1: Narasi lama menyuarakan formula Rodrigues polinomial Legendre, sedangkan slide menampilkan bentuk standar PDB Legendre dan 4 Persamaan Maxwell.
- C2: Narasi lama hanya menyebut kelistrikan dan kemagnetan, sedangkan slide eksplisit memuat peran fisis arus pergeseran $\partial \vec{D}/\partial t$ dalam menjaga kekekalan muatan.
- C3 & C4: Narasi lama melompati penurunan potensial elektrostatik bola konduktor netral ($V(r, \theta)$) dan memajukan penurunan persamaan gelombang EM 3D.
- C5: Narasi lama menyebut standar ICNIRP, sedangkan slide memuat validasi kesamaan arus konduksi $I_c$ dan arus pergeseran $I_d$ serta batas paparan medan SUTET **IEEE C95.1**.
- C6: Narasi lama menyebut pemrograman Julia, sedangkan slide menyatakan sintesis peta konseptual unifikasi (PDB, Laplace, Fourier, dan PDP).

---

## 2. Tindakan Korektif & Sinkronisasi
1. **Pembaruan Naskah Data Narasi ([video_builder/data_w15.py](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_builder/data_w15.py)):**
   - Teks narasi audio Salindia 02 dan daftar tuple `cpmk` disinkronkan 100% kata demi kata sesuai dengan teks salindia Beamer.
2. **Pembaruan Dokumen Naskah ([video_script_pd_w15_v2.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_script_pd_w15_v2.md)):**
   - Bagian 2 (Capaian Pembelajaran) dan Bagian 3 (Salindia 02) diperbarui secara penuh.
3. **Pembersihan Cache & Re-rendering:**
   - Cache `scratch/w15_v2` dibersihkan dan video dirender ulang secara paralel dalam 1 menit 49 detik.
   - Hasil video baru: [video_pd_minggu15.mp4](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_pd_minggu15.mp4) (Resolusi 1080p Full HD, durasi 12:13, delta audio-video drift hanya 23 ms / 0 ms perseptual).
4. **Re-upload ke YouTube Resmi:**
   - Diunggah ke kanal resmi dengan ID baru: `J4XziBcVtfk`
   - URL: `https://youtu.be/J4XziBcVtfk`
   - Berhasil dimasukkan ke playlist resmi `PLS5oOZWXZeTw`.
5. **Pembaruan Portal & Deployment:**
   - Berkas basis data [portal/src/data/pdData.ts](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/portal/src/data/pdData.ts) dan tabel [docs/index.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/docs/index.md) diperbarui dengan URL baru.
   - Portal Astro dan dokumentasi MkDocs dibangun ulang dan berhasil dideploy ke peladen produksi Vercel: `https://pd.ndaratha.my.id`.
   - Perubahan di-commit (`e5e730a`) dan di-push ke branch `main`.
