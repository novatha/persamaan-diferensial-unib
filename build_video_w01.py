import subprocess
import os
import time
import asyncio
import edge_tts

slides_data = [
    {
        "slide_num": 1,
        "title": "Judul & Pembukaan Kuliah",
        "chapter": "01. Pembukaan Perkuliahan Persamaan Diferensial",
        "text": (
            "Halo rekan-rekan mahasiswa Program Studi Teknik Elektro Universitas Bengkulu, "
            "selamat datang dalam perkuliahan daring Persamaan Diferensial semester genap 2026. "
            "Mata kuliah ini dirancang khusus untuk membangun fondasi analisis matematika yang kokoh "
            "dalam memodelkan fenomena fisis kelistrikan dan elektromagnetika. "
            "Pada pertemuan perdana minggu pertama ini, kita akan membahas: "
            "Klasifikasi PDB dan PDP, Konsep Orde dan Derajat, Syarat Linieritas, "
            "Solusi Umum versus Solusi Khusus, Masalah Nilai Awal atau Initial Value Problem, "
            "serta Pemodelan Fisis Rangkaian Listrik berbasis Hukum Kirchhoff. "
            "Kuliah ini diampu bersama saya, Insinyur Novalio Daratha dan Bapak Muhammad Arfan."
        )
    },
    {
        "slide_num": 2,
        "title": "Outline Pembelajaran",
        "chapter": "02. Agenda Pembelajaran Pekan 1",
        "text": (
            "Berikut adalah pokok-pokok bahasan yang akan kita pelajari pada pertemuan hari ini. "
            "Pertama, pengantar dan komparasi fundamental antara Persamaan Diferensial Biasa dan Persamaan Diferensial Parsial. "
            "Kedua, klasifikasi persamaan berdasarkan tingkat turunan tertinggi atau orde, serta derajat dan linieritas."
        )
    },
    {
        "slide_num": 3,
        "title": "Outline Pembelajaran (Lanjutan)",
        "chapter": "03. Agenda Lanjutan: Solusi & Pemodelan Fisis",
        "text": (
            "Ketiga, kita akan mengkaji konsep keluarga kurva pada solusi umum serta penentuan solusi khusus unik "
            "melalui penerapan syarat awal atau Initial Value Problem. "
            "Dan keempat, kita akan mempraktikkan penurunan model fisis matematika dari hukum pertama fisika "
            "menggunakan Hukum Tegangan Kirchhoff pada rangkaian transien listrik RL."
        )
    },
    {
        "slide_num": 4,
        "title": "Definisi Persamaan Diferensial Biasa (PDB)",
        "chapter": "04. Konsep Dasar Persamaan Diferensial Biasa",
        "text": (
            "Mari kita mulai dari definisi Persamaan Diferensial Biasa atau PDB. "
            "PDB adalah persamaan diferensial yang memuat turunan dari satu atau lebih variabel tak bebas "
            "hanya terhadap satu variabel bebas tunggal, misalnya waktu t. "
            "Dalam disiplin Teknik Elektro, PDB selalu muncul dalam pemodelan sistem elemen terpusat atau lumped systems. "
            "Contohnya pada pengosongan muatan kapasitor melalui resistor: R dikali d q per d t ditambah satu per C dikali q sama dengan nol. "
            "Atau pada dinamika osilasi rangkaian RLC orde dua: L dikali d kuadrat i per d t kuadrat ditambah R d i per d t ditambah satu per C i sama dengan nol."
        )
    },
    {
        "slide_num": 5,
        "title": "Definisi Persamaan Diferensial Parsial (PDP)",
        "chapter": "05. Konsep Dasar Persamaan Diferensial Parsial",
        "text": (
            "Berbeda dengan PDB, Persamaan Diferensial Parsial atau PDP adalah persamaan yang memuat turunan parsial "
            "terhadap dua atau lebih variabel bebas, misalnya koordinat spasial x, y, z serta waktu t. "
            "Dalam Teknik Elektro, PDP muncul pada sistem terdistribusi atau distributed systems dan fenomena medan. "
            "Dua contoh fundamental yang akan menjadi jembatan menuju mata kuliah Medan Elektromagnetika adalah: "
            "Persamaan Laplace dua dimensi untuk distribusi potensial elektrostatika tanpa muatan, "
            "serta Persamaan Gelombang untuk perambatan medan listrik pada saluran transmisi dan ruang bebas."
        )
    },
    {
        "slide_num": 6,
        "title": "Kuis Interaktif: Tebak Persamaan 1",
        "chapter": "06. Kuis Interaktif: Klasifikasi PDB vs PDP",
        "text": (
            "Untuk menguji pemahaman awal Anda, mari kita cermati kuis interaktif berikut. "
            "Perhatikan persamaan nomor satu: turunan ketiga y terhadap x dikurang empat x dikali d y per d x sama dengan e pangkat x. "
            "Apakah persamaan ini tergolong PDB atau PDP?"
        )
    },
    {
        "slide_num": 7,
        "title": "Kuis 1: Analisis Jawaban",
        "chapter": "07. Pembahasan Kuis 1",
        "text": (
            "Jawabannya adalah Persamaan Diferensial Biasa atau PDB. "
            "Alasannya sangat tegas: persamaan tersebut hanya memiliki satu variabel bebas tunggal, yaitu variabel x, "
            "dan seluruh turunannya adalah turunan biasa d y per d x, bukan turunan parsial."
        )
    },
    {
        "slide_num": 8,
        "title": "Kuis Interaktif: Tebak Persamaan 2",
        "chapter": "08. Kuis 2: Persamaan Difusi Dua Dimensi",
        "text": (
            "Sekarang perhatikan persamaan nomor dua: parsial u per parsial t sama dengan alpha kuadrat dikalikan "
            "jumlah parsial kuadrat u per parsial x kuadrat ditambah parsial kuadrat u per parsial y kuadrat. "
            "Bagaimana klasifikasi persamaan ini?"
        )
    },
    {
        "slide_num": 9,
        "title": "Kuis 2: Analisis Jawaban",
        "chapter": "09. Pembahasan Kuis 2",
        "text": (
            "Tepat sekali, ini adalah Persamaan Diferensial Parsial atau PDP. "
            "Persamaan ini memiliki tiga variabel bebas sekaligus, yaitu waktu t serta koordinat spasial x dan y. "
            "Persamaan ini merepresentasikan fenomena difusi panas atau penetrasi medan elektromagnetik ke dalam konduktor."
        )
    },
    {
        "slide_num": 10,
        "title": "Kuis Interaktif: Tebak Persamaan 3",
        "chapter": "10. Kuis 3: Rangkaian Listrik dengan Sumber AC",
        "text": (
            "Terakhir, perhatikan persamaan nomor tiga: L dikali d i per d t ditambah R dikali i sama dengan V nol sinus omega t. "
            "Ini adalah persamaan tegangan pada rangkaian RL seri dengan sumber eksitasi sinusoidal bolak-balik."
        )
    },
    {
        "slide_num": 11,
        "title": "Kuis 3: Analisis Jawaban",
        "chapter": "11. Pembahasan Kuis 3",
        "text": (
            "Persamaan ini jelas merupakan Persamaan Diferensial Biasa atau PDB. "
            "Meskipun di ruas kanan terdapat fungsi sinusoidal, satu-satunya variabel bebas yang menentukan dinamika arus adalah waktu t."
        )
    },
    {
        "slide_num": 12,
        "title": "Klasifikasi: Konsep Orde",
        "chapter": "12. Klasifikasi PDB Berdasarkan Orde",
        "text": (
            "Selanjutnya kita masuk ke klasifikasi kedua, yaitu Orde atau Tingkat. "
            "Orde suatu persamaan diferensial ditentukan secara mutlak oleh turunan tertinggi yang muncul di dalam persamaan tersebut."
        )
    },
    {
        "slide_num": 13,
        "title": "Contoh Analisis Orde 1",
        "chapter": "13. Contoh Penentuan Orde Persamaan",
        "text": (
            "Mari kita analisis contoh konkret pertama: persamaan y double prime ditambah tiga y prime ditambah dua y sama dengan nol."
        )
    },
    {
        "slide_num": 14,
        "title": "Analisis Orde 2",
        "chapter": "14. Identifikasi Orde 2",
        "text": (
            "Karena di dalam persamaan terdapat suku y double prime, yaitu turunan kedua terhadap variabel bebas, "
            "maka persamaan ini diklasifikasikan sebagai PDB Orde dua."
        )
    },
    {
        "slide_num": 15,
        "title": "Pentingnya Membedakan Orde dan Pangkat",
        "chapter": "15. Membedakan Konsep Orde dan Pangkat",
        "text": (
            "Sekarang perhatikan contoh yang sering mengecoh: "
            "kurung d y per d t tutup pangkat tiga, ditambah y sama dengan nol. Berapakah ordenya?"
        )
    },
    {
        "slide_num": 16,
        "title": "Perbedaan Mendasar Orde vs Derajat",
        "chapter": "16. Konsep Orde vs Derajat",
        "text": (
            "Persamaan ini tetap merupakan PDB Orde satu! "
            "Mengapa demikian? Karena turunan tertingginya hanyalah turunan pertama, yaitu d y per d t. "
            "Adapun angka pangkat tiga di luar tanda kurung dinamakan Derajat atau degree, bukan orde. "
            "Jangan pernah mencampuradukkan antara orde turunan dengan derajat pangkat aljabar."
        )
    },
    {
        "slide_num": 17,
        "title": "Syarat Linieritas Persamaan Diferensial",
        "chapter": "17. Tiga Syarat Linieritas PDB",
        "text": (
            "Klasifikasi ketiga yang sangat krusial adalah Linieritas. "
            "Suatu persamaan diferensial dinyatakan linier jika memenuhi tiga syarat mutlak: "
            "Pertama, variabel terikat y dan seluruh suku turunannya hanya boleh berpangkat satu. "
            "Kedua, tidak ada perkalian antara variabel terikat dengan turunannya sendiri, seperti suku y dikali d y per d x. "
            "Dan ketiga, tidak ada fungsi transendental yang memuat variabel terikat y, misalnya sinus y, eksponensial y, atau logaritma y."
        )
    },
    {
        "slide_num": 18,
        "title": "Contoh Identifikasi Sifat Linieritas",
        "chapter": "18. Uji Linieritas Contoh Kasus",
        "text": (
            "Mari kita uji pemahaman linieritas pada beberapa persamaan berikut ini."
        )
    },
    {
        "slide_num": 19,
        "title": "Uji Kasus 1: Persamaan Linier",
        "chapter": "19. Kasus 1: Eksitasi Sinusoidal pada Variabel Bebas",
        "text": (
            "Pada persamaan d kuadrat x per d t kuadrat ditambah lima x sama dengan sinus t: "
            "Persamaan ini adalah linier. Perhatikan bahwa fungsi sinus t beroperasi pada variabel bebas t, "
            "bukan pada variabel terikat x, sehingga tidak melanggar syarat linieritas apapun."
        )
    },
    {
        "slide_num": 20,
        "title": "Uji Kasus 2: Suku Non-Linier",
        "chapter": "20. Kasus 2: Pelanggaran Derajat Variabel Terikat",
        "text": (
            "Sekarang perhatikan persamaan kedua: d y per d x ditambah y kuadrat sama dengan nol."
        )
    },
    {
        "slide_num": 21,
        "title": "Kesimpulan Kasus 2: Non-Linier",
        "chapter": "21. Analisis Suku Non-Linier y Kuadrat",
        "text": (
            "Persamaan ini jelas non-linier, karena variabel terikat y berpangkat dua. "
            "Kehadiran suku y kuadrat menghancurkan prinsip superposisi yang menjadi fondasi sistem linier."
        )
    },
    {
        "slide_num": 22,
        "title": "Uji Kasus 3: Koefisien Variabel Bebas",
        "chapter": "22. Kasus 3: Koefisien Berupa Fungsi Variabel Bebas",
        "text": (
            "Pada persamaan ketiga: cosinus x dikalikan d y per d x sama dengan y."
        )
    },
    {
        "slide_num": 23,
        "title": "Kesimpulan Kasus 3: Linier",
        "chapter": "23. Validasi Linieritas dengan Koefisien Variabel",
        "text": (
            "Persamaan ini tetap linier sempurna! "
            "Meskipun memuat fungsi trigonometri cosinus x, fungsi tersebut melekat pada variabel bebas x sebagai koefisien. "
            "Variabel terikat y dan turunannya d y per d x tetap berpangkat satu dan terpisah secara linier."
        )
    },
    {
        "slide_num": 24,
        "title": "Konsep Solusi Umum Persamaan Diferensial",
        "chapter": "24. Solusi Umum & Keluarga Kurva",
        "text": (
            "Kini kita beralih ke konsep Solusi: apa perbedaan Solusi Umum dan Solusi Khusus? "
            "Solusi umum adalah solusi analitis yang masih memuat konstanta integrasi sembarang, misalnya konstanta C. "
            "Secara geometri, solusi umum y sama dengan C dikali e pangkat t tidak hanya mewakili satu garis lengkung, "
            "melainkan mewakili seluruh keluarga kurva tak hingga banyaknya di bidang koordinat."
        )
    },
    {
        "slide_num": 25,
        "title": "Konsep Solusi Khusus & Kondisi Batas",
        "chapter": "25. Solusi Khusus Unik pada Initial Value Problem",
        "text": (
            "Namun di dunia rekayasa nyata, tegangan kapasitor atau arus induktor pada saat awal sakelar dinyalakan memiliki nilai pasti. "
            "Jika kita diberikan satu kondisi awal atau Initial Condition, misalnya y pada saat t sama dengan nol bernilai dua, "
            "maka kita dapat mengunci nilai konstanta C sama dengan dua. "
            "Hasilnya adalah Solusi Khusus unik, yaitu satu lintasan kurva merah tunggal yang persis melewati titik koordinat nol koma dua."
        )
    },
    {
        "slide_num": 26,
        "title": "Contoh Hitungan Masalah Nilai Awal (IVP)",
        "chapter": "26. Perhitungan Step-by-Step Initial Value Problem",
        "text": (
            "Mari kita buktikan prosedur ini melalui contoh perhitungan langsung Masalah Nilai Awal. "
            "Diberikan PDB peluruhan: d y per d t sama dengan minus tiga y."
        )
    },
    {
        "slide_num": 27,
        "title": "Langkah 1: Menentukan Solusi Umum",
        "chapter": "27. Solusi Umum Peluruhan Eksponensial",
        "text": (
            "Langkah pertama, dengan metode pemisahan variabel, kita peroleh solusi umum: "
            "y sebagai fungsi waktu sama dengan C dikalikan eksponensial minus tiga t."
        )
    },
    {
        "slide_num": 28,
        "title": "Langkah 2: Menetapkan Kondisi Awal",
        "chapter": "28. Penetapan Syarat Awal y(0) = 10",
        "text": (
            "Langkah kedua, kita terapkan syarat awal Masalah Nilai Awal: "
            "pada saat waktu t sama dengan nol detik, nilai respons y terukur sebesar sepuluh, atau y nol sama dengan sepuluh."
        )
    },
    {
        "slide_num": 29,
        "title": "Langkah 3: Substitusi ke Solusi Umum",
        "chapter": "29. Evaluasi Konstanta Integrasi C",
        "text": (
            "Langkah ketiga, substitusikan t sama dengan nol dan y sama dengan sepuluh ke dalam solusi umum. "
            "Kita peroleh sepuluh sama dengan C dikali e pangkat minus tiga dikali nol. "
            "Karena eksponensial nol bernilai satu, maka konstanta C secara eksak bernilai sepuluh."
        )
    },
    {
        "slide_num": 30,
        "title": "Langkah 4: Formulasi Solusi Khusus Akhir",
        "chapter": "30. Formulasi Solusi Khusus Akhir",
        "text": (
            "Langkah keempat, masukkan kembali nilai C sama dengan sepuluh ke dalam persamaan. "
            "Kita mendapatkan solusi khusus akhir yang definitif: y t sama dengan sepuluh dikali e pangkat minus tiga t. "
            "Respons ini menunjukkan peluruhan eksponensial stabil menuju nol seiring berjalannya waktu."
        )
    },
    {
        "slide_num": 31,
        "title": "Pemodelan Fisis Rangkaian Listrik: Hukum KVL",
        "chapter": "31. Pemodelan Rangkaian Listrik RL dengan Hukum Kirchhoff",
        "text": (
            "Sekarang kita masuki Pilar keempat: menghubungkan matematika dengan rekayasa nyata. "
            "Bagaimana persamaan diferensial diturunkan dari rangkaian listrik? "
            "Perhatikan rangkaian seri resistor R dan induktor L yang terhubung dengan sumber tegangan V t. "
            "Berdasarkan Hukum Tegangan Kirchhoff atau KVL, jumlah aljabar tegangan pada loop tertutup sama dengan nol, "
            "sehingga tegangan jatuh pada resistor V R ditambah tegangan induktor V L harus persis sama dengan tegangan sumber V t."
        )
    },
    {
        "slide_num": 32,
        "title": "Karakteristik Komponen R dan L",
        "chapter": "32. Hukum Ohm dan Hukum Induksi Faraday",
        "text": (
            "Kita substitusikan karakteristik fisis masing-masing komponen: "
            "Tegangan resistor mematuhi Hukum Ohm disipatif: V R sama dengan arus i t dikalikan resistansi R. "
            "Sedangkan tegangan induktor mematuhi Hukum Induksi Faraday: V L sama dengan induktansi L dikalikan laju perubahan arus d i t per d t. "
            "Induktor melawan perubahan arus sesaat dengan membangkitkan gaya gerak listrik induksi diri."
        )
    },
    {
        "slide_num": 33,
        "title": "Model Matematika Akhir: PDB Orde 1",
        "chapter": "33. Model Matematika PDB Orde 1 Transien Listrik",
        "text": (
            "Dengan menyubstitusikan kedua hubungan konstitutif tersebut, kita memperoleh model matematika akhir: "
            "L dikali d i per d t ditambah R dikali i sama dengan V t. "
            "Inilah bentuk kanonik Persamaan Diferensial Biasa linier orde satu non-homogen. "
            "Persamaan inilah yang mengatur seluruh perilaku transien pengisian dan penyaluran arus pada transformator, motor listrik, dan saluran transmisi."
        )
    },
    {
        "slide_num": 34,
        "title": "Rangkuman Perkuliahan & Penutup",
        "chapter": "34. Rangkuman Perkuliahan Minggu 01 & Penutup",
        "text": (
            "Sebagai rangkuman perkuliahan minggu pertama kita: "
            "PDB memodelkan sistem terpusat dengan satu variabel bebas, sedangkan PDP memodelkan medan terdistribusi. "
            "Orde ditentukan oleh turunan tertinggi, sedangkan linieritas mensyaratkan variabel terikat berpangkat satu tanpa suku perkalian silang. "
            "Solusi umum memuat konstanta sembarang yang dikonversi menjadi solusi khusus unik melalui syarat awal IVP. "
            "Serta dinamika rangkaian listrik dapat dimodelkan secara elegan menjadi PDB melalui Hukum Kirchhoff. "
            "Silakan unduh salindia materi dan kerjakan Lembar Kerja Mahasiswa serta Problem Set Minggu satu. "
            "Pada minggu kedua, kita akan membedah metode analitis penyelesaian PDB orde satu: separabel, eksak, dan faktor integrasi. "
            "Saya, Insinyur Novalio Daratha bersama Bapak Muhammad Arfan, terima kasih atas perhatian Anda, dan Wassalamu'alaikum warahmatullahi wabarakatuh."
        )
    }
]

VOICE = "id-ID-ArdiNeural"
OUTPUT_DIR = "scratch/audio_w01"
FRAMES_DIR = "scratch/slide_frames_w01"
VIDEO_OUT = "scratch/video_pd_minggu01.mp4"
ROOT_VIDEO = "video_pd_minggu01.mp4"
SCRIPT_MD = "video_script_pd_w01.md"

async def generate_speech(text, outfile):
    for attempt in range(8):
        try:
            communicate = edge_tts.Communicate(text, VOICE, rate="-2%")
            await asyncio.wait_for(communicate.save(outfile), timeout=30.0)
            if os.path.exists(outfile) and os.path.getsize(outfile) > 8000:
                return
            else:
                if os.path.exists(outfile):
                    os.remove(outfile)
        except Exception as e:
            print(f"  [Percobaan {attempt+1}/8] TTS Error: {e}, mencoba kembali dalam 2 detik...")
            if os.path.exists(outfile):
                try:
                    os.remove(outfile)
                except OSError:
                    pass
            await asyncio.sleep(2)

def get_audio_duration(audio_file):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        audio_file
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())

def format_timestamp(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"

async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(VIDEO_OUT), exist_ok=True)
    
    print(f"=== 1. SINTESIS AUDIO PER SALINDIA MINGGU 01 ({len(slides_data)} SLIDES) ===")
    total_time = 0.0
    timestamps = []
    
    for item in slides_data:
        s_num = item["slide_num"]
        audio_file = os.path.join(OUTPUT_DIR, f"slide_{s_num:02d}.mp3")
        padded_audio = os.path.join(OUTPUT_DIR, f"slide_{s_num:02d}_padded.mp3")
        
        # Hapus file korup jika < 8KB
        if os.path.exists(audio_file) and os.path.getsize(audio_file) < 8000:
            os.remove(audio_file)
            
        if not os.path.exists(audio_file):
            print(f"  Membuat sintesis audio Salindia {s_num:02d}: {item['title']}...")
            await generate_speech(item["text"], audio_file)
        
        # Tambahkan jeda padding 1.2 detik di akhir audio
        cmd_pad = [
            "ffmpeg", "-y", "-i", audio_file,
            "-af", "apad=pad_dur=1.2",
            padded_audio
        ]
        subprocess.run(cmd_pad, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        
        dur = get_audio_duration(padded_audio)
        timestamps.append((format_timestamp(total_time), item["chapter"], dur, item["title"]))
        total_time += dur

    mins_total = int(total_time // 60)
    secs_total = int(total_time % 60)
    print(f"\nTotal estimasi durasi video: {mins_total:02d}:{secs_total:02d} ({total_time:.2f} detik)")

    # Tulis naskah YouTube Markdown
    print(f"\n=== 2. MEMBUAT NASKAH METADATA YOUTUBE ({SCRIPT_MD}) ===")
    with open(SCRIPT_MD, "w", encoding="utf-8") as f:
        f.write("# Naskah & Metadata Video Kuliah Minggu 01: Persamaan Diferensial\n\n")
        f.write("### 1. Metadata Siap Unggah YouTube (SEO Optimized)\n\n")
        f.write("**Judul Video (Opsi 1 - Utama):**\n")
        f.write("`[Minggu 01] Pengantar PDB vs PDP, Orde, Linieritas, IVP & Rangkaian Listrik | Persamaan Diferensial`\n\n")
        f.write("**Judul Alternatif:**\n")
        f.write("`Kuliah 01 Persamaan Diferensial: Klasifikasi PDB/PDP, Initial Value Problem, dan Model Kirchhoff`\n\n")
        f.write("**Deskripsi Siap Unggah:**\n")
        f.write("```text\n")
        f.write("Kuliah Daring Minggu 01 - Persamaan Diferensial (Teknik Elektro UNIB)\n")
        f.write("Topik: Klasifikasi PDB vs PDP, Orde, Derajat, Linieritas, Masalah Nilai Awal (IVP), dan Pemodelan Fisis Rangkaian Listrik.\n\n")
        f.write("Dosen Pengampu:\n")
        f.write("- Ir. Novalio Daratha, S.T., M.Sc., Ph.D.\n")
        f.write("- Muhammad Arfan, S.T., M.T.\n")
        f.write("Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika\n")
        f.write("Fakultas Teknik, Universitas Bengkulu\n\n")
        f.write("Akses portal perkuliahan, modul ajar, lembar kerja C1-C6, dan notebook simulasi:\n")
        f.write("https://www.ndaratha.my.id/persamaan-diferensial/\n\n")
        f.write("Linimasa Bab (Timestamps):\n")
        for ts, ch, d, tit in timestamps:
            f.write(f"{ts} - {ch}\n")
        f.write("\nBuku Referensi Pembelajaran:\n")
        f.write("1. Erwin Kreyszig, Advanced Engineering Mathematics, 10th Ed., John Wiley & Sons.\n")
        f.write("2. Dennis G. Zill, A First Course in Differential Equations with Modeling Applications, Cengage.\n")
        f.write("3. William H. Hayt & John A. Buck, Engineering Electromagnetics, McGraw-Hill.\n\n")
        f.write("#TeknikElektro #PersamaanDiferensial #UniversitasBengkulu #PDB #PDP #KalkulusLanjut #RangkaianListrik #HukumKirchhoff #InitialValueProblem #MedanElektromagnetika\n")
        f.write("```\n\n")
        f.write("### 2. Naskah Audio Narasi Per Salindia\n\n")
        for item in slides_data:
            f.write(f"#### Salindia {item['slide_num']:02d}: {item['title']}\n\n")
            f.write(f"{item['text']}\n\n")

    print(f"Naskah YouTube tersimpan di: {SCRIPT_MD}")

    # Build klip video per salindia
    CLIPS_DIR = "scratch/clips_w01"
    os.makedirs(CLIPS_DIR, exist_ok=True)
    
    print("\n=== 3. MEMBANGUN KLIP STILLIMAGE 1080p PER SALINDIA ===")
    for item in slides_data:
        s_num = item["slide_num"]
        frame_png = os.path.join(FRAMES_DIR, f"slide-{s_num:02d}.png")
        padded_audio = os.path.join(OUTPUT_DIR, f"slide_{s_num:02d}_padded.mp3")
        clip_mp4 = os.path.join(CLIPS_DIR, f"clip_{s_num:02d}.mp4")
        
        if not os.path.exists(clip_mp4) or os.path.getsize(clip_mp4) == 0:
            cmd_clip = [
                "ffmpeg", "-y",
                "-loop", "1", "-i", frame_png,
                "-i", padded_audio,
                "-c:v", "libx264", "-tune", "stillimage",
                "-pix_fmt", "yuv420p",
                "-vf", "scale=1920:1080,format=yuv420p",
                "-c:a", "aac", "-b:a", "192k",
                "-shortest", clip_mp4
            ]
            subprocess.run(cmd_clip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"  [OK] Klip Salindia {s_num:02d} selesai")

    print("\n=== 4. PENGGABUNGAN KLIP DENGAN FFMPEG CONCAT FILTER (0 MS DRIFT) ===")
    cmd_concat = ["ffmpeg", "-y"]
    filter_inputs = ""
    for i in range(len(slides_data)):
        s_num = slides_data[i]["slide_num"]
        clip_mp4 = os.path.join(CLIPS_DIR, f"clip_{s_num:02d}.mp4")
        cmd_concat.extend(["-i", clip_mp4])
        filter_inputs += f"[{i}:v:0][{i}:a:0]"

    filter_complex = f"{filter_inputs}concat=n={len(slides_data)}:v=1:a=1[outv][outa]"
    cmd_concat.extend([
        "-filter_complex", filter_complex,
        "-map", "[outv]", "-map", "[outa]",
        "-c:v", "libx264", "-preset", "faster", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k",
        VIDEO_OUT
    ])
    
    t0 = time.time()
    subprocess.run(cmd_concat, check=True)
    t1 = time.time()
    
    file_size_mb = os.path.getsize(VIDEO_OUT) / (1024 * 1024)
    print(f"\n[SUKSES] Video Minggu 01 berhasil dirakit!")
    print(f"  Lokasi berkas : {VIDEO_OUT}")
    print(f"  Ukuran berkas : {file_size_mb:.2f} MB")
    print(f"  Waktu render  : {t1 - t0:.2f} detik")

    # Salin ke root untuk referensi
    subprocess.run(["cp", VIDEO_OUT, ROOT_VIDEO], check=True)
    print(f"  Tersalin ke   : {ROOT_VIDEO}")

if __name__ == "__main__":
    asyncio.run(main())
