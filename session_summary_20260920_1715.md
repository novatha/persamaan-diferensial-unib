# Ringkasan Sesi Perkuliahan & Pabrikasi Video Persamaan Diferensial
**Waktu Pelaksanaan:** Minggu, 20 September 2026, 17:15 WIB  
**Dosen Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Institusi:** Program Studi S1 Teknik Elektro, Fakultas Teknik, Universitas Bengkulu  

---

## 1. Penyelesaian Utama Sesi Ini
1. **Perbaikan Masalah Desinkronisasi Suara & Pergeseran Salindia:**
   - **Akar Masalah:** Flag `-shortest` pada FFmpeg menghasilkan surplus frame video (~1,5 detik) per salindia. Saat digabungkan via `concat copy`, surplus ini terakumulasi hingga audio mendahului video sebesar ~22 detik pada akhir video.
   - **Solusi Analitik:** Meniadakan `-shortest`, menghitung durasi analitik presisi frame 25 fps ditambah jeda hening pergantian salindia 1,0 detik (`PAD_DUR = 1.0` s), memotong audio persis pada `exact_dur` (`-af "apad,atrim=0:{exact_dur:.4f}"`), dan mengunci durasi video (`-t {exact_dur:.4f}`).
   - **Hasil:** Selisih audio-video per klip mencapai **0,00 ms**, dan selisih akhir berkas utuh hanya 23 ms (setara 1 frame audio AAC). **Kumulatif drift antar-salindia adalah 0 ms**.

2. **Perbaikan Kuis Salindia 14 Video Minggu 03 (Menit 09:40):**
   - Naskah narasi lama yang membacakan kasus relay transistor diperbarui total agar selaras 100% dengan teks visual salindia [ch3.pdf](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/ch3.pdf) (Kasus dinamika termal Trafo 60 MVA beban lebih 150%, kapasitas kalor massa minyak vs kawat tembaga).
   - Audio TTS `id-ID-ArdiNeural` disintesis ulang dengan jeda hening berpikir 8 detik terprogram.
   - Video Minggu 03 dibuat ulang secara penuh, diverifikasi, dan disinkronkan ke portal.

3. **Pabrikasi Batch Seluruh 14 Pekan Perkuliahan (W01 s.d. W15):**
   - Seluruh 14 pekan perkuliahan (Minggu 01–07 dan 09–15) telah berhasil dirender ulang dengan standar presisi 0 ms drift.
   - Semua berkas tersinkronisasi di root (`video_pd_mingguXX.mp4`), di portal web (`portal/public/video/video_pd_mingguXX.mp4`), dan naskah linimasa YouTube (`video_script_pd_wXX_v2.md`).

---

## 2. Tabel Rekapitulasi 14 Video Perkuliahan (Status Final)

| Pekan | Topik Perkuliahan | Durasi | Resolusi / Audio | Delta A-V | Status Sinkronisasi |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **W01** | Klasifikasi PDB/PDP & Pemodelan RL | 10:51 | 1080p CRF 18 / Stereo 192k | 23,24 ms | Perfect Sync (0 ms Drift) |
| **W02** | Separabel, Eksak & Transien RC | 13:09 | 1080p CRF 18 / Stereo 192k | 23,22 ms | Perfect Sync (0 ms Drift) |
| **W03** | Rekayasa PDB Orde 1 & Termal Trafo | 11:29 | 1080p CRF 18 / Stereo 192k | 23,24 ms | Perfect Sync (0 ms Drift) |
| **W04** | PDB Orde 2 Homogen & Tiga Ragam Redaman | 11:08 | 1080p CRF 18 / Stereo 192k | 23,22 ms | Perfect Sync (0 ms Drift) |
| **W05** | PDB Non-Homogen & Resonansi RLC | 10:57 | 1080p CRF 18 / Stereo 192k | 23,24 ms | Perfect Sync (0 ms Drift) |
| **W06** | Transformasi Laplace Dasar & IVP S-Domain | 11:04 | 1080p CRF 18 / Stereo 192k | 23,24 ms | Perfect Sync (0 ms Drift) |
| **W07** | Invers Laplace & Analisis Sirkuit S-Domain | 11:16 | 1080p CRF 18 / Stereo 192k | 23,24 ms | Perfect Sync (0 ms Drift) |
| **W09** | Deret Fourier Trigonometri & Harmonisa THD | 11:22 | 1080p CRF 18 / Stereo 192k | 23,24 ms | Perfect Sync (0 ms Drift) |
| **W10** | BVP & Difusi Busbar Termal GITET | 11:21 | 1080p CRF 18 / Stereo 192k | 23,24 ms | Perfect Sync (0 ms Drift) |
| **W11** | Persamaan Gelombang 1D Saluran Transmisi | 11:05 | 1080p CRF 18 / Stereo 192k | 23,24 ms | Perfect Sync (0 ms Drift) |
| **W12** | Persamaan Panas 1D Kabel Bawah Tanah | 11:13 | 1080p CRF 18 / Stereo 192k | 23,22 ms | Perfect Sync (0 ms Drift) |
| **W13** | Persamaan Laplace 2D Isolator 150 kV | 11:29 | 1080p CRF 18 / Stereo 192k | 23,22 ms | Perfect Sync (0 ms Drift) |
| **W14** | Fungsi Bessel Silinder & Skin Effect ACSR | 11:32 | 1080p CRF 18 / Stereo 192k | 23,22 ms | Perfect Sync (0 ms Drift) |
| **W15** | Polinomial Legendre & 4 Persamaan Maxwell | 11:31 | 1080p CRF 18 / Stereo 192k | 23,22 ms | Perfect Sync (0 ms Drift) |
