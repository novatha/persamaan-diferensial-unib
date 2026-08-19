# Modul 5: PDB Orde 2 Non-Homogen (Metode Koefisien Tak Tentu) & Aplikasi RLC Seri

## Pendahuluan
Pada minggu kelima ini, kita akan mempelajari Persamaan Diferensial Biasa (PDB) linier orde 2 non-homogen dengan koefisien konstan. Fokus utama kita adalah menemukan solusi partikular menggunakan metode Koefisien Tak Tentu. Setelah menguasai metode penyelesaian matematis ini, kita akan melihat bagaimana PDB orde 2 ini diaplikasikan pada analisis rangkaian listrik AC RLC seri, yang sangat fundamental di Teknik Elektro.

## Materi Utama
## Bentuk Umum PDB Orde 2 Non-Homogen
Bentuk umum dari PDB linier orde 2 dengan koefisien konstan non-homogen adalah:

$$
a y'' + b y' + c y = f(x)
$$

dimana $a$, $b$, dan $c$ adalah konstanta riil ($a \neq 0$), dan fungsi di ruas kanan $f(x) \neq 0$ dikenal sebagai fungsi paksa (forcing function) atau fungsi input.

Solusi umum dari persamaan ini terdiri dari penjumlahan antara solusi umum PDB homogennya (sering disebut fungsi komplementer) dan solusi partikular PDB non-homogen tersebut:

$$
y(x) = y_h(x) + y_p(x)
$$

dimana:

- $y_h(x)$ adalah solusi dari persamaan homogen $ay'' + by' + cy = 0$.
- $y_p(x)$ adalah sembarang solusi partikular yang memenuhi $ay_p'' + by_p' + cy_p = f(x)$.

## Metode Koefisien Tak Tentu
Metode Koefisien Tak Tentu adalah metode untuk menebak bentuk solusi partikular $y_p(x)$ berdasarkan bentuk dari fungsi ruas kanan $f(x)$. Metode ini efektif hanya jika fungsi $f(x)$ berbentuk polinomial, eksponensial, sinus, kosinus, atau perkalian dan penjumlahan dari bentuk-bentuk tersebut.

**Aturan Dasar Tebakan $y_p(x)$:**

- Jika $f(x) = P_n(x)$ (Polinomial derajat $n$), tebak $y_p(x) = A_n x^n + \dots + A_1 x + A_0$.
- Jika $f(x) = k e^{\alpha x}$, tebak $y_p(x) = A e^{\alpha x}$.
- Jika $f(x) = k \sin(\beta x)$ atau $k \cos(\beta x)$, tebak $y_p(x) = A \cos(\beta x) + B \sin(\beta x)$.

**Aturan Modifikasi:**
Jika ada suku pada tebakan $y_p(x)$ yang merupakan bagian dari solusi homogen $y_h(x)$, maka kita kalikan tebakan $y_p(x)$ dengan $x^s$, di mana $s$ adalah bilangan bulat positif terkecil ($s=1$ atau $s=2$) sedemikian sehingga tidak ada suku pada $y_p(x)$ yang merupakan bagian dari $y_h(x)$.

**Contoh:**

Selesaikan PDB: $y'' - 3y' + 2y = 4e^{3x}$.

**Penyelesaian:**

- **Solusi Homogen ($y_h$):** Persamaan karakteristik: $r^2 - 3r + 2 = 0 \implies (r-1)(r-2) = 0 \implies r_1=1, r_2=2$. Solusi: $y_h(x) = C_1 e^x + C_2 e^{2x}$.
- **Solusi Partikular ($y_p$):** Karena $f(x) = 4e^{3x}$ dan $e^{3x}$ bukan bagian dari $y_h$, kita tebak $y_p(x) = A e^{3x}$. Turunkan: $y_p' = 3A e^{3x}$, $y_p'' = 9A e^{3x}$. Substitusi ke PDB:

$$
9A e^{3x} - 3(3A e^{3x}) + 2(A e^{3x}) = 4e^{3x}
$$
$$
(9 - 9 + 2)A = 4 \implies 2A = 4 \implies A = 2
$$

Jadi $y_p(x) = 2e^{3x}$.
- **Solusi Umum:** $y(x) = y_h(x) + y_p(x) = C_1 e^x + C_2 e^{2x} + 2e^{3x}$.

## Aplikasi Rangkaian RLC Seri
Pada rangkaian listrik yang terdiri dari resistor ($R$), induktor ($L$), dan kapasitor ($C$) yang dihubungkan seri dengan sumber tegangan $E(t)$, Hukum Tegangan Kirchhoff (KVL) menyatakan:

$$
V_L + V_R + V_C = E(t)
$$

Substitusi relasi tegangan-arus: $V_L = L \frac{di}{dt}$, $V_R = R i$, $V_C = \frac{q}{C}$, dimana arus $i = \frac{dq}{dt}$. Kita peroleh PDB orde 2 untuk muatan listrik $q(t)$:

$$
L \frac{d^2q}{dt^2} + R \frac{dq}{dt} + \frac{1}{C} q = E(t)
$$

Jika kita diferensialkan terhadap waktu, kita juga bisa mendapatkan PDB untuk arus $i(t)$:

$$
L \frac{d^2i}{dt^2} + R \frac{di}{dt} + \frac{1}{C} i = \frac{dE}{dt}
$$

Persamaan ini ekuivalen secara matematis dengan sistem pegas-massa mekanik yang teredam secara gaya paksa.
Fungsi paksa $E(t)$ sering berbentuk sinusoidal (AC), misalnya $E(t) = E_0 \cos(\omega t)$. Metode Koefisien Tak Tentu dapat digunakan untuk menemukan respon keadaan mantap (steady-state) arus pada rangkaian tersebut (solusi partikular $i_p(t)$).

## Ringkasan
Metode Koefisien Tak Tentu memberikan algoritma praktis untuk mencari solusi partikular PDB orde 2 non-homogen dengan fungsi pendorong yang spesifik. Dalam teknik elektro, persamaan diferensial ini adalah pondasi untuk menganalisis rangkaian AC dinamik, seperti rangkaian RLC. Solusi homogen memberikan respon sementara (transien), dan solusi partikular memberikan respon tetap (steady-state).

## Referensi

- Zill, D. G. (2018). *A First Course in Differential Equations with Modeling Applications*. Cengage Learning.
- Kreyszig, E. (2011). *Advanced Engineering Mathematics*. John Wiley & Sons.