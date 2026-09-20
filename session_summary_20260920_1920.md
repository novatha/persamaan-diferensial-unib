# Ringkasan Sesi Perkuliahan: Sinkronisasi Variabel Salindia 4 Minggu 4 & Unggah Ulang YouTube
**Tanggal & Waktu:** 20 September 2026, 19:20 WIB  
**Berkas:** `session_summary_20260920_1920.md`  
**Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Institusi:** Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika, Fakultas Teknik, Universitas Bengkulu  
**URL Produksi:** [https://pd.ndaratha.my.id](https://pd.ndaratha.my.id)  
**Tautan YouTube Resmi Minggu 4:** [https://youtu.be/Auxi-6ZSJ6o](https://youtu.be/Auxi-6ZSJ6o)

---

## 1. Masalah yang Diperbaiki
Pada video perkuliahan **Minggu 4**, Salindia 4 menampilkan persamaan diferensial linier orde 2 homogen koefisien konstan dengan variabel bebas $x$:
$$a \frac{d^2 y}{dx^2} + b \frac{dy}{dx} + c y = 0, \quad (a \neq 0)$$
dengan postulat basis solusi eksponensial $y(x) = e^{rx}$, persamaan karakteristik:
$$a r^2 + b r + c = 0$$
serta akar kuadrat $r_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ dan diskriminan $D = b^2 - 4ac$.

Namun narasi suara audio lama menyebutkan variabel waktu $t$ dan variabel Laplace $s$.

---

## 2. Tindakan dan Solusi yang Dilakukan
1. **Pembaruan Naskah Narasi TTS (`video_builder/data_w04.py`):**
   - Mengubah narasi audio Salindia 4 secara presisi:
     > *"Bentuk umum PDB orde dua linier homogen koefisien konstan dinyatakan sebagai: a dikali d kuadrat y per d x kuadrat ditambah b dikali d y per d x ditambah c dikali y sama dengan nol, dengan konstanta a tidak sama dengan nol. Dengan menggunakan postulat solusi basis eksponensial y x sama dengan e pangkat r dikali x, kita turunkan Persamaan Karakteristik: a dikali r kuadrat ditambah b dikali r ditambah c sama dengan nol. Akar-akar persamaan kuadrat ini ditentukan oleh rumus a b c, yaitu r satu dan r dua sama dengan minus b plus minus akar b kuadrat dikurang empat a c seluruhnya dibagi dua a. Sifat dari solusi sistem sepenuhnya ditentukan oleh tanda diskriminan D sama dengan b kuadrat dikurang empat a c."*
   - Memperbarui naskah dokumentasi YouTube pada `video_script_pd_w04_v2.md`.

2. **Pembersihan Cache & Render Ulang Video:**
   - Menghapus direktori cache `scratch/w04_v2`.
   - Melakukan sintesis ulang Microsoft Edge TTS (`id-ID-ArdiNeural`) dan rendering 15 klip video 1080p secara paralel menggunakan `video_builder/run_batch.py 04`.
   - Durasi total video: **11 menit 20 detik** (680,60 s).
   - Selisih durasi video vs audio: **23,2 ms** (1 frame audio AAC, setara **0,00 ms drift** yang dapat dirasakan).

3. **Pengunggahan Ulang ke YouTube:**
   - Video berhasil diunggah menggunakan `upload_to_youtube.py` dengan akun resmi pengampu.
   - **Video ID Baru:** `Auxi-6ZSJ6o`
   - **URL Video:** [https://youtu.be/Auxi-6ZSJ6o](https://youtu.be/Auxi-6ZSJ6o)
   - Berhasil dimasukkan ke dalam *playlist* resmi: `Persamaan Diferensial - Teknik Elektro UNIB` (`PLS5oOZWXZeTw`).
   - Berkas `uploaded_youtube_videos.json` diperbarui secara otomatis.

4. **Sinkronisasi Web Portal & Deployment:**
   - Memperbarui tautan YouTube di katalog materi portal ([portal/src/data/pdData.ts](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/portal/src/data/pdData.ts)) dan tabel panduan MkDocs ([docs/index.md](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/docs/index.md)).
   - Membangun portal Astro (`npm --prefix portal run build`) dan MkDocs (`mkdocs build`).
   - Melakukan rsync aset statis portal ke repositori publik utama `ndaratha.my.id`.
   - Melakukan deployment produksi ke Vercel (`vercel --prod --yes`), menghasilkan respon HTTP/2 200 OK pada domain `https://pd.ndaratha.my.id`.

5. **Version Control:**
   - Seluruh perubahan berkas sumber telah di-*commit* (`e8b9759`) dan di-*push* ke remote GitHub `main`.
