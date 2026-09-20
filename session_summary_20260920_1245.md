# Ringkasan Sesi Perkuliahan: Penyempurnaan Visual & Interaktif Salindia Beamer
Tanggal & Waktu: **20 September 2026, 12:45 WIB**  
Mata Kuliah: **Persamaan Diferensial (Fokus Teknik Elektro)**  
Dosen Pengampu: **Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.**  
Institusi: **Jurusan Teknik Elektro, Fakultas Teknik, Universitas Bengkulu**

---

## 1. Latar Belakang & Tujuan Sesi
Setelah menyelesaikan revitalisasi 14 salindia Beamer perkuliahan (`ch1` s.d. `ch7` dan `ch9` s.d. `ch15`) ke format standar 15 frame, pengguna menginstruksikan untuk melakukan penyempurnaan menyeluruh atas kelemahan-kelemahan pedagogis yang diidentifikasi, khususnya:
1. Menyediakan visualisasi kurva grafik hasil simulasi secara nyata pada salindia komputasi Julia.
2. Mentransformasi format kuis evaluasi pasif menjadi kuis konseptual interaktif (*Peer Instruction*) untuk menguji miskonsepsi fisik secara aktif di ruang kuliah.
3. Mempertegas notasi dan satuan SI standar pada seluruh pemodelan fisis.

---

## 2. Rincian Capaian Kerja

### A. Pembangkitan 14 Grafik Simulasi Beresolusi Tinggi (`figures/slides/`)
Dibuat skrip Python komputasi ilmiah `generate_slide_plots.py` yang menghasilkan 14 grafik plot dengan resolusi 300 DPI dan palet warna institusional UNIB (*Navy* `#002060`, *Gold* `#C5A059`, *Green* `#22703C`):
- `plot_ch1.png`: Kurva respon transien pengisian induktor RL (Analitik vs Julia `Tsit5()`).
- `plot_ch2.png`: Kurva pengisian tegangan kapasitor $v_C(t)$ dan peluruhan arus $i(t)$ pada rangkaian RC.
- `plot_ch3.png`: Dinamika termal hotspot kumparan vs minyak atas trafo 60 MVA sesuai standar IEEE C57.91.
- `plot_ch4.png`: Perbandingan dinamika respon waktu 3 ragam redaman RLC seri (*underdamped, critically damped, overdamped*).
- `plot_ch5.png`: Kurva respon frekuensi resonansi seri RLC dan selektivitas faktor kualitas $Q = 2, 5, 10$.
- `plot_ch6.png`: Gelombang impuls surja petir standar IEC 60060-1 ($1{,}2/50\,\mu\text{s}$) dengan penanda titik puncak dan ekor.
- `plot_ch7.png`: Respon *Transient Recovery Voltage* (TRV) pada pemutus tenaga PMT IEC 62271-100 pasca pemutusan arus gangguan.
- `plot_ch9.png`: Rekonstruksi gelombang kotak dengan deret Fourier ($N=1, 5, 25$) dan visualisasi lonjakan fenomena Gibbs ($8{,}95\%$).
- `plot_ch10.png`: Distribusi suhu tunak spasial 1D pada rel busbar gardu induk GITET 500 kV (IEEE Std 738).
- `plot_ch11.png`: Gelombang berjalan pantulan surja transmisi d'Alembert untuk kondisi terbuka ($\Gamma_L = +1$) dan hubung singkat ($\Gamma_L = -1$).
- `plot_ch12.png`: Difusi difusivitas termal transien pada lapisan isolasi kabel tanah XLPE 20 kV (IEC 60287).
- `plot_ch13.png`: Kontur ekuipotensial 2D medan Laplace di sekitar isolator tumpu 150 kV hasil iterasi relaksasi FDM.
- `plot_ch14.png`: Fungsi Bessel orde pertama dan profil rapat arus radial *skin effect* kawat transmisi ACSR.
- `plot_ch15.png`: Polinomial Legendre $P_0$ s.d. $P_3$ koordinat bola dan diagram gelombang transversal TEM.

### B. Integrasi Gambar pada Frame 13 (Praktikum Julia)
Setiap Frame 13 pada ke-14 deck perkuliahan kini menyajikan tata letak dua kolom:
- Kolom kiri ($0{,}50\textwidth$): Listing kode Julia yang bersih, terformat dengan `listings`, siap uji mandiri oleh mahasiswa.
- Kolom kanan ($0{,}48\textwidth$): Gambar grafik kurva hasil simulasi yang disematkan dengan pembatas aspek rasio (`keepaspectratio`) ditambah kotak intisari dinamika transien / fisis.

### C. Transformasi Frame 14 Menjadi *Peer Instruction Concept Quiz*
Format butir soal esai pasif diubah menjadi pertanyaan studi kasus pilihan ganda interaktif (A/B/C/D) yang menyasar miskonsepsi fisik fundamental:
- **W1:** Mengapa arus induktor $i(0^+) = 0$ saat sakelar ditutup (Hukum Lenz & kontinuitas fluks).
- **W2:** Paradoks energi pengisian kapasitor selalu 50% hilang pada resistor independen dari nilai $R$.
- **W3:** Perbedaan drastis inersia termal minyak trafo (puluhan ton) vs kawat tembaga kecil.
- **W4:** Mengapa aktuator PMT dan jarum ukur analog dirancang pada redaman kritis $\zeta = 1$.
- **W5:** Fenomena kenaikan tegangan kapasitor melampaui tegangan sumber saat resonansi seri ($V_C = Q V_s$).
- **W6:** Keunggulan operasional aljabar domain-$s$ Laplace menangani switching diskontinu Heaviside/Dirac.
- **W7:** Mengapa momen paling berbahaya pemutusan arus hubung singkat justru terjadi sesaat setelah busur api padam (laju RRRV).
- **W9:** Mengapa fenomena Gibbs tetap bernilai $8{,}95\%$ kendati jumlah harmonisa $N \to \infty$.
- **W10:** Mengapa konstanta pemisah PDP difusi wajib bernilai negatif demi hukum stabilitas termodinamika.
- **W11:** Mengapa surja petir memantul melipatgandakan tegangan ($2\text{ pu}$) pada ujung saluran terbuka.
- **W12:** Mengapa kawat tanah berisolasi XLPE memiliki ampacity lebih rendah daripada kawat telanjang di udara.
- **W13:** Konsekuensi teorema rata-rata Gauss bahwa potensial elektrostatik tidak pernah memiliki ekstremum lokal di ruang bebas.
- **W14:** Mengapa konduktor transmisi SUTET dibuat berlapis aluminium luar dan inti baja dalam (ACSR).
- **W15:** Hukum kekekalan muatan listrik yang mendasari penambahan arus pergeseran Maxwell.

### D. Hasil Pengujian Mutu Otomatis
- **100% Salindia (14 dari 14):** Tepat 15 frame/halaman per berkas.
- **100% Salindia (14 dari 14):** Bebas peringatan tipografi ($0\text{ Overfull \hbox}$ dan $0\text{ Overfull \vbox}$).
- Seluruh 14 file PDF dikompilasi ulang dan disinkronkan ke direktori portal dan situs produksi.
- Deployment Vercel produksi selesai dieksekusi.

---

## 3. Status Berkas Akhir
- Naskah LaTeX: [`ch1.tex`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/ch1.tex) s.d. [`ch7.tex`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/ch7.tex), [`ch9.tex`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/ch9.tex) s.d. [`ch15.tex`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/ch15.tex).
- Berkas PDF: [`ch1.pdf`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/ch1.pdf) s.d. [`ch15.pdf`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/ch15.pdf).
- Direktori Gambar: [`figures/slides/`](file:///Users/novaliodaratha/Documents/2026/mengajar/Persamaan%20Diferensial/figures/slides/) (14 berkas `.png` 300 DPI).
- Web Portal Publik: `https://www.ndaratha.my.id/persamaan-diferensial/`.
