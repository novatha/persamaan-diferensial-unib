# Ringkasan Sesi Kerja: Overhaul Total Worksheet & Problem Set (1–15) Berbasis OBE
**Mata Kuliah:** Persamaan Diferensial (2 SKS)  
**Program Studi:** S1 Teknik Elektro, Fakultas Teknik, Universitas Bengkulu  
**Dosen Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Waktu Pelaksanaan:** Minggu, 20 September 2026, Pukul 12:00 – 13:15 WIB  
**Status Sesi:** **SUKSES PENUH (100% Selesai & Terverifikasi Produksi)**

---

## 1. Tujuan & Ruang Lingkup Pekerjaan

Sesi kerja ini berfokus pada audit kritis, redesain komprehensif, pemutakhiran pedagogis berbasis **Outcome-Based Education (OBE)**, dan pabrikasi tipografi profesional terhadap seluruh 28 instrumen evaluasi mingguan:
1. **14 Lembar Kerja Mahasiswa (LKM):** `worksheet1.pdf` s.d. `worksheet7.pdf` dan `worksheet9.pdf` s.d. `worksheet15.pdf`.
2. **14 Problem Set (Tugas Mandiri Terstruktur):** `problem_set1.pdf` s.d. `problem_set7.pdf` dan `problem_set9.pdf` s.d. `problem_set15.pdf`.

---

## 2. Masalah Kritis yang Berhasil Diatasi

### A. Pada Lembar Kerja Mahasiswa (Worksheet Lama)
1. **Kehilangan Tingkat Kognitif Bloom:** `worksheet3` kehilangan 3 tingkat kognitif (C1, C2, C6), dan `worksheet2` kehilangan tingkat C1.
2. **Ketiadaan Kotak Sub-CPMK:** Tidak ada perumusan capaian pembelajaran mingguan yang terukur untuk akreditasi IABEE.
3. **Ketiadaan Diagram Sirkuit:** Seluruh soal rangkaian listrik hanya disajikan dalam bentuk teks abstrak tanpa diagram skematik fisis.
4. **Anakronisme Komputasi:** Masih menyebut Python dan Jupyter Notebook, bertentangan dengan standar mata kuliah yang mengadopsi **Julia 1.12+**.
5. **Layout Tumpah:** Penggunaan `\vspace{8cm}` yang kaku menyebabkan halaman 2 kosong atau tumpah tidak beraturan.

### B. Pada Problem Set (Tugas Mandiri Lama)
1. **Kehilangan Tingkat Kognitif:** `problem_set3.tex` kehilangan C1, C2, C3; `problem_set2.tex` kehilangan C1.
2. **Tumpahan Halaman Canggung:** `problem_set9.pdf` tumpah ke halaman 3 hanya berisi 2 baris teks ("Semoga berhasil!"), dan `problem_set4.pdf` terpotong canggung di tengah soal 5.
3. **Ketiadaan Boks Formula & Standar Industri:** Tidak ada rangkuman formula teknis dan ketiadaan kaitan eksplisit dengan standar IEEE/IEC/SPLN.
4. **Zero Diagram Skematik:** Tidak ada ilustrasi grafis CircuiTikZ atau TikZ.

---

## 3. Implementasi Solusi & Standar Mutu Baru

Seluruh berkas LaTeX dibangun ulang secara terprogram menggunakan generator master berbasis Python:
- **LKM Generator:** `build_worksheets.py`
- **Problem Set Generator:** `build_problem_sets.py`

### Standar Teknis & Pedagogis yang Ditegakkan:
1. **Model 4-Pilar Pedagogis:**
   - *Intuisi Fisika Rekayasa:* Mengaitkan dinamika sistem dengan energi resistor, induktor $\frac{1}{2}Li^2$, dan kapasitor $\frac{1}{2}Cv^2$.
   - *Derivasi Eksplisit:* Penurunan rumus analitis langkah demi langkah tanpa melompati baris.
   - *Komputasi Terbuka Julia 1.12+:* Soal C6 menuntut perancangan program numerik menggunakan pustaka `DifferentialEquations.jl`, `Plots.jl`, `FFTW.jl`, dan `SpecialFunctions.jl`.
   - *Aplikasi Standar Industri:* Mengintegrasikan **IEEE Std C57.91**, **IEC 60060-1**, **IEC 62271-100**, **IEEE Std 519**, **SPLN D3.022-1**, **IEC 61089**, dan **IEEE Std C95.1**.
2. **Taksonomi Bloom Lengkap Berbobot 100 Poin:**
   - C1 (Mengingat) = 10 Pts
   - C2 (Memahami) = 15 Pts
   - C3 (Menerapkan) = 20 Pts
   - C4 (Menganalisis) = 20 Pts
   - C5 (Mengevaluasi) = 20 Pts
   - C6 (Merancang/Komputasi Julia) = 15 Pts
3. **Presisi Format Tepat 2 Halaman (1 Lembar Bolak-Balik):**
   - **Halaman 1 (Muka):** Identitas Mahasiswa, Boks Sub-CPMK OBE, Bagian I (C1, C2, C3 + CircuiTikZ), dan Boks Rujukan Formula Teknis & Standar Industri berpalet `unibblue`.
   - **Halaman 2 (Punggung):** Bagian II (C4, C5, C6 Julia), Tabel Skor OBE (100 Pts), Verifikasi Dosen/Asisten, dan Boks Rubrik Evaluasi Pemeriksaan Tugas setinggi 1,6 cm.
4. **Kualitas Tipografi:** Bebas kesalahan tumpukan teks (Zero `Overfull \hbox` dan Zero `Overfull \vbox`).

---

## 4. Hasil Verifikasi Kompilasi & Pengujian

### Hasil Uji Kompilasi Problem Set (`compile_and_verify_problem_sets.py`):
```text
Week   | Status | Pages  | Overfull H | Overfull V | Notes
-----------------------------------------------------------------
W1     | OK     | 2      | 0          | 0          | Perfect (2 Pages, 0 Overfull)
W2     | OK     | 2      | 0          | 0          | Perfect (2 Pages, 0 Overfull)
W3     | OK     | 2      | 0          | 0          | Perfect (2 Pages, 0 Overfull)
W4     | OK     | 2      | 0          | 0          | Perfect (2 Pages, 0 Overfull)
W5     | OK     | 2      | 0          | 0          | Perfect (2 Pages, 0 Overfull)
W6     | OK     | 2      | 0          | 0          | Perfect (2 Pages, 0 Overfull)
W7     | OK     | 2      | 0          | 0          | Perfect (2 Pages, 0 Overfull)
W9     | OK     | 2      | 0          | 0          | Perfect (2 Pages, 0 Overfull)
W10    | OK     | 2      | 0          | 0          | Perfect (2 Pages, 0 Overfull)
W11    | OK     | 2      | 0          | 0          | Perfect (2 Pages, 0 Overfull)
W12    | OK     | 2      | 0          | 0          | Perfect (2 Pages, 0 Overfull)
W13    | OK     | 2      | 0          | 0          | Perfect (2 Pages, 0 Overfull)
W14    | OK     | 2      | 0          | 0          | Perfect (2 Pages, 0 Overfull)
W15    | OK     | 2      | 0          | 0          | Perfect (2 Pages, 0 Overfull)
-----------------------------------------------------------------
ALL 14 PROBLEM SETS PASSED VERIFICATION WITH ZERO OVERFULLS AND EXACTLY 2 PAGES!
```

---

## 5. Rantai Distribusi & Deployment Produksi Vercel

1. **Sinkronisasi Berkas:** Seluruh 14 berkas `problem_set*.pdf` dan 14 berkas `worksheet*.pdf` disalin ke `portal/public/pdf/`.
2. **Kompilasi Astro Portal:** Dijalankan `npm run build` di direktori `portal/`, selesai dalam 429 ms tanpa galat.
3. **Rsync ke Repositori Web Utama:** Seluruh hasil build (`portal/dist/`) disinkronkan ke `/Users/novaliodaratha/Documents/ndaratha.my.id/public/persamaan-diferensial/`.
4. **Deploy Vercel Production:** Perintah `vercel --prod` dieksekusi dengan sukses di `/Users/novaliodaratha/Documents/ndaratha.my.id`.
5. **Verifikasi HTTP Live:** Pengujian `curl -s -o /dev/null -w "%{http_code}"` terhadap domain publik `https://www.ndaratha.my.id/persamaan-diferensial/pdf/`:
   - `problem_set1.pdf` s.d. `problem_set15.pdf` -> **HTTP 200 OK (14/14)**
   - `worksheet1.pdf` s.d. `worksheet15.pdf` -> **HTTP 200 OK (14/14)**

---

## 6. Berkas & Skrip Penting yang Dihasilkan
- `build_problem_sets.py`: Skrip master generator LaTeX Problem Set mingguan.
- `compile_and_verify_problem_sets.py`: Skrip kompilasi otomatis dan verifikasi metrik mutu Problem Set.
- `problem_set1.tex` s.d. `problem_set15.tex`: Sumber naskah LaTeX resmi Problem Set.
- `problem_set1.pdf` s.d. `problem_set15.pdf`: Berkas siap cetak dan distribusi.
- `walkthrough.md`: Dokumentasi komprehensif seluruh perbaikan Worksheet dan Problem Set.

*Sesi selesai dengan status sempurna dan seluruh perubahan telah terpasang secara live di server produksi.*
