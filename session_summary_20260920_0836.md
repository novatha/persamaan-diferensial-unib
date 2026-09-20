# Ringkasan Sesi Perkuliahan: Replikasi Standar Modul DSTL ke Persamaan Diferensial
**Waktu Eksekusi:** Minggu, 20 September 2026, Pukul 08:36 WIB  
**Mata Kuliah:** Persamaan Diferensial (Fokus Medan Elektromagnetika & Rangkaian Listrik)  
**Pengampu:** Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.  
**Program Studi:** S1 Teknik Elektro, Fakultas Teknik, Universitas Bengkulu  

---

## 1. Analisis & Peniruan Standar Emas Modul DSTL
Berdasarkan instruksi pengguna untuk *"tiru modul yang ada pada kuliah dasar sistem tenaga listrik"*, dilakukan penelusuran terhadap repositori referensi di `/Users/novaliodaratha/Documents/pengajaran/dasar sistem tenaga listrik/2026/` (`notes_dstl_w01.tex` s.d. `notes_dstl_w07.tex`, masing-masing 20 s.d. 30 halaman PDF).

Ditemukan bahwa modul ajar DSTL memiliki arsitektur monograf berstandar emas:
1. **Tipografi & Desain LaTeX Profesional:** Format `article` 11pt, margin 2.5 cm, `fancyhdr` resmi UNIB, palet warna institusi (`headercolor` Navy, `accentcolor` Blue, `shadecolor`).
2. **Capaian Pembelajaran Berbasis OBE:** Kotak `tcolorbox` Sub-CPMK terperinci mencakup Taksonomi Bloom berjenjang dari level **C1 (Mengingat)** hingga **C6 (Menciptakan/Komputasi)**.
3. **Peta Konsep & Posisi Kurikulum:** Diagram alir visual menggunakan **TikZ** yang memetakan posisi pekan perkuliahan dalam alur semester (PDB Paruh 1 vs PDP Paruh 2).
4. **Model 4-Pilar Pedagogis:**
   - *Pilar 1: Intuisi Fisika Rekayasa* (Mengapa persamaan diferensial muncul dari dinamika energi medan magnet $\frac{1}{2} L i^2$, medan listrik $\frac{1}{2} C v^2$, dan disipasi kalor).
   - *Pilar 2: Derivasi Matematis Eksplisit* (Penurunan analitis langkah-demi-langkah tanpa loncatan baris/rumus).
   - *Pilar 3: Komputasi Numerik Terbuka* (Skrip lengkap **GNU Octave** siap pakai untuk simulasi transien, perbandingan analitis vs numerik `ode45`, dan *slope field*).
   - *Pilar 4: Aplikasi Nyata Industri & Standar Teknik Elektro* (Transien gardu induk, arus inrush, proteksi trafo).
5. **Contoh Soal Terhitung (*Worked Numerical Examples*):** Contoh soal langkah demi langkah dengan angka riil.
6. **Evaluasi & Bank Soal Mandiri Berjenjang (Bloom C1 s.d. C6).**
7. **Rangkuman Konseptual, Glosarium Istilah Teknis, & Referensi Standar (Kreyszig, Zill, Hayt, Alexander & Sadiku, IEEE/IEC/Grid Code).**

---

## 2. Realisasi pada Modul 1 Persamaan Diferensial
Modul 1 (`modul_1.tex`) yang sebelumnya hanya berupa ringkasan 3 halaman (92 baris kode) telah ditransformasikan secara radikal menjadi monograf lengkap berbobot **16 halaman PDF (393 KB)** dengan rincian 12 bab utama:
- **Sub-CPMK 1 (Bloom C1–C6):** Pemahaman PDB/PDP, IVP, pemodelan RL, kontinuitas energi medan, evaluasi non-linieritas, dan perancangan skrip Octave.
- **Peta Konsep TikZ:** Visualisasi alur 16 pekan kurikulum PD 2026.
- **Fisika Dinamika Energi:** Pembuktian mengapa induktor merespons $di/dt$ dan kapasitor merespons $dv/dt$.
- **Taksonomi & Klasifikasi PD:** PDB vs PDP, Orde, Derajat, Linieritas, dan Homogenitas.
- **Medan Arah (*Slope Field*):** Interpretasi geometris keluarga kurva integral konvergen ke keadaan mantap $I_{\text{ss}} = V_0/R$.
- **Hukum Kontinuitas Energi:** Pembuktian fisis mengapa $i_L(0^-) = i_L(0^+)$ dan $v_C(0^-) = v_C(0^+)$ berdasarkan ketiadaan daya tak terhingga di alam nyata.
- **Pemodelan KVL Rangkaian RL:** Derivasi lengkap dengan metode pemisahan variabel dan pemaknaan konstanta waktu $\tau = L/R$ (kelipatan $1\tau$ hingga $5\tau$).
- **Studi Kasus Industri:** Transien inrush current pada transformator Gardu Induk 150 kV Bengkulu.
- **Contoh Soal Terhitung:** 2 contoh soal besar langkah demi langkah (klasifikasi dan perhitungan transien solenoida pemutus tenaga 125 V DC).
- **Praktikum GNU Octave:** Skrip modular lengkap dengan visualisasi analitik vs `ode45`, penanda garis $1\tau$ dan $5\tau$, serta disipasi daya termal.
- **Bank Soal Evaluasi Mandiri:** Soal C1 sampai C6 lengkap.
- **Glosarium & Pustaka Rujukan.**

---

## 3. Kompilasi & Penyebaran (Deployment)
1. **Kompilasi LaTeX:** `modul_1.tex` berhasil dikompilasi menjadi `modul_1.pdf` (16 halaman, 393 KB).
2. **Sinkronisasi Berkas:** Disalin ke `docs/files/modul_1.pdf`.
3. **Pembaruan Portal Dokumentasi:** `docs/01_modul_1.md` diperbarui lengkap dengan integrasi video YouTube, boks Sub-CPMK, diagram Mermaid, tabel, dan skrip Octave.
4. **Build & Deploy:** Dibangun dengan MkDocs Material dan dideploy secara live ke Vercel Production:
   - **Tautan Langsung Modul 1:** `https://www.ndaratha.my.id/persamaan-diferensial/01_modul_1/` (HTTP 200 OK diverifikasi).
