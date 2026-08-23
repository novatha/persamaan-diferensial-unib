# Catatan Kuliah Persamaan Diferensial - Minggu 1: Pengantar Persamaan Diferensial

## Pendahuluan
Persamaan Diferensial (PD) memegang peranan krusial dalam memodelkan berbagai fenomena fisik, terutama dalam disiplin ilmu Teknik Elektro. Secara umum, sistem dinamis, seperti rangkaian listrik, medan elektromagnetik, hingga sistem kendali, dapat direpresentasikan melalui suatu persamaan yang melibatkan fungsi beserta turunannya. Modul ini bertujuan untuk memberikan pemahaman dasar mengenai klasifikasi persamaan diferensial, pembedaan antara solusi umum dan solusi khusus, masalah nilai awal (Initial Value Problem - IVP), serta penerapannya secara dasar pada rangkaian listrik melalui Hukum Kirchhoff.

## Materi Utama

### Klasifikasi Persamaan Diferensial: PDB dan PDP
Persamaan Diferensial dibagi menjadi dua kategori utama berdasarkan jumlah variabel bebas yang terlibat.

!!! info "Persamaan Diferensial Biasa (PDB)"
    Persamaan Diferensial Biasa (PDB) adalah persamaan diferensial yang hanya mengandung turunan terhadap **satu** variabel bebas (misalnya waktu $t$).

Bentuk umum PDB:
$$ F\left(x, y, \frac{dy}{dx}, \frac{d^2y}{dx^2}, \dots, \frac{d^ny}{dx^n}\right) = 0 $$

!!! info "Persamaan Diferensial Parsial (PDP)"
    Persamaan Diferensial Parsial (PDP) adalah persamaan diferensial yang mengandung turunan parsial terhadap **dua atau lebih** variabel bebas.

### Solusi Umum, Solusi Khusus, dan IVP

    - **Solusi Umum:** Solusi yang memuat konstanta sembarang ($C$).
    - **Solusi Khusus:** Solusi yang diperoleh dari solusi umum dengan memasukkan nilai *Initial Value Problem* (IVP) atau kondisi awal.

!!! example "Penyelesaian IVP Langkah-demi-Langkah"
    Tinjau PDB: $\frac{dy}{dt} = -2y$, dengan kondisi awal $y(0) = 5$.

    **Langkah 1: Temukan Solusi Umum.** 
    Berdasarkan pengalaman, fungsi yang turunannya adalah kelipatan dirinya sendiri adalah eksponensial. Solusi umumnya: 
    $y(t) = C e^{-2t}$.

    **Langkah 2: Terapkan Kondisi Awal.**
    Substitusi $t = 0$ dan $y = 5$:
    $5 = C e^{-2(0)} \implies 5 = C(1) \implies C = 5$.

    **Langkah 3: Solusi Khusus.**
    Maka solusi khususnya adalah $y(t) = 5 e^{-2t}$.

### Aplikasi Awal: Hukum Kirchhoff pada Rangkaian Listrik
!!! example "Rangkaian RL Seri"
    Tinjau sebuah rangkaian yang terdiri dari resistor $R$ dan induktor $L$ seri dengan sumber tegangan DC $V_0$. Hukum KVL menyatakan:
    $$ V_R + V_L = V_0 \implies R \cdot i(t) + L \frac{di(t)}{dt} = V_0 $$
    Persamaan ini adalah PDB orde 1 linear. 

    *Catatan Komputasi:* Untuk melihat visualisasi grafis bagaimana arus $i(t)$ naik secara eksponensial terhadap waktu, silakan jalankan `Simulasi_Transien_RC_RL.ipynb` di Jupyter Notebook Anda. Cobalah mengubah nilai $R$ dan $L$ pada *slider* untuk melihat pengaruhnya terhadap konstanta waktu!

## Ringkasan
Klasifikasi PD menjadi PDB dan PDP sangat bergantung pada jumlah variabel bebas. Selalu gunakan simulasi Python/Julia untuk memvalidasi pemahaman analitik Anda secara visual.

## Referensi

    - Erwin Kreyszig, *Advanced Engineering Mathematics*.
    - `Simulasi_Transien_RC_RL.ipynb` (Praktikum Komputasi).
