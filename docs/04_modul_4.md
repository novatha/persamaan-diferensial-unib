# {Modul Pembelajaran Persamaan Diferensial

\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=Capaian Pembelajaran Khusus (Sub-CPMK 4)]
Setelah mempelajari modul ini, mahasiswa diharapkan mampu:

    - Menjelaskan struktur PDB linier orde 2 homogen dengan koefisien konstan.
    - Menguji kebebasan linier pasangan solusi basis menggunakan determinan Wronskian.
    - Membuktikan kemunculan suku $x e^{rx}$ pada akar kembar melalui Metode Reduksi Orde.
    - Menyelesaikan Masalah Nilai Awal (IVP) untuk 3 kasus diskriminan ($D > 0, D = 0, D < 0$).
    - Memodelkan osilasi alami pada sistem fisik rangkaian listrik LC murni tanpa redaman.

\end{tcolorbox}

## Pendahuluan: Sistem Orde Dua dalam Rekayasa Elektro
Pada perkuliahan minggu sebelumnya, kita telah mempelajari sistem orde satu yang hanya memuat satu elemen penyimpan energi (seperti induktor pada rangkaian RL atau kapasitor pada rangkaian RC). Namun, mayoritas sistem kelistrikan industri bersifat **orde dua atau lebih tinggi** karena memuat dua elemen penyimpan energi yang saling bertukar medan, yaitu:

    - **Induktor ($L$):** menyimpan energi dalam bentuk medan magnetik ($E_L = \frac{1}{2} L i^2$).
    - **Kapasitor ($C$):** menyimpan energi dalam bentuk medan listrik ($E_C = \frac{1}{2} C v^2 = \frac{q^2}{2C}$).

Interaksi dinamis antara kedua elemen ini melahirkan persamaan diferensial yang melibatkan turunan kedua terhadap waktu ($\frac{d^2 i}{dt^2}$ atau $\frac{d^2 q}{dt^2}$). Sebelum menganalisis pengaruh sumber tegangan luar (sistem non-homogen pada Minggu 5), kita wajib menguasai perilaku alami (*natural response*) sistem melalui **PDB Linier Orde 2 Homogen**.

---

## Bentuk Standar \& Prinsip Superposisi

!!! info "PDB Linier Orde 2 Homogen Koefisien Konstan"
    Bentuk umum PDB linier orde 2 dengan koefisien konstan dinyatakan oleh:
    \begin{equation}
    a \frac{d^2y}{dx^2} + b \frac{dy}{dx} + c y = 0 \quad \iff \quad a y'' + b y' + c y = 0
    \end{equation}
    di mana $a, b, c \in \mathbb{R}$ adalah konstanta riil dengan $a \neq 0$.

\begin{theorem}[Prinsip Superposisi Linier]
Jika $y_1(x)$ dan $y_2(x)$ adalah dua solusi bebas dari persamaan homogen $a y'' + b y' + c y = 0$, maka sembarang kombinasi linier:
\begin{equation}
y(x) = C_1 y_1(x) + C_2 y_2(x)
\end{equation}
juga merupakan solusi dari persamaan tersebut untuk sembarang konstanta $C_1, C_2 \in \mathbb{R}$.
\end{theorem}

### Uji Kebebasan Linier: Determinan Wronskian
Dua buah fungsi $y_1(x)$ dan $y_2(x)$ dikatakan **bebas linier** (*linearly independent*) pada suatu interval $I$ jika tidak ada konstanta $k$ sehingga $y_1(x) = k y_2(x)$. Untuk membuktikan kebebasan linier secara matematis, digunakan **Determinan Wronskian**:
\begin{equation}
W(y_1, y_2)(x) = \begin{vmatrix} y_1(x) & y_2(x) 

y_1'(x) & y_2'(x) \end{vmatrix} = y_1(x) y_2'(x) - y_1'(x) y_2(x)
\end{equation}

    - Jika $W(y_1, y_2) \neq 0$ untuk setiap $x \in I$, maka $y_1$ dan $y_2$ membentuk **Himpunan Solusi Fundamental** (*Fundamental Set of Solutions*), dan solusi umum $y = C_1 y_1 + C_2 y_2$ dijamin mampu memenuhi sembarang kondisi awal (IVP).
    - Jika $W(y_1, y_2) = 0$, kedua fungsi bergantung linier dan tidak dapat membentuk solusi umum.

---

## Persamaan Karakteristik \& Tiga Ragam Solusi
Untuk menyelesaikan $a y'' + b y' + c y = 0$, kita mengasumsikan solusi eksponensial $y = e^{rx}$. Mengingat sifat turunan fungsi eksponensial $y' = r e^{rx}$ dan $y'' = r^2 e^{rx}$, substitusi ke dalam PDB menghasilkan:
\begin{equation}
a (r^2 e^{rx}) + b (r e^{rx}) + c (e^{rx}) = e^{rx}(a r^2 + b r + c) = 0
\end{equation}
Karena fungsi eksponensial $e^{rx} \neq 0$ untuk seluruh $x \in \mathbb{R}$, syarat agar persamaan bernilai nol adalah:
\begin{equation}
a r^2 + b r + c = 0 \quad \text{(Persamaan Karakteristik / Polinomial Pembantu)}
\end{equation}

Akar-akar dari persamaan kuadrat ini diberikan oleh rumus kuadratik:
\begin{equation}
r_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{equation}
Bentuk solusi umum sangat bergantung pada nilai diskriminan $D = b^2 - 4ac$.

---

### Kasus 1: Diskriminan Positif ($D = b^2 - 4ac > 0$)
Pada kasus ini, persamaan karakteristik menghasilkan dua akar real berbeda ($r_1 \neq r_2$).
Pasangan solusi basis adalah $y_1 = e^{r_1 x}$ dan $y_2 = e^{r_2 x}$.
Wronskian dari pasangan ini adalah:
\begin{equation}
W(e^{r_1 x}, e^{r_2 x}) = e^{r_1 x}(r_2 e^{r_2 x}) - (r_1 e^{r_1 x})e^{r_2 x} = (r_2 - r_1) e^{(r_1+r_2)x} \neq 0
\end{equation}
Karena $r_1 \neq r_2$, maka $W \neq 0$, membuktikan bahwa kedua solusi bebas linier.

\begin{tcolorbox}[colback=green!5!white,colframe=green!60!black,title=Bentuk Solusi Umum Kasus 1 (Akar Real Berbeda)]
\begin{equation}
y(x) = C_1 e^{r_1 x} + C_2 e^{r_2 x}
\end{equation}
*Interpretasi Fisis:* Bersesuaian dengan sistem tanpa osilasi yang kembali ke titik kesetimbangan secara lambat (*Overdamped*).
\end{tcolorbox}

!!! example "Masalah Nilai Awal Kasus 1"
    Selesaikan Masalah Nilai Awal (IVP) berikut:
    $$ y'' - y' - 6y = 0, \quad y(0) = 5, \quad y'(0) = 0 $$
    **Langkah Penyelesaian:**
    
        - **Susun Persamaan Karakteristik:**
        $$ r^2 - r - 6 = 0 \implies (r - 3)(r + 2) = 0 \implies r_1 = 3, \quad r_2 = -2 $$
        - **Tuliskan Solusi Umum:**
        $$ y(x) = C_1 e^{3x} + C_2 e^{-2x} $$
        - **Hitung Turunan Pertama:**
        $$ y'(x) = 3C_1 e^{3x} - 2C_2 e^{-2x} $$
        - **Terapkan Kondisi Awal:**
        $$ y(0) = C_1 + C_2 = 5 $$
        $$ y'(0) = 3C_1 - 2C_2 = 0 \implies C_2 = \frac{3}{2} C_1 $$
        Substitusi ke persamaan pertama:
        $$ C_1 + \frac{3}{2} C_1 = 5 \implies \frac{5}{2} C_1 = 5 \implies C_1 = 2 \implies C_2 = 3 $$
        - **Solusi Khusus:**
        $$ \mathbf{y(x) = 2e^{3x} + 3e^{-2x}} $$
    

---

### Kasus 2: Diskriminan Nol ($D = b^2 - 4ac = 0$)
Jika diskriminan bernilai nol, persamaan karakteristik menghasilkan sepasang **akar kembar real**:
$$ r_1 = r_2 = r = -\frac{b}{2a} $$
Dari akar ini, kita baru memiliki satu solusi basis: $y_1(x) = e^{rx}$. Kita memerlukan solusi kedua $y_2(x)$ yang bebas linier agar membentuk himpunan solusi fundamental.

\begin{tcolorbox}[colback=yellow!10!white,colframe=orange!80!black,title=Penurunan: Mengapa Muncul Faktor Pengali $x$ (Metode Reduksi Orde)?]
Misalkan solusi kedua berbentuk $y_2(x) = u(x) y_1(x) = u(x) e^{rx}$.

Turunkan $y_2(x)$:
$$ y_2' = u' e^{rx} + r u e^{rx} $$
$$ y_2'' = u'' e^{rx} + 2r u' e^{rx} + r^2 u e^{rx} $$
Substitusikan ke dalam PDB $a y_2'' + b y_2' + c y_2 = 0$:
$$ a(u'' + 2r u' + r^2 u)e^{rx} + b(u' + r u)e^{rx} + c u e^{rx} = 0 $$
Kumpulkan suku-suku berdasarkan turunan $u$:
$$ e^{rx} \Big[ a u'' + (2ar + b)u' + (a r^2 + b r + c)u \Big] = 0 $$
Perhatikan dua identitas penting:

    - Karena $r = -\frac{b}{2a}$, maka $2ar + b = 2a\left(-\frac{b}{2a}\right) + b = 0$.
    - Karena $r$ adalah akar karakteristik, maka $a r^2 + b r + c = 0$.

Sehingga persamaan tereduksi secara dramatis menjadi:
$$ a u'' = 0 \implies u''(x) = 0 \quad (\text{karena } a \neq 0) $$
Integrasikan dua kali terhadap $x$:
$$ u'(x) = C \implies u(x) = C x + K $$
Dengan mengambil konstanta sederhana $C = 1$ dan $K = 0$, diperoleh:
$$ u(x) = x \implies \mathbf{y_2(x) = x e^{rx}} $$
\end{tcolorbox}

\begin{tcolorbox}[colback=green!5!white,colframe=green!60!black,title=Bentuk Solusi Umum Kasus 2 (Akar Real Kembar)]
\begin{equation}
y(x) = C_1 e^{rx} + C_2 x e^{rx} = (C_1 + C_2 x) e^{rx}
\end{equation}
*Interpretasi Fisis:* Bersesuaian dengan sistem redaman kritis (*Critically Damped*) yang kembali ke titik netral paling cepat tanpa pernah berosilasi.
\end{tcolorbox}

!!! example "Masalah Nilai Awal Kasus 2"
    Selesaikan IVP: $y'' + 6y' + 9y = 0$, dengan $y(0) = 2$ dan $y'(0) = -1$.
    
        - Persamaan karakteristik: $r^2 + 6r + 9 = (r + 3)^2 = 0 \implies r = -3$ (akar kembar).
        - Solusi umum: $y(x) = (C_1 + C_2 x)e^{-3x}$.
        - Turunan: $y'(x) = C_2 e^{-3x} - 3(C_1 + C_2 x)e^{-3x}$.
        - Kondisi awal:
        $$ y(0) = C_1 = 2 $$
        $$ y'(0) = C_2 - 3C_1 = -1 \implies C_2 - 3(2) = -1 \implies C_2 = 5 $$
        - Solusi khusus: $\mathbf{y(x) = (2 + 5x)e^{-3x}}$.
    

---

### Kasus 3: Diskriminan Negatif ($D = b^2 - 4ac < 0$)
Jika diskriminan negatif, akar-akar karakteristik berupa pasangan **bilangan kompleks konjugat**:
\begin{equation}
r_{1,2} = \alpha \pm j\beta, \quad \text{dengan } \alpha = -\frac{b}{2a}, \quad \beta = \frac{\sqrt{4ac - b^2}}{2a}
\end{equation}
Solusi formal dalam domain kompleks adalah:
$$ y(x) = c_1 e^{(\alpha + j\beta)x} + c_2 e^{(\alpha - j\beta)x} = e^{\alpha x} \left( c_1 e^{j\beta x} + c_2 e^{-j\beta x} \right) $$
Menggunakan **Formula Euler** ($e^{j\theta} = \cos\theta + j\sin\theta$ dan $e^{-j\theta} = \cos\theta - j\sin\theta$):
$$ y(x) = e^{\alpha x} \left[ c_1(\cos\beta x + j\sin\beta x) + c_2(\cos\beta x - j\sin\beta x) \right] $$
$$ y(x) = e^{\alpha x} \left[ (c_1 + c_2)\cos\beta x + j(c_1 - c_2)\sin\beta x \right] $$
Agar solusi bernilai riil untuk fenomena fisik rekayasa nyata, kita mendefinisikan konstanta riil baru:
$$ C_1 = c_1 + c_2 \quad \text{dan} \quad C_2 = j(c_1 - c_2) $$
sehingga bilangan imajiner $j$ melebur secara alami ke dalam konstanta riil $C_2$.

\begin{tcolorbox}[colback=green!5!white,colframe=green!60!black,title=Bentuk Solusi Umum Kasus 3 (Akar Kompleks Konjugat)]
\begin{equation}
y(x) = e^{\alpha x} \left( C_1 \cos(\beta x) + C_2 \sin(\beta x) \right)
\end{equation}
*Interpretasi Fisis:* Bersesuaian dengan sistem osilasi teredam (*Underdamped*), di mana $\alpha$ mengatur laju peluruhan amplutido dan $\beta$ mengatur frekuensi osilasi sudut.
\end{tcolorbox}

!!! example "Masalah Nilai Awal Kasus 3"
    Tentukan solusi dari: $y'' + 4y' + 13y = 0$, $y(0) = 3$, $y'(0) = 2$.
    
        - Karakteristik: $r^2 + 4r + 13 = 0 \implies r = \frac{-4 \pm \sqrt{16 - 52}}{2} = \frac{-4 \pm \sqrt{-36}}{2} = -2 \pm 3j$.
        - Parameter: $\alpha = -2, \beta = 3$.
        - Solusi umum: $y(x) = e^{-2x}(C_1 \cos 3x + C_2 \sin 3x)$.
        - Turunan:
        $$ y'(x) = -2e^{-2x}(C_1 \cos 3x + C_2 \sin 3x) + e^{-2x}(-3C_1 \sin 3x + 3C_2 \cos 3x) $$
        - Masukkan kondisi awal:
        $$ y(0) = C_1 = 3 $$
        $$ y'(0) = -2C_1 + 3C_2 = 2 \implies -2(3) + 3C_2 = 2 \implies 3C_2 = 8 \implies C_2 = \frac{8}{3} $$
        - Solusi khusus: $\mathbf{y(x) = e^{-2x}\left( 3\cos 3x + \frac{8}{3}\sin 3x \right)}$.
    

---

## Aplikasi Fisik: Rangkaian Osilator LC Murni

Tinjau sebuah rangkaian tertutup yang terdiri atas induktor ideal $L$ (Henry) dan kapasitor ideal $C$ (Farad) tanpa adanya hambatan resistor ($R = 0$). Rangkaian ini dikenal sebagai **Tangki Osilator Frekuensi Radio (*RF Tank Circuit*)**.

### Penurunan Model dari Hukum Kirchhoff (KVL)
Berdasarkan Hukum Tegangan Kirchhoff (KVL), jumlah tegangan dalam loop tertutup bernilai nol:
\begin{equation}
v_L(t) + v_C(t) = 0
\end{equation}
Mengingat hubungan arus dan muatan listrik:
$$ i(t) = \frac{dq}{dt}, \quad v_L = L \frac{di}{dt} = L \frac{d^2q}{dt^2}, \quad v_C = \frac{q}{C} $$
Substitusikan ke persamaan KVL:
\begin{equation}
L \frac{d^2q}{dt^2} + \frac{1}{C} q(t) = 0 \quad \iff \quad \frac{d^2q}{dt^2} + \omega_0^2 q(t) = 0
\end{equation}
di mana $\omega_0 = \frac{1}{\sqrt{LC}}$ adalah **frekuensi sudut resonansi alami** (*undamped natural resonant angular frequency*) dalam satuan rad/s.

### Solusi Muatan dan Arus Listrik
Persamaan karakteristik: $r^2 + \omega_0^2 = 0 \implies r = \pm j\omega_0$.
Karena $\alpha = 0$ dan $\beta = \omega_0$, maka solusi muatan pada kapasitor adalah osilasi harmonik abadi:
\begin{equation}
q(t) = C_1 \cos(\omega_0 t) + C_2 \sin(\omega_0 t)
\end{equation}
Arus listrik yang mengalir dalam loop:
\begin{equation}
i(t) = \frac{dq}{dt} = -\omega_0 C_1 \sin(\omega_0 t) + \omega_0 C_2 \cos(\omega_0 t)
\end{equation}

### Kekekalan Energi Total Rangkaian
Energi total sistem pada sembarang waktu $t$ adalah jumlah energi magnetik induktor dan energi elektrostatik kapasitor:
\begin{equation}
E_{\text{total}}(t) = E_L(t) + E_C(t) = \frac{1}{2} L [i(t)]^2 + \frac{1}{2C} [q(t)]^2
\end{equation}
Jika kita masukkan solusi $q(t) = Q_0 \cos(\omega_0 t)$ (asumsi muatan awal $Q_0$ dan arus awal $i(0) = 0$), maka $i(t) = -\omega_0 Q_0 \sin(\omega_0 t)$:
$$ E_{\text{total}} = \frac{1}{2} L \left(-\frac{1}{\sqrt{LC}} Q_0 \sin\omega_0 t\right)^2 + \frac{1}{2C} (Q_0 \cos\omega_0 t)^2 $$
$$ E_{\text{total}} = \frac{Q_0^2}{2C} \sin^2(\omega_0 t) + \frac{Q_0^2}{2C} \cos^2(\omega_0 t) = \frac{Q_0^2}{2C} (\sin^2\omega_0 t + \cos^2\omega_0 t) = \mathbf{\frac{Q_0^2}{2C} = \text{Konstan}} $$
Persamaan ini membuktikan secara analitik bahwa energi berpindah secara kontinu bolak-balik antara kapasitor dan induktor tanpa ada energi yang terdisipasi (hilang menjadi panas).

---

## Rangkuman Komparatif
\begin{table}[h!]
\centering
\small
\begin{tabular}{@{}llll@{}}
\toprule
**Kriteria** & **Kasus 1 ($D > 0$)** & **Kasus 2 ($D = 0$)** & **Kasus 3 ($D < 0$)** 

\midrule
**Akar Karakteristik** & Real Berbeda ($r_1 \neq r_2$) & Real Kembar ($r_1 = r_2 = r$) & Kompleks Konjugat ($\alpha \pm j\beta$) 

**Solusi Basis** & $e^{r_1 x}, e^{r_2 x}$ & $e^{rx}, x e^{rx}$ & $e^{\alpha x}\cos\beta x, e^{\alpha x}\sin\beta x$ 

**Bentuk Solusi** & $y = C_1 e^{r_1 x} + C_2 e^{r_2 x}$ & $y = (C_1 + C_2 x)e^{rx}$ & $y = e^{\alpha x}(C_1 \cos\beta x + C_2 \sin\beta x)$ 

**Rezim Fisik** & *Overdamped* (Sangat Redam) & *Critically Damped* (Redam Kritis) & *Underdamped* (Kurang Redam) 

**Osilasi** & Tidak ada osilasi & Tidak ada osilasi & Ada osilasi sinusoidal 

**Kecepatan Redaman** & Paling lambat (ekivalen $R$ besar) & Tercepat mencapai nol & Meluruh perlahan jika $\alpha < 0$ 

\bottomrule
\end{tabular}
\end{table}

---

## Referensi

    - Erwin Kreyszig, *Advanced Engineering Mathematics*, 10th Edition, John Wiley \& Sons, 2011.
    - Dennis G. Zill, *A First Course in Differential Equations with Modeling Applications*, 11th Edition, Cengage Learning, 2018.
    - Charles K. Alexander \& Matthew N. O. Sadiku, *Fundamentals of Electric Circuits*, 7th Edition, McGraw-Hill, 2021.
