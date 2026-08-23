# Catatan Kuliah Persamaan Diferensial - Minggu 2: Persamaan Diferensial Biasa Orde 1

## Pendahuluan
Persamaan Diferensial Biasa (PDB) Orde 1 merupakan fondasi dalam mempelajari persamaan diferensial. Pada minggu ini, kita akan membahas berbagai teknik analitik, yang meliputi metode persamaan separabel, persamaan eksak, dan penggunaan faktor integrasi.

## Materi Utama

### Persamaan Diferensial Separabel
Sebuah PDB orde 1 dikatakan *separabel* (dapat dipisahkan) jika dapat ditulis dalam bentuk:
$$ \frac{dy}{dx} = g(x)h(y) $$
Pisahkan variabel $x$ dengan $dx$ dan variabel $y$ dengan $dy$, kemudian integralkan kedua ruas:
$$ \int \frac{1}{h(y)} dy = \int g(x) dx + C $$

### Persamaan Diferensial Eksak
Bentuk $M(x,y)dx + N(x,y)dy = 0$ disebut **eksak** jika:
$$ \frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} $$

!!! example "Penyelesaian PD Eksak Langkah-demi-Langkah"
    Selesaikan: $(2xy)dx + (x^2 - 1)dy = 0$

    **Langkah 1: Uji Eksak** 
    $M = 2xy \implies \frac{\partial M}{\partial y} = 2x$. 
    $N = x^2 - 1 \implies \frac{\partial N}{\partial x} = 2x$. 
    Karena sama, maka persamaannya Eksak.

    **Langkah 2: Cari fungsi Potensial $F(x,y)$**
    $F(x,y) = \int M \, dx = \int 2xy \, dx = x^2 y + g(y)$.

    **Langkah 3: Turunkan terhadap $y$ dan samakan dengan $N$**
    $\frac{\partial F}{\partial y} = x^2 + g'(y)$. Samakan: $x^2 + g'(y) = x^2 - 1 \implies g'(y) = -1$.
    Maka $g(y) = \int -1 \, dy = -y$.

    **Langkah 4: Tulis Solusi Umum**
    Solusi: $F(x,y) = C \implies x^2 y - y = C$.

### Persamaan Linear dan Faktor Integrasi
Bentuk umum: $\frac{dy}{dx} + P(x)y = Q(x)$. Faktor integrasi adalah $\mu(x) = e^{\int P(x) dx}$.

!!! example "Penyelesaian dengan Faktor Integrasi"
    Selesaikan PDB Rangkaian RL: $L\frac{di}{dt} + Ri = V_0$.
    Ubah ke bentuk standar: $\frac{di}{dt} + \frac{R}{L}i = \frac{V_0}{L}$.

    **Langkah 1: Tentukan Faktor Integrasi**
    $P(t) = \frac{R}{L} \implies \mu(t) = e^{\int \frac{R}{L} dt} = e^{\frac{R}{L}t}$.

    **Langkah 2: Kalikan ruas dengan $\mu(t)$**
    $e^{\frac{R}{L}t} \frac{di}{dt} + \frac{R}{L} e^{\frac{R}{L}t} i = \frac{V_0}{L} e^{\frac{R}{L}t}$.
    Bagian kiri adalah turunan dari $i \cdot e^{\frac{R}{L}t}$.

    **Langkah 3: Integrasikan**
    $i \cdot e^{\frac{R}{L}t} = \int \frac{V_0}{L} e^{\frac{R}{L}t} dt = \frac{V_0}{L} \frac{L}{R} e^{\frac{R}{L}t} + C = \frac{V_0}{R} e^{\frac{R}{L}t} + C$.
    Maka $i(t) = \frac{V_0}{R} + C e^{-\frac{R}{L}t}$. 
    *(Bandingkan hasil analitik ini dengan output komputasi di `Simulasi_Transien_RC_RL.ipynb`!)*

## Ringkasan
Persamaan eksak diselesaikan menggunakan fungsi potensial $F(x,y)$. Persamaan linear diselesaikan dengan faktor integrasi $\mu(x) = e^{\int P(x) dx}$. 

## Referensi

    - Erwin Kreyszig, *Advanced Engineering Mathematics*.
    - `Simulasi_Transien_RC_RL.ipynb` (Praktikum Komputasi).
