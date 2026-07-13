# Modul 9: Pengantar PDP & Deret Fourier

## Pendahuluan
Dalam analisis teknik elektro, seperti pemrosesan sinyal dan gelombang elektromagnetik, fenomena fisik seringkali dipengaruhi oleh lebih dari satu variabel independen (seperti posisi dan waktu). Persamaan diferensial yang melibatkan lebih dari satu variabel bebas disebut Persamaan Diferensial Parsial (PDP). 

Untuk memecahkan PDP dengan kondisi batas tertentu, kita sering kali memerlukan alat matematika yang tangguh, salah satunya adalah Deret Fourier. Deret Fourier memungkinkan kita untuk mengekspresikan fungsi periodik secara umum (seperti sinyal tegangan kotak atau gigi gergaji) sebagai jumlahan tak hingga dari fungsi sinusoidal (sinus dan kosinus).

## Materi Utama

## Persamaan Diferensial Parsial (PDP)
**Definisi: Persamaan Diferensial Parsial**

Suatu persamaan diferensial parsial (PDP) adalah persamaan yang mengandung turunan parsial dari satu variabel tak bebas terhadap dua atau lebih variabel bebas.


Bentuk umum orde kedua untuk fungsi $u(x,y)$:
$$ A \frac{\partial^2 u}{\partial x^2} + B \frac{\partial^2 u}{\partial x \partial y} + C \frac{\partial^2 u}{\partial y^2} + D \frac{\partial u}{\partial x} + E \frac{\partial u}{\partial y} + F u = G $$
dimana $A, B, C, D, E, F, G$ dapat berupa konstanta atau fungsi dari $x$ dan $y$.

## Deret Fourier
Suatu fungsi periodik $f(t)$ dengan periode $T = 2L$ dapat dinyatakan dalam Deret Fourier sebagai berikut:
$$ f(t) = a_0 + \sum_{n=1}^{\infty} \left( a_n \cos\left(\frac{n\pi t}{L}\right) + b_n \sin\left(\frac{n\pi t}{L}\right) \right) $$

Koefisien Fourier dihitung dengan rumus:

$$

\begin{align*}
a_0 &= \frac{1}{2L} \int_{-L}^{L} f(t) \,dt \\
a_n &= \frac{1}{L} \int_{-L}^{L} f(t) \cos\left(\frac{n\pi t}{L}\right) \,dt, \quad n=1,2,3,\dots \\
b_n &= \frac{1}{L} \int_{-L}^{L} f(t) \sin\left(\frac{n\pi t}{L}\right) \,dt, \quad n=1,2,3,\dots
\end{align*}

$$

## Fungsi Genap dan Ganjil (Simetri)
Dalam kasus-kasus tertentu di teknik elektro, sinyal periodik memiliki sifat simetri yang memudahkan perhitungan Deret Fourier:

**1. Fungsi Genap ($f(-t) = f(t)$):**
Sinyal yang simetris terhadap sumbu $y$. Untuk fungsi genap, $b_n = 0$ untuk semua $n$. Deret Fourier hanya mengandung suku kosinus dan konstanta:
$$ a_0 = \frac{1}{L} \int_{0}^{L} f(t) \,dt, \quad a_n = \frac{2}{L} \int_{0}^{L} f(t) \cos\left(\frac{n\pi t}{L}\right) \,dt $$

**2. Fungsi Ganjil ($f(-t) = -f(t)$):**
Sinyal yang antisimetris (simetris terhadap titik asal). Untuk fungsi ganjil, $a_0 = 0$ dan $a_n = 0$ untuk semua $n$. Deret Fourier hanya mengandung suku sinus:
$$ b_n = \frac{2}{L} \int_{0}^{L} f(t) \sin\left(\frac{n\pi t}{L}\right) \,dt $$

**Contoh:**

Misalkan sebuah gelombang kotak ganjil dengan periode $2\pi$ yang bernilai $+1$ dari $0$ hingga $\pi$ dan $-1$ dari $-\pi$ hingga $0$. Karena ganjil, $a_0 = 0$ dan $a_n = 0$. Nilai $b_n$ akan menjadi $\frac{4}{n\pi}$ untuk $n$ ganjil dan $0$ untuk $n$ genap.


## Ringkasan
Persamaan Diferensial Parsial (PDP) digunakan untuk memodelkan sistem dengan lebih dari satu variabel independen. Deret Fourier merupakan alat penting untuk memecahkan PDP, dengan merepresentasikan fungsi periodik sembarang ke dalam harmonik dasar fungsi sinus dan kosinus. Memanfaatkan sifat fungsi genap atau ganjil dari sebuah sinyal dapat sangat mempercepat perhitungan koefisien Fourier.

## Referensi

    - Erwin Kreyszig, *Advanced Engineering Mathematics*, 10th Edition, John Wiley & Sons.
    - Dennis G. Zill, *Differential Equations with Boundary-Value Problems*, Cengage Learning.