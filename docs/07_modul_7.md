# Modul 7: Invers Laplace & Solusi PDB dengan Laplace

## Pendahuluan
Setelah memahami bagaimana mengubah domain waktu menjadi frekuensi kompleks (domain $s$) dengan Transformasi Laplace, pada minggu ke-7 ini kita akan belajar bagaimana mengembalikannya (invers Transformasi Laplace). Dengan penguasaan Invers Laplace dan Transformasi Turunan, kita dapat dengan mudah menyelesaikan Persamaan Diferensial Biasa (PDB) serta mendefinisikan masalah nilai awal tanpa harus mencari solusi homogen dan partikular secara terpisah.

## Materi Utama
## Invers Transformasi Laplace
Jika $F(s)$ melambangkan transformasi Laplace dari $f(t)$, yaitu $\mathcal{L}\{f(t)\} = F(s)$, maka $f(t)$ disebut transformasi invers Laplace dari $F(s)$ dan dituliskan:
$$
f(t) = \mathcal{L}^{-1}\{F(s)\}
$$

Sama seperti transformasi Laplace, transformasi Laplace Invers juga memiliki sifat linieritas:
$$ \mathcal{L}^{-1}\{c_1 F(s) + c_2 G(s)\} = c_1 \mathcal{L}^{-1}\{F(s)\} + c_2 \mathcal{L}^{-1}\{G(s)\} $$

Seringkali $F(s)$ tidak berada dalam bentuk di tabel secara langsung. Teknik Ekspansi Pecahan Parsial (Partial Fraction Expansion) digunakan untuk memecah $F(s)$ ke bentuk pecahan-pecahan sederhana.

**Contoh:**

Tentukan $\mathcal{L}^{-1} \left\lbrace  \frac{s+1}{s^2-4s+3} \right\rbrace $.

**Solusi:**
Faktorkan penyebut: $s^2-4s+3 = (s-1)(s-3)$. Pecahan parsial:
$$ \frac{s+1}{(s-1)(s-3)} = \frac{A}{s-1} + \frac{B}{s-3} $$
$s+1 = A(s-3) + B(s-1)$
Untuk $s=1 \implies 2 = -2A \implies A = -1$
Untuk $s=3 \implies 4 = 2B \implies B = 2$
Maka: $\mathcal{L}^{-1} \left\lbrace  \frac{-1}{s-1} + \frac{2}{s-3} \right\rbrace  = -e^{t} + 2e^{3t}$.

## Transformasi Laplace dari Turunan
Salah satu kemampuan luar biasa Laplace Transform adalah mereduksi operasi diferensial kalkulus menjadi perkalian aljabar di domain $s$.

    - Transformasi Laplace turunan pertama: $\mathcal{L}\{y'(t)\} = sY(s) - y(0)$
    - Transformasi Laplace turunan kedua: $\mathcal{L}\{y''(t)\} = s^2Y(s) - s y(0) - y'(0)$
    - Secara umum: $\mathcal{L}\{y^{(n)}(t)\} = s^n Y(s) - s^{n-1}y(0) - s^{n-2}y'(0) - \dots - y^{(n-1)}(0)$

dimana $Y(s) = \mathcal{L}\{y(t)\}$. Syarat nilai awal secara eksplisit diikutsertakan di dalam persamaan.

## Menyelesaikan PDB Menggunakan Laplace
Prosedur umum:

    - Terapkan Transformasi Laplace di kedua ruas PDB (serta aplikasikan syarat nilai awal).
    - Pecahkan persamaan aljabar yang terbentuk untuk mencari $Y(s)$.
    - Terapkan Transformasi Laplace Invers $\mathcal{L}^{-1}$ pada $Y(s)$ untuk mendapatkan $y(t)$.

**Contoh:**

Selesaikan PDB nilai awal berikut: $y'' - y' - 2y = 0$; dengan nilai awal $y(0)=1, y'(0)=0$.

**Solusi:**
1. Ambil Laplace kedua sisi:
$$ [s^2Y(s) - sy(0) - y'(0)] - [sY(s) - y(0)] - 2Y(s) = 0 $$
$$ [s^2Y(s) - s(1) - 0] - [sY(s) - 1] - 2Y(s) = 0 $$
2. Kumpulkan $Y(s)$:
$$ (s^2 - s - 2)Y(s) - s + 1 = 0 \implies (s^2 - s - 2)Y(s) = s - 1 $$
$$ Y(s) = \frac{s-1}{s^2-s-2} = \frac{s-1}{(s-2)(s+1)} $$
Lakukan pecahan parsial: $\frac{s-1}{(s-2)(s+1)} = \frac{A}{s-2} + \frac{B}{s+1}$.
Didapat $A=1/3, B=2/3$. Jadi $Y(s) = \frac{1/3}{s-2} + \frac{2/3}{s+1}$.
3. Invers Laplace:
$$ y(t) = \mathcal{L}^{-1} \left\lbrace  \frac{1}{3} \frac{1}{s-2} + \frac{2}{3} \frac{1}{s+1} \right\rbrace  = \frac{1}{3}e^{2t} + \frac{2}{3}e^{-t} $$

## Ringkasan
Metode Transformasi Laplace untuk PDB menggabungkan pemecahan PDB sekaligus syarat awalnya tanpa tahap mencari solusi umum. Proses utamanya mencakup transformasi domain waktu (PDB) ke ranah s (Aljabar), penyederhanaan aljabar menggunakan teknik Ekspansi Pecahan Parsial, dan diakhiri dengan Transformasi Laplace Invers. Metode ini menjadi senjata andalan mahasiswa kelistrikan dalam analisis sistem redaman sirkuit atau sistem kontrol dan respon transien.

## Referensi

    - Zill, D. G. (2018). *A First Course in Differential Equations with Modeling Applications*. Cengage Learning.
    - Ogata, K. (2010). *Modern Control Engineering*. Prentice Hall.