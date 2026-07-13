# Modul 4: Persamaan Diferensial Biasa Orde 2 Linier Homogen

## Pendahuluan
Persamaan Diferensial Orde 2 banyak muncul dalam pemodelan sistem dinamik yang memiliki elemen penyimpan energi ganda, seperti rangkaian RLC pada Teknik Elektro maupun sistem massa-pegas pada mekanika. Pada minggu ini, kita akan berfokus pada Persamaan Diferensial Biasa (PDB) Orde 2 Linier Homogen dengan Koefisien Konstan. Pemahaman terhadap metode persamaan karakteristik menjadi kunci untuk menganalisis respons natural dari sistem orde dua.

## Materi Utama

## Bentuk Umum
Bentuk umum PDB Orde 2 Linier dengan Koefisien Konstan adalah:
$$ a \frac{d^2y}{dx^2} + b \frac{dy}{dx} + cy = f(x) $$
Jika $f(x) = 0$, maka persamaan disebut **Homogen**. Sehingga bentuk PDB linier orde 2 homogen adalah:
$$ ay'' + by' + cy = 0 $$
dengan $a, b, c$ adalah konstanta real dan $a \neq 0$.

## Persamaan Karakteristik
Solusi untuk PDB jenis ini dicari dalam bentuk fungsi eksponensial $y = e^{rx}$. Dengan mensubstitusikan $y$, $y' = re^{rx}$, dan $y'' = r^2e^{rx}$ ke persamaan asli, kita dapatkan:
$$ a(r^2e^{rx}) + b(re^{rx}) + c(e^{rx}) = 0 $$
$$ e^{rx} (ar^2 + br + c) = 0 $$
Karena $e^{rx} \neq 0$ untuk setiap nilai $x$, maka haruslah:
$$ ar^2 + br + c = 0 $$
Persamaan kuadrat ini disebut **Persamaan Karakteristik** (atau Persamaan Pembantu). Akar-akar dari persamaan karakteristik ($r_1$ dan $r_2$) menentukan bentuk solusi umum.

## Tiga Kasus Solusi Umum
Diskriminan dari persamaan karakteristik adalah $D = b^2 - 4ac$. Terdapat tiga kasus solusi tergantung nilai $D$:

**Kasus I: Dua Akar Real dan Berbeda ($D > 0$)**<br>
Jika $r_1 \neq r_2$ dan keduanya adalah bilangan real, maka basis solusinya adalah $y_1 = e^{r_1x}$ dan $y_2 = e^{r_2x}$.
Solusi umum:
$$ y(x) = C_1 e^{r_1x} + C_2 e^{r_2x} $$
(Dalam analisis rangkaian RLC, kondisi ini bersesuaian dengan sistem *overdamped*).

**Kasus II: Akar Kembar / Real Sama ($D = 0$)**<br>
Jika $r_1 = r_2 = r$, maka solusi basisnya adalah $y_1 = e^{rx}$ dan agar linier independen, solusi kedua dikalikan $x$, menjadi $y_2 = x e^{rx}$.
Solusi umum:
$$ y(x) = C_1 e^{rx} + C_2 x e^{rx} = (C_1 + C_2 x) e^{rx} $$
(Kondisi ini bersesuaian dengan sistem *critically damped*).

**Kasus III: Akar Kompleks Konjugat ($D < 0$)**<br>
Jika akar-akar tersebut kompleks berbentuk $r_1 = \alpha + i\beta$ dan $r_2 = \alpha - i\beta$ dengan $\alpha = -\frac{b}{2a}$ dan $\beta = \frac{\sqrt{4ac - b^2}}{2a}$.
Menggunakan identitas Euler ($e^{i\theta} = \cos\theta + i\sin\theta$), solusi umumnya dapat ditulis dalam bentuk sinus dan kosinus beramplitudo eksponensial.
Solusi umum:
$$ y(x) = e^{\alpha x} (C_1 \cos \beta x + C_2 \sin \beta x) $$
(Kondisi ini bersesuaian dengan sistem *underdamped*, menunjukkan osilasi yang meluruh jika $\alpha < 0$).

**Contoh:**

Tentukan solusi umum PDB: $y'' + 5y' + 6y = 0$<br>
**Penyelesaian:**<br>
Persamaan karakteristik: $r^2 + 5r + 6 = 0$<br>
Faktorisasi: $(r+2)(r+3) = 0 \implies r_1 = -2, r_2 = -3$<br>
Karena $r_1 \neq r_2$ real (Kasus I), maka solusi umumnya adalah:
$$ y(x) = C_1 e^{-2x} + C_2 e^{-3x} $$


## Ringkasan
Penyelesaian PDB Orde 2 Linier Homogen dengan Koefisien Konstan didasarkan pada pencarian akar-akar dari Persamaan Karakteristik $ar^2 + br + c = 0$. Bentuk solusi umum dijamin secara eksklusif jatuh ke dalam tiga kasus: akar real berbeda (sistem *overdamped*), akar kembar (sistem *critically damped*), atau akar kompleks konjugat (sistem *underdamped*).

## Referensi

    - Erwin Kreyszig, *Advanced Engineering Mathematics*, John Wiley & Sons.
    - Dennis G. Zill, *A First Course in Differential Equations with Modeling Applications*, Cengage Learning.