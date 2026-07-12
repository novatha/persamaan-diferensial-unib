# Modul 3: Aplikasi Persamaan Diferensial Biasa Orde 1

## Pendahuluan
Setelah memahami cara menyelesaikan Persamaan Diferensial Biasa (PDB) Orde 1, penerapan langsung yang paling sering dijumpai dalam dunia rekayasa, khususnya Teknik Elektro, adalah pada analisis kondisi transien rangkaian listrik. Pada modul ini, kita akan membahas penerapan PDB Orde 1 dalam menganalisis rangkaian Resistor-Kapasitor (RC) dan Resistor-Induktor (RL). Selain itu, kita juga akan meninjau Hukum Pendinginan Newton, sebagai bentuk permodelan fenomena termal pada konduktor/komponen elektronik.

## Materi Utama

## Analisis Transien Rangkaian RL
Tinjau rangkaian seri Resistor $R$ dan Induktor $L$ dengan sumber tegangan arus searah (DC) $V_0$ yang terhubung melalui saklar pada saat $t=0$. Hukum Tegangan Kirchhoff (KVL) menyatakan:
$$ V_R + V_L = V_0 \implies R i(t) + L \frac{di(t)}{dt} = V_0 $$
Persamaan ini dapat ditulis ulang menjadi PDB Linear Orde 1:
$$ \frac{di}{dt} + \frac{R}{L} i = \frac{V_0}{L} $$
Dengan faktor integrasi $\mu(t) = e^{\int \frac{R}{L} dt} = e^{\frac{R}{L}t}$, solusi umum dari arus adalah:
$$ i(t) = \frac{V_0}{R} + C e^{-\frac{R}{L}t} $$
Jika diasumsikan pada saat awal $t=0$, tidak ada arus yang mengalir (syarat awal $i(0) = 0$), maka konstanta $C = -\frac{V_0}{R}$.
**Solusi Khusus:**
$$ i(t) = \frac{V_0}{R} \left( 1 - e^{-\frac{R}{L}t} \right) $$
Nilai $\tau = \frac{L}{R}$ disebut konstanta waktu (time constant) dari rangkaian RL.

## Rangkaian RC: Pengisian dan Pengosongan Kapasitor
Untuk rangkaian seri Resistor $R$ dan Kapasitor $C$ yang terhubung ke sumber DC $V_0$, persamaan KVL adalah:
$$ V_R + V_C = V_0 \implies R i(t) + \frac{1}{C} \int i(t) dt = V_0 $$
Dalam bentuk tegangan kapasitor, mengingat $i(t) = C \frac{dV_C}{dt}$, persamaannya menjadi:
$$ RC \frac{dV_C}{dt} + V_C = V_0 $$
**Kasus Pengosongan Kapasitor:**
Ketika sumber tegangan dilepas ($V_0 = 0$) dan kapasitor memilki tegangan awal $V_C(0) = V_{awal}$, persamaannya adalah PDB separabel homogen:
$$ RC \frac{dV_C}{dt} + V_C = 0 \implies \frac{dV_C}{V_C} = -\frac{1}{RC} dt $$
Dengan mengintegralkan kedua ruas, didapat solusi pengosongan:
$$ V_C(t) = V_{awal} e^{-\frac{1}{RC}t} $$
Konstanta waktu untuk rangkaian ini adalah $\tau = RC$.

## Hukum Pendinginan Newton (Newton's Law of Cooling)
Hukum ini menyatakan bahwa laju perubahan suhu suatu benda sebanding dengan selisih antara suhu benda tersebut $T(t)$ dan suhu medium sekitarnya $T_m$. Hal ini berguna, misalnya, untuk memodelkan disipasi panas pada transformator atau IC.
Persamaan matematisnya adalah:
$$ \frac{dT}{dt} = -k(T - T_m) $$
dimana $k > 0$ adalah konstanta proporsionalitas. Persamaan ini merupakan persamaan separabel:
$$ \frac{dT}{T - T_m} = -k dt $$
Sehingga solusi untuk suhu benda tiap saat adalah:
$$ T(t) = T_m + (T_0 - T_m)e^{-kt} $$
dengan $T_0$ adalah suhu awal benda pada $t=0$.

## Ringkasan
Aplikasi PDB Orde 1 sangat nyata dalam menganalisis kondisi transien rangkaian listrik sederhana. Rangkaian seri RL dan RC menghasilkan model matematika berupa PDB linear atau separabel yang menunjukkan perilaku eksponensial terhadap waktu dengan parameter konstanta waktu $\tau = L/R$ atau $\tau = RC$. Selain itu, fenomena termal sederhana dapat dimodelkan secara elegan menggunakan Hukum Pendinginan Newton, memperluas wawasan aplikasi persamaan diferensial di luar listrik ke arah disipasi daya.

## Referensi

    - Charles K. Alexander & Matthew N.O. Sadiku, *Fundamentals of Electric Circuits*, McGraw-Hill.
    - Erwin Kreyszig, *Advanced Engineering Mathematics*, John Wiley & Sons.