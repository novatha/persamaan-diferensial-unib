#!/usr/bin/env python3
"""
video_builder/run_batch.py — Batch Runner Video Perkuliahan PD v2.0 (Minggu 03–15)
Teknik Elektro UNIB — Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.

Penggunaan:
  python3 video_builder/run_batch.py          # Jalankan semua minggu yang tersisa (W03 s.d. W15)
  python3 video_builder/run_batch.py 04 05    # Jalankan minggu tertentu saja
"""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from video_builder.engine import build_week_video
from video_builder.data_w01 import DATA as W01
from video_builder.data_w02 import DATA as W02
from video_builder.data_w03 import DATA as W03
from video_builder.data_w04 import DATA as W04
from video_builder.data_w05 import DATA as W05
from video_builder.data_w06 import DATA as W06
from video_builder.data_w07 import DATA as W07
from video_builder.data_w09 import DATA as W09
from video_builder.data_w10 import DATA as W10
from video_builder.data_w11 import DATA as W11
from video_builder.data_w12 import DATA as W12
from video_builder.data_w13 import DATA as W13
from video_builder.data_w14 import DATA as W14
from video_builder.data_w15 import DATA as W15

ALL_WEEKS = {
    "01": W01,
    "02": W02,
    "03": W03,
    "04": W04,
    "05": W05,
    "06": W06,
    "07": W07,
    "09": W09,
    "10": W10,
    "11": W11,
    "12": W12,
    "13": W13,
    "14": W14,
    "15": W15,
}

def main():
    target_keys = [arg.zfill(2) for arg in sys.argv[1:]] if len(sys.argv) > 1 else list(ALL_WEEKS.keys())
    target_keys = [k for k in target_keys if k in ALL_WEEKS]

    print("=" * 70)
    print(" BATCH PABRIKASI VIDEO PERKULIAHAN v2.0 (TEKNIK ELEKTRO UNIB)")
    print(f" Target Minggu: {', '.join(target_keys)}")
    print(f" Total Target : {len(target_keys)} video perkuliahan")
    print("=" * 70)

    t_start = time.time()
    results = {}

    for k in target_keys:
        week_data = ALL_WEEKS[k]
        try:
            print(f"\n>>> MEMULAI MINGGU {k}...")
            build_week_video(week_data, workers=4)
            results[k] = "SUKSES"
        except Exception as e:
            results[k] = f"GAGAL: {e}"
            print(f"[ERROR] Gagal memproses Minggu {k}: {e}")

    t_elapsed = time.time() - t_start
    m_el, s_el = divmod(int(t_elapsed), 60)

    print("\n" + "=" * 70)
    print(f" LAPORAN AKHIR BATCH PABRIKASI ({m_el:02d}:{s_el:02d})")
    print("=" * 70)
    for k, status in results.items():
        print(f"  Minggu {k}: {status}")
    print("=" * 70)

if __name__ == "__main__":
    main()
