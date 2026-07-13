# Modul 14: Fungsi Khusus 1 (Persamaan Bessel & Aplikasi Gelombang Silinder)

## Pendahuluan
Persoalan-persoalan teknik dengan geometri tabung/silinder (seperti waveguide silinder, kabel koaksial, atau perambatan sinyal pada serat optik) umumnya dimodelkan dalam koordinat silinder. Saat memecahkan Persamaan Gelombang atau Persamaan Helmholtz dalam sistem koordinat ini menggunakan pemisahan variabel, kita sering menemukan bentuk persamaan diferensial khusus yang dikenal sebagai Persamaan Bessel.

Modul ini membahas definisi Persamaan Bessel, solusinya (Fungsi Bessel), dan bagaimana fungsi ini digunakan dalam menggambarkan gelombang silinder di bidang rekayasa gelombang elektromagnetik.

## Materi Utama
## Persamaan Bessel
Persamaan diferensial Bessel berorde $\nu$ dituliskan sebagai:

$$
x^2 y'' + x y' + (x^2 - \nu^2)y = 0
$$

dimana parameter $\nu$ merupakan bilangan riil tak negatif. Dalam banyak penerapan teknik elektro, parameter ini bernilai bilangan bulat $n$ ($n = 0, 1, 2, \dots$).

Persamaan ini memiliki titik singular beraturan di $x = 0$, sehingga dapat diselesaikan menggunakan *Metode Frobenius* dengan berasumsi $y(x) = \sum_{m=0}^\infty c_m x^{m+r}$.

## Fungsi Bessel Jenis Pertama, $J_\nu(x)$
Solusi utama Persamaan Bessel yang konvergen dan berhingga pada $x=0$ (untuk $\nu \ge 0$) disebut Fungsi Bessel jenis pertama, direpresentasikan sebagai $J_\nu(x)$:

$$
J_\nu(x) = \sum_{m=0}^{\infty} \frac{(-1)^m}{m! \Gamma(m + \nu + 1)} \left( \frac{x}{2} \right)^{2m+\nu}
$$

Karakteristik fungsi $J_\nu(x)$ tampak menyerupai osilasi sinus dan kosinus namun amplitudonya meluruh seiring pertambahan $x$.

## Fungsi Bessel Jenis Kedua, $Y_\nu(x)$
Solusi linear independen kedua dinamakan Fungsi Bessel jenis kedua (atau Fungsi Neumann), $Y_\nu(x)$. Fungsi ini membesar mendekati tak hingga ($\to -\infty$) saat $x \to 0$. Oleh karena itu, $Y_\nu(x)$ biasanya dieliminasi dari solusi fisis di mana medan di titik pusat silinder ($x=0$) harus bernilai terhingga.

Solusi umum persamaan Bessel:

$$
y(x) = C_1 J_\nu(x) + C_2 Y_\nu(x)
$$

## Aplikasi: Gelombang dalam Waveguide Silinder
Tinjau perambatan medan listrik di dalam tabung konduktor silinder kosong dengan jari-jari $a$. Komponen longitudinal medan elektromagnetik, misalnya $E_z$ (pada mode TM), memenuhi Persamaan Helmholtz:

$$
\nabla^2 E_z + k^2 E_z = 0
$$

Dalam koordinat silinder $(\rho, \phi, z)$, pemisahan variabel pada variabel radial $\rho$ menghasilkan persamaan yang ekuivalen dengan Persamaan Bessel:

$$
\rho^2 \frac{d^2 R}{d\rho^2} + \rho \frac{dR}{d\rho} + (k_c^2 \rho^2 - n^2)R = 0
$$

dengan $k_c$ sebagai bilangan gelombang *cut-off*. Solusinya berupa fungsi $J_n(k_c \rho)$. Medan harus bernilai nol di dinding konduktor ($\rho=a$), sehingga:

$$
J_n(k_c a) = 0
$$

Persamaan ini digunakan untuk menemukan frekuensi cut-off dari mode gelombang di dalam pandu gelombang silinder.

## Ringkasan
Fungsi Bessel muncul secara alamiah ketika menyelesaikan masalah fisika dan teknik pada bidang dan volume berbentuk silinder. Dalam rekayasa elektromagnetik dan telekomunikasi optik, pemahaman Fungsi Bessel merupakan fondasi untuk merancang pandu gelombang (waveguides) dan menganalisis antena yang meradiasikan gelombang silinder.

## Referensi

- Balanis, C. A. (2012). *Advanced Engineering Electromagnetics* (2nd ed.). Wiley.
- Pozar, D. M. (2011). *Microwave Engineering* (4th ed.). Wiley.