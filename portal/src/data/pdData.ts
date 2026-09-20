export interface PdModule {
  week: number;
  title: string;
  subTitle: string;
  category: 'Fondasi PDB & Rangkaian' | 'Aplikasi Transien' | 'Sistem Orde 2 & Resonansi' | 'Metode Laplace' | 'PDP & Deret Fourier' | 'Medan EM & Gelombang';
  subCpmk: string;
  summary: string;
  theoryTopics: string[];
  computationLab: string;
  slidesPdf: string;
  problemSetPdf?: string;
  solvedPdf?: string;
  worksheetPdf?: string;
  notesPdf?: string;
  videoFile?: string;
  youtubeUrl?: string;
  formulaLatex: string;
  bloomHighlights: {
    c1_c2: string;
    c3_c4: string;
    c5_c6: string;
  };
}

export const pdMetadata = {
  courseName: "Persamaan Diferensial",
  courseSubtitle: "Fokus Landasan Medan Elektromagnetika & Analisis Rangkaian Listrik",
  courseCode: "TEE-203",
  credits: "3 SKS (2 Teori, 1 Komputasi Ilmiah Julia)",
  semester: "Semester Genap 2026",
  studyProgram: "S1 Teknik Elektro",
  faculty: "Fakultas Teknik",
  university: "Universitas Bengkulu (UNIB)",
  lecturers: [
    {
      name: "Ir. Novalio Daratha, S.T., M.Sc., Ph.D.",
      role: "Dosen Pengampu Utama",
      lab: "Laboratorium Sistem Tenaga dan Komputasi Cerdas"
    },
    {
      name: "Muhammad Arfan, S.T., M.T.",
      role: "Dosen Pengampu Pendamping",
      lab: "Laboratorium Teknik Elektro UNIB"
    }
  ],
  rpsPdf: "/pdf/RPS_Persamaan_Diferensial.pdf",
  cpmkList: [
    { code: "CPMK-1", desc: "Mampu mengklasifikasikan PDB/PDP, menyelesaikan Masalah Nilai Awal (IVP), serta memodelkan dinamika energi rangkaian elektrik orde 1." },
    { code: "CPMK-2", desc: "Mampu menyelesaikan PDB linier orde 1 (Separabel, Eksak, Faktor Integrasi) dan menganalisis respon transien RC, RL, serta hukum pendinginan termal." },
    { code: "CPMK-3", desc: "Mampu menyelesaikan PDB linier orde 2 homogen dan non-homogen, menguji determinan Wronskian, serta mengevaluasi respon transien dan resonansi RLC seri AC." },
    { code: "CPMK-4", desc: "Mampu menerapkan Transformasi Laplace dan Invers Laplace (dekomposisi pecahan parsial) untuk menyelesaikan IVP rangkaian elektrik pada domain kompleks s." },
    { code: "CPMK-5", desc: "Mampu menyelesaikan Persamaan Diferensial Parsial (PDP) dengan Deret Fourier dan Metode Pemisahan Variabel (Separation of Variables)." },
    { code: "CPMK-6", desc: "Mampu menganalisis persamaan gelombang 1D (telegrafer transmisi), persamaan panas 1D, persamaan Laplace 2D, fungsi Bessel, dan 4 Persamaan Maxwell." }
  ]
};

export const pdModules: PdModule[] = [
  {
    week: 1,
    title: "Pengantar & Klasifikasi Persamaan Diferensial",
    subTitle: "Klasifikasi PDB/PDP, Masalah Nilai Awal (IVP), Dinamika Energi Rangkaian & Komputasi Berbasis Julia",
    category: "Fondasi PDB & Rangkaian",
    subCpmk: "Sub-CPMK 1: Mampu mengidentifikasi PDB/PDP, orde, derajat, linieritas, merumuskan IVP rangkaian RL, dan membuktikan kontinuitas energi medan magnet/listrik.",
    summary: "Memahami hakikat persamaan diferensial sebagai bahasa dinamika laju perubahan alam semesta, klasifikasi orde, linieritas, dan kontinuitas energi fisik induktor dan kapasitor.",
    theoryTopics: ["Klasifikasi PDB vs PDP", "Orde & Derajat PD", "Linieritas & Superposisi", "Masalah Nilai Awal (IVP)", "Kontinuitas Arus i_L & Tegangan v_C", "Model KVL Loop RL"],
    computationLab: "Julia (DifferentialEquations.jl): Validasi Transien RL Eksak vs Tsit5() & Visualisasi Dinamika Sistem",
    slidesPdf: "/pdf/ch1.pdf",
    videoFile: "/video/video_pd_minggu01.mp4",
    youtubeUrl: "https://youtu.be/Zq6IbzuVLBw",
    notesPdf: "/pdf/modul_1.pdf",
    worksheetPdf: "/pdf/worksheet1.pdf",
    solvedPdf: "/pdf/problem_set1.pdf",
    formulaLatex: "L \\frac{di(t)}{dt} + R i(t) = V_0 \\implies i(t) = \\frac{V_0}{R} \\left(1 - e^{-t/\\tau}\\right), \\quad \\tau = \\frac{L}{R}",
    bloomHighlights: {
      c1_c2: "C1: Definisi PDB vs PDP, Orde, Derajat. C2: Makna fisis kontinuitas energi.",
      c3_c4: "C3: Solusi analitis IVP. C4: Penurunan KVL hukum Faraday & arus perpindahan Maxwell.",
      c5_c6: "C5: Evaluasi non-linieritas induktor jenuh. C6: Skrip Julia pemodelan IVP & kurva daya."
    }
  },
  {
    week: 2,
    title: "PDB Orde 1: Separabel, Eksak & Faktor Integrasi",
    subTitle: "Metodologi Solusi Analitik PDB Orde 1, Uji Diferensial Eksak, Faktor Pengintegrasi & Rangkaian RC",
    category: "Fondasi PDB & Rangkaian",
    subCpmk: "Sub-CPMK 2: Mampu menyelesaikan PDB orde 1 menggunakan metode separabel, eksak, dan faktor integrasi untuk respons transien rangkaian RC.",
    summary: "Menguasai metode integrasi analitis PDB orde 1, pengujian syarat keeksakan Cauchy-Euler, dan teknik pengali faktor integrasi pada fenomena pengosongan kapasitor.",
    theoryTopics: ["Persamaan Separabel", "Persamaan Diferensial Eksak", "Uji Euler dM/dy = dN/dx", "Faktor Integrasi mu(x)", "Pengosongan Kapasitor RC", "Disipasi Kalor Joule"],
    computationLab: "Julia: Uji Keeksakan, Solusi Simbolik & Simulasi Transien RC",
    slidesPdf: "/pdf/ch2.pdf",
    videoFile: "/video/video_pd_minggu02.mp4",
    youtubeUrl: "https://youtu.be/5GQHKrvaSwg",
    notesPdf: "/pdf/modul_2.pdf",
    worksheetPdf: "/pdf/worksheet2.pdf",
    solvedPdf: "/pdf/problem_set2.pdf",
    formulaLatex: "M(x,y)dx + N(x,y)dy = 0, \\quad \\mu(x) = \\exp\\left( \\int \\frac{\\frac{\\partial M}{\\partial y} - \\frac{\\partial N}{\\partial x}}{N} dx \\right)",
    bloomHighlights: {
      c1_c2: "C1: Bentuk umum PDB orde 1. C2: Syarat kecukupan keeksakan integral.",
      c3_c4: "C3: Perhitungan faktor integrasi. C4: Analisis kesetimbangan energi kalor resistor.",
      c5_c6: "C5: Evaluasi domain validitas solusi. C6: Skrip Julia kurva integral keluarga solusi."
    }
  },
  {
    week: 3,
    title: "Aplikasi PDB Orde 1 dalam Rekayasa Elektro",
    subTitle: "Transien Pengisian/Pengosongan RC, RL, & Hukum Pendinginan Termal Newton Trafo Daya",
    category: "Aplikasi Transien",
    subCpmk: "Sub-CPMK 2: Mampu memodelkan dan menganalisis transien pengisian/pengosongan RC-RL serta manajemen termal transformator gardu induk.",
    summary: "Menerapkan PDB orde satu pada respon transien energi induktor dan kapasitor serta penurunan hukum pendinginan Newton untuk mitigasi panas isolasi transformator daya.",
    theoryTopics: ["Transien Pengisian RC", "Transien Pengisian RL", "Konstanta Waktu tau", "Hukum Pendinginan Newton", "Manajemen Termal Trafo", "Dinamika Suhu Belitan"],
    computationLab: "Pluto Notebook & Julia: Simulasi_Transien_RC_RL.jl",
    slidesPdf: "/pdf/ch3.pdf",
    videoFile: "/video/video_pd_minggu03.mp4",
    youtubeUrl: "https://youtu.be/_JZ7kBkgxlk",
    notesPdf: "/pdf/modul_3.pdf",
    worksheetPdf: "/pdf/worksheet3.pdf",
    solvedPdf: "/pdf/problem_set3.pdf",
    formulaLatex: "\\frac{dT(t)}{dt} = -k (T - T_{\\text{amb}}) + \\frac{P_{\\text{loss}}}{C_{\\text{th}}} \\implies T(t) = T_{\\text{amb}} + \\Delta T_{\\text{ss}} (1 - e^{-t/\\tau_{\\text{th}}})",
    bloomHighlights: {
      c1_c2: "C1: Definisi konstanta waktu tau = RC dan tau = L/R. C2: Interpretasi fisis pendinginan Newton.",
      c3_c4: "C3: Perhitungan arus transien. C4: Analisis batas pembebanan termal transformator PLN.",
      c5_c6: "C5: Evaluasi kapasitas pembebanan darurat. C6: Simulasi interaktif respon termal trafo."
    }
  },
  {
    week: 4,
    title: "PDB Linier Orde 2 Homogen Koefisien Konstan",
    subTitle: "Persamaan Karakteristik, Determinan Wronskian, Tiga Ragam Redaman & Tangki LC RF",
    category: "Sistem Orde 2 & Resonansi",
    subCpmk: "Sub-CPMK 3: Mampu menyelesaikan PDB linier orde 2 homogen, menguji kebebasan linier solusi (Wronskian), dan memodelkan osilasi alami tangki LC.",
    summary: "Mempelajari struktur PDB orde 2 homogen koefisien konstan, uji kebebasan linier Wronskian, penurunan tiga kasus akar karakteristik, dan pembuktian reduksi orde.",
    theoryTopics: ["Bentuk Standar PDB Orde 2", "Uji Wronskian W(y1,y2)", "Persamaan Karakteristik", "Kasus Overdamped (D>0)", "Kasus Critically Damped (D=0)", "Kasus Underdamped (D<0)", "Tangki Osilator LC RF"],
    computationLab: "Julia: Simulasi Tiga Ragam Redaman & Ruang Fasa Titik Fokus",
    slidesPdf: "/pdf/ch4.pdf",
    videoFile: "/video/video_pd_minggu04.mp4",
    youtubeUrl: "https://youtu.be/7GUGYVkbPbE",
    notesPdf: "/pdf/modul_4.pdf",
    worksheetPdf: "/pdf/worksheet4.pdf",
    solvedPdf: "/pdf/problem_set4.pdf",
    formulaLatex: "a y'' + b y' + c y = 0 \\implies r_{1,2} = -\\alpha \\pm \\sqrt{\\alpha^2 - \\omega_0^2}, \\quad W(y_1, y_2) = y_1 y_2' - y_2 y_1' \\neq 0",
    bloomHighlights: {
      c1_c2: "C1: Persamaan karakteristik kuadrat. C2: Makna fisis rasio redaman zeta.",
      c3_c4: "C3: Penyelesaian 3 kasus diskriminan. C4: Pembuktian suku x e^{rx} metode reduksi orde.",
      c5_c6: "C5: Evaluasi osilasi bebas tangki LC RF. C6: Skrip Julia trajektori ruang fasa."
    }
  },
  {
    week: 5,
    title: "PDB Linier Orde 2 Non-Homogen & RLC Seri",
    subTitle: "Metode Koefisien Tak Tentu, Respons Frekuensi Sinusoidal AC, Resonansi Tegangan & Fenomena Beat",
    category: "Sistem Orde 2 & Resonansi",
    subCpmk: "Sub-CPMK 3: Mampu menyelesaikan PDB orde 2 non-homogen dengan koefisien tak tentu dan menganalisis resonansi transien rangkaian RLC seri AC.",
    summary: "Menghitung solusi partikular PDB orde 2 akibat eksitasi luar, menganalisis respon transien dan mantap rangkaian RLC seri, fenomena resonansi tegangan, dan faktor kualitas Q.",
    theoryTopics: ["Metode Koefisien Tak Tentu", "Respon Total y = yh + yp", "Rangkaian RLC Seri AC", "Faktor Kualitas Q", "Resonansi Seri omega0", "Fenomena Beat (Layangan)"],
    computationLab: "Pluto Notebook & Julia: Simulasi_Transien_RLC.jl",
    slidesPdf: "/pdf/ch5.pdf",
    videoFile: "/video/video_pd_minggu05.mp4",
    youtubeUrl: "https://youtu.be/x15SuJBvZQE",
    notesPdf: "/pdf/modul_5.pdf",
    worksheetPdf: "/pdf/worksheet5.pdf",
    solvedPdf: "/pdf/problem_set5.pdf",
    formulaLatex: "L \\frac{d^2 i}{dt^2} + R \\frac{di}{dt} + \\frac{1}{C} i = \\omega V_m \\cos(\\omega t) \\implies i(t) = i_h(t) + I_m \\sin(\\omega t - \\phi)",
    bloomHighlights: {
      c1_c2: "C1: Tabel tebakan solusi partikular yp. C2: Konsep amplifikasi tegangan faktor Q.",
      c3_c4: "C3: Solusi lengkap respon transien RLC. C4: Analisis lonjakan tegangan overvoltage pada C.",
      c5_c6: "C5: Evaluasi fenomena resonansi sub-sinkron (SSR). C6: Simulasi interaktif kurva resonansi."
    }
  },
  {
    week: 6,
    title: "Transformasi Laplace Dasar & Teorema Pergeseran",
    subTitle: "Transformasi Domain Waktu ke Domain Kompleks s, Sifat Linieritas, Teorema Geser & Turunan",
    category: "Metode Laplace",
    subCpmk: "Sub-CPMK 4: Mampu menghitung transformasi Laplace fungsi elementer, menerapkan teorema pergeseran pertama, dan mentransformasikan turunan PDB.",
    summary: "Memetakan fungsi domain waktu ke domain frekuensi kompleks s, mempermudah penyelesaian PDB transien menjadi operasi aljabar linier yang efisien.",
    theoryTopics: ["Definisi Integral Laplace", "Wilayah Konvergensi (ROC)", "Fungsi Step Heaviside u(t)", "Fungsi Impuls Dirac delta(t)", "Teorema Pergeseran Pertama", "Transformasi Turunan L[y'] & L[y'']"],
    computationLab: "Julia: Pemetaan Kutub-Nol (Pole-Zero) & Transformasi Laplace",
    slidesPdf: "/pdf/ch6.pdf",
    videoFile: "/video/video_pd_minggu06.mp4",
    youtubeUrl: "https://youtu.be/iIYM-WRaTiU",
    notesPdf: "/pdf/modul_6.pdf",
    worksheetPdf: "/pdf/worksheet6.pdf",
    solvedPdf: "/pdf/problem_set6.pdf",
    formulaLatex: "\\mathcal{L}\\{f(t)\\} = F(s) = \\int_0^\\infty f(t) e^{-st} dt, \\quad \\mathcal{L}\\{f''(t)\\} = s^2 F(s) - s f(0) - f'(0)",
    bloomHighlights: {
      c1_c2: "C1: Pasangan baku transformasi Laplace. C2: Makna fisis variabel frekuensi kompleks s.",
      c3_c4: "C3: Transformasi fungsi tangga dan sinus. C4: Konversi PDB diferensial ke aljabar linier.",
      c5_c6: "C5: Evaluasi kestabilan dari lokasi kutub. C6: Skrip Julia plot bidang kompleks s."
    }
  },
  {
    week: 7,
    title: "Invers Transformasi Laplace & Rangkaian Domain s",
    subTitle: "Ekspansi Pecahan Parsial (Heaviside), Akar Riil & Kompleks, Impedansi Operasional s Rangkaian Elektrik",
    category: "Metode Laplace",
    subCpmk: "Sub-CPMK 4: Mampu menyelesaikan invers transformasi Laplace dan menentukan solusi transien lengkap rangkaian elektrik domain s.",
    summary: "Mengembalikan ekspresi domain s ke domain waktu menggunakan ekspansi pecahan parsial dan menyelesaikan rangkaian RLC menggunakan impedansi operasional sL dan 1/sC.",
    theoryTopics: ["Invers Laplace L^-1", "Dekomposisi Pecahan Parsial", "Metode Tutup Heaviside", "Impedansi Kompleks Z(s)", "Kapasitor 1/sC & Induktor sL", "Solusi IVP Orde 2 RLC"],
    computationLab: "Julia: Invers Laplace & Respon Impuls Sistem Kendali",
    slidesPdf: "/pdf/ch7.pdf",
    videoFile: "/video/video_pd_minggu07.mp4",
    youtubeUrl: "https://youtu.be/crWRyniSoi0",
    notesPdf: "/pdf/modul_7.pdf",
    worksheetPdf: "/pdf/worksheet7.pdf",
    solvedPdf: "/pdf/problem_set7.pdf",
    formulaLatex: "F(s) = \\frac{P(s)}{(s-p_1)(s-p_2)} = \\frac{A_1}{s-p_1} + \\frac{A_2}{s-p_2} \\implies f(t) = A_1 e^{p_1 t} + A_2 e^{p_2 t}",
    bloomHighlights: {
      c1_c2: "C1: Kategori faktor penyebut D(s). C2: Representasi sumber awal pada impedansi s.",
      c3_c4: "C3: Perhitungan koefisien Heaviside. C4: Analisis respon transien rangkaian tangga.",
      c5_c6: "C5: Evaluasi kestabilan BIBO sistem kendali. C6: Skrip Julia respon impuls & kestabilan domain s."
    }
  },
  {
    week: 8,
    title: "Pengantar PDP & Analisis Deret Fourier",
    subTitle: "Persamaan Diferensial Parsial dalam Fisika Teknik, Deret Fourier Trigonometrik, Simetri & Harmonisa Inverter",
    category: "PDP & Deret Fourier",
    subCpmk: "Sub-CPMK 5: Mampu mengklasifikasikan PDP dan menguraikan sinyal periodik non-sinusoidal (gelombang kotak inverter) ke dalam Deret Fourier.",
    summary: "Memasuki paruh kedua kuliah: pengenalan PDP spasial-temporal, penurunan deret Fourier trigonometrik, pemanfaatan simetri gelombang, dan analisis distorsi harmonisa THD.",
    theoryTopics: ["Klasifikasi PDP (Hiperbolik, Parabolik, Eliptik)", "Deret Fourier Trigonometrik", "Koefisien Euler a0, an, bn", "Simetri Genap/Ganjil/Half-Wave", "Harmonisa Inverter SPWM", "Total Harmonic Distortion (THD)"],
    computationLab: "Julia: Sintesis Fourier & Analisis Spektrum Harmonisa (FFT)",
    slidesPdf: "/pdf/ch9.pdf",
    videoFile: "/video/video_pd_minggu09.mp4",
    youtubeUrl: "https://youtu.be/VaRiwphPnaw",
    notesPdf: "/pdf/modul_9.pdf",
    worksheetPdf: "/pdf/worksheet9.pdf",
    solvedPdf: "/pdf/problem_set9.pdf",
    formulaLatex: "f(t) = a_0 + \\sum_{n=1}^\\infty \\left[ a_n \\cos\\left(\\frac{n\\pi t}{L}\\right) + b_n \\sin\\left(\\frac{n\\pi t}{L}\\right) \\right], \\quad b_n = \\frac{4 V_{\\text{dc}}}{n\\pi} \\text{ (ganjil)}",
    bloomHighlights: {
      c1_c2: "C1: Rumus integral koefisien Fourier. C2: Makna fisis spektrum frekuensi diskrit.",
      c3_c4: "C3: Perhitungan deret Fourier gelombang kotak. C4: Analisis THD tegangan inverter PLN.",
      c5_c6: "C5: Evaluasi efektivitas filter pasif LC. C6: Skrip Julia sintesis deret Fourier bertingkat."
    }
  },
  {
    week: 9,
    title: "Solusi PDP: Metode Pemisahan Variabel",
    subTitle: "Teknik Produk Fungsi u(x,t) = X(x)T(t), Masalah Nilai Batas Dirichlet-Neumann & Nilai Eigen",
    category: "PDP & Deret Fourier",
    subCpmk: "Sub-CPMK 5: Mampu menyelesaikan PDP linier menggunakan metode pemisahan variabel dan menentukan nilai eigen serta fungsi eigen spasial-temporal.",
    summary: "Menguraikan PDP multivariabel menjadi sistem PDB satu variabel independen, menentukan syarat batas fisik, serta menyusun solusi umum melalui superposisi Fourier.",
    theoryTopics: ["Asumsi Produk Solusi u(x,t) = X(x)T(t)", "Konstanta Pemisahan -k^2", "Syarat Batas Dirichlet & Neumann", "Fungsi Eigen Spasial sin(n pi x / L)", "Fungsi Waktu Eksponensial/Osilasi", "Superposisi Deret Fourier"],
    computationLab: "Julia: Animasi Konvergensi Solusi Spasial-Waktu PDP",
    slidesPdf: "/pdf/ch10.pdf",
    videoFile: "/video/video_pd_minggu10.mp4",
    youtubeUrl: "https://youtu.be/oEBvpt86fvI",
    notesPdf: "/pdf/modul_10.pdf",
    worksheetPdf: "/pdf/worksheet10.pdf",
    solvedPdf: "/pdf/problem_set10.pdf",
    formulaLatex: "\\frac{X''(x)}{X(x)} = \\frac{1}{c^2} \\frac{T''(t)}{T(t)} = -\\lambda \\implies X_n(x) = \\sin\\left(\\frac{n\\pi x}{L}\\right), \\quad \\lambda_n = \\left(\\frac{n\\pi}{L}\\right)^2",
    bloomHighlights: {
      c1_c2: "C1: Definisi syarat batas Dirichlet vs Neumann. C2: Makna konstanta pemisahan lambda.",
      c3_c4: "C3: Penurunan nilai eigen spasial. C4: Superposisi suku tak terhingga kondisi awal.",
      c5_c6: "C5: Evaluasi ortogonalitas fungsi sinus. C6: Visualisasi profil spasial gelombang berdiri."
    }
  },
  {
    week: 10,
    title: "Persamaan Gelombang 1D & Telegrafer Saluran Transmisi",
    subTitle: "Persamaan Telegrafer Lossless, Solusi d'Alembert Gelombang Berjalan, Kecepatan Fasa & Refleksi",
    category: "Medan EM & Gelombang",
    subCpmk: "Sub-CPMK 6: Mampu menurunkan persamaan gelombang 1D dari hukum saluran transmisi, menganalisis solusi d'Alembert, dan memodelkan pantulan gelombang.",
    summary: "Menghubungkan teori rangkaian terdistribusi dengan perambatan gelombang tegangan dan arus pada kawat transmisi daya, kecepatan rambat, dan efek refleksi surja petir.",
    theoryTopics: ["Persamaan Telegrafer Lossless", "Kecepatan Rambat v = 1/sqrt(LC)", "Impedansi Karakteristik Z0", "Solusi d'Alembert f(x-vt) + g(x+vt)", "Koefisien Refleksi Beban Gamma", "Gelombang Berdiri (VSWR)"],
    computationLab: "Pluto Notebook & Julia: Simulasi_Gelombang_1D.jl",
    slidesPdf: "/pdf/ch11.pdf",
    videoFile: "/video/video_pd_minggu11.mp4",
    youtubeUrl: "https://youtu.be/RxoN7UaK3OI",
    notesPdf: "/pdf/modul_11.pdf",
    worksheetPdf: "/pdf/worksheet11.pdf",
    solvedPdf: "/pdf/problem_set11.pdf",
    formulaLatex: "\\frac{\\partial^2 v}{\\partial x^2} = L C \\frac{\\partial^2 v}{\\partial t^2} = \\frac{1}{v_p^2} \\frac{\\partial^2 v}{\\partial t^2}, \\quad Z_0 = \\sqrt{\\frac{L}{C}}, \\quad \\Gamma_L = \\frac{Z_L - Z_0}{Z_L + Z_0}",
    bloomHighlights: {
      c1_c2: "C1: Bentuk kanonik persamaan gelombang 1D. C2: Makna fisis impedansi karakteristik Z0.",
      c3_c4: "C3: Perhitungan tegangan pantul. C4: Penurunan persamaan telegrafer dari KVL/KCL terdistribusi.",
      c5_c6: "C5: Evaluasi tegangan lebih surja petir (switching surge). C6: Simulasi FDTD gelombang berjalan 1D."
    }
  },
  {
    week: 11,
    title: "Persamaan Panas 1D & Manajemen Termal Konduktor Daya",
    subTitle: "Difusi Termal pada Inti Konduktor SUTT & Kabel Bawah Tanah, Konduktivitas Kalor & Batas Ampacity",
    category: "Aplikasi Transien",
    subCpmk: "Sub-CPMK 6: Mampu menyelesaikan persamaan panas 1D parabolik untuk memodelkan distribusi suhu konduktor daya saat dialiri arus beban lebih.",
    summary: "Menganalisis difusi panas pada konduktor saluran udara tegangan tinggi dan kabel tanah akibat rugi-rugi tembaga Joule untuk menentukan kapasitas hantar arus aman (Ampacity).",
    theoryTopics: ["Persamaan Difusi Panas Fourier", "Difusivitas Termal alpha = k/(rho cp)", "Syarat Batas Konduksi & Konveksi", "Peluruhan Eksponensial Transien", "Distribusi Suhu Keadaan Mantap", "Batas Kemampuan Hantar Arus (Ampacity)"],
    computationLab: "Pluto Notebook & Julia: Simulasi_Persamaan_Panas_1D.jl",
    slidesPdf: "/pdf/ch12.pdf",
    videoFile: "/video/video_pd_minggu12.mp4",
    youtubeUrl: "https://youtu.be/piBpNjXaKpQ",
    notesPdf: "/pdf/modul_12.pdf",
    worksheetPdf: "/pdf/worksheet12.pdf",
    solvedPdf: "/pdf/problem_set12.pdf",
    formulaLatex: "\\frac{\\partial T(x,t)}{\\partial t} = \\alpha \\frac{\\partial^2 T(x,t)}{\\partial x^2} + \\frac{q_{\\text{joule}}}{\\rho c_p}, \\quad T(x,t) = \\sum_{n=1}^\\infty B_n \\sin\\left(\\frac{n\\pi x}{L}\\right) e^{-\\alpha \\left(\\frac{n\\pi}{L}\\right)^2 t}",
    bloomHighlights: {
      c1_c2: "C1: Karakteristik persamaan parabolik. C2: Konsep waktu relaksasi termal konduktor.",
      c3_c4: "C3: Solusi distribusi suhu kabel. C4: Analisis pemanasan titik sambungan (hot spot) gardu induk.",
      c5_c6: "C5: Evaluasi penuaan isolasi termal trafo (Arrhenius). C6: Simulasi numerik FTCS difusi termal."
    }
  },
  {
    week: 12,
    title: "Persamaan Laplace 2D & Potensial Elektrostatik",
    subTitle: "Dari Hukum Gauss ke Persamaan Laplace & Poisson, Teorema Keunikan, Relaksasi Gauss-Seidel",
    category: "Medan EM & Gelombang",
    subCpmk: "Sub-CPMK 6: Mampu menurunkan persamaan Laplace 2D dari Hukum Gauss elektrostatik, menyelesaikan secara analitik, dan memetakan kontur potensial.",
    summary: "Menurunkan persamaan Laplace eliptik untuk distribusi potensial elektrostatik bebas muatan, teorema nilai rata-rata, dan pemecahan numerik menggunakan beda hingga relaksasi.",
    theoryTopics: ["Hukum Gauss & Medan Konservatif", "Persamaan Poisson & Laplace nabla^2 V = 0", "Teorema Keunikan Elektrostatik", "Syarat Batas Pelat Konduktor", "Fungsi Harmonik & Nilai Rata-Rata", "Relaksasi Beda Hingga Gauss-Seidel"],
    computationLab: "Pluto Notebook & Julia: Simulasi_Potensial_Laplace_2D.jl",
    slidesPdf: "/pdf/ch13.pdf",
    videoFile: "/video/video_pd_minggu13.mp4",
    youtubeUrl: "https://youtu.be/JgFsCfTgg4U",
    notesPdf: "/pdf/modul_13.pdf",
    worksheetPdf: "/pdf/worksheet13.pdf",
    solvedPdf: "/pdf/problem_set13.pdf",
    formulaLatex: "\\nabla^2 V = \\frac{\\partial^2 V}{\\partial x^2} + \\frac{\\partial^2 V}{\\partial y^2} = 0 \\implies V(x,y) = \\sum_{n=1,3,\\dots}^\\infty \\frac{4 V_0}{n\\pi \\sinh(n\\pi)} \\sin\\left(\\frac{n\\pi x}{a}\\right) \\sinh\\left(\\frac{n\\pi y}{a}\\right)",
    bloomHighlights: {
      c1_c2: "C1: Bentuk operator Laplacian nabla^2. C2: Teorema nilai rata-rata fungsi harmonik.",
      c3_c4: "C3: Solusi deret Fourier dua dimensi. C4: Analisis konsentrasi stres medan listrik sudut tajam.",
      c5_c6: "C5: Evaluasi breakdown isolasi dielektrik gas SF6. C6: Simulasi numerik kontur equipotensial."
    }
  },
  {
    week: 13,
    title: "Fungsi Khusus: Persamaan Bessel & Efek Kulit (*Skin Effect*)",
    subTitle: "Laplacian Koordinat Silinder, Fungsi Bessel Jenis 1 & 2, Rapat Arus Frekuensi Tinggi Konduktor ACSR",
    category: "Medan EM & Gelombang",
    subCpmk: "Sub-CPMK 6: Mampu menyelesaikan persamaan Bessel pada koordinat silinder dan menganalisis fenomena efek kulit (skin effect) pada konduktor kawat bundar.",
    summary: "Memperkenalkan koordinat silinder pada kabel konduktor bundar, solusi fungsi Bessel J0 dan Y0, serta perhitungan kedalaman penetrasi arus AC frekuensi tinggi.",
    theoryTopics: ["Laplacian Koordinat Silinder (r, theta, z)", "Persamaan Diferensial Bessel", "Fungsi Bessel Jenis 1 J0(x) & Jenis 2 Y0(x)", "Kedalaman Penetrasi Kulit delta", "Distribusi Rapat Arus Radial J(r)", "Resistansi AC vs Resistansi DC Kawat"],
    computationLab: "Julia (SpecialFunctions.jl): Evaluasi Fungsi Bessel & Efek Kulit",
    slidesPdf: "/pdf/ch14.pdf",
    videoFile: "/video/video_pd_minggu14.mp4",
    youtubeUrl: "https://youtu.be/VidTzwMhRDo",
    notesPdf: "/pdf/modul_14.pdf",
    worksheetPdf: "/pdf/worksheet14.pdf",
    solvedPdf: "/pdf/problem_set14.pdf",
    formulaLatex: "r^2 \\frac{d^2 R}{dr^2} + r \\frac{dR}{dr} + (k^2 r^2 - n^2) R = 0, \\quad \\delta = \\sqrt{\\frac{2}{\\omega \\mu \\sigma}} = \\sqrt{\\frac{1}{\\pi f \\mu \\sigma}}",
    bloomHighlights: {
      c1_c2: "C1: Bentuk umum PDB Bessel. C2: Sifat fungsi Bessel berosilasi dengan amplitudo meluruh.",
      c3_c4: "C3: Perhitungan kedalaman kulit tembaga & aluminium pada 50 Hz vs 100 kHz. C4: Analisis desain kawat ACSR.",
      c5_c6: "C5: Evaluasi rasio Rac/Rdc pada saluran transmisi 150/500 kV. C6: Skrip Julia plot rapat arus radial J(r)."
    }
  },
  {
    week: 14,
    title: "Sintesis PDP: 4 Persamaan Maxwell & Team-Based Project",
    subTitle: "Empat Persamaan Maxwell Bentuk Diferensial, Persamaan Gelombang Elektromagnetik 3D & Panduan Proyek",
    category: "Medan EM & Gelombang",
    subCpmk: "Sub-CPMK 6: Mampu mensintesiskan konsep PDP ke dalam 4 Persamaan Maxwell diferensial dan merancang solusi numerik/analitik pada Team-Based Project.",
    summary: "Puncak kurikulum matematika teknik elektro: integrasi seluruh konsep diferensial ke dalam mahakarya James Clerk Maxwell, pembuktian kecepatan cahaya, dan panduan proyek akhir.",
    theoryTopics: ["Hukum Gauss Elektrostatik (div D = rho)", "Hukum Gauss Magnetostatik (div B = 0)", "Hukum Induksi Faraday (curl E = -dB/dt)", "Hukum Ampere-Maxwell (curl H = J + dD/dt)", "Penurunan Persamaan Gelombang 3D", "Rubrik Penilaian Team-Based Project"],
    computationLab: "Julia & Pluto: Pemodelan Gelombang EM Maxwell & Presentasi Akhir",
    slidesPdf: "/pdf/ch15.pdf",
    videoFile: "/video/video_pd_minggu15.mp4",
    youtubeUrl: "https://youtu.be/J4XziBcVtfk",
    notesPdf: "/pdf/modul_15.pdf",
    worksheetPdf: "/pdf/worksheet15.pdf",
    solvedPdf: "/pdf/problem_set15.pdf",
    formulaLatex: "\\nabla \\times (\\nabla \\times \\vec{E}) = -\\mu \\varepsilon \\frac{\\partial^2 \\vec{E}}{\\partial t^2} \\implies \\nabla^2 \\vec{E} - \\mu \\varepsilon \\frac{\\partial^2 \\vec{E}}{\\partial t^2} = 0, \\quad c = \\frac{1}{\\sqrt{\\mu_0 \\varepsilon_0}}",
    bloomHighlights: {
      c1_c2: "C1: Bentuk diferensial 4 Persamaan Maxwell. C2: Makna fisis arus perpindahan displacement current.",
      c3_c4: "C3: Penurunan kecepatan cahaya c dari konstanta vakum. C4: Analisis gelombang datar TEM.",
      c5_c6: "C5: Evaluasi rubrik penilaian proyek OBE. C6: Presentasi Team-Based Project berbasis simulasi terbuka."
    }
  }
];
