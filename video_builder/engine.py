#!/usr/bin/env python3
"""
video_builder/engine.py — Batch Engine Pabrikasi Video Perkuliahan v2.0
Mata Kuliah: Persamaan Diferensial (Teknik Elektro UNIB)
Dosen Pengampu: Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.

Spesifikasi:
- Visual: 300 DPI Beamer Madrid 16:9 dari chN.pdf
- Audio: Stereo AAC 192k (44.1 kHz, 2 ch) via edge-tts 'id-ID-ArdiNeural'
- Encoding: 1080p Full HD (1920x1080), H.264 CRF 18, multi-core parallel rendering
- Kuis: 8s silence pause terprogram pada Slide 14
- Sinkronisasi: portal/public/video/video_pd_mingguXX.mp4 dan video_script_pd_wXX_v2.md
"""

import os
import sys
import time
import shutil
import asyncio
import subprocess
from concurrent.futures import ThreadPoolExecutor
import edge_tts

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRATCH_ROOT = os.path.join(PROJ_DIR, "scratch")
PORTAL_DIR = os.path.join(PROJ_DIR, "portal", "public", "video")
QUIZ_PAUSE_MP3 = os.path.join(SCRATCH_ROOT, "quiz_pause_8s.mp3")
VOICE = "id-ID-ArdiNeural"

os.makedirs(SCRATCH_ROOT, exist_ok=True)
os.makedirs(PORTAL_DIR, exist_ok=True)

def run_cmd(cmd, cwd=None):
    res = subprocess.run(cmd, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Command failed: {cmd}\nError: {res.stderr}")
    return res.stdout

async def synth_tts(text, outfile):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(outfile)

def get_duration(audio_file):
    out = run_cmd(f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{audio_file}"')
    return float(out.strip())

PAD_DUR = 1.0  # Jeda pergantian salindia 1.0 s sesuai standar AGENTS.md

def ensure_quiz_pause():
    if not os.path.exists(QUIZ_PAUSE_MP3):
        run_cmd(f'ffmpeg -y -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 -t 8 -c:a libmp3lame -b:a 192k "{QUIZ_PAUSE_MP3}"')

def render_single_clip(args):
    img, aud, clip_out, exact_dur = args
    # Menjamin 0 ms audio-video drift: durasi video dan audio identik hingga ke frame 25 fps
    cmd = (
        f'ffmpeg -y -loop 1 -r 25 -i "{img}" -i "{aud}" '
        f'-af "apad,atrim=0:{exact_dur:.4f}" '
        f'-c:v libx264 -preset faster -crf 18 -pix_fmt yuv420p -r 25 '
        f'-vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p" '
        f'-c:a aac -b:a 192k -ac 2 -ar 44100 '
        f'-t {exact_dur:.4f} "{clip_out}"'
    )
    run_cmd(cmd)
    return clip_out

def build_week_video(week_data, workers=4):
    wk = week_data["week_num"].zfill(2)
    pdf_file = week_data["pdf_path"]
    title_full = week_data["title"]
    subtitle = week_data["subtitle"]
    cpmk_list = week_data["cpmk"]
    slides = week_data["slides"]

    scratch_w = os.path.join(SCRATCH_ROOT, f"w{wk}_v2")
    os.makedirs(scratch_w, exist_ok=True)
    ensure_quiz_pause()

    final_root_video = os.path.join(PROJ_DIR, f"video_pd_minggu{wk}.mp4")
    final_portal_video = os.path.join(PORTAL_DIR, f"video_pd_minggu{wk}.mp4")
    script_md = os.path.join(PROJ_DIR, f"video_script_pd_w{wk}_v2.md")

    print("\n" + "=" * 65)
    print(f" MEMBANGUN VIDEO MINGGU {wk}: {title_full}")
    print("=" * 65)
    t0 = time.time()

    # 1. Ekstraksi Salindia PDF Beamer 300 DPI
    print(f"[1/5] Ekstraksi slide {pdf_file} ke PNG 300 DPI...")
    run_cmd(f'pdftoppm -r 300 -png "{pdf_file}" "{os.path.join(scratch_w, "frame")}"')
    frames = sorted([f for f in os.listdir(scratch_w) if f.startswith("frame-") and f.endswith(".png")])
    if len(frames) != len(slides):
        print(f"  [PERINGATAN] Jumlah frame ({len(frames)}) != jumlah salindia ({len(slides)})")

    # 2. TTS Narasi Suara Alami (Konkuren dengan asyncio.gather)
    print(f"[2/5] Sintesis TTS id-ID-ArdiNeural paralel ({len(slides)} salindia)...")
    
    async def synth_all_tts():
        tasks = []
        for item in slides:
            sn = item["num"]
            if not item.get("quiz", False):
                afile = os.path.join(scratch_w, f"tts_{sn:02d}.mp3")
                if not os.path.exists(afile):
                    tasks.append(synth_tts(item["text"], afile))
            else:
                afile_p1 = os.path.join(scratch_w, f"tts_{sn:02d}_p1.mp3")
                afile_p2 = os.path.join(scratch_w, f"tts_{sn:02d}_p2.mp3")
                if not os.path.exists(afile_p1):
                    tasks.append(synth_tts(item["text_part1"], afile_p1))
                if not os.path.exists(afile_p2):
                    tasks.append(synth_tts(item["text_part2"], afile_p2))
        if tasks:
            await asyncio.gather(*tasks)

    t_tts = time.time()
    asyncio.run(synth_all_tts())
    print(f"  -> Sintesis TTS paralel selesai dalam {time.time() - t_tts:.1f} detik.")

    audio_files = []
    durations = []
    for item in slides:
        sn = item["num"]
        if not item.get("quiz", False):
            afile = os.path.join(scratch_w, f"tts_{sn:02d}.mp3")
            audio_files.append(afile)
            dur_aud = get_duration(afile)
        else:
            afile_p1 = os.path.join(scratch_w, f"tts_{sn:02d}_p1.mp3")
            afile_p2 = os.path.join(scratch_w, f"tts_{sn:02d}_p2.mp3")
            afile_comb = os.path.join(scratch_w, f"tts_{sn:02d}_combined.mp3")
            if not os.path.exists(afile_comb):
                concat_quiz = os.path.join(scratch_w, "quiz_concat.txt")
                with open(concat_quiz, "w") as f:
                    f.write(f"file '{afile_p1}'\nfile '{QUIZ_PAUSE_MP3}'\nfile '{afile_p2}'\n")
                run_cmd(f'ffmpeg -y -f concat -safe 0 -i "{concat_quiz}" -c copy "{afile_comb}"')
            audio_files.append(afile_comb)
            dur_aud = get_duration(afile_comb)

        # Hitung durasi presisi 25 fps + jeda hening pergantian slide (0 ms audio-video drift)
        raw_target = dur_aud + PAD_DUR
        num_frames = int(round(raw_target * 25))
        exact_dur = num_frames / 25.0
        durations.append(exact_dur)

    total_duration = sum(durations)
    mm, ss = divmod(int(total_duration), 60)
    print(f"  -> Total Estimasi Durasi: {mm:02d}:{ss:02d} ({total_duration:.2f} s)")

    # 3. Parallel Rendering Klip (Multi-Core)
    print(f"[3/5] Encoding {len(slides)} Klip MP4 1080p CRF 18 (Parallel {workers} Workers)...")
    clip_tasks = []
    for i, item in enumerate(slides):
        sn = item["num"]
        fidx = min(i, len(frames)-1)
        img = os.path.join(scratch_w, frames[fidx])
        aud = audio_files[i]
        dur = durations[i]
        clip_out = os.path.join(scratch_w, f"clip_{sn:02d}.mp4")
        clip_tasks.append((img, aud, clip_out, dur))

    t_render = time.time()
    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(render_single_clip, clip_tasks))
    print(f"  -> Rendering paralel selesai dalam {time.time() - t_render:.1f} detik.")

    # 4. Concat Final
    print(f"[4/5] Menggabungkan klip video final...")
    concat_txt = os.path.join(scratch_w, "concat_final.txt")
    with open(concat_txt, "w") as f:
        for c in results:
            f.write(f"file '{c}'\n")

    run_cmd(f'ffmpeg -y -f concat -safe 0 -i "{concat_txt}" -c copy "{final_root_video}"')
    shutil.copy2(final_root_video, final_portal_video)
    print(f"  -> Video Utama : {final_root_video}")
    print(f"  -> Portal Video: {final_portal_video}")

    # 5. Metadata YouTube
    print(f"[5/5] Membuat naskah metadata YouTube...")
    timestamps = []
    accum = 0.0
    for i, item in enumerate(slides):
        t_m, t_s = divmod(int(accum), 60)
        timestamps.append(f"{t_m:02d}:{t_s:02d} - {item['chapter']}")
        accum += durations[i]

    cpmk_text = "\n".join([f"- **{c[0]} ({c[1]}):** {c[2]}" for c in cpmk_list])

    script_content = f"""# Naskah & Metadata Video Kuliah Minggu {wk}: Persamaan Diferensial v2.0

### 1. Metadata Siap Unggah YouTube (SEO Optimized)

**Judul Resmi:** `[Minggu {wk}] {title_full} | Persamaan Diferensial | Teknik Elektro UNIB`

**Deskripsi Siap Unggah:**
```text
Kuliah Daring Minggu {wk} - Persamaan Diferensial (Teknik Elektro UNIB)
Topik: {subtitle}

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
4. Standar Industri Terkait (IEEE & IEC).

#PersamaanDiferensial #TeknikElektro #UniversitasBengkulu #KalkulusLanjut #DifferentialEquations #JuliaLang
```

---

## 2. Capaian Pembelajaran (Sub-CPMK {int(wk)} OBE Taksonomi Bloom)
{cpmk_text}

---

## 3. Naskah Audio Narasi Per Salindia (15 Slide Lengkap)

"""
    for item in slides:
        sn = item["num"]
        script_content += f"### Salindia {sn:02d}: {item['title']}\n\n"
        if not item.get("quiz", False):
            script_content += f"{item['text']}\n\n"
        else:
            script_content += f"**[Bagian 1 - Pertanyaan Kuis]:**\n{item['text_part1']}\n\n"
            script_content += f"*[Jeda Hening Berpikir: 8 Detik Terprogram]*\n\n"
            script_content += f"**[Bagian 2 - Pembahasan Kuis & Tantangan Bloom]:**\n{item['text_part2']}\n\n"

    with open(script_md, "w") as f:
        f.write(script_content)
    print(f"  -> Naskah Berhasil Disimpan: {script_md}")

    t_total = time.time() - t0
    m_tot, s_tot = divmod(int(t_total), 60)
    print(f"[SELESAI] Minggu {wk} Sukses dalam {m_tot:02d}:{s_tot:02d}! Durasi: {mm:02d}:{ss:02d}")
    return True
