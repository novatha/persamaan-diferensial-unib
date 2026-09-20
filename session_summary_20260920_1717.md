# Ringkasan Sesi Perkuliahan & Pabrikasi Video Persamaan Diferensial
**Waktu Pelaksanaan:** Minggu, 20 September 2026, 17:17 WIB  
**Dosen Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Institusi:** Program Studi S1 Teknik Elektro, Fakultas Teknik, Universitas Bengkulu  

---

## 1. Perbaikan Kuis Salindia 14 Video Minggu 04 (Kasus Serupa dengan W03)
- **Gejala Laporan Pengguna:** Pada video Minggu 04, soal kuis yang disuarakan oleh narator TTS dan soal yang ditampilkan pada salindia tidak sama.
- **Investigasi:**
  - Salindia visual pada [ch4.pdf](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/ch4.pdf) (Frame 14) menampilkan:
    - **Kasus Rekayasa:** *"Mengapa aktuator penutup pemutus tenaga (PMT) gardu induk dan jarum ukur analog selalu dirancang tepat pada kondisi redaman kritis ($\zeta = 1$)?"*
    - **Pilihan Jawaban:** [A] Mengurangi daya baterai DC, [B] Mencapai posisi tunak dalam waktu tersingkat tanpa mengalami lenting/osilasi (*overshoot*)!, [C] Menghasilkan tegangan transien terbesar, [D] Mencegah panas kumparan.
    - **Tantangan Bloom C4–C6:** Wronskian $W(y_1, y_2)(0) \ne 0$, radiasi tangki LC, desain resistansi filter $\omega_d = 314\text{ rad/s}$.
  - Namun naskah narasi audio lama pada [video_builder/data_w04.py](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_builder/data_w04.py) masih membacakan soal kuis lama tentang variasi nilai $R$ dari 0 hingga tak hingga (tahapan transisi ragam respon).
- **Tindakan Perbaikan:**
  1. Memperbarui `video_builder/data_w04.py` (Salindia 14 Bagian 1 dan 2) agar tepat 100% selaras kata-demi-kata dan rumus dengan teks salindia `ch4.tex`.
  2. Menghapus *cache* audio lama salindia 14 (`scratch/w04_v2/tts_14*.mp3` dan `clip_14.mp4`).
  3. Membangun ulang video Minggu 04 secara penuh:
     - Durasi total: 11 menit 15 detik ($675{,}68\text{ s}$).
     - Selisih akhir video dan audio: **23,24 ms** (setara 1 frame audio AAC, **0 ms cumulative drift**).
     - Sinkronisasi otomatis ke direktori root [video_pd_minggu04.mp4](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_pd_minggu04.mp4) dan portal [portal/public/video/video_pd_minggu04.mp4](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/portal/public/video/video_pd_minggu04.mp4).
     - Naskah YouTube diperbarui pada [video_script_pd_w04_v2.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_script_pd_w04_v2.md) dengan linimasa akurat bab Salindia 14 dimulai tepat pada **08:47**.

---

## 2. Audit Komprehensif Salindia 14 untuk Pekan Lainnya
Dari hasil audit skrip perbandingan lintas pekan antara berkas sumber `chXX.tex` dan `data_wXX.py`:
- **Pekan yang sudah 100% Sesuai:** Minggu 01, Minggu 02, Minggu 03, Minggu 04, Minggu 14, Minggu 15.
- **Pekan yang memiliki perbedaan teks kuis Salindia 14:** Minggu 05, Minggu 06, Minggu 07, Minggu 09, Minggu 10, Minggu 11, Minggu 12, Minggu 13.
- Disiapkan rencana penyesuaian otomatis naskah kuis untuk seluruh pekan tersebut agar semua video seri memiliki konsistensi audio-visual 100%.
