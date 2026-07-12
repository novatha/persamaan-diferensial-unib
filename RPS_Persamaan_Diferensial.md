# Rencana Pembelajaran Semester (RPS)
## Mata Kuliah: Persamaan Diferensial (Fokus Persiapan Medan Elektromagnetika)

**Deskripsi Mata Kuliah:**
Mata kuliah ini membahas teori dan aplikasi Persamaan Diferensial Biasa (PDB) dan Persamaan Diferensial Parsial (PDP) dengan penekanan khusus pada pemodelan fenomena fisis di bidang Teknik Elektro. RPS ini dirancang secara khusus untuk membangun fondasi matematis yang kuat agar mahasiswa siap menghadapi mata kuliah tingkat lanjut, terutama **Medan Elektromagnetika**.

**Capaian Pembelajaran Mata Kuliah (CPMK):**
1. Mahasiswa mampu mengidentifikasi dan menyelesaikan berbagai jenis Persamaan Diferensial Biasa (PDB) orde satu dan orde dua.
2. Mahasiswa mampu memodelkan dan menganalisis respons transien dan steady-state sistem kelistrikan dasar (Rangkaian RC, RL, RLC) menggunakan PDB.
3. Mahasiswa memahami konsep dasar dan mampu menyelesaikan Persamaan Diferensial Parsial (PDP) menggunakan metode pemisahan variabel dan deret Fourier.
4. Mahasiswa mampu menyelesaikan dan memahami makna fisis dari PDP utama yang relevan dengan fenomena elektromagnetika (Persamaan Gelombang, Persamaan Laplace, Persamaan Poisson, dan Persamaan Difusi).
5. Mahasiswa memahami penggunaan berbagai sistem koordinat orthogonal (Kartesian, Silinder, Bola) dalam penyelesaian PDP sebagai persiapan untuk menyelesaikan persamaan Maxwell dan masalah nilai batas elektromagnetik.

---

### Rencana Pertemuan (16 Minggu)

#### Bagian 1: Persamaan Diferensial Biasa & Pemodelan Sistem Fisis Dasar

*   **Minggu 1: Pengantar Persamaan Diferensial & Pemodelan Matematis**
    *   Definisi, klasifikasi (PDB vs PDP), orde, derajat, dan linearitas.
    *   Konsep solusi umum, solusi khusus, dan Masalah Nilai Awal (Initial Value Problem/IVP).
    *   Pengenalan pemodelan fenomena fisis dasar (misal: Hukum Kirchhoff, Hukum Ohm).
*   **Minggu 2: PDB Orde Satu & Metode Penyelesaian Analitis**
    *   PDB Separabel (Variabel yang dapat dipisahkan).
    *   PDB Eksak dan Non-Eksak.
    *   PDB Linier Orde Satu & Metode Faktor Integrasi.
*   **Minggu 3: Aplikasi PDB Orde Satu pada Rangkaian Listrik**
    *   Pemodelan rangkaian RC dan RL menggunakan Hukum Kirchhoff.
    *   Analisis respons transien (pengisian/pengosongan kapasitor, induktor).
    *   Konsep konstanta waktu ($\tau$).
*   **Minggu 4: PDB Linier Orde Dua (Homogen & Non-Homogen)**
    *   PDB Linier Orde Dua Homogen dengan koefisien konstan.
    *   Analisis akar persamaan karakteristik: Real berbeda, Real kembar, dan Kompleks konjugat.
    *   PDB Non-Homogen: Metode Koefisien Tak Tentu (Undetermined Coefficients).
*   **Minggu 5: Aplikasi PDB Orde Dua pada Osilasi & Rangkaian RLC**
    *   Pemodelan rangkaian RLC seri dan paralel.
    *   Analisis respons: *Overdamped, Critically Damped, Underdamped*.
    *   Osilasi harmonik, frekuensi alami, dan resonansi pada sistem kelistrikan.
*   **Minggu 6: Transformasi Laplace untuk Penyelesaian PDB**
    *   Definisi, sifat-sifat Transformasi Laplace, dan Transformasi invers.
    *   Menyelesaikan PDB (IVP) menggunakan Transformasi Laplace.
    *   Fungsi langkah (Step Function) dan fungsi impuls (Dirac Delta) untuk memodelkan sumber tegangan/arus sesaat.
*   **Minggu 7: Sistem Persamaan Diferensial Linier**
    *   Penyelesaian sistem PDB (Metode Eliminasi, Pendekatan Matriks).
    *   Aplikasi pada rangkaian tergandeng (*Coupled Circuits* / Transformator dasar).
*   **Minggu 8: Ujian Tengah Semester (UTS)**

#### Bagian 2: Persamaan Diferensial Parsial & Fondasi Analisis Elektromagnetik

*   **Minggu 9: Pengantar PDP & Deret Fourier**
    *   Konsep Persamaan Diferensial Parsial (PDP) linear orde dua.
    *   Klasifikasi PDP secara matematis: Eliptik, Parabolik, Hiperbolik.
    *   Review Deret Fourier (Fungsi periodik, ganjil/genap) untuk merepresentasikan syarat batas berkala.
*   **Minggu 10: Pemisahan Variabel (Separation of Variables) & Masalah Nilai Batas**
    *   Konsep dasar metode pemisahan variabel pada sistem koordinat kartesian.
    *   Penerapan pada Masalah Nilai Batas (*Boundary Value Problems* - BVP) linier dan homogen.
*   **Minggu 11: Persamaan Gelombang (Wave Equation) 1D & Aplikasinya**
    *   Penyelesaian Persamaan Gelombang 1D ($ \frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2} $).
    *   Solusi d'Alembert (Gelombang berjalan) dan solusi pemisahan variabel (Gelombang berdiri).
    *   Aplikasi fisis: Gelombang elektromagnetik pada Saluran Transmisi (*Transmission Lines*).
*   **Minggu 12: Persamaan Laplace & Persamaan Poisson (Elektrostatika)**
    *   Penyelesaian Persamaan Laplace ($\nabla^2 V = 0$) dalam koordinat Kartesian 2D.
    *   Interpretasi fisis: Distribusi potensial listrik ($V$) pada daerah tanpa muatan dan pencarian Medan Listrik ($\mathbf{E} = -\nabla V$).
    *   Pengantar Persamaan Poisson ($\nabla^2 V = -\rho/\epsilon$).
*   **Minggu 13: PDP dalam Sistem Koordinat Orthogonal (Silinder & Bola)**
    *   Transformasi Laplacian ke koordinat silinder dan bola (Penting untuk pemodelan antena, kabel koaksial, dan perambatan gelombang).
    *   Pengantar penyelesaian persamaan diferensial khusus: Fungsi Bessel (Silinder) dan Polinomial Legendre (Bola) secara konseptual.
*   **Minggu 14: Persamaan Difusi / Panas (Heat Equation)**
    *   Penyelesaian Persamaan Difusi 1D ($ \frac{\partial u}{\partial t} = \alpha^2 \frac{\partial^2 u}{\partial x^2} $).
    *   Aplikasi fisis: Pengantar konseptual difusi medan elektromagnetik ke dalam konduktor yang baik dan pengantar konsep *Skin Effect* (Efek Kulit).
*   **Minggu 15: Integrasi PDP menuju Persamaan Maxwell**
    *   Review dan sintesis persamaan diferensial yang telah dipelajari.
    *   Review bentuk diferensial dari Hukum Elektromagnetik: Gauss, Faraday, dan Ampere (Pengenalan curl dan divergensi).
    *   Konsep penurunan Persamaan Gelombang Elektromagnetika dari Persamaan Maxwell.
*   **Minggu 16: Ujian Akhir Semester (UAS)**

---
**Referensi Utama:**
1.  Erwin Kreyszig, *Advanced Engineering Mathematics*, 10th Edition, John Wiley & Sons. (Buku utama untuk PDB, PDP, Transformasi Laplace, Fourier).
2.  Dennis G. Zill, *A First Course in Differential Equations with Modeling Applications*, Cengage Learning.
3.  William H. Hayt, Jr., & John A. Buck, *Engineering Electromagnetics*, McGraw-Hill. (Referensi pendukung untuk melihat konteks aplikasi PDB dan PDP secara langsung di dalam teori medan).
