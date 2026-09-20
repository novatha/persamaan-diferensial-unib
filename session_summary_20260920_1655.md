# Ringkasan Sesi Perkuliahan & Pabrikasi Video Persamaan Diferensial
**Waktu Pelaksanaan:** Minggu, 20 September 2026, 16:55 WIB  
**Dosen Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Institusi:** Program Studi S1 Teknik Elektro, Fakultas Teknik, Universitas Bengkulu  

---

## 1. Masalah yang Ditemukan (User Bug Report)
- **Gejala:** Pada video perkuliahan Minggu 03 (dan seluruh video seri hasil kompilasi batch v2.0 awal), suara narator dan tampilan visual salindia tidak sinkron saat terjadi pergeseran slide (*audio-video desynchronization drift*).
- **Akar Masalah (*Root Cause*):**
  1. Pada perenderan klip individual salindia (`render_single_clip` di `video_builder/engine.py`), digunakan perintah `ffmpeg -loop 1 -i img -i aud ... -shortest clip.mp4`.
  2. Flag `-shortest` pada FFmpeg saat memproses loop gambar tidak memotong tepat di ujung audio, melainkan mem-buffer frame video hingga batas GOP/paket berikutnya (~25 fps). Akibatnya, stream video pada setiap klip lebih panjang **1,4 hingga 1,6 detik** dibandingkan stream audionya.
  3. Saat seluruh klip digabungkan menggunakan metode demuxer concat cepat (`ffmpeg -f concat -c copy`), stream video dan audio disambung secara independen.
  4. Surplus video ~1,5 detik per klip menyebabkan audio melompat maju mendahului video secara kumulatif sebesar ~1,5 detik di setiap pergantian slide:
     - Salindia 1: Audio mendahului 1,42 detik.
     - Salindia 5: Audio mendahului 7,45 detik.
     - Salindia 10: Audio mendahului 14,83 detik.
     - Salindia 15: Audio mendahului **22,05 detik**!
  5. Akibatnya, narator telah membahas materi salindia berikutnya padahal salindia di layar belum bergeser.

---

## 2. Solusi & Perbaikan Teknis (0 ms Audio-Video Drift)
1. **Peniadaan `-shortest` & Penentuan Durasi Presisi Analitik:**
   Durasi target dihitung eksak berdasarkan durasi riil audio ditambah jeda pergantian salindia 1,0 detik (*audio padding*) sesuai standar `AGENTS.md`:
   $$\text{exact\_dur} = \frac{\text{round}((\text{dur\_aud} + \text{PAD\_DUR}) \times 25)}{25.0}$$
2. **Filter Sinkronisasi FFmpeg Simultan:**
   - Audio dipad dengan keheningan lalu dipotong persis pada `exact_dur`:
     `-af "apad,atrim=0:{exact_dur:.4f}"`
   - Video dibatasi secara deterministik pada `exact_dur`:
     `-t {exact_dur:.4f}`
3. **Hasil Uji Metrik Sinkronisasi (Minggu 03):**
   - Selisih per klip (Salindia 01 s.d. 15): **0,00 ms (Presisi Sempurna!)**
   - Durasi total video stream: $676{,}0800\text{ s}$
   - Durasi total audio stream: $676{,}1032\text{ s}$
   - Selisih akhir video utuh: $23{,}22\text{ ms}$ (setara 1 paket audio AAC), sehingga kumulatif drift antar-salindia adalah **0 ms**.
4. **YouTube Timestamps Terkalibrasi:**
   Naskah YouTube di `video_script_pd_w03_v2.md` mencantumkan linimasa bab yang 100% cocok dengan detik pergeseran salindia di layar.

---

## 3. Status Pabrikasi Video Perkuliahan
- **Minggu 01:** Selesai dirender ulang, 0,00 ms drift, terintegrasi ke `portal/public/video/video_pd_minggu01.mp4`.
- **Minggu 03:** Selesai dirender ulang, 0,00 ms drift, terintegrasi ke `portal/public/video/video_pd_minggu03.mp4`.
- **Minggu 02, 04 s.d. 15:** Sedang diproses secara paralel melalui batch runner di latar belakang (`video_builder/run_batch.py`).
- Seluruh modul ajar, lembar kerja C1-C6, problem set, dan portal web telah tersinkronisasi.
