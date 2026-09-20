import subprocess
import os
import time
import asyncio
import edge_tts

slides_data = [
    {
        "slide_num": 1,
        "title": "Judul & Pembukaan Kuliah Minggu 02",
        "chapter": "01. Pembukaan Kuliah Minggu 02",
        "text": (
            "Halo rekan-rekan mahasiswa Teknik Elektro Universitas Bengkulu, "
            "berjumpa kembali dalam perkuliahan daring Persamaan Diferensial semester genap 2026. "
            "Pada Minggu kedua ini, kita melangkah lebih dalam ke inti metode analitis analitik "
            "untuk menyelesaikan Persamaan Diferensial Biasa Orde Satu. "
            "Kita akan membedah secara tuntas tiga teknik penyelesaian utama: "
            "Persamaan Separabel, Persamaan Eksak berbasis medan konservatif, "
            "serta penanganan Persamaan Non-Eksak menggunakan Faktor Integrasi. "
            "Kuliah ini dipandu bersama saya, Insinyur Novalio Daratha dan Bapak Muhammad Arfan."
        )
    },
    {
        "slide_num": 2,
        "title": "Outline Pembelajaran Pekan 2",
        "chapter": "02. Agenda Pembahasan Pekan 2",
        "text": (
            "Berikut adalah tiga pilar agenda pembahasan kita hari ini. "
            "Pertama, bentuk kanonik umum PDB orde satu dalam format diferensial. "
            "Kedua, metode pemisahan variabel atau separabel dan aplikasinya. "
            "Ketiga, uji ke-eksak-an turunan silang Cauchy-Riemann serta teknik rekonstruksi fungsi potensial. "
            "Dan keempat, perumusan faktor integrasi pengubah persamaan non-eksak menjadi eksak."
        )
    },
    {
        "slide_num": 3,
        "title": "Bentuk Umum PDB Orde 1",
        "chapter": "03. Bentuk Umum PDB Orde 1",
        "text": (
            "Secara matematis, PDB orde satu dapat dinyatakan dalam dua bentuk standar. "
            "Bentuk turunan: d y per d x sama dengan f kurung x koma y. "
            "Atau bentuk simetris diferensial total: M kurung x koma y d x ditambah N kurung x koma y d y sama dengan nol. "
            "Pemilihan metode penyelesaian sangat bergantung pada struktur aljabar fungsi M dan N tersebut, "
            "apakah dapat dipisahkan variabelnya, memenuhi syarat eksak, atau memerlukan faktor integrasi."
        )
    },
    {
        "slide_num": 4,
        "title": "Definisi Persamaan Separabel",
        "chapter": "04. Konsep Persamaan Separabel",
        "text": (
            "Metode pertama adalah Persamaan Separabel atau dapat dipisahkan. "
            "Suatu PDB disebut separabel jika fungsi f kurung x koma y dapat difaktorkan "
            "secara murni menjadi perkalian fungsi g x dan fungsi h y. "
            "Prosedur penyelesaiannya sangat sistematis: "
            "Langkah satu, kumpulkan semua suku bervariabel y berdampingan dengan diferensial d y. "
            "Langkah dua, kumpulkan semua suku bervariabel x berdampingan dengan diferensial d x. "
            "Dan langkah tiga, integrasikan kedua ruas secara independen sehingga menghasilkan bentuk: "
            "integral satu per h y d y sama dengan integral g x d x ditambah konstanta sembarang C."
        )
    },
    {
        "slide_num": 5,
        "title": "Contoh Soal Persamaan Separabel",
        "chapter": "05. Contoh Kasus Persamaan Separabel",
        "text": (
            "Mari kita buktikan metode separabel melalui contoh soal berikut: "
            "selesaikan persamaan diferensial d y per d x sama dengan minus dua x dikali y kuadrat."
        )
    },
    {
        "slide_num": 6,
        "title": "Langkah 1: Pemisahan Variabel",
        "chapter": "06. Langkah 1: Isolasi Variabel y dan x",
        "text": (
            "Langkah pertama, pisahkan variabel x dan y ke ruas yang berlawanan. "
            "Bagilah kedua ruas dengan y kuadrat dan kalikan dengan d x. "
            "Kita peroleh d y per y kuadrat sama dengan minus dua x d x."
        )
    },
    {
        "slide_num": 7,
        "title": "Langkah 2: Menyiapkan Integrasi",
        "chapter": "07. Langkah 2: Integrasi Kedua Ruas",
        "text": (
            "Langkah kedua, terapkan operator integral pada kedua ruas persamaan. "
            "Tuliskan suku satu per y kuadrat sebagai y pangkat minus dua agar siap diintegrasikan."
        )
    },
    {
        "slide_num": 8,
        "title": "Evaluasi Integral",
        "chapter": "08. Evaluasi Integral Kalkulus",
        "text": (
            "Kita peroleh integral y pangkat minus dua d y sama dengan integral minus dua x d x."
        )
    },
    {
        "slide_num": 9,
        "title": "Langkah 3: Hasil Integrasi Analitis",
        "chapter": "09. Langkah 3: Hasil Integrasi Analitis",
        "text": (
            "Langkah ketiga, lakukan evaluasi integrasi. "
            "Integral dari y pangkat minus dua adalah minus y pangkat minus satu. "
            "Sedangkan integral dari minus dua x adalah minus x kuadrat, ditambah konstanta integrasi C. "
            "Sehingga persamaannya menjadi: minus y pangkat minus satu sama dengan minus x kuadrat ditambah C."
        )
    },
    {
        "slide_num": 10,
        "title": "Langkah 4: Membentuk Solusi Eksplisit",
        "chapter": "10. Langkah 4: Manipulasi Aljabar Eksplisit",
        "text": (
            "Langkah keempat, kita ubah bentuk implisit ini menjadi fungsi eksplisit y terhadap x. "
            "Kalikan kedua ruas dengan minus satu, sehingga satu per y sama dengan x kuadrat dikurang C."
        )
    },
    {
        "slide_num": 11,
        "title": "Solusi Umum Akhir Persamaan Separabel",
        "chapter": "11. Solusi Umum Akhir",
        "text": (
            "Dengan mendefinisikan konstanta baru K sama dengan minus C, "
            "kita balikkan pecahan tersebut untuk memperoleh solusi umum akhir: "
            "y sebagai fungsi x sama dengan satu dibagi kurung x kuadrat ditambah K. "
            "Inilah keluarga kurva solusi yang memenuhi persamaan diferensial awal."
        )
    },
    {
        "slide_num": 12,
        "title": "Konsep Persamaan Eksak & Medan Konservatif",
        "chapter": "12. Konsep Persamaan Eksak & Fisika Medan",
        "text": (
            "Kini kita beralih ke metode kedua yang sangat istimewa: Persamaan Eksak. "
            "Bentuk M d x ditambah N d y sama dengan nol disebut Eksak jika memenuhi syarat turunan parsial silang: "
            "parsial M per parsial y sama dengan parsial N per parsial x. "
            "Secara intuisi fisika, konsep ini identik dengan Medan Vektor Konservatif dalam elektrostatika. "
            "Persamaan eksak merepresentasikan total diferensial dari suatu fungsi potensial skalar F kurung x koma y sama dengan C, "
            "di mana curl dari gradien potensial selalu bernilai nol."
        )
    },
    {
        "slide_num": 13,
        "title": "Contoh Kasus Persamaan Eksak",
        "chapter": "13. Contoh Soal Persamaan Eksak",
        "text": (
            "Mari kita selesaikan persamaan diferensial: "
            "kurung dua x y d x ditambah kurung x kuadrat dikurang satu d y sama dengan nol."
        )
    },
    {
        "slide_num": 14,
        "title": "Langkah 1: Uji Ke-Eksak-an",
        "chapter": "14. Langkah 1: Uji Turunan Parsial Silang",
        "text": (
            "Langkah pertama yang wajib dilakukan sebelum menyelesaikan adalah menguji ke-eksak-annya terlebih dahulu."
        )
    },
    {
        "slide_num": 15,
        "title": "Turunan Parsial M terhadap y",
        "chapter": "15. Menghitung Turunan Parsial M",
        "text": (
            "Kita identifikasi M sama dengan dua x y. "
            "Turunkan M secara parsial terhadap y dengan memperlakukan x sebagai konstanta, menghasilkan dua x."
        )
    },
    {
        "slide_num": 16,
        "title": "Turunan Parsial N terhadap x",
        "chapter": "16. Menghitung Turunan Parsial N",
        "text": (
            "Selanjutnya kita identifikasi N sama dengan x kuadrat dikurang satu. "
            "Turunkan N secara parsial terhadap x, menghasilkan dua x."
        )
    },
    {
        "slide_num": 17,
        "title": "Verifikasi Syarat Eksak Terpenuhi",
        "chapter": "17. Verifikasi Ke-Eksak-an",
        "text": (
            "Karena parsial M per parsial y persis sama dengan parsial N per parsial x, yaitu sama-sama bernilai dua x, "
            "maka persamaan ini terbukti seratus persen Eksak!"
        )
    },
    {
        "slide_num": 18,
        "title": "Langkah 2: Rekonstruksi Fungsi Potensial F",
        "chapter": "18. Langkah 2: Rekonstruksi Fungsi Potensial",
        "text": (
            "Langkah kedua, kita rekonstruksi fungsi potensial F kurung x koma y dengan mengintegrasikan M terhadap x."
        )
    },
    {
        "slide_num": 19,
        "title": "Hasil Integrasi M terhadap x",
        "chapter": "19. Integrasi M dan Suku g(y)",
        "text": (
            "Integral dari dua x y terhadap x adalah x kuadrat y. "
            "Namun jangan lupa menambahkan konstanta integrasi sembarang g y, "
            "karena g y bertindak sebagai konstanta terhadap peubah x."
        )
    },
    {
        "slide_num": 20,
        "title": "Langkah 3: Menentukan Bentuk Fungsi g(y)",
        "chapter": "20. Langkah 3: Menentukan Fungsi g(y)",
        "text": (
            "Langkah ketiga, turunkan fungsi F tadi secara parsial terhadap y, "
            "kemudian samakan hasilnya dengan komponen N pada soal."
        )
    },
    {
        "slide_num": 21,
        "title": "Turunan Parsial F terhadap y",
        "chapter": "21. Evaluasi parsial F terhadap y",
        "text": (
            "Turunan parsial F terhadap y adalah x kuadrat ditambah g prime y."
        )
    },
    {
        "slide_num": 22,
        "title": "Pencocokan Koefisien",
        "chapter": "22. Menyamakan dengan Komponen N",
        "text": (
            "Samakan x kuadrat ditambah g prime y dengan N, yaitu x kuadrat dikurang satu. "
            "Suku x kuadrat di kedua ruas saling meniadakan, menyisakan g prime y sama dengan minus satu."
        )
    },
    {
        "slide_num": 23,
        "title": "Integrasi Nilai g(y)",
        "chapter": "23. Integrasi g prime y",
        "text": (
            "Dengan mengintegrasikan minus satu terhadap y, kita peroleh g y sama dengan minus y."
        )
    },
    {
        "slide_num": 24,
        "title": "Solusi Umum Akhir Persamaan Eksak",
        "chapter": "24. Solusi Umum Akhir Bentuk Implisit",
        "text": (
            "Masukkan kembali g y sama dengan minus y ke dalam fungsi potensial F. "
            "Kita peroleh solusi umum akhir F kurung x koma y sama dengan C, "
            "yaitu: x kuadrat dikali y dikurang y sama dengan C. Solusi ini telah tuntas sempurna."
        )
    },
    {
        "slide_num": 25,
        "title": "Konsep Faktor Integrasi untuk Kasus Non-Eksak",
        "chapter": "25. Konsep Dasar Faktor Integrasi",
        "text": (
            "Lalu bagaimana jika turunan silang parsial M per parsial y tidak sama dengan parsial N per parsial x? "
            "Persamaan tersebut diklasifikasikan sebagai Non-Eksak. "
            "Namun jangan menyerah, kita dapat mentransformasikannya menjadi eksak dengan mengalikannya pada suatu pengali "
            "yang disebut Faktor Integrasi mu kurung x koma y. "
            "Jika selisih M y dikurang N x dibagi N murni hanya fungsi dari x, sebut p x, "
            "maka faktor integrasinya adalah eksponensial integral p x d x. "
            "Sebaliknya, jika N x dikurang M y dibagi M hanya fungsi dari y, "
            "maka faktor integrasinya adalah eksponensial integral q y d y."
        )
    },
    {
        "slide_num": 26,
        "title": "Jaminan Ke-Eksak-an Persamaan Tertransformasi",
        "chapter": "26. Jaminan Ke-Eksak-an Sistem Tertransformasi",
        "text": (
            "Setelah seluruh ruas persamaan dikalikan dengan faktor integrasi mu, "
            "persamaan baru mu dikali M d x ditambah mu dikali N d y sama dengan nol "
            "dijamin seratus persen berubah menjadi eksak, dan selanjutnya dapat diselesaikan dengan prosedur standar sebelumnya."
        )
    },
    {
        "slide_num": 27,
        "title": "Kuis Interaktif: Mencari Faktor Integrasi",
        "chapter": "27. Kuis Interaktif: Uji Non-Eksak Kasus Khusus",
        "text": (
            "Mari kita uji pemahaman Anda melalui kuis interaktif berikut. "
            "Tinjau persamaan: kurung tiga x y ditambah y kuadrat d x ditambah kurung x kuadrat ditambah x y d y sama dengan nol. "
            "Pertama, uji turunan silang: M y bernilai tiga x ditambah dua y, sedangkan N x bernilai dua x ditambah y. "
            "Karena hasilnya tidak sama, persamaan ini terbukti Non-Eksak."
        )
    },
    {
        "slide_num": 28,
        "title": "Evaluasi Rumus Rasio Faktor Integrasi",
        "chapter": "28. Evaluasi Rasio M_y dikurang N_x",
        "text": (
            "Sekarang kita evaluasi rumus selisih: M y dikurang N x dibagi N. "
            "Pembilang kurung tiga x ditambah dua y dikurang kurung dua x ditambah y menghasilkan x ditambah y. "
            "Penyebut difaktorkan menjadi x dikali kurung x ditambah y. "
            "Suku x ditambah y saling membagi, menyisakan fungsi sederhana satu per x. "
            "Ini adalah fungsi murni dari x!"
        )
    },
    {
        "slide_num": 29,
        "title": "Pertanyaan Kuis: Berapakah Faktor Integrasinya?",
        "chapter": "29. Pertanyaan Kuis Faktor Integrasi",
        "text": (
            "Berdasarkan hasil satu per x tadi, berapakah nilai Faktor Integrasi mu x yang tepat?"
        )
    },
    {
        "slide_num": 30,
        "title": "Jawaban & Penjelasan Kuis",
        "chapter": "30. Jawaban Kuis & Verifikasi",
        "text": (
            "Jawabannya adalah mu x sama dengan x! "
            "Mari kita buktikan: mu x sama dengan e pangkat integral satu per x d x. "
            "Integral dari satu per x adalah logaritma natural x. "
            "Karena eksponensial dari len x saling meniadakan, hasilnya persis sama dengan x. "
            "Jika seluruh persamaan diferensial awal tadi kita kalikan dengan x, "
            "persamaan tersebut seketika menjadi eksak dan mudah diselesaikan!"
        )
    },
    {
        "slide_num": 31,
        "title": "Rangkuman Perkuliahan Minggu 02 & Penutup",
        "chapter": "31. Rangkuman Perkuliahan Minggu 02 & Penutup",
        "text": (
            "Sebagai rangkuman perkuliahan minggu kedua: "
            "Persamaan separabel diselesaikan dengan mengisolasi variabel sejenis ke ruas yang sama sebelum integrasi. "
            "Persamaan eksak memerlukan pemenuhan syarat turunan parsial silang dan berkaitan erat dengan medan potensial konservatif. "
            "Serta faktor integrasi adalah kunci pembuka untuk mengubah persamaan non-eksak menjadi eksak secara matematis. "
            "Silakan unduh salindia PDF, pelajari modul lengkap, dan kerjakan Lembar Kerja Mahasiswa serta Problem Set Minggu dua. "
            "Pada minggu ketiga, kita akan mengaplikasikan seluruh metode PDB orde satu ini pada analisis transien rangkaian listrik RC dan RL. "
            "Saya, Insinyur Novalio Daratha bersama Bapak Muhammad Arfan, terima kasih atas fokus dan semangat belajar Anda, dan Wassalamu'alaikum warahmatullahi wabarakatuh."
        )
    }
]

VOICE = "id-ID-ArdiNeural"
OUTPUT_DIR = "scratch/audio_w02"
FRAMES_DIR = "scratch/slide_frames_w02"
VIDEO_OUT = "scratch/video_pd_minggu02.mp4"
ROOT_VIDEO = "video_pd_minggu02.mp4"
SCRIPT_MD = "video_script_pd_w02.md"

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
    
    print(f"=== 1. SINTESIS AUDIO PER SALINDIA MINGGU 02 ({len(slides_data)} SLIDES) ===")
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
        f.write("# Naskah & Metadata Video Kuliah Minggu 02: Persamaan Diferensial\n\n")
        f.write("### 1. Metadata Siap Unggah YouTube (SEO Optimized)\n\n")
        f.write("**Judul Video (Opsi 1 - Utama):**\n")
        f.write("`[Minggu 02] PDB Orde 1: Persamaan Separabel, Eksak & Faktor Integrasi | Persamaan Diferensial`\n\n")
        f.write("**Judul Alternatif:**\n")
        f.write("`Kuliah 02 Persamaan Diferensial: Metode Separabel, Uji Eksak Turunan Silang, dan Faktor Integrasi`\n\n")
        f.write("**Deskripsi Siap Unggah:**\n")
        f.write("```text\n")
        f.write("Kuliah Daring Minggu 02 - Persamaan Diferensial (Teknik Elektro UNIB)\n")
        f.write("Topik: Persamaan Diferensial Biasa (PDB) Orde Satu: Bentuk Diferensial M dx + N dy = 0, Metode Separabel, Uji Ke-Eksak-an Turunan Silang (Medan Konservatif), Rekonstruksi Potensial, dan Penentuan Faktor Integrasi.\n\n")
        f.write("Dosen Pengampu:\n")
        f.write("- Ir. Novalio Daratha, S.T., M.Sc., Ph.D.\n")
        f.write("- Muhammad Arfan, S.T., M.T.\n")
        f.write("Program Studi S1 Teknik Elektro, Jurusan Teknik Elektro & Informatika\n")
        f.write("Fakultas Teknik, Universitas Bengkulu\n\n")
        f.write("Akses portal perkuliahan, modul ajar, lembar kerja C1-C6, dan problem set:\n")
        f.write("https://www.ndaratha.my.id/persamaan-diferensial/\n\n")
        f.write("Linimasa Bab (Timestamps):\n")
        for ts, ch, d, tit in timestamps:
            f.write(f"{ts} - {ch}\n")
        f.write("\nBuku Referensi Pembelajaran:\n")
        f.write("1. Erwin Kreyszig, Advanced Engineering Mathematics, 10th Ed., John Wiley & Sons.\n")
        f.write("2. Dennis G. Zill, A First Course in Differential Equations with Modeling Applications, Cengage.\n")
        f.write("3. William H. Hayt & John A. Buck, Engineering Electromagnetics, McGraw-Hill.\n\n")
        f.write("#TeknikElektro #PersamaanDiferensial #UniversitasBengkulu #PDBOrde1 #Separabel #PersamaanEksak #FaktorIntegrasi #MedanKonservatif #KalkulusLanjut #TeknikElektroUNIB\n")
        f.write("```\n\n")
        f.write("### 2. Naskah Audio Narasi Per Salindia\n\n")
        for item in slides_data:
            f.write(f"#### Salindia {item['slide_num']:02d}: {item['title']}\n\n")
            f.write(f"{item['text']}\n\n")

    print(f"Naskah YouTube tersimpan di: {SCRIPT_MD}")

    # Build klip video per salindia
    CLIPS_DIR = "scratch/clips_w02"
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
    print(f"\n[SUKSES] Video Minggu 02 berhasil dirakit!")
    print(f"  Lokasi berkas : {VIDEO_OUT}")
    print(f"  Ukuran berkas : {file_size_mb:.2f} MB")
    print(f"  Waktu render  : {t1 - t0:.2f} detik")

    # Salin ke root untuk referensi
    subprocess.run(["cp", VIDEO_OUT, ROOT_VIDEO], check=True)
    print(f"  Tersalin ke   : {ROOT_VIDEO}")

if __name__ == "__main__":
    asyncio.run(main())
