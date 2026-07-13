# Modul 10: Solusi PDP dengan Metode Pemisahan Variabel

## Pendahuluan
Persamaan Diferensial Parsial (PDP) linear homogen banyak dijumpai dalam pemodelan masalah rekayasa, seperti distribusi panas pada kabel listrik atau konduktor tembaga, getaran struktural, dan fenomena difusi. Salah satu teknik matematika paling efektif untuk memecahkan kelas PDP ini adalah Metode Pemisahan Variabel (Separation of Variables).

Ide dasar dari metode ini sangat elegan: kita mengasumsikan solusi fungsi multivariabel dapat dinyatakan sebagai hasil kali (perkalian) dari fungsi-fungsi yang masing-masing hanya bergantung pada satu variabel independen tunggal. Pendekatan ini mereduksi persoalan PDP menjadi sekumpulan Persamaan Diferensial Biasa (PDB) yang lebih mudah diselesaikan.

## Materi Utama

## Prinsip Dasar Metode Pemisahan Variabel
Misalkan kita mencari solusi $u(x, t)$ untuk sebuah persamaan diferensial parsial linear homogen (contohnya persamaan panas 1-dimensi). Kita asumsikan bentuk solusi sebagai hasil kali dua fungsi independen:

$$
u(x,t) = X(x) \cdot T(t)
$$

di mana:

- $X(x)$ adalah fungsi yang hanya bergantung pada variabel posisi $x$.
- $T(t)$ adalah fungsi yang hanya bergantung pada variabel waktu $t$.

Turunan parsial dari solusi usulan ini adalah:

$$
\frac{\partial u}{\partial x} = X'(x)T(t), \quad \frac{\partial^2 u}{\partial x^2} = X''(x)T(t)
$$

$$
\frac{\partial u}{\partial t} = X(x)T'(t), \quad \frac{\partial^2 u}{\partial t^2} = X(x)T''(t)
$$

## Langkah-langkah Pemecahan
Secara umum, terdapat tiga langkah utama dalam pemisahan variabel:

- **Pemisahan Variabel:** Substitusikan asumsi $u(x,t) = X(x)T(t)$ ke dalam PDP asal dan pisahkan variabel-variabelnya sehingga fungsi yang memuat $x$ berada di satu sisi dan fungsi yang memuat $t$ berada di sisi lain. Keduanya harus disamakan dengan konstanta pemisahan yang sama, misal $k$ atau $-\lambda^2$.
- **Penyelesaian PDB:** Selesaikan dua (atau lebih) Persamaan Diferensial Biasa (PDB) yang dihasilkan dengan menggunakan syarat batas homogen untuk menemukan nilai eigen ($\lambda$) dan fungsi eigen.
- **Deret Fourier (Kondisi Awal):** Gunakan prinsip superposisi dan selesaikan syarat awal menggunakan Deret Fourier untuk mencari koefisien pada deret tak hingga yang menyusun solusi akhir.

## Contoh: Persamaan Panas 1D
Persamaan konduksi panas (misal pada konduktor kawat):

$$
\frac{\partial u}{\partial t} = \alpha^2 \frac{\partial^2 u}{\partial x^2}
$$

Substitusi $u(x,t) = X(x)T(t)$:

$$
X(x)T'(t) = \alpha^2 X''(x)T(t)
$$

Bagi dengan $\alpha^2 X(x)T(t)$:

$$
\frac{T'(t)}{\alpha^2 T(t)} = \frac{X''(x)}{X(x)} = -\lambda^2
$$

Kita gunakan $-\lambda^2$ untuk memastikan solusi tidak tumbuh tak terhingga seiring waktu (karena fisik panas yang terdisipasi).
Dari situ didapat dua PDB:
1. $X''(x) + \lambda^2 X(x) = 0$
2. $T'(t) + \alpha^2 \lambda^2 T(t) = 0$

Solusi ini akan dievaluasi lebih lanjut dengan syarat batas pada $x=0$ dan $x=L$.

## Ringkasan
Metode pemisahan variabel adalah teknik yang ampuh untuk memecahkan PDP dengan menyederhanakannya menjadi sekumpulan PDB. Solusi umum dibentuk dengan menggabungkan (mengalikan) solusi-solusi PDB tersebut, dan solusi khusus diperoleh dengan menerapkan syarat batas sistem serta syarat awal melalui analisis Deret Fourier.

## Referensi

- Erwin Kreyszig, *Advanced Engineering Mathematics*, 10th Edition, John Wiley & Sons.
- William E. Boyce, Richard C. DiPrima, *Elementary Differential Equations and Boundary Value Problems*.