# Ringkasan Sesi Kerja: Replikasi Ekosistem 4-Pilar untuk Persamaan Diferensial
**Tanggal & Waktu:** 20 September 2026, 08:02 WIB  
**Mata Kuliah:** Persamaan Diferensial (Fokus Persiapan Medan Elektromagnetika & Rangkaian Listrik)  
**Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Institusi:** Program Studi S1 Teknik Elektro, Universitas Bengkulu  

---

## 1. Konteks & Tujuan Sesi
Menerapkan ekosistem pembelajaran digital terpadu berbasis **Model 4-Pilar Pedagogis OBE** (yang telah berhasil diselesaikan untuk mata kuliah *Dasar-Dasar Sistem Tenaga Listrik*) ke dalam mata kuliah **Persamaan Diferensial**.

---

## 2. Rincian Pekerjaan yang Diselesaikan

### A. Standarisasi Mutu Pedagogis (`AGENTS.md`)
- Berkas [AGENTS.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/AGENTS.md) dibentuk khusus untuk mata kuliah Persamaan Diferensial.
- Mengatur 4 pilar wajib:
  1. **Pilar 1 (Intuisi Fisika Rekayasa):** Fenomena fisis nyata (transien rangkaian, osilasi RLC, gelombang 1D saluran transmisi, distribusi potensial Laplace, dan difusi medan / efek kulit).
  2. **Pilar 2 (Derivasi Matematika Eksplisit):** Penurunan analitis *step-by-step* tanpa *skipped steps*.
  3. **Pilar 3 (Komputasi Numerik Terbuka):** Python (NumPy, SciPy, Matplotlib) & GNU Octave serta Jupyter Notebooks bebas lisensi.
  4. **Pilar 4 (Aplikasi Nyata Teknik Elektro):** Hubungan langsung ke saluran transmisi, kabel koaksial, pembumian, dan 4 Persamaan Maxwell.
- Standar Taksonomi Bloom berjenjang C1–C6 dan standar Beamer 16:9.

### B. Otomasi YouTube Resmi
- Kredensial YouTube API (`client_secrets.json` dan `token.json`) dikonfigurasi.
- Playlist YouTube baru dibuat secara otomatis:
  - **Nama:** *Persamaan Diferensial - Teknik Elektro UNIB*
  - **ID:** `PLS5oOZWXZeTw`
  - **URL:** [https://www.youtube.com/playlist?list=PLS5oOZWXZeTw](https://www.youtube.com/playlist?list=PLS5oOZWXZeTw)
- Skrip otomasi [upload_to_youtube.py](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/upload_to_youtube.py) dibuat dengan kemampuan upload resumable, auto-playlist assignment, dan verifikasi kuota.

### C. Pabrikasi Video Kuliah Minggu 01 (1080p Full HD)
- Skrip [build_video_w01.py](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/build_video_w01.py) berhasil merender:
  - Ekstraksi 34 salindia Beamer 1080p dari `ch1.pdf` (`scratch/slide_frames_w01/`).
  - Narasi suara alami bahasa Indonesia `id-ID-ArdiNeural` dengan jeda transisi 1,2 detik.
  - Video final: [video_pd_minggu01.mp4](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_pd_minggu01.mp4) (Resolusi $1920 \times 1080$, Durasi 12 menit 19 detik, Ukuran 13,85 MB).
  - Naskah siap unggah: [video_script_pd_w01.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_script_pd_w01.md).
- **Unggah YouTube Berhasil:**
  - Status: **Public**
  - URL Video: [https://youtu.be/umcAHSZyhCE](https://youtu.be/umcAHSZyhCE)
  - Video ID: `umcAHSZyhCE`
  - Tercatat di `uploaded_youtube_videos.json`.

### D. Integrasi Web Portal & Live Deployment
- [docs/01_modul_1.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/docs/01_modul_1.md) diperbarui dengan pemutar video YouTube responsif dan kotak unduhan berkas pembelajaran.
- [docs/index.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/docs/index.md) diperbarui dengan banner playlist resmi dan kolom video YouTube pada tabel modul.
- MkDocs berhasil dikompilasi (`mkdocs build`), disinkronkan ke `ndaratha.my.id/public/persamaan-diferensial/`, di-commit dan di-push ke GitHub (`62ffc98`), serta didistribusikan ke Vercel Production.

---

## 3. Rencana Tindak Lanjut
- Memproduksi video perkuliahan secara beruntun untuk **Minggu 02 s.d. Minggu 07** dan **Minggu 09 s.d. Minggu 15**.
- Memperkaya pemutar video YouTube pada seluruh halaman modul `docs/02_modul_2.md` s.d. `docs/15_modul_15.md`.
