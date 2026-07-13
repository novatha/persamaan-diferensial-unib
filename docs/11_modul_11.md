# Modul 11: Persamaan Gelombang 1D (Vibrasi & Transmisi Sinyal)

## Pendahuluan
Banyak fenomena dalam fisika dan teknik elektro melibatkan perambatan gelombang di ruang dan waktu. Contoh klasik meliputi getaran mekanis pada senar (dawai) dan perambatan tegangan atau arus listrik pada saluran transmisi (Transmission Line) ideal tanpa rugi-rugi (Lossless). Keduanya dapat dimodelkan secara matematis melalui Persamaan Gelombang 1-Dimensi.

Pemahaman tentang perambatan gelombang sangat krusial dalam rekayasa telekomunikasi dan sistem daya listrik untuk meminimalkan pantulan gelombang serta mendesain penyesuaian impedansi.

## Materi Utama

## Bentuk Persamaan Gelombang 1-Dimensi
Persamaan gelombang 1-dimensi adalah sebuah Persamaan Diferensial Parsial orde dua linear homogen yang dituliskan sebagai:
$$ \frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2} $$
dimana:

    - $u(x,t)$ dapat berupa perpindahan senar dari posisi kesetimbangan atau amplitudo tegangan/arus $V(x,t)$ atau $I(x,t)$ sepanjang kabel transmisi.
    - $t$ adalah waktu.
    - $x$ adalah posisi.
    - $c$ adalah kecepatan rambat gelombang. Pada elektromagnetik bebas, $c \approx 3 \times 10^8$ m/s, sedangkan pada kabel transmisi dipengaruhi oleh induktansi ($L$) dan kapasitansi ($C$) per satuan panjang, $c = 1/\sqrt{LC}$.

## Solusi Pemisahan Variabel (Gelombang Berdiri)
Dengan memisalkan $u(x,t) = X(x)T(t)$, persamaan gelombang di atas menghasilkan dua PDB:
$$ X''(x) + \lambda^2 X(x) = 0 $$
$$ T''(t) + c^2 \lambda^2 T(t) = 0 $$
Penyelesaian sistem ini menghasilkan frekuensi alami (frekuensi fundamental dan harmoniknya) serta fungsi bentuk gelombang berdiri.

## Solusi D'Alembert (Gelombang Berjalan)
Pendekatan lain untuk menyelesaikan persamaan gelombang (tanpa syarat batas yang tetap) adalah menggunakan metode D'Alembert. Persamaan ini memiliki solusi umum yang mencerminkan fisik gelombang berjalan:
$$ u(x,t) = f(x - ct) + g(x + ct) $$
Penjelasan fisik:

    - $f(x - ct)$ merepresentasikan bentuk gelombang asal yang merambat ke arah sumbu $x$ positif (ke kanan) dengan kecepatan $c$.
    - $g(x + ct)$ merepresentasikan gelombang pantul atau gelombang berjalan yang merambat ke arah sumbu $x$ negatif (ke kiri) dengan kecepatan $c$.

Konsep ini sangat relevan pada Telegrapher's Equations di saluran transmisi, dimana impedansi karakteristik menentukan besarnya gelombang datang dan pantul.

## Ringkasan
Persamaan gelombang 1D memodelkan dinamika transmisi energi mekanik atau elektromagnetik. Solusi melalui pemisahan variabel memberikan deskripsi mode getaran dalam bentuk gelombang berdiri. Sementara itu, solusi D'Alembert menginterpretasikan fenomena ini sebagai superposisi dari dua gelombang yang berjalan ke arah berlawanan, sebuah pemahaman kritis dalam desain saluran transmisi tegangan tinggi (SUTET) maupun frekuensi radio (RF).

## Referensi

    - Erwin Kreyszig, *Advanced Engineering Mathematics*, 10th Edition, John Wiley & Sons.
    - William H. Hayt, John A. Buck, *Engineering Electromagnetics*, McGraw-Hill Education.