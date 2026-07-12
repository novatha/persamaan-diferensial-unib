# Modul 6: Transformasi Laplace Dasar

## Pendahuluan
Transformasi Laplace adalah alat matematis yang sangat berharga untuk menyelesaikan persamaan diferensial, khususnya pada sistem yang melibatkan gaya yang berupa fungsi diskontinyu, sinyal impuls, atau untuk mencari respon sistem. Metode ini mentransformasikan persamaan diferensial (domain waktu) menjadi persamaan aljabar (domain kompleks atau frekuensi $s$). Hal ini mempermudah penyelesaian, layaknya kita mengubah operasi perkalian rumit dengan logaritma.

## Materi Utama
## Definisi Transformasi Laplace
**Definisi:**

Misalkan $f(t)$ adalah fungsi yang didefinisikan untuk $t \ge 0$. Transformasi Laplace dari $f(t)$, dinotasikan dengan $\mathcal{L}\{f(t)\}$ atau $F(s)$, didefinisikan sebagai integral tak wajar:
$$
\mathcal{L}\{f(t)\} = F(s) = \int_{0}^{\infty} e^{-st} f(t) dt
$$
asalkan integral tersebut konvergen (memiliki nilai batas berhingga). Variabel $s$ merupakan parameter riil atau kompleks.


**Contoh Pencarian Transformasi Laplace dari Definisi:**
Mari kita cari $\mathcal{L}\{1\}$.
$$ \mathcal{L}\{1\} = \int_{0}^{\infty} e^{-st} (1) dt = \lim_{b \to \infty} \int_{0}^{b} e^{-st} dt = \lim_{b \to \infty} \left[ -\frac{1}{s} e^{-st} \right]_0^b = \lim_{b \to \infty} \left( -\frac{1}{s} e^{-sb} + \frac{1}{s} e^0 \right) = \frac{1}{s} $$
Integral konvergen jika $s > 0$.

**Tabel Transformasi Laplace Dasar:**
Beberapa transformasi fungsi dasar yang umum dijumpai:

    - $\mathcal{L}\{1\} = \frac{1}{s}, \quad s > 0$
    - $\mathcal{L}\{t^n\} = \frac{n!}{s^{n+1}}, \quad s > 0$
    - $\mathcal{L}\{e^{at}\} = \frac{1}{s-a}, \quad s > a$
    - $\mathcal{L}\{\sin(\omega t)\} = \frac{\omega}{s^2 + \omega^2}, \quad s > 0$
    - $\mathcal{L}\{\cos(\omega t)\} = \frac{s}{s^2 + \omega^2}, \quad s > 0$

## Sifat Linieritas
Transformasi Laplace bersifat linier. Artinya, untuk dua fungsi sembarang $f(t)$ dan $g(t)$ serta konstanta $c_1, c_2$:
$$
\mathcal{L}\{c_1 f(t) + c_2 g(t)\} = c_1 \mathcal{L}\{f(t)\} + c_2 \mathcal{L}\{g(t)\}
$$
**Contoh:**

Tentukan $\mathcal{L}\{3e^{2t} - 5\cos(4t)\}$.\\
**Solusi:**
$\mathcal{L}\{3e^{2t} - 5\cos(4t)\} = 3\mathcal{L}\{e^{2t}\} - 5\mathcal{L}\{\cos(4t)\} = 3\left(\frac{1}{s-2}\right) - 5\left(\frac{s}{s^2 + 16}\right)$.


## Teorema Pergeseran (Translasi) Pertama
Teorema ini berguna ketika mencari transformasi Laplace dari fungsi yang dikalikan eksponensial.
**Definisi: Teorema Pergeseran pada Sumbu-$s$**

Jika $\mathcal{L}\{f(t)\} = F(s)$ ada untuk $s>c$, maka untuk konstanta riil $a$:
$$
\mathcal{L}\{e^{at} f(t)\} = F(s-a)
$$


**Contoh:**

Tentukan $\mathcal{L}\{e^{3t} t^2\}$.\\
**Solusi:**
Kita tahu $\mathcal{L}\{t^2\} = \frac{2}{s^3} = F(s)$.
Menurut Teorema Pergeseran, $\mathcal{L}\{e^{3t} t^2\} = F(s-3) = \frac{2}{(s-3)^3}$.


Teorema Pergeseran Pertama merepresentasikan perkalian domain waktu oleh $e^{at}$ menyebabkan pergeseran $a$ unit pada variabel $s$ di domain frekuensi (Laplace). Ini banyak dijumpai dalam bentuk redaman (damping) pada sistem dinamis elektro dan mekanik (misalnya faktor redaman $e^{-\alpha t}$).

## Ringkasan
Transformasi Laplace memetakan fungsi-fungsi waktu $f(t)$ menjadi fungsi aljabar $F(s)$. Transformasi ini membantu dalam mengubah masalah PDB yang rumit menjadi manipulasi aljabar pecahan. Kita telah mempelajari definisi dasar dari transformasi Laplace, tabel standar, serta sifat-sifat utamanya: linieritas dan Teorema Pergeseran.

## Referensi

    - Zill, D. G. (2018). *A First Course in Differential Equations with Modeling Applications*. Cengage Learning.
    - Lathi, B. P. (2005). *Linear Systems and Signals*. Oxford University Press.