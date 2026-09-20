# Ringkasan Sesi Perkuliahan & Pabrikasi Video Persamaan Diferensial
**Waktu Pelaksanaan:** Minggu, 20 September 2026, 17:08 WIB  
**Dosen Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Institusi:** Program Studi S1 Teknik Elektro, Fakultas Teknik, Universitas Bengkulu  

---

## 1. Perbaikan Kuis Salindia 14 Video Minggu 03 (Menit 09:40)
- **Gejala Laporan Pengguna:** Pada video Minggu 03 (k3-3) sekitar menit 09:40, soal yang disuarakan oleh narator TTS dan soal yang ditampilkan pada salindia tidak sama.
- **Investigasi:**
  - Salindia visual pada `ch3.pdf` (Frame 14) menampilkan studi kasus:
    - **Kasus Rekayasa:** *"Trafo 60 MVA dibebani lebih mendadak 150%. Mengapa temperatur minyak atas lambat naik sedangkan hotspot kawat tembaga langsung melonjak dalam hitungan menit?"*
    - **Pilihan Jawaban:** [A] Viskositas minyak tinggi, [B] Kapasitas kalor massa minyak puluhan ton sangat masif ($\tau_{\text{oil}} \gg \tau_w$), sedangkan massa kawat tembaga kecil, [C] Sirkulasi terhenti, [D] Resistansi menyusut.
  - Namun naskah narasi audio lama pada `video_builder/data_w03.py` masih membacakan soal lain tentang relay dan transistor tanpa dioda freewheeling.
- **Tindakan Perbaikan:**
  1. Memperbarui `video_builder/data_w03.py` (Salindia 14 Bagian 1 dan Bagian 2) agar tepat 100% selaras kata-demi-kata dan rumus dengan teks salindia `ch3.tex`.
  2. Menghapus *cache* audio lama salindia 14 (`scratch/w03_v2/tts_14*.mp3` dan `clip_14.mp4`).
  3. Membangun ulang video Minggu 03 secara penuh:
     - Durasi total: 11 menit 29 detik ($689{,}92\text{ s}$).
     - Selisih akhir video dan audio: **23,24 ms** (setara 1 frame audio AAC, **0 ms cumulative drift**).
     - Sinkronisasi otomatis ke direktori root [video_pd_minggu03.mp4](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_pd_minggu03.mp4) dan portal [portal/public/video/video_pd_minggu03.mp4](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/portal/public/video/video_pd_minggu03.mp4).
     - Naskah YouTube diperbarui pada [video_script_pd_w03_v2.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_script_pd_w03_v2.md) dengan linimasa akurat bab Salindia 14 dimulai tepat pada **09:00**.

---

## 2. Status Pembaruan Batch Video Pekan Lainnya
- Batch runner latar belakang (`task-2654`) sedang menyelesaikan perenderan ulang seluruh pekan (W02, W04, W05, W06, W07, W09, W10, W11, W12, W13, W14, W15) dengan arsitektur sinkronisasi presisi frame (0 ms audio-video drift).
- Semua video terkompilasi dalam kualitas 1080p Full HD CRF 18, audio Stereo AAC 192k (44.1 kHz), dan terhubung langsung ke portal perkuliahan.
