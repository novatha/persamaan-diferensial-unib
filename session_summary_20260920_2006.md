# Ringkasan Sesi Perkuliahan: Rekonstruksi Total Naskah Minggu 4 & Unggah Ulang YouTube
**Tanggal & Waktu:** 20 September 2026, 20:06 WIB  
**Berkas:** `session_summary_20260920_2006.md`  
**Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Institusi:** Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika, Fakultas Teknik, Universitas Bengkulu  
**URL Produksi:** [https://pd.ndaratha.my.id](https://pd.ndaratha.my.id)  
**Tautan YouTube Resmi Minggu 4:** [https://youtu.be/be3FdcQkq6o](https://youtu.be/be3FdcQkq6o)

---

## 1. Masalah yang Diselesaikan
Dilakukan audit dan pembacaan kritis terhadap berkas sumber presentasi Beamer [ch4.tex](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/ch4.tex). Ditemukan bahwa naskah narasi video Minggu 4 sebelumnya memiliki beberapa ketidaksesuaian substantif antara apa yang ditampilkan di salindia dan apa yang diucapkan oleh narasi audio:
1. **Salindia 02 (Sub-CPMK & Bloom):** Narasi lama menyebutkan target C1–C6 secara generik, padahal salindia memuat butir target spesifik (Wronskian, interaksi medan magnet $L$ vs medan listrik $C$, 3 kasus diskriminan, rasio redaman $\zeta$, dan trajektori ruang fasa).
2. **Salindia 03 (Peta Konsep):** Penjelasan fisis pertukaran energi medan magnet $\frac{1}{2}Li^2$ dan medan listrik $\frac{1}{2}Cv^2$ belum disebutkan secara utuh.
3. **Salindia 04 (Bentuk Standar PDB Orde 2 Homogen):** Salindia memuat PDB dengan variabel bebas $x$, solusi coba $y(x) = e^{rx}$, dan karakteristik $ar^2+br+c=0$, namun narasi suara lama menyebutkan variabel waktu $t$ dan variabel Laplace $s$.
4. **Salindia 05 (Teorema Superposisi & Wronskian):** Narasi lama tidak menyebutkan ekspresi eksplisit $W(y_1, y_2) = y_1 y_2' - y_1' y_2 \neq 0$ dan implikasi $W = 0$.
5. **Salindia 06 (Pemodelan Sirkuit RLC Seri):** Salindia menurunkan KVL dalam muatan $q(t)$ ($L q'' + R q' + \frac{1}{C}q = 0$) lalu diturunkan menjadi persamaan arus $i(t)$, sedangkan narasi lama membahas tegangan kapasitor $v_C(t)$.
6. **Salindia 07–10 (Tiga Ragam Redaman):** Konstanta solusi umum pada salindia menggunakan notasi $C_1, C_2$, sedangkan narasi lama menggunakan notasi $A_1, A_2$ dan $B_1, B_2$.
7. **Salindia 11 (Tangki LC Murni & Ruang Fasa):** Narasi lama belum menguraikan persamaan analitis $v_C(t) = V_m \cos(\omega_0 t + \phi)$ dan hukum kekekalan energi total $E_{\text{total}} = \frac{1}{2} C V_m^2 = \text{Konstan}$.
8. **Salindia 12 (Worked Example RLC Seri Industri):** Narasi lama membacakan angka-angka yang sama sekali berbeda ($L=10\text{ mH}, C=1\,\mu\text{F}, \omega_0=10.000\text{ rad/s}$), padahal angka riil pada salindia adalah $L=0{,}5\text{ H}$, $C=20\,\mu\text{F}$, $\omega_0=316{,}2\text{ rad/s}$, $R_{\text{kritis}}=316{,}2\ \Omega$, $R=60\ \Omega$, $\alpha=60\text{ Np/s}$, $\omega_d=310{,}5\text{ rad/s}$, $C_1=100\text{ V}$, $C_2=19{,}32\text{ V}$, $v_C(t) = e^{-60t}(100\cos 310{,}5t + 19{,}3\sin 310{,}5t)$, dan $T_d = 20{,}2\text{ ms}$.
9. **Salindia 13 (Praktikum Julia):** Belum menjelaskan secara presisi fungsi `rlc!(du, u, p, t)`, solver `Tsit5()`, serta interpretasi 3 kurva respon.

---

## 2. Tindakan dan Solusi
1. **Rekonstruksi Total Naskah Narasi (`video_builder/data_w04.py`):**
   - Menulis ulang naskah narasi ke-15 salindia kata demi kata agar 100% selaras dengan tampilan teks, simbol matematika, variabel, grafik, dan blok kode pada [ch4.tex](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/ch4.tex).
   - Memperbarui dokumentasi YouTube naskah pada [video_script_pd_w04_v2.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/video_script_pd_w04_v2.md).

2. **Sintesis Audio & Render Video Ulang:**
   - Membersihkan *cache* `scratch/w04_v2` dan menjalankan pabrikasi video melalui `video_builder/run_batch.py 04`.
   - Durasi video: **14 menit 14 detik** (854,52 s).
   - Selisih durasi video vs audio: **23,2 ms** (1 frame audio AAC, setara **0,00 ms *drift***).

3. **Pengunggahan ke YouTube:**
   - Berhasil diunggah ke YouTube dengan Video ID baru: **`be3FdcQkq6o`**.
   - Tautan Resmi: [https://youtu.be/be3FdcQkq6o](https://youtu.be/be3FdcQkq6o).
   - Video telah dimasukkan ke *playlist* resmi `Persamaan Diferensial - Teknik Elektro UNIB` (`PLS5oOZWXZeTw`).

4. **Sinkronisasi Web Portal & Deployment Produksi:**
   - Memperbarui tautan di [portal/src/data/pdData.ts](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/portal/src/data/pdData.ts) dan [docs/index.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/docs/index.md).
   - Re-build Astro portal & MkDocs dokumentasi.
   - Sinkronisasi aset statis portal ke repositori hosting `ndaratha.my.id`.
   - Deployment produksi ke Vercel: domain `https://pd.ndaratha.my.id` (**HTTP/2 200 OK**).

5. **Version Control:**
   - Seluruh perubahan berkas sumber dan naskah telah di-*commit* dan di-*push* ke remote GitHub `main`.
