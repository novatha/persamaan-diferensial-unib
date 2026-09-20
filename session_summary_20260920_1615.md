# Ringkasan Sesi Perkuliahan: Pabrikasi Video Kuliah v2.0 (Minggu 02)
**Waktu Eksekusi:** Minggu, 20 September 2026, 16:15 WIB  
**Mata Kuliah:** Persamaan Diferensial (Teknik Elektro UNIB)  
**Dosen Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.

---

## 1. Latar Belakang & Tindakan
Sesuai arahan pengampu (Opsi A), dilakukan redesain dan pabrikasi ulang video perkuliahan **Minggu 02** ke standar mutu **Versi 2.0 (v2.0)** untuk mengatasi seluruh kelemahan versi awal (audio mono, bitrate rendah, ketidaksesuaian salindia dengan modul/OBE, dan ketiadaan jeda kuis).

---

## 2. Hasil Eksekusi Minggu 02 (v2.0)

| Parameter | Spesifikasi Teknis Hasil | Catatan Mutu |
|---|---|---|
| **Resolusi Video** | **1080p Full HD (1920 × 1080)** | Diekstrak pada 300 DPI langsung dari `ch2.pdf` resmi |
| **Durasi Total** | **13 menit 18 detik** (798.1 detik) | 15 Salindia berbobot pedagogis komprehensif |
| **Ukuran Berkas** | **31,4 MB** (31.447.960 bytes) | Efisiensi kompresi H.264 CRF 18 |
| **Format Audio** | **Stereo AAC 192 kbps, 44.1 kHz** | 2 Saluran audio jernih dan imersif |
| **Mesin TTS** | **Microsoft Edge TTS (`id-ID-ArdiNeural`)** | Diksi bahasa Indonesia alami dan formal |
| **Jeda Kuis Terprogram** | **8 Detik Hening** (`quiz_pause_8s.mp3`) | Mahasiswa diberi ruang berpikir sebelum pembahasan |
| **Sinkronisasi Portal** | `portal/public/video/video_pd_minggu02.mp4` | Siap tayang di web portal resmi |
| **Naskah YouTube** | `video_script_pd_w02_v2.md` | Lengkap dengan timestamps 15 bab, CPMK & tagar |

---

## 3. Cakupan Materi 15 Salindia Minggu 02
1. **Slide 01:** Judul Resmi & Perkenalan Dosen Pengampu
2. **Slide 02:** Capaian Pembelajaran (Sub-CPMK 2 OBE) & Taksonomi Bloom C1–C6
3. **Slide 03:** Peta Konsep Metodologi Solusi PDB Orde 1 (Diagram Alir TikZ)
4. **Slide 04:** Metode 1: Persamaan Separabel (Pemisahan Variabel)
5. **Slide 05:** Metode 2: Persamaan Diferensial Eksak (Teorema Euler-Clairaut)
6. **Slide 06:** Intuisi Fisika: Medan Vektor Konservatif ($\nabla \times \mathbf{E} = 0$) & Garis Ekuipotensial
7. **Slide 07:** Metode 3: Faktor Pengintegrasi $\mu(x)$ dan $\mu(y)$
8. **Slide 08:** Pemodelan Fisis Rangkaian: Pengisian Kapasitor RC (KVL First-Principles)
9. **Slide 09:** Derivasi Analitik Solusi Khusus Tegangan $v_C(t)$ dan Arus $i(t)$
10. **Slide 10:** Dinamika Transien & Paradoks Efisiensi Disipasi Kalor 50%
11. **Slide 11:** Studi Kasus Industri: Proteksi Sakelar IGBT (Rangkaian RC Snubber IEEE/IEC)
12. **Slide 12:** Contoh Soal Terhitung (*Worked Example*): Bank Kapasitor Gardu Induk
13. **Slide 13:** Praktikum Komputasi Numerik Terbuka **Julia** (`DifferentialEquations.jl` & `Tsit5()`)
14. **Slide 14:** Kuis Konseptual Interaktif (dengan Jeda 8 Detik) & Tantangan Bloom C4–C6
15. **Slide 15:** Rangkuman Inti Perkuliahan 4-Pilar & Referensi Buku Acuan

---

## 4. Berkas yang Dihasilkan
- [`video_pd_minggu02.mp4`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_pd_minggu02.mp4)
- [`portal/public/video/video_pd_minggu02.mp4`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/portal/public/video/video_pd_minggu02.mp4)
- [`video_script_pd_w02_v2.md`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_script_pd_w02_v2.md)
- [`build_video_w02_v2.py`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/build_video_w02_v2.py)

---

## 5. Rencana Langkah Selanjutnya
Memulai pabrikasi otomatis berurutan (*batch processing*) untuk **Minggu 03 s.d. Minggu 15** (kecuali Minggu 08 UTS) menggunakan arsitektur pipeline v2.0 yang telah terbukti andal ini.
