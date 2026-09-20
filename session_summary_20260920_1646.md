# Ringkasan Sesi Perkuliahan: Penyelesaian Penuh Pabrikasi Video Kuliah v2.0 (Minggu 01–15)
**Waktu Eksekusi:** Minggu, 20 September 2026, 16:46 WIB  
**Mata Kuliah:** Persamaan Diferensial (Teknik Elektro UNIB)  
**Dosen Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.

---

## 1. Pencapaian Utama Sesi Ini
Seluruh rangkaian video perkuliahan daring untuk mata kuliah **Persamaan Diferensial** semester genap 2026 (**14 Video Lengkap, Minggu 01 s.d. Minggu 15, minus W08 UTS**) telah **100% SELESAI DIPRODUKSI** dengan standar mutu tinggi **Versi 2.0 (v2.0)** berbasis **Model 4-Pilar Pedagogis OBE**.

---

## 2. Matriks Verifikasi Teknis 14 Video Perkuliahan (v2.0)

| Minggu | Berkas Video Utama | Durasi | Resolusi | Format Audio | Saluran | Ukuran | Status Portal |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **01** | `video_pd_minggu01.mp4` | 14:34 | 1920 × 1080 | AAC 192k | 2 ch (Stereo) | 18.8 MB | ✅ Tersinkron |
| **02** | `video_pd_minggu02.mp4` | 13:18 | 1920 × 1080 | AAC 192k | 2 ch (Stereo) | 30.0 MB | ✅ Tersinkron |
| **03** | `video_pd_minggu03.mp4` | 11:23 | 1920 × 1080 | AAC 192k | 2 ch (Stereo) | 26.0 MB | ✅ Tersinkron |
| **04** | `video_pd_minggu04.mp4` | 11:16 | 1920 × 1080 | AAC 192k | 2 ch (Stereo) | 25.1 MB | ✅ Tersinkron |
| **05** | `video_pd_minggu05.mp4` | 11:04 | 1920 × 1080 | AAC 192k | 2 ch (Stereo) | 26.1 MB | ✅ Tersinkron |
| **06** | `video_pd_minggu06.mp4` | 11:12 | 1920 × 1080 | AAC 192k | 2 ch (Stereo) | 24.6 MB | ✅ Tersinkron |
| **07** | `video_pd_minggu07.mp4` | 11:24 | 1920 × 1080 | AAC 192k | 2 ch (Stereo) | 25.6 MB | ✅ Tersinkron |
| **09** | `video_pd_minggu09.mp4` | 11:30 | 1920 × 1080 | AAC 192k | 2 ch (Stereo) | 27.6 MB | ✅ Tersinkron |
| **10** | `video_pd_minggu10.mp4` | 11:29 | 1920 × 1080 | AAC 192k | 2 ch (Stereo) | 27.1 MB | ✅ Tersinkron |
| **11** | `video_pd_minggu11.mp4` | 11:13 | 1920 × 1080 | AAC 192k | 2 ch (Stereo) | 26.5 MB | ✅ Tersinkron |
| **12** | `video_pd_minggu12.mp4` | 11:21 | 1920 × 1080 | AAC 192k | 2 ch (Stereo) | 27.1 MB | ✅ Tersinkron |
| **13** | `video_pd_minggu13.mp4` | 11:37 | 1920 × 1080 | AAC 192k | 2 ch (Stereo) | 27.9 MB | ✅ Tersinkron |
| **14** | `video_pd_minggu14.mp4` | 11:39 | 1920 × 1080 | AAC 192k | 2 ch (Stereo) | 27.9 MB | ✅ Tersinkron |
| **15** | `video_pd_minggu15.mp4` | 11:39 | 1920 × 1080 | AAC 192k | 2 ch (Stereo) | 27.5 MB | ✅ Tersinkron |

*Total Durasi Seluruh Video:* **2 jam 42 menit 59 detik** tayangan akademik berkualitas tinggi.

---

## 3. Standar Mutu yang Diterapkan pada Seluruh Video
1. **Visual Beresolusi Tinggi (300 DPI):**
   - Diekstrak langsung dari salindia resmi Beamer 16:9 Madrid (`ch1.pdf` s.d. `ch15.pdf`).
   - Bebas distorsi, teks formula tajam, diagram TikZ dan CircuiTikZ presisi.
2. **Audio Stereo AAC 192 kbps (44.1 kHz, 2 Channel):**
   - Suara sintesis Microsoft Edge TTS `id-ID-ArdiNeural` dengan intonasi formal akademik dan artikulasi bahasa Indonesia alami.
3. **Kuis Interaktif Terprogram:**
   - Setiap video pada slide kuis (Slide 14) memuat jeda hening terprogram selama **8 detik** (`quiz_pause_8s.mp3`) memberi ruang mahasiswa berpikir dan menganalisis sebelum kunci jawaban dibahas.
4. **Pilar 3 Komputasi Julia:**
   - Setiap video memuat visualisasi simulasi numerik terbuka berbasis paket `DifferentialEquations.jl`, `Plots.jl`, atau `SpecialFunctions.jl`.
5. **Metadata YouTube Lengkap (SEO Optimized):**
   - Seluruh berkas `video_script_pd_w01_v2.md` s.d. `video_script_pd_w15_v2.md` tersedia lengkap dengan timestamps linimasa 15 bab, Sub-CPMK OBE C1–C6, dan referensi standar IEEE/IEC.
6. **Integrasi Portal Otomatis:**
   - Seluruh 14 berkas video telah tersinkronkan ke direktori aset web: `portal/public/video/video_pd_minggu*.mp4`.

---

## 4. Struktur Modul & Skrip Pembangun yang Diciptakan
- `video_builder/engine.py` (Mesin komputasi paralel multi-core dan asinkron TTS `asyncio.gather`)
- `video_builder/run_batch.py` (Orkestrator batch runner)
- `video_builder/data_w03.py` s.d. `video_builder/data_w15.py` (Basis data narasi 15 slide per pekan)
- `build_video_w01_v2.py` & `build_video_w02_v2.py` (Skrip mandiri minggu pembuka)
