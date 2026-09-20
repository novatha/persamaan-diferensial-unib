# Ringkasan Sesi Kerja: Replikasi Ekosistem 4-Pilar untuk Persamaan Diferensial (Minggu 01 & 02)
**Tanggal & Waktu:** 20 September 2026, 08:25 WIB  
**Mata Kuliah:** Persamaan Diferensial (Fokus Persiapan Medan Elektromagnetika & Rangkaian Listrik)  
**Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Institusi:** Program Studi S1 Teknik Elektro, Universitas Bengkulu  

---

## 1. Konteks & Pencapaian Sesi
Melanjutkan ekosistem **Digital Course Engine 4-Pilar** ke **Minggu 02: PDB Orde 1 (Persamaan Separabel, Eksak & Faktor Integrasi)** setelah sukses menuntaskan Minggu 01.

---

## 2. Rincian Pekerjaan Minggu 02 yang Telah Selesai

### A. Pabrikasi Video Kuliah 1080p Full HD
- **Skrip Generator:** [build_video_w02.py](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/build_video_w02.py)
- **Ekstraksi Salindia:** 31 salindia Beamer dari [ch2.pdf](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/ch2.pdf) diekstrak ke dalam resolusi $1920 \times 1080$ Full HD (`scratch/slide_frames_w02/`).
- **Sintesis Audio:** Seluruh narasi audio alami bahasa Indonesia berhasil disintesis menggunakan Microsoft Edge TTS (`id-ID-ArdiNeural`) dengan jeda bantalan (*padding*) 1,2 detik per pergantian slide.
- **Hasil Video Final:**
  - Berkas: [video_pd_minggu02.mp4](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_pd_minggu02.mp4)
  - Resolusi: **1080p Full HD ($1920 \times 1080$)**
  - Durasi: **10 menit 06 detik** (606 detik)
  - Ukuran: **11,49 MB** (kompresi optimal `libx264 stillimage` + `aac 192k`).

### B. Naskah YouTube SEO & Unggah Otomatis
- **Naskah Metadata:** [video_script_pd_w02.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_script_pd_w02.md) dibuat lengkap dengan timestamps bab per detik, referensi buku (Kreyszig, Zill, Hayt), dan tagar resmi.
- **Unggah YouTube:** Berhasil diunggah ke kanal resmi **Novalio Daratha** dengan visibilitas **Public**:
  - **URL Resmi:** [https://youtu.be/r5nFrD9DkOE](https://youtu.be/r5nFrD9DkOE)
  - **Video ID:** `r5nFrD9DkOE`
  - **Playlist Resmi:** Otomatis dimasukkan ke dalam [Persamaan Diferensial - Teknik Elektro UNIB](https://www.youtube.com/playlist?list=PLS5oOZWXZeTw).
  - **Pelacakan ID:** Diperbarui di [uploaded_youtube_videos.json](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/uploaded_youtube_videos.json).

### C. Integrasi Web Portal & Live Deployment
- [docs/02_modul_2.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/docs/02_modul_2.md) diperbarui dengan pemutar video YouTube responsif dan kotak unduhan berkas pembelajaran Minggu 2.
- [docs/index.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/docs/index.md) diperbarui dengan tautan tonton video Minggu 2 pada tabel perkuliahan.
- MkDocs berhasil dikompilasi ulang (`mkdocs build`) dan disinkronkan ke repositori portal produksi di `ndaratha.my.id/public/persamaan-diferensial/`.
- Perubahan di-commit dan di-push ke GitHub (`97679ed`) serta didistribusikan ke Vercel Production.

---

## 3. Matriks Video Perkuliahan YouTube

| Minggu | Topik Materi Perkuliahan | Durasi | Tautan Resmi YouTube (Public) |
| :---: | :--- | :---: | :---: |
| **01** | Pengantar PDB vs PDP, Orde, Linieritas, IVP & Rangkaian Listrik | 12:19 | [https://youtu.be/umcAHSZyhCE](https://youtu.be/umcAHSZyhCE) |
| **02** | PDB Orde 1: Persamaan Separabel, Eksak & Faktor Integrasi | 10:06 | [https://youtu.be/r5nFrD9DkOE](https://youtu.be/r5nFrD9DkOE) |
| **03** | Aplikasi PDB Orde 1: Transien Rangkaian Listrik RC & RL | *Antrean* | Minggu Berikutnya |

---

## 4. Tautan Penting
- **Portal Perkuliahan Live:** [https://www.ndaratha.my.id/persamaan-diferensial/](https://www.ndaratha.my.id/persamaan-diferensial/)
- **Modul Minggu 02 Live:** [https://www.ndaratha.my.id/persamaan-diferensial/02_modul_2/](https://www.ndaratha.my.id/persamaan-diferensial/02_modul_2/)
- **Playlist YouTube Resmi:** [https://www.youtube.com/playlist?list=PLS5oOZWXZeTw](https://www.youtube.com/playlist?list=PLS5oOZWXZeTw)
