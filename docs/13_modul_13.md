# Modul 13: Persamaan Laplace 2D (Distribusi Potensial Elektrostatik)

## Pendahuluan
Dalam elektromagnetika, distribusi potensial listrik pada area yang tidak mengandung muatan bebas dapat dimodelkan menggunakan Persamaan Laplace. Ini adalah dasar penting untuk perancangan kapasitor, isolator tegangan tinggi, dan elektroda dalam berbagai peralatan teknik elektro.

Modul ini membahas Persamaan Laplace pada koordinat Kartesian 2 dimensi (2D). Kita akan menggunakan metode pemisahan variabel yang telah diperkenalkan sebelumnya untuk menentukan solusi potensial elektrostatik pada berbagai geometri berbatas.

## Materi Utama
## Persamaan Laplace 2D
Persamaan Laplace adalah Persamaan Diferensial Parsial (PDP) eliptik, dituliskan sebagai $\nabla^2 u = 0$. Dalam koordinat Kartesian 2D, persamaan ini menjadi:

$$

\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0

$$

dimana $u(x,y)$ menyatakan potensial elektrostatik (tegangan) pada titik $(x,y)$.

## Metode Pemisahan Variabel
Misalkan solusi dapat dipisahkan menjadi perkalian dua fungsi dari variabel bebasnya:

$$

u(x,y) = X(x)Y(y)

$$

Substitusi ke dalam Persamaan Laplace memberikan:

$$

X''(x)Y(y) + X(x)Y''(y) = 0 \implies \frac{X''(x)}{X(x)} = -\frac{Y''(y)}{Y(y)} = -\lambda^2

$$

Konstanta pemisahan $-\lambda^2$ dipilih negatif agar fungsi pada salah satu arah (misalnya $X(x)$) bersifat osilatorik untuk memenuhi kondisi batas bernilai nol, sedangkan arah lainnya ($Y(y)$) eksponensial atau hiperbolik.
Hal ini memberikan dua PDB:

$$

\begin{align}
X''(x) + \lambda^2 X(x) &= 0 \\
Y''(y) - \lambda^2 Y(y) &= 0
\end{align}

$$

## Solusi pada Pelat Persegi Panjang
Misalkan kita memiliki sebuah pelat dielektrik persegi panjang pada daerah $0 \le x \le a$ dan $0 \le y \le b$. Kondisi batas elektrostatiknya adalah:

$$

\begin{align*}
u(0,y) &= 0, \quad u(a,y) = 0 \\
u(x,0) &= 0, \quad u(x,b) = f(x)
\end{align*}

$$

(Ini merepresentasikan tiga sisi yang di-ground-kan dan satu sisi atas diberikan potensial $f(x)$).

Dari batas pada sumbu-$x$, kita dapatkan $X(0)=0$ dan $X(a)=0$, sehingga solusinya:

$$

X_n(x) = \sin\left(\frac{n\pi x}{a}\right), \quad \text{dengan } \lambda_n = \frac{n\pi}{a}

$$

Untuk arah-$y$, dengan kondisi $Y(0)=0$:

$$

Y_n(y) = \sinh\left(\frac{n\pi y}{a}\right)

$$

Maka, solusi umumnya:

$$

u(x,y) = \sum_{n=1}^{\infty} A_n \sin\left(\frac{n\pi x}{a}\right) \sinh\left(\frac{n\pi y}{a}\right)

$$

Koefisien $A_n$ ditentukan menggunakan batas $u(x,b) = f(x)$:

$$

A_n \sinh\left(\frac{n\pi b}{a}\right) = \frac{2}{a} \int_{0}^{a} f(x) \sin\left(\frac{n\pi x}{a}\right) dx

$$

## Ringkasan
Persamaan Laplace digunakan secara luas dalam persoalan keseimbangan statik (steady-state). Pada bidang teknik elektro, persamaan ini berfungsi menentukan distribusi potensial listrik dalam ruang kosong antar elektroda. Pendekatan pemisahan variabel memungkinkan kita memecahkan permasalahan ini dengan memanfaatkan deret Fourier dan fungsi hiperbolik (atau eksponensial) untuk memenuhi seluruh nilai batas yang ditetapkan.

## Referensi

    - Cheng, D. K. (1989). *Field and Wave Electromagnetics* (2nd ed.). Addison-Wesley.
    - Sadiku, M. N. O. (2014). *Elements of Electromagnetics* (6th ed.). Oxford University Press.