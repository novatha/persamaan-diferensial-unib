# Modul 15: Kaitan PDP dengan Persamaan Maxwell

## Pendahuluan
Puncak pemahaman tentang persamaan diferensial parsial (PDP) di bidang kelistrikan adalah penggunaannya untuk merumuskan hukum-hukum fundamental elektromagnetisme, yaitu Persamaan Maxwell. Persamaan-persoalan dari fenomena listrik statis, magnet statis, hingga radiasi gelombang elektromagnetik dan optika berakar dari serangkaian PDP yang dikemukakan oleh James Clerk Maxwell.

Modul penutup ini merangkum keterkaitan erat antara konsep dasar persamaan diferensial parsial yang dipelajari dan perumusan matematis Persamaan Maxwell.

## Materi Utama
## Persamaan Maxwell Bentuk Diferensial
Persamaan Maxwell dalam wujud matematis lokal (bentuk diferensial parsial) di ruang vakum terdiri dari empat hukum utama:

$$

\begin{align}
\nabla \cdot \mathbf{E} &= \frac{\rho_v}{\varepsilon_0} \quad &\text{(Hukum Gauss untuk Listrik)} \\
\nabla \cdot \mathbf{B} &= 0 \quad &\text{(Hukum Gauss untuk Magnet)} \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \quad &\text{(Hukum Faraday)} \\
\nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} \quad &\text{(Hukum Ampere-Maxwell)}
\end{align}

$$

di mana $\mathbf{E}$ adalah medan listrik, $\mathbf{B}$ induksi magnetik, $\rho_v$ rapat muatan, $\mathbf{J}$ rapat arus, serta $\varepsilon_0$ dan $\mu_0$ berturut-turut merupakan permitivitas dan permeabilitas vakum. Operator nabla ($\nabla$) memuat turunan parsial terhadap variabel ruang ($x, y, z$).

## Menurunkan Persamaan Gelombang dari Maxwell
Salah satu pencapaian terbesar teori Maxwell adalah memprediksi keberadaan gelombang elektromagnetik yang bergerak pada kecepatan cahaya. Hal ini dibuktikan melalui manipulasi persamaan-persoalannya.

Pertimbangkan daerah bebas muatan dan arus ($\rho_v = 0, \mathbf{J} = \mathbf{0}$).
Ambil *curl* ($\nabla \times$) pada Hukum Faraday:

$$

\nabla \times (\nabla \times \mathbf{E}) = -\frac{\partial}{\partial t}(\nabla \times \mathbf{B})

$$

Gunakan identitas vektor $\nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$.
Karena $\nabla \cdot \mathbf{E} = 0$, ruas kiri menjadi $-\nabla^2 \mathbf{E}$.
Substitusi Hukum Ampere pada ruas kanan:

$$

-\nabla^2 \mathbf{E} = -\frac{\partial}{\partial t}\left(\mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}\right) = -\mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2}

$$

Sehingga didapatkan **Persamaan Gelombang Tiga Dimensi**:

$$

\nabla^2 \mathbf{E} = \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2}

$$

Bentuk ini adalah klasifikasi PDP hiperbolik. Kecepatan rambat gelombangnya didefinisikan sebagai $v = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \approx c$ (kecepatan cahaya).

## Kaitan dengan Persamaan Laplace dan Poisson
Pada kondisi elektrostatis, yakni bidang tidak berubah terhadap waktu ($\frac{\partial}{\partial t} = 0$), Hukum Faraday berbunyi $\nabla \times \mathbf{E} = 0$. Hal ini memungkinkan pendefinisian medan listrik dari sebuah potensial skalar $V$, $\mathbf{E} = -\nabla V$.
Bila disubstitusikan ke Hukum Gauss untuk Listrik, dihasilkan:

$$

\nabla \cdot (-\nabla V) = \frac{\rho_v}{\varepsilon_0} \implies \nabla^2 V = -\frac{\rho_v}{\varepsilon_0}

$$

Persamaan tersebut dinamakan **Persamaan Poisson**. Apabila pada ruang tersebut tidak ada muatan ($\rho_v = 0$), persamaan bereduksi menjadi **Persamaan Laplace** ($\nabla^2 V = 0$), yang telah kita bedah panjang lebar di bab-bab sebelumnya.

## Ringkasan
Matakuliah Persamaan Diferensial memberikan piranti matematika berupa PDB maupun PDP untuk menafsirkan perilaku alam. Keterkaitan antara PDP dengan Persamaan Maxwell merepresentasikan inti sari ilmu teknik elektro: di mana perambatan gelombang, sinyal nirkabel, hingga rancangan sirkuit dapat direpresentasikan ke dalam bentuk persamaan matematis yang presisi (hiperbolik, parabolik, maupun eliptik).

## Referensi

    - Griffiths, D. J. (2017). *Introduction to Electrodynamics* (4th ed.). Cambridge University Press.
    - Hayt, W. H., & Buck, J. A. (2018). *Engineering Electromagnetics* (9th ed.). McGraw-Hill Education.