# Ringkasan Sesi Perkuliahan: Redesain Komprehensif Lembar Kerja Mahasiswa (Worksheet 1–15) Berbasis OBE

**Tanggal & Waktu:** 20 September 2026, 12:58 WIB  
**Mata Kuliah:** Persamaan Diferensial (2 SKS)  
**Institusi:** Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika, Fakultas Teknik, Universitas Bengkulu  
**Dosen Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Domain Produksi:** `https://www.ndaratha.my.id/persamaan-diferensial/`

---

## 1. Latar Belakang & Evaluasi Kritis Worksheet Lama
Sesi ini diawali dengan audit kritis menyeluruh terhadap seluruh 14 berkas Lembar Kerja Mahasiswa (LKM) lama (`worksheet1.tex` s.d. `worksheet15.tex`). Ditemukan kelemahan-kelemahan struktural:
1. **Ketidaklengkapan Taksonomi Bloom:** `worksheet3` kehilangan jenjang C1, C2, C6 (hanya 3 soal); `worksheet2` kehilangan jenjang C1.
2. **Ketiadaan Header Sub-CPMK OBE:** Tidak ada kotak indikator capaian pembelajaran mingguan.
3. **Anakronisme Komputasi:** Masih menyebut Python/Jupyter Notebook (`Simulasi_Transien_RC_RL.ipynb`), padahal standar resmi perkuliahan menggunakan **Julia 1.12+**.
4. **Ketiadaan Ilustrasi Rangkaian / Medan:** 0% diagram sirkuit elektrik (`circuitikz`) dan geometri medan (`tikz`).
5. **Tata Letak Kasar & Ruang Menggantung:** Penggunaan `\vspace{8cm}` manual yang menyebabkan halaman kedua beberapa worksheet hanya memuat 5–8 baris teks (*orphan/widow lines*).

---

## 2. Pekerjaan yang Dilakukan

### A. Perancangan Template Master LKM Berstandar OBE (2 Halaman Bolak-Balik)
- **Halaman 1 (Depan):**
  - Header resmi Universitas Bengkulu, Program Studi S1 Teknik Elektro.
  - Isian identitas mahasiswa: Nama, NPM, Kelas/Kelompok, dan Kotak Nilai Final (/100).
  - Boks Sub-CPMK OBE resmi (sinkron dengan `ch*.pdf`), estimasi waktu (50–60 menit), dan bahasa komputasi Julia 1.12+.
  - Soal 1 (C1 - Mengingat, 10 Poin) + Kotak Jawaban Terstruktur (`answerbox`).
  - Soal 2 (C2 - Memahami, 15 Poin) + Kotak Jawaban Terstruktur.
  - Soal 3 (C3 - Menerapkan, 20 Poin) + Diagram Skematik Rangkaian/Medan `circuitikz` + Kotak Jawaban Terstruktur.
- **Halaman 2 (Belakang):**
  - Soal 4 (C4 - Menganalisis, 20 Poin) + Kotak Jawaban Terstruktur.
  - Soal 5 (C5 - Mengevaluasi, 20 Poin) + Kotak Jawaban Terstruktur.
  - Soal 6 (C6 - Merancang & Komputasi Julia, 15 Poin) + Kotak Jawaban Terstruktur.
  - Tabel Rekapitulasi Skor OBE (C1, C2, C3, C4, C5, C6, Total 100 Poin) dan Ruang Tanda Tangan Verifikasi Dosen/Asisten.

### B. Otomasi Pembangkitan & Sanitasi Berkas (`build_worksheets.py`)
- Dibuat skrip master `build_worksheets.py` yang memuat basis data pedagogis lengkap 14 pekan perkuliahan (Minggu 1–7 dan Minggu 9–15).
- Dilengkapi fungsi sanitasi otomatis karakter khusus LaTeX (`&` menjadi `\&`, `%` menjadi `\%`, dan pembagi suku kata `Differential\-Equations.jl`).

### C. Kompilasi & Verifikasi Mutu Teknis (`compile_and_verify_worksheets.py`)
- Seluruh 14 lembar kerja dikompilasi ulang dengan `pdflatex` (2 pass).
- Hasil pengujian: **100% PASS (14/14 berkas)** dengan rincian:
  - Jumlah halaman: **Tepat 2 halaman** pada setiap berkas (1 lembar bolak-balik sempurna).
  - Overfull horizontal (`\hbox`): **0** (Zero Overfull).
  - Overfull vertikal (`\vbox`): **0** (Zero Overfull).
  - Exit code: **0** (Bebas galat kompilasi).

### D. Sinkronisasi Portal Web & Deployment Produksi
1. Seluruh PDF hasil kompilasi disinkronkan ke direktori portal:
   - `portal/public/pdf/worksheet*.pdf`
   - `/Users/novaliodaratha/Documents/ndaratha.my.id/public/persamaan-diferensial/pdf/worksheet*.pdf`
2. Build statis portal Astro (`npm run build`) selesai dalam **401 ms** tanpa galat.
3. Deployment ke Vercel Production (`https://www.ndaratha.my.id`) selesai dalam **58 detik**.
4. Uji konektivitas live via `curl`: Seluruh 14 tautan merespons dengan status **HTTP 200 OK**.

---

## 3. Matriks Status Akhir 14 Lembar Kerja (Worksheet)

| Minggu | Berkas | Topik Rekayasa Elektro | Sub-CPMK | Bloom C1–C6 | Diagram | Status |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **W1** | `worksheet1.pdf` | Klasifikasi PDB/PDP & Rangkaian RL DC | Sub-CPMK 1 | Lengkap (100 Pts) | CircuiTikZ | **OK (2 Hal, 0 Overfull)** |
| **W2** | `worksheet2.pdf` | PDB Orde 1 Separabel & Eksak (RC) | Sub-CPMK 2 | Lengkap (100 Pts) | CircuiTikZ | **OK (2 Hal, 0 Overfull)** |
| **W3** | `worksheet3.pdf` | Model Termal Trafo Daya IEEE C57.91 | Sub-CPMK 3 | Lengkap (100 Pts) | CircuiTikZ | **OK (2 Hal, 0 Overfull)** |
| **W4** | `worksheet4.pdf` | PDB Orde 2 Homogen & 3 Ragam Redaman RLC | Sub-CPMK 3 | Lengkap (100 Pts) | CircuiTikZ | **OK (2 Hal, 0 Overfull)** |
| **W5** | `worksheet5.pdf` | PDB Orde 2 Non-Homogen & Resonansi AC | Sub-CPMK 3 | Lengkap (100 Pts) | CircuiTikZ | **OK (2 Hal, 0 Overfull)** |
| **W6** | `worksheet6.pdf` | Transformasi Laplace & Surja Petir IEC 60060 | Sub-CPMK 4 | Lengkap (100 Pts) | CircuiTikZ | **OK (2 Hal, 0 Overfull)** |
| **W7** | `worksheet7.pdf` | Invers Laplace & TRV Pemutus Tenaga IEC 62271| Sub-CPMK 4 | Lengkap (100 Pts) | CircuiTikZ | **OK (2 Hal, 0 Overfull)** |
| **W9** | `worksheet9.pdf` | Deret Fourier & THD Inverter IEEE 519 | Sub-CPMK 5 | Lengkap (100 Pts) | TikZ | **OK (2 Hal, 0 Overfull)** |
| **W10** | `worksheet10.pdf` | Pemisahan Variabel & Busbar Termal IEEE 738 | Sub-CPMK 5 | Lengkap (100 Pts) | TikZ | **OK (2 Hal, 0 Overfull)** |
| **W11** | `worksheet11.pdf` | Gelombang 1D & Telegrafer Transmisi IEC 60071 | Sub-CPMK 6 | Lengkap (100 Pts) | TikZ | **OK (2 Hal, 0 Overfull)** |
| **W12** | `worksheet12.pdf` | Persamaan Panas 1D & Kabel XLPE IEC 60287 | Sub-CPMK 6 | Lengkap (100 Pts) | TikZ | **OK (2 Hal, 0 Overfull)** |
| **W13** | `worksheet13.pdf` | Laplace 2D & Elektrostatika Isolator 150 kV | Sub-CPMK 6 | Lengkap (100 Pts) | TikZ | **OK (2 Hal, 0 Overfull)** |
| **W14** | `worksheet14.pdf` | Bessel & Efek Kulit Kawat ACSR IEC 61089 | Sub-CPMK 6 | Lengkap (100 Pts) | TikZ | **OK (2 Hal, 0 Overfull)** |
| **W15** | `worksheet15.pdf` | Legendre, 4 Persamaan Maxwell & Sintesis | Sub-CPMK 15 | Lengkap (100 Pts) | TikZ | **OK (2 Hal, 0 Overfull)** |

---

## 4. Tindak Lanjut yang Direkomendasikan
1. **Audit & Penyelarasan Problem Set:** Meninjau berkas kumpulan soal mandiri (`problem_set1.tex` s.d. `problem_set15.tex`) untuk memastikan jenjang C1–C6 dan kunci jawaban/solusi terdistribusi dengan kualitas setara.
2. **Sinkronisasi Bank Soal Ujian (UTS & UAS):** Memastikan cakupan soal UTS (Minggu 1–7) dan UAS (Minggu 9–15) bersesuaian dengan tipe-tipe analisis transien dan PDP yang telah dilatihkan pada lembar kerja ini.
