# Modul 1: Pengantar Persamaan Diferensial

## Pendahuluan
Persamaan Diferensial (PD) memegang peranan krusial dalam memodelkan berbagai fenomena fisik, terutama dalam disiplin ilmu Teknik Elektro. Secara umum, sistem dinamis, seperti rangkaian listrik, medan elektromagnetik, hingga sistem kendali, dapat direpresentasikan melalui suatu persamaan yang melibatkan fungsi beserta turunannya. Modul ini bertujuan untuk memberikan pemahaman dasar mengenai klasifikasi persamaan diferensial, pembedaan antara solusi umum dan solusi khusus, masalah nilai awal (Initial Value Problem - IVP), serta penerapannya secara dasar pada rangkaian listrik melalui Hukum Kirchhoff.

## Materi Utama

## Klasifikasi Persamaan Diferensial: PDB dan PDP
Persamaan Diferensial dibagi menjadi dua kategori utama berdasarkan jumlah variabel bebas yang terlibat.

**Definisi: Persamaan Diferensial Biasa (PDB)**

Persamaan Diferensial Biasa (PDB) adalah persamaan diferensial yang hanya mengandung turunan terhadap **satu** variabel bebas.

Bentuk umum PDB:

$$
F\left(x, y, \frac{dy}{dx}, \frac{d^2y}{dx^2}, \dots, \frac{d^ny}{dx^n}\right) = 0
$$

dengan $x$ adalah variabel bebas dan $y$ adalah variabel terikat.

**Definisi: Persamaan Diferensial Parsial (PDP)**

Persamaan Diferensial Parsial (PDP) adalah persamaan diferensial yang mengandung turunan parsial terhadap **dua atau lebih** variabel bebas.

Contoh PDP dalam Teknik Elektro adalah Persamaan Gelombang Elektromagnetik dan Persamaan Panas (Heat Equation).

## Orde dan Derajat Persamaan Diferensial

    - **Orde:** Tingkat turunan tertinggi yang terdapat dalam persamaan diferensial.
    - **Derajat (Degree):** Pangkat dari turunan tertinggi dalam persamaan, asalkan persamaan tersebut dalam bentuk polinomial dari turunan-turunannya.

Contoh: 

$$
\left( \frac{d^2y}{dx^2} \right)^3 + 4\frac{dy}{dx} - y = e^x
$$

Persamaan di atas merupakan PDB orde 2 berderajat 3.

## Solusi Umum dan Solusi Khusus
Solusi dari persamaan diferensial adalah suatu fungsi yang, ketika disubstitusikan ke dalam persamaan beserta turunannya, menghasilkan identitas yang benar.

    - **Solusi Umum:** Solusi yang memuat konstanta sembarang ($C$). Solusi umum untuk PDB orde $n$ akan memuat $n$ buah konstanta sembarang yang saling bebas.
    - **Solusi Khusus:** Solusi yang diperoleh dari solusi umum dengan memberikan nilai tertentu pada konstanta sembarang. Nilai konstanta ini biasanya ditentukan melalui syarat awal (Initial Conditions) atau syarat batas (Boundary Conditions).

## Masalah Nilai Awal (Initial Value Problem - IVP)
Masalah Nilai Awal (IVP) adalah persamaan diferensial yang disertai dengan syarat awal sedemikian rupa sehingga kita dapat menentukan solusi khusus yang unik. 
Untuk PDB orde 1: $\frac{dy}{dx} = f(x,y)$, syarat awalnya adalah $y(x_0) = y_0$.

## Aplikasi Awal: Hukum Kirchhoff pada Rangkaian Listrik
Dalam Teknik Elektro, Hukum Tegangan Kirchhoff (KVL) dan Hukum Arus Kirchhoff (KCL) sering menghasilkan persamaan diferensial.

**Contoh: Rangkaian RL Seri**

Tinjau sebuah rangkaian yang terdiri dari resistor $R$ dan induktor $L$ yang dihubungkan secara seri dengan sumber tegangan $V(t)$. Berdasarkan Hukum Tegangan Kirchhoff (KVL):

$$
V_R + V_L = V(t)
$$

Kita mengetahui bahwa $V_R = R \cdot i(t)$ dan $V_L = L \frac{di(t)}{dt}$. Dengan demikian, persamaan rangkaiannya adalah:

$$
L \frac{di}{dt} + R i = V(t)
$$

Persamaan ini merupakan Persamaan Diferensial Biasa (PDB) orde 1 linear.

## Ringkasan
Minggu ini kita telah mempelajari konsep dasar Persamaan Diferensial. Klasifikasi PD menjadi PDB dan PDP sangat bergantung pada jumlah variabel bebas. Orde menunjukkan turunan tertinggi, sedangkan solusi umum memuat konstanta yang dapat ditentukan melalui Masalah Nilai Awal (IVP) sehingga menjadi solusi khusus. Pemodelan rangkaian seri sederhana dengan Hukum Kirchhoff merupakan contoh fundamental tentang bagaimana PDB diterapkan dalam analisis rangkaian di Teknik Elektro.

## Referensi

    - Erwin Kreyszig, *Advanced Engineering Mathematics*, John Wiley & Sons.
    - Dennis G. Zill, *A First Course in Differential Equations with Modeling Applications*, Cengage Learning.