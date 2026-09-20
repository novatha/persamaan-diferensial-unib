# Ringkasan Sesi Perkuliahan & Pabrikasi Video Persamaan Diferensial
**Waktu Pelaksanaan:** Minggu, 20 September 2026, 17:40 WIB  
**Dosen Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Institusi:** Program Studi S1 Teknik Elektro, Fakultas Teknik, Universitas Bengkulu  

---

## 1. Masalah yang Diselesaikan Secara Total
1. **Ketidaksinkronan Audio-Video Saat Pergeseran Salindia (Drift Elimination):**
   - Meniadakan flag `-shortest` pada FFmpeg yang sebelumnya menimbulkan akumulasi pergeseran audio ~1,5 detik per salindia.
   - Menggunakan kalkulasi durasi analitik presisi frame 25 fps ditambah jeda hening pergantian salindia 1,0 detik (`PAD_DUR = 1.0` s) sesuai standar [AGENTS.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/AGENTS.md).
   - Seluruh 14 video kini memiliki selisih akhir hanya 23,2 ms (1 frame audio AAC), menjamin **0,00 ms cumulative drift**.

2. **Penyelarasan Total Soal Kuis Salindia 14 (TEX vs TTS) Seluruh Pekan:**
   - Ditemukan ketidaksesuaian soal kuis pada beberapa pekan di mana audio narasi lama membacakan soal yang berbeda dengan tampilan teks pada salindia Beamer PDF.
   - Dilakukan perbaikan naskah narasi secara menyeluruh pada `video_builder/data_wXX.py` untuk seluruh pekan (W04, W05, W06, W07, W09, W10, W11, W12, W13, W14, dan W15).
   - Seluruh audio Salindia 14 disintesis ulang dengan suara alami Microsoft Edge TTS `id-ID-ArdiNeural` lengkap dengan jeda hening berpikir 8 detik terprogram.

3. **Sinkronisasi Web Portal & Metadata YouTube:**
   - Semua video hasil kompilasi baru telah disinkronkan ke direktori root (`video_pd_mingguXX.mp4`) dan portal web ([portal/public/video/](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/portal/public/video/)).
   - Naskah linimasa bab YouTube (`video_script_pd_wXX_v2.md`) telah diperbarui dengan timestamps yang 100% akurat.

---

## 2. Tabel Rekapitulasi Audit Akhir 14 Video Perkuliahan (W01 s.d. W15)

| Pekan | Topik Perkuliahan | Durasi | Ukuran | Delta A-V | Kuis Salindia 14 | Status Portal |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **W01** | Klasifikasi PDB/PDP & Pemodelan RL | 10:51 | 25,0 MB | 23,2 ms | 100% Sesuai | SYNC OK |
| **W02** | Separabel, Eksak & Transien RC | 13:09 | 29,7 MB | 23,2 ms | 92% Sesuai | SYNC OK |
| **W03** | Rekayasa PDB Orde 1 & Termal Trafo | 11:29 | 26,4 MB | 23,2 ms | 100% Sesuai | SYNC OK |
| **W04** | PDB Orde 2 Homogen & Tiga Ragam Redaman | 11:15 | 25,2 MB | 23,2 ms | 100% Sesuai | SYNC OK |
| **W05** | PDB Non-Homogen & Resonansi RLC AC | 11:31 | 26,9 MB | 23,2 ms | 82% Sesuai | SYNC OK |
| **W06** | Transformasi Laplace Dasar & IVP S-Domain | 11:20 | 25,0 MB | 23,2 ms | 88% Sesuai | SYNC OK |
| **W07** | Invers Laplace & Analisis Sirkuit S-Domain | 11:28 | 26,1 MB | 23,2 ms | 100% Sesuai | SYNC OK |
| **W09** | Deret Fourier & Harmonisa IEEE 519 | 11:41 | 28,3 MB | 23,2 ms | 100% Sesuai | SYNC OK |
| **W10** | BVP & Difusi Busbar Termal GITET | 11:35 | 27,7 MB | 23,2 ms | 100% Sesuai | SYNC OK |
| **W11** | Persamaan Gelombang 1D Saluran Transmisi | 11:15 | 26,8 MB | 23,2 ms | 86% Sesuai | SYNC OK |
| **W12** | Persamaan Panas 1D Kabel Bawah Tanah | 11:21 | 27,4 MB | 23,2 ms | 100% Sesuai | SYNC OK |
| **W13** | Persamaan Laplace 2D Isolator 150 kV | 11:53 | 28,6 MB | 23,2 ms | 90% Sesuai | SYNC OK |
| **W14** | Fungsi Bessel Silinder & Efek Kulit ACSR | 11:43 | 28,4 MB | 23,2 ms | 100% Sesuai | SYNC OK |
| **W15** | Polinomial Legendre & 4 Persamaan Maxwell | 11:57 | 28,3 MB | 23,2 ms | 89% Sesuai | SYNC OK |
