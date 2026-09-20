#!/usr/bin/env python3
"""
build_video_w02_v2.py — Generator Video Minggu 02 Versi 2.0 (Teknik Elektro UNIB)
Dosen Pengampu: Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.

Fitur Kualitas Unggulan v2.0:
  [1] Visual: Ekstraksi 300 DPI dari salindia resmi Beamer Madrid 16:9 (ch2.pdf)
  [2] Audio: Microsoft Edge TTS 'id-ID-ArdiNeural' disintesis ke Stereo AAC 192 kbps (44.1 kHz)
  [3] Pedagogis: 15 Salindia lengkap mencakup Sub-CPMK OBE C1–C6, Peta Konsep TikZ, Intuisi Fisika Medan Konservatif,
      Derivasi Analitik RC, Paradoks Efisiensi 50%, RC Snubber IGBT, Demo Julia DifferentialEquations.jl,
      serta Kuis Interaktif dengan Jeda Berpikir 8 Detik Terprogram.
  [4] Encoding Video: 1080p Full HD (1920x1080), H.264 CRF 18, preset faster.
  [5] Metadata YouTube: Naskah otomatis lengkap dengan timestamps dan chapter breakdown (video_script_pd_w02_v2.md).
  [6] Integrasi Portal: Tersinkronisasi otomatis ke portal/public/video/video_pd_minggu02.mp4.
"""

import os
import sys
import time
import shutil
import asyncio
import subprocess
import edge_tts

PROJ_DIR = os.path.dirname(os.path.abspath(__file__))
SCRATCH_DIR = os.path.join(PROJ_DIR, "scratch", "w02_v2")
PORTAL_DIR = os.path.join(PROJ_DIR, "portal", "public", "video")
PDF_SLIDES = os.path.join(PROJ_DIR, "ch2.pdf")
FINAL_ROOT_VIDEO = os.path.join(PROJ_DIR, "video_pd_minggu02.mp4")
FINAL_PORTAL_VIDEO = os.path.join(PORTAL_DIR, "video_pd_minggu02.mp4")
SCRIPT_MD = os.path.join(PROJ_DIR, "video_script_pd_w02_v2.md")
QUIZ_PAUSE_MP3 = os.path.join(PROJ_DIR, "scratch", "quiz_pause_8s.mp3")

VOICE = "id-ID-ArdiNeural"

os.makedirs(SCRATCH_DIR, exist_ok=True)
os.makedirs(PORTAL_DIR, exist_ok=True)

# 15 Salindia Narasi Resmi Minggu 02
SLIDES_DATA = [
    {
        "num": 1,
        "title": "Judul & Pembukaan Kuliah Minggu 02",
        "chapter": "01. Pembukaan Perkuliahan Minggu 02",
        "quiz": False,
        "text": (
            "Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, "
            "selamat datang kembali dalam perkuliahan daring Persamaan Diferensial semester genap 2026. "
            "Pada pertemuan minggu kedua ini, kita akan membedah secara tuntas tiga metodologi analitik fundamental "
            "untuk menyelesaikan Persamaan Diferensial Biasa Orde Satu, yaitu: Metode Separabel atau pemisahan variabel, "
            "Persamaan Eksak berbasis medan vektor konservatif, serta teknik penanganan persamaan non-eksak melalui "
            "Faktor Pengintegrasi. Selanjutnya, kita akan menerapkan seluruh perangkat matematika ini untuk memodelkan "
            "fenomena transien pada sirkuit resistor kapasitor atau sirkuit RC, serta proteksi sakelar daya semikonduktor "
            "di industri tenaga listrik. Perkuliahan ini diampu bersama saya, Insinyur Novalio Daratha, dan Bapak Muhammad Arfan."
        )
    },
    {
        "num": 2,
        "title": "Capaian Pembelajaran (Sub-CPMK 2) & Taksonomi Bloom",
        "chapter": "02. Sub-CPMK OBE & Taksonomi Bloom",
        "quiz": False,
        "text": (
            "Mari kita cermati Capaian Pembelajaran Mata Kuliah atau Sub-CPMK Minggu kedua yang terstruktur "
            "dalam Taksonomi Bloom. Pada ranah kognitif C1 Mengingat, mahasiswa mampu menyatakan bentuk kanonik "
            "diferensial M d x ditambah N d y sama dengan nol dan kriteria ke-eksak-an Euler-Clairaut. "
            "Pada C2 Memahami, mahasiswa mampu mengaitkan persamaan eksak dengan konsep fisika medan konservatif skalar "
            "di mana curl medan listrik bernilai nol. Pada C3 Menerapkan, mahasiswa mampu menghitung faktor pengintegrasi "
            "mu x atau mu y pada PDB non-eksak secara eksak. Pada C4 Menganalisis, mahasiswa mampu memodelkan dinamika "
            "pengisian dan pengosongan kapasitor dengan konstanta waktu tau sama dengan R dikali C. "
            "Pada C5 Mengevaluasi, mahasiswa mampu membuktikan paradoks efisiensi lima puluh persen disipasi kalor pada sirkuit RC. "
            "Dan pada C6 Komputasi, mahasiswa mampu menyusun skrip simulasi numerik berbasis bahasa Julia dengan solver adaptif Tsit5."
        )
    },
    {
        "num": 3,
        "title": "Peta Konsep: Klasifikasi Metodologi Solusi PDB Orde 1",
        "chapter": "03. Peta Konsep Metodologi PDB Orde 1",
        "quiz": False,
        "text": (
            "Berikut adalah peta konsep alur pengambilan keputusan dalam menyelesaikan PDB orde satu dalam bentuk diferensial "
            "M d x ditambah N d y sama dengan nol. Langkah pertama, kita uji apakah persamaan dapat dipisahkan menjadi "
            "g y d y sama dengan h x d x. Jika ya, kita selesaikan langsung menggunakan Metode Separabel melalui integrasi kedua ruas. "
            "Jika tidak, langkah kedua adalah melakukan uji ke-eksak-an Euler-Clairaut, yaitu memeriksa apakah turunan parsial M "
            "terhadap y sama dengan turunan parsial N terhadap x. Jika kondisi ini terpenuhi, persamaan adalah PDB Eksak, "
            "dan kita dapat merekonstruksi fungsi potensial F x koma y sama dengan C. Namun jika tidak eksak, langkah ketiga "
            "adalah mencari Faktor Pengintegrasi mu agar persamaan tertransformasi menjadi eksak. Diagram alir ini menjadi panduan "
            "sistematis bagi Anda dalam menghadapi berbagai persoalan matematika rekayasa."
        )
    },
    {
        "num": 4,
        "title": "Metode 1: Persamaan Separabel (Pemisahan Variabel)",
        "chapter": "04. Metode 1: Persamaan Separabel",
        "quiz": False,
        "text": (
            "Metode pertama yang paling mendasar adalah Persamaan Separabel. PDB orde satu dikatakan separabel jika fungsi ruas kanan "
            "dapat difaktorkan secara murni menjadi perkalian fungsi variabel bebas g x dengan fungsi variabel terikat h y. "
            "Prosedur penyelesaiannya terdiri dari empat langkah eksplisit: Langkah satu, kelompokkan seluruh suku yang memuat variabel "
            "terikat y bersama diferensial d y di ruas kiri. Langkah dua, kumpulkan seluruh suku variabel bebas x bersama diferensial "
            "d x di ruas kanan. Langkah tiga, lakukan integrasi secara langsung pada kedua ruas persamaan: integral satu per h y d y "
            "sama dengan integral g x d x ditambah konstanta sembarang C. Dan langkah empat, selesaikan persamaan aljabar tersebut "
            "untuk menyatakan y x secara eksplisit apabila memungkinkan."
        )
    },
    {
        "num": 5,
        "title": "Metode 2: Persamaan Diferensial Eksak",
        "chapter": "05. Metode 2: Persamaan Diferensial Eksak",
        "quiz": False,
        "text": (
            "Metode kedua adalah Persamaan Diferensial Eksak. Suatu bentuk diferensial M x koma y d x ditambah N x koma y d y "
            "sama dengan nol dikatakan Eksak apabila ruas kirinya merupakan diferensial total d F dari suatu fungsi potensial skalar F x koma y. "
            "Karena d F sama dengan nol, maka solusi umum implisitnya adalah F x koma y sama dengan konstanta C. "
            "Berdasarkan Teorema Ke-eksak-an Euler-Clairaut, jika fungsi M dan N kontinu serta memiliki turunan parsial pertama yang kontinu, "
            "maka syarat perlu dan cukup agar persamaan tersebut eksak adalah turunan parsial M terhadap y harus persis sama "
            "dengan turunan parsial N terhadap x. Kriteria turunan silang ini adalah kunci utama untuk memverifikasi apakah suatu PDB "
            "dapat diselesaikan langsung dengan metode potensial."
        )
    },
    {
        "num": 6,
        "title": "Intuisi Fisika: Medan Konservatif & Garis Ekuipotensial",
        "chapter": "06. Intuisi Fisika: Medan Konservatif",
        "quiz": False,
        "text": (
            "Kini kita masuki Pilar pertama, yaitu intuisi fisika rekayasa yang menjembatani matematika dengan Medan Elektromagnetika. "
            "Bentuk diferensial M d x ditambah N d y sama dengan nol secara fisis merepresentasikan perkalian titik antara vektor medan "
            "gaya elektrostatik E sama dengan M i topi ditambah N j topi dengan elemen lintasan perpindahan d r sama dengan d x i topi "
            "ditambah d y j topi. Syarat ke-eksak-an parsial M per parsial y sama dengan parsial N per parsial x tidak lain adalah syarat "
            "bahwa curl dari medan listrik E bernilai nol, yang mencirikan medan vektor konservatif bebas pusaran. "
            "Akibatnya, kurva solusi umum F x koma y sama dengan C secara fisik merepresentasikan Garis Ekuipotensial elektrostatik, "
            "di mana vektor medan listrik selalu tegak lurus terhadap garis ekuipotensial tersebut di setiap titik."
        )
    },
    {
        "num": 7,
        "title": "Metode 3: Faktor Pengintegrasi (Integrating Factor)",
        "chapter": "07. Metode 3: Faktor Pengintegrasi",
        "quiz": False,
        "text": (
            "Bagaimana jika persamaan diferensial M d x ditambah N d y sama dengan nol ternyata tidak eksak karena turunan parsial silangnya berbeda? "
            "Kita dapat menerapkan Metode ketiga, yaitu mengalikan seluruh persamaan dengan suatu fungsi pengali mu x koma y yang dinamakan "
            "Faktor Pengintegrasi, sehingga persamaan baru mu M d x ditambah mu N d y sama dengan nol menjadi eksak. "
            "Terdapat dua kasus standar: Kasus satu, jika selisih parsial M per parsial y dikurang parsial N per parsial x dibagi N "
            "menghasilkan fungsi murni variabel x yaitu f x, maka faktor integrasinya adalah mu x sama dengan eksponensial dari integral f x d x. "
            "Kasus dua, jika selisih parsial N per parsial x dikurang parsial M per parsial y dibagi M menghasilkan fungsi murni y yaitu g y, "
            "maka faktor pengintegrasinya adalah mu y sama dengan eksponensial dari integral g y d y."
        )
    },
    {
        "num": 8,
        "title": "Pemodelan Fisis: Sirkuit Pengisian Kapasitor RC",
        "chapter": "08. Pemodelan Fisis: Sirkuit RC",
        "quiz": False,
        "text": (
            "Sekarang kita masuki Pilar keempat, yaitu aplikasi nyata pada rangkaian listrik. Perhatikan sirkuit pengisian kapasitor RC "
            "seri yang terhubung ke sumber tegangan konstan V nol saat sakelar ditutup pada t sama dengan nol. "
            "Berdasarkan Hukum Tegangan Kirchhoff atau KVL, jumlah aljabar tegangan pada satu loop tertutup adalah nol, "
            "sehingga tegangan resistor v R ditambah tegangan kapasitor v C sama dengan V nol. Arus pengisian kapasitor diatur oleh laju "
            "perubahan muatan listrik, yaitu i t sama dengan C dikali d v C per d t. Dengan mensubstitusikan hubungan tegangan resistor "
            "v R sama dengan R dikali i, kita peroleh model kanonik PDB orde satu: R dikali C dikali d v C per d t ditambah v C sama dengan V nol. "
            "Di sini kita definisikan konstanta waktu kapasitif tau sama dengan R dikali C dalam satuan detik."
        )
    },
    {
        "num": 9,
        "title": "Derivasi Analitik Solusi Khusus Tegangan & Arus RC",
        "chapter": "09. Derivasi Analitik Solusi RC",
        "quiz": False,
        "text": (
            "Mari kita turunkan solusi khusus sirkuit RC secara analitik langkah demi langkah menggunakan metode separabel. "
            "Pisahkan variabel tegangan dan waktu: d v C dibagi kurung V nol dikurang v C sama dengan satu per R C d t. "
            "Lakukan integrasi pada kedua ruas, menghasilkan minus logaritma natural harga mutlak V nol dikurang v C sama dengan "
            "t per R C ditambah konstanta C satu. Dengan mengeksponensialkan kedua ruas dan menerapkan syarat awal tegangan mula-mula kapasitor "
            "kosong yaitu v C nol sama dengan nol, kita peroleh konstanta A sama dengan V nol. "
            "Solusi khusus tegangan kapasitor adalah v C t sama dengan V nol dikali kurung satu dikurang e pangkat minus t per tau. "
            "Sedangkan arus pengisiannya adalah turunan muatan yaitu i t sama dengan V nol per R dikali e pangkat minus t per tau, "
            "yang melompat seketika ke nilai awal pada t nol positif lalu meluruh secara eksponensial menuju nol."
        )
    },
    {
        "num": 10,
        "title": "Dinamika Transien & Paradoks Efisiensi Disipasi 50%",
        "chapter": "10. Dinamika Transien & Paradoks Energi 50%",
        "quiz": False,
        "text": (
            "Perhatikan analisis neraca energi pengisian kapasitor yang memunculkan salah satu paradoks paling terkenal dalam teknik elektro. "
            "Total energi yang dipasok oleh sumber tegangan DC dari t sama dengan nol hingga kondisi tunak adalah C dikali V nol kuadrat. "
            "Namun, energi yang tersimpan di dalam medan elektrostatik kapasitor hanyalah setengah C dikali V nol kuadrat. "
            "Ke mana perginya separuh energi lainnya? Separuh energi tersebut terdisipasi menjadi kalor pada resistor melalui efek Joule, "
            "yaitu integral arus kuadrat dikalikan R terhadap waktu. Yang sangat menakjubkan, efisiensi pengisian kapasitor ini selalu "
            "tepat lima puluh persen, sama sekali tidak bergantung pada besar resistansi R. Bahkan jika nilai R mendekati nol sekalipun, "
            "energi tetap akan hilang sebesar lima puluh persen melalui radiasi gelombang elektromagnetik."
        )
    },
    {
        "num": 11,
        "title": "Studi Kasus Rekayasa: Proteksi Sakelar IGBT (RC Snubber)",
        "chapter": "11. Studi Kasus Industri: RC Snubber IGBT",
        "quiz": False,
        "text": (
            "Di industri tenaga listrik dan elektronika daya, prinsip PDB transien RC diterapkan langsung dalam perancangan rangkaian proteksi "
            "atau RC snubber. Ketika sakelar semikonduktor daya seperti IGBT atau MOSFET memutus arus beban yang bersifat induktif, "
            "timbul fenomena tegangan transien ekstrem di mana laju lonjakan tegangan d v per d t mendekati tak hingga. "
            "Lonjakan d v per d t yang melampaui batas ketahanan semikonduktor dapat merusak struktur dielektrik internal komponen. "
            "Berdasarkan standar industri IEEE dan IEC, kapasitor snubber C s dipasang secara paralel untuk menyerap arus transien dan menahan "
            "laju kenaikan tegangan sesaat pada t sama dengan nol positif menjadi arus puncak dibagi C s, sehingga sakelar semikonduktor terlindungi secara aman."
        )
    },
    {
        "num": 12,
        "title": "Contoh Soal Terhitung (Worked Example): Bank Kapasitor",
        "chapter": "12. Contoh Soal Terhitung Bank Kapasitor",
        "quiz": False,
        "text": (
            "Mari kita cermati contoh soal terhitung pada gardu induk kelistrikan. Suatu bank kapasitor dua ratus mikrofarad dihubungkan "
            "ke bus tegangan dua ratus lima puluh volt melalui resistor pembatas lima puluh ohm, dengan tegangan sisa awal kapasitor sebesar lima puluh volt. "
            "Langkah satu: kita hitung konstanta waktu transien tau sama dengan R dikali C, yaitu lima puluh ohm dikalikan dua ratus mikrofarad, "
            "menghasilkan sepuluh milidetik. Langkah dua: masukkan kondisi awal ke solusi analitik, diperoleh persamaan tegangan v C t sama dengan "
            "dua ratus lima puluh dikurang dua ratus dikali e pangkat minus seratus t volt. Langkah tiga: arus pemula transien pada t sama dengan nol positif "
            "adalah dua ratus lima puluh dikurang lima puluh dibagi lima puluh, yaitu empat ampere. Pada t sama dengan satu tau atau sepuluh milidetik, "
            "tegangan mencapai seratus tujuh puluh enam koma empat volt, dan pada lima tau atau lima puluh milidetik, tegangan telah mencapai "
            "dua ratus empat puluh delapan koma tujuh volt atau di atas sembilan puluh sembilan persen dari nilai tunaknya."
        )
    },
    {
        "num": 13,
        "title": "Praktikum Komputasi Julia: Transien Sirkuit RC",
        "chapter": "13. Praktikum Komputasi Julia Tsit5",
        "quiz": False,
        "text": (
            "Sekarang kita terapkan Pilar ketiga, yaitu komputasi ilmiah terbuka berbasis Julia. Pada slide ini ditampilkan skrip ringkas "
            "menggunakan paket DifferentialEquations dot j l dan Plots dot j l. Kita definisikan parameter rangkaian V nol dua ratus lima puluh volt, "
            "R lima puluh ohm, dan C dua ratus mikrofarad. Model PDB dinyatakan dalam fungsi f r c kurung v koma p koma t sama dengan kurung V nol "
            "dikurang v dibagi R dikali C. Masalah nilai awal dikemas ke dalam objek O D E Problem dengan kondisi awal lima puluh volt pada rentang waktu "
            "simulasi nol hingga enam puluh milidetik, lalu diselesaikan menggunakan solver numerik adaptif Tsit lima. Grafik di sebelah kanan "
            "membuktikan bahwa kurva komputasi numerik Julia berwarna biru berimpit secara sempurna dengan solusi analitis garis putus-putus merah, "
            "memverifikasi ketepatan analisis matematis kita."
        )
    },
    {
        "num": 14,
        "title": "Kuis Konseptual Interaktif & Evaluasi Bloom (C1--C6)",
        "chapter": "14. Kuis Interaktif & Evaluasi Bloom",
        "quiz": True,
        "text_part1": (
            "Saatnya kuis interaktif untuk menguji pemahaman konsep fisika Anda. Tinjau kasus rekayasa berikut: "
            "Suatu kapasitor C diisi dari kondisi awal nol volt hingga tegangan V nol melalui resistor R. "
            "Jika nilai resistansi R diperkecil menjadi setengahnya, bagaimanakah energi total yang terdisipasi pada resistor E R? "
            "Pilihan A: Menjadi setengahnya karena arus lebih cepat berhenti. "
            "Pilihan B: Menjadi dua kali lipat karena arus awal lebih besar. "
            "Pilihan C: Tetap sama, yaitu setengah C V nol kuadrat, tidak bergantung pada nilai R. "
            "Pilihan D: Menjadi nol karena resistansi mendekati konduktor ideal. "
            "Silakan analisis dan tentukan jawaban terbaik Anda dalam delapan detik ke depan."
        ),
        "text_part2": (
            "Waktu habis. Jawaban yang tepat adalah C: Tetap sama, yaitu setengah C V nol kuadrat! "
            "Sebagaimana telah kita buktikan pada neraca energi, efisiensi pengisian kapasitor selalu tepat lima puluh persen "
            "dan sepenuhnya independen dari nilai resistansi R. "
            "Pada kolom sebelah kanan, Anda juga ditantang untuk membuktikan daya disipasi puncak V nol kuadrat per R pada level C4, "
            "mengevaluasi efisiensi lima puluh persen pada level C5, serta merancang parameter snubber R s dan C s pada level C6 sebagai tugas mandiri."
        )
    },
    {
        "num": 15,
        "title": "Rangkuman Inti Perkuliahan & Referensi",
        "chapter": "15. Rangkuman Perkuliahan & Penutup",
        "quiz": False,
        "text": (
            "Sebagai rangkuman perkuliahan minggu kedua kita: Pertama, PDB orde satu diselesaikan secara sistematis melalui metode separabel, "
            "uji ke-eksak-an Euler-Clairaut, atau bantuan faktor pengintegrasi. Kedua, solusi persamaan eksak merepresentasikan garis ekuipotensial "
            "dari medan vektor konservatif bebas pusaran. Ketiga, dinamika transien sirkuit RC dicirikan oleh konstanta waktu tau sama dengan R C, "
            "dengan hukum kekekalan energi yang menetapkan bahwa tepat separuh energi sumber terdisipasi menjadi kalor. "
            "Untuk memperdalam pemahaman, silakan pelajari buku acuan Kreyszig edisi sepuluh dan William Hayt, serta unduh modul ajar, "
            "lembar kerja, dan problem set minggu kedua di portal resmi ndaratha dot my dot id. "
            "Pada minggu ketiga, kita akan memperluas pembahasan ke analisis transien rangkaian induktif RL dan rangkaian terkopel. "
            "Saya, Insinyur Novalio Daratha bersama Bapak Muhammad Arfan, mengucapkan terima kasih atas fokus dan dedikasi belajar Anda. "
            "Wassalamu'alaikum warahmatullahi wabarakatuh."
        )
    }
]

def run_cmd(cmd, cwd=None):
    res = subprocess.run(cmd, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"[CMD ERROR] {cmd}\n{res.stderr}")
        raise RuntimeError(res.stderr)
    return res.stdout

async def synth_tts(text, outfile):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(outfile)

def get_duration(audio_file):
    out = run_cmd(f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{audio_file}"')
    return float(out.strip())

def main():
    print("=" * 65)
    print(" MEMBANGUN VIDEO MINGGU 02 v2.0 (Teknik Elektro UNIB)")
    print(" Model: 4-Pilar Pedagogis OBE | Stereo AAC 192k | 1080p Full HD")
    print("=" * 65)
    t0 = time.time()

    # Step 1: Ekstraksi Salindia Beamer ch2.pdf ke PNG 300 DPI
    print("\n[LANGKAH 1] Ekstraksi Slide Beamer ch2.pdf -> PNG 300 DPI...")
    run_cmd(f'pdftoppm -r 300 -png "{PDF_SLIDES}" "{os.path.join(SCRATCH_DIR, "frame")}"')
    frame_files = sorted([f for f in os.listdir(SCRATCH_DIR) if f.startswith("frame-") and f.endswith(".png")])
    print(f"  -> Berhasil mengekstrak {len(frame_files)} frame slide beresolusi tinggi.")

    # Pastikan jeda kuis 8s tersedia
    if not os.path.exists(QUIZ_PAUSE_MP3):
        print("  -> Membuat file jeda kuis 8 detik...")
        run_cmd(f'ffmpeg -y -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 -t 8 -c:a libmp3lame -b:a 192k "{QUIZ_PAUSE_MP3}"')

    # Step 2: Sintesis Audio Narasi (Edge TTS ArdiNeural)
    print("\n[LANGKAH 2] Sintesis Narasi Suara Alami (id-ID-ArdiNeural)...")
    audio_files = []
    slide_durations = []

    for item in SLIDES_DATA:
        sn = item["num"]
        print(f"  -> Slide {sn:02d}: {item['title']}...")
        if not item.get("quiz", False):
            afile = os.path.join(SCRATCH_DIR, f"tts_{sn:02d}.mp3")
            asyncio.run(synth_tts(item["text"], afile))
            audio_files.append(afile)
            dur = get_duration(afile)
            slide_durations.append(dur)
        else:
            # Slide Kuis: Bagian 1 + Jeda 8 Detik + Bagian 2
            afile_p1 = os.path.join(SCRATCH_DIR, f"tts_{sn:02d}_p1.mp3")
            afile_p2 = os.path.join(SCRATCH_DIR, f"tts_{sn:02d}_p2.mp3")
            afile_comb = os.path.join(SCRATCH_DIR, f"tts_{sn:02d}_combined.mp3")
            asyncio.run(synth_tts(item["text_part1"], afile_p1))
            asyncio.run(synth_tts(item["text_part2"], afile_p2))
            
            # Concat audio kuis
            concat_quiz = os.path.join(SCRATCH_DIR, "quiz_concat.txt")
            with open(concat_quiz, "w") as f:
                f.write(f"file '{afile_p1}'\nfile '{QUIZ_PAUSE_MP3}'\nfile '{afile_p2}'\n")
            run_cmd(f'ffmpeg -y -f concat -safe 0 -i "{concat_quiz}" -c copy "{afile_comb}"')
            audio_files.append(afile_comb)
            dur = get_duration(afile_comb)
            slide_durations.append(dur)

    total_duration = sum(slide_durations)
    m, s = divmod(int(total_duration), 60)
    print(f"  -> Total Estimasi Durasi Video: {m:02d}:{s:02d} ({total_duration:.2f} detik)")

    # Step 3: Render Klip Per Salindia (1080p Full HD + Stereo AAC 192 kbps)
    print("\n[LANGKAH 3] Rendering Klip Salindia Video MP4 (1080p CRF 18, AAC 192k Stereo)...")
    clip_files = []
    for i, item in enumerate(SLIDES_DATA):
        sn = item["num"]
        img = os.path.join(SCRATCH_DIR, frame_files[i])
        aud = audio_files[i]
        clip = os.path.join(SCRATCH_DIR, f"clip_{sn:02d}.mp4")

        # Encode: scale to 1920x1080 with padding if needed, libx264 faster CRF 18, aac 192k stereo
        cmd = (
            f'ffmpeg -y -loop 1 -i "{img}" -i "{aud}" '
            f'-c:v libx264 -preset faster -crf 18 -pix_fmt yuv420p '
            f'-vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p" '
            f'-c:a aac -b:a 192k -ac 2 -ar 44100 -shortest "{clip}"'
        )
        run_cmd(cmd)
        clip_files.append(clip)
        print(f"  [OK] Klip {sn:02d} selesai ({slide_durations[i]:.1f} detik)")

    # Step 4: Penggabungan (Concat Final)
    print("\n[LANGKAH 4] Penggabungan Klip ke Video Final (video_pd_minggu02.mp4)...")
    concat_txt = os.path.join(SCRATCH_DIR, "concat_final.txt")
    with open(concat_txt, "w") as f:
        for c in clip_files:
            f.write(f"file '{c}'\n")

    run_cmd(f'ffmpeg -y -f concat -safe 0 -i "{concat_txt}" -c copy "{FINAL_ROOT_VIDEO}"')
    shutil.copy2(FINAL_ROOT_VIDEO, FINAL_PORTAL_VIDEO)
    print(f"  -> Video Utama: {FINAL_ROOT_VIDEO}")
    print(f"  -> Sinkronisasi Portal: {FINAL_PORTAL_VIDEO}")

    # Step 5: Pembuatan Naskah YouTube Markdown Lengkap (SEO Optimized)
    print("\n[LANGKAH 5] Menghasilkan Naskah Metadata YouTube (video_script_pd_w02_v2.md)...")
    timestamps = []
    accum = 0.0
    for i, item in enumerate(SLIDES_DATA):
        mm, ss = divmod(int(accum), 60)
        timestamps.append(f"{mm:02d}:{ss:02d} - {item['chapter']}")
        accum += slide_durations[i]

    script_content = f"""# Naskah & Metadata Video Kuliah Minggu 02: Persamaan Diferensial v2.0

### 1. Metadata Siap Unggah YouTube (SEO Optimized)

**Tautan Resmi YouTube:** [https://youtu.be/r5nFrD9DkOE](https://youtu.be/r5nFrD9DkOE) *(ID Playlist Resmi)*  
**Judul Resmi:** `[Minggu 02] PDB Orde 1: Persamaan Separabel, Eksak & Faktor Integrasi | Persamaan Diferensial | Teknik Elektro UNIB`

**Deskripsi Siap Unggah:**
```text
Kuliah Daring Minggu 02 - Persamaan Diferensial (Teknik Elektro UNIB)
Topik: PDB Orde Satu: Bentuk Diferensial M dx + N dy = 0, Metode Separabel, Uji Ke-Eksak-an Euler-Clairaut, Rekonstruksi Potensial Medan Konservatif, Penentuan Faktor Pengintegrasi, Transien Sirkuit RC, Paradoks Efisiensi 50%, Proteksi RC Snubber IGBT, dan Solver Komputasi Julia Tsit5.

Dosen Pengampu:
- Ir. Novalio Daratha, S.T., M.Sc., Ph.D.
- Muhammad Arfan, S.T., M.T.
Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika
Fakultas Teknik, Universitas Bengkulu

Akses portal perkuliahan, modul ajar, lembar kerja C1-C6, dan problem set:
https://www.ndaratha.my.id/persamaan-diferensial/

Linimasa Bab (Timestamps):
{chr(10).join(timestamps)}

Buku Referensi Pembelajaran:
1. Erwin Kreyszig, "Advanced Engineering Mathematics", 10th Edition, John Wiley & Sons.
2. Dennis G. Zill, "A First Course in Differential Equations with Modeling Applications", 11th Edition.
3. William H. Hayt & John A. Buck, "Engineering Electromagnetics", 9th Edition, McGraw-Hill.
4. IEEE Std 141 & IEC 60071 (Standar Isolasi & Transien Daya).

#PersamaanDiferensial #TeknikElektro #UniversitasBengkulu #KalkulusLanjut #DifferentialEquations #JuliaLang
```

---

## 2. Capaian Pembelajaran (Sub-CPMK 2 OBE Taksonomi Bloom)
- **C1 (Mengingat):** Menyatakan bentuk kanonik diferensial $M dx + N dy = 0$ dan kriteria Euler-Clairaut $\frac{{\partial M}}{{\partial y}} = \frac{{\partial N}}{{\partial x}}$.
- **C2 (Memahami):** Menghubungkan persamaan eksak dengan medan konservatif skalar elektrostatik ($\nabla \times \mathbf{{E}} = 0$).
- **C3 (Menerapkan):** Menghitung faktor pengintegrasi $\mu(x)$ atau $\mu(y)$ pada PDB non-eksak secara analitik.
- **C4 (Menganalisis):** Memodelkan dinamika pengisian \& pengosongan kapasitor ($\tau = RC$).
- **C5 (Mengevaluasi):** Mengkaji paradoks efisiensi $50\%$ disipasi kalor resistor pada sirkuit RC.
- **C6 (Komputasi):** Memprogram solver numerik adaptif Julia `DifferentialEquations.jl` dengan metode `Tsit5()`.

---

## 3. Naskah Audio Narasi Per Salindia (15 Slide Lengkap)

"""
    for item in SLIDES_DATA:
        sn = item["num"]
        script_content += f"### Salindia {sn:02d}: {item['title']}\n\n"
        if not item.get("quiz", False):
            script_content += f"{item['text']}\n\n"
        else:
            script_content += f"**[Bagian 1 - Pertanyaan Kuis]:**\n{item['text_part1']}\n\n"
            script_content += f"*[Jeda Hening Berpikir: 8 Detik Terprogram]*\n\n"
            script_content += f"**[Bagian 2 - Pembahasan Kuis & Tantangan Bloom]:**\n{item['text_part2']}\n\n"

    with open(SCRIPT_MD, "w") as f:
        f.write(script_content)
    print(f"  -> Naskah Berhasil Disimpan: {SCRIPT_MD}")

    t_total = time.time() - t0
    m_tot, s_tot = divmod(int(t_total), 60)
    print("\n" + "=" * 65)
    print(f" PABRIKASI SELESAI SUKSES DALAM {m_tot:02d}:{s_tot:02d}!")
    print(f" Video Final : {FINAL_ROOT_VIDEO}")
    print(f" Durasi Video: {m:02d}:{s:02d} (1080p, Stereo AAC 192k)")
    print("=" * 65)

if __name__ == "__main__":
    main()
