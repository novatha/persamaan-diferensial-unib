import os
import sys
import re
import json
import argparse
import time
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube"
]

CLIENT_SECRETS_FILE = "client_secrets.json"
TOKEN_FILE = "token.json"
PLAYLIST_TITLE = "Persamaan Diferensial - Teknik Elektro UNIB"

def get_authenticated_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        except Exception as e:
            print(f"Error loading token: {e}")
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing expired credentials...")
            creds.refresh(Request())
        else:
            if not os.path.exists(CLIENT_SECRETS_FILE):
                raise FileNotFoundError(f"Missing {CLIENT_SECRETS_FILE}!")
            print("Memulai proses otentikasi browser (OAuth 2.0)...")
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE,
                scopes=SCOPES
            )
            creds = flow.run_local_server(port=0, prompt="consent")
        
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
        print(f"[SUCCESS] Credentials saved to {TOKEN_FILE}")

    return build("youtube", "v3", credentials=creds)

def get_or_create_playlist(youtube):
    playlists = []
    next_page = None
    while True:
        res = youtube.playlists().list(part="snippet", mine=True, maxResults=50, pageToken=next_page).execute()
        playlists.extend(res.get("items", []))
        next_page = res.get("nextPageToken")
        if not next_page:
            break

    for pl in playlists:
        if "Persamaan Diferensial" in pl["snippet"]["title"]:
            return pl["id"]

    # Create new playlist if not found
    new_pl = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": PLAYLIST_TITLE,
                "description": "Mata Kuliah Persamaan Diferensial (Fokus Persiapan Medan Elektromagnetika & Rangkaian Listrik) - S1 Teknik Elektro Universitas Bengkulu. Dosen: Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T."
            },
            "status": {
                "privacyStatus": "public"
            }
        }
    ).execute()
    return new_pl["id"]

def add_video_to_playlist(youtube, playlist_id, video_id):
    try:
        youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
        ).execute()
        print(f"[PLAYLIST] Berhasil menambahkan video {video_id} ke playlist {playlist_id}")
    except HttpError as e:
        print(f"[PLAYLIST WARNING] Gagal menambahkan ke playlist: {e}")

def parse_metadata(week_num):
    script_file = f"video_script_pd_w{week_num:02d}_v2.md"
    if not os.path.exists(script_file):
        script_file = f"video_script_pd_w{week_num:02d}.md"
    if not os.path.exists(script_file):
        raise FileNotFoundError(f"Script metadata file not found: {script_file}")

    content = open(script_file, "r", encoding="utf-8").read()

    # Title extraction
    title = None
    m1 = re.search(r"\*\*Judul[^:]*:\*\*\s*[`]+([^`\n]+)[`]+", content)
    if m1:
        title = m1.group(1).strip()
    else:
        m2 = re.search(r"Judul[^\n]*\n+```[a-z]*\n([^\n]+)\n```", content)
        if m2:
            title = m2.group(1).strip()

    if not title:
        title = f"[Minggu {week_num:02d}] Kuliah Persamaan Diferensial | Teknik Elektro UNIB"

    # Enforce YouTube 100 character limit strictly
    if len(title) > 100:
        if "|" in title:
            prefix, suffix = title.rsplit("|", 1)
            allowed_len = 100 - len(suffix) - 3
            title = f"{prefix[:allowed_len].strip()} |{suffix}"
        else:
            title = title[:97].strip() + "..."

    # Description extraction
    desc = None
    m_desc = re.search(r"Deskripsi[^\n]*\n(?:[^\n]*\n)?```text\n(.*?)\n```", content, re.DOTALL)
    if m_desc:
        desc = m_desc.group(1).strip()
    else:
        m_desc2 = re.search(r"Deskripsi.*?\n```.*?\n(.*?)\n```", content, re.DOTALL)
        if m_desc2:
            desc = m_desc2.group(1).strip()

    if not desc:
        desc = (
            f"Kuliah Daring Minggu {week_num:02d} - Persamaan Diferensial\n"
            f"Program Studi S1 Teknik Elektro, Universitas Bengkulu\n"
            f"Dosen Pengampu: Ir. Novalio Daratha, S.T., M.Sc., Ph.D. & Muhammad Arfan, S.T., M.T.\n"
            f"https://www.ndaratha.my.id/persamaan-diferensial/\n"
        )

    # Remove any stray angle brackets
    desc = desc.replace("<", "").replace(">", "")
    title = title.replace("<", "").replace(">", "")

    tags = [
        "Teknik Elektro", "Universitas Bengkulu", "Persamaan Diferensial",
        "PDB", "PDP", "Kalkulus Lanjut", "Initial Value Problem", "Hukum Kirchhoff",
        "Rangkaian Listrik", "Medan Elektromagnetika", "Novalio Daratha", "Muhammad Arfan"
    ]

    return title, desc, tags

def upload_video(youtube, week_num, privacy="public", dry_run=False):
    # Try finding video in root or scratch
    video_path = f"video_pd_minggu{week_num:02d}.mp4"
    if not os.path.exists(video_path):
        video_path = f"scratch/video_pd_minggu{week_num:02d}.mp4"
    
    if not os.path.exists(video_path):
        print(f"[SKIP] Berkas video untuk Minggu {week_num:02d} tidak ditemukan ({video_path})")
        return None

    title, description, tags = parse_metadata(week_num)

    file_size_mb = os.path.getsize(video_path) / (1024 * 1024)
    print(f"\n========================================================")
    print(f"SIAP MENGUNGGAH: MINGGU {week_num:02d}")
    print(f"File       : {video_path} ({file_size_mb:.2f} MB)")
    print(f"Judul ({len(title)} char): {title}")
    print(f"Privasi    : {privacy}")
    print(f"Tags       : {', '.join(tags[:6])}...")
    print(f"========================================================")

    if dry_run:
        print("[DRY-RUN] Uji coba berhasil tanpa mengunggah ke YouTube.")
        return "DRY_RUN_ID"

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "27"  # Education
        },
        "status": {
            "privacyStatus": privacy,
            "selfDeclaredMadeForKids": False
        }
    }

    media = MediaFileUpload(
        video_path,
        mimetype="video/mp4",
        chunksize=1024*1024*4,  # 4MB chunks
        resumable=True
    )

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )

    print("Sedang mengunggah berkas video ke YouTube...")
    response = None
    start_time = time.time()
    while response is None:
        status, response = request.next_chunk()
        if status:
            pct = int(status.progress() * 100)
            print(f"  Progres unggahan: {pct}% ({status.resumable_progress / (1024*1024):.1f} MB)...")

    video_id = response.get("id")
    video_url = f"https://youtu.be/{video_id}"
    print(f"\n[SUKSES] Video Minggu {week_num:02d} berhasil diunggah!")
    print(f"Video ID   : {video_id}")
    print(f"URL Resmi  : {video_url}")
    print(f"Waktu      : {time.time() - start_time:.1f} detik")

    # Masukkan ke playlist resmi
    try:
        pl_id = get_or_create_playlist(youtube)
        add_video_to_playlist(youtube, pl_id, video_id)
    except Exception as e:
        print(f"[WARNING] Kendala playlist: {e}")

    # Perbarui metadata script dengan link YouTube resmi
    for s_name in [f"video_script_pd_w{week_num:02d}_v2.md", f"video_script_pd_w{week_num:02d}.md"]:
        if os.path.exists(s_name):
            s_content = open(s_name, "r", encoding="utf-8").read()
            if "**Tautan Resmi YouTube:**" not in s_content:
                s_content = s_content.replace(
                    "### 1. Metadata Siap Unggah YouTube (SEO Optimized)\n",
                    f"### 1. Metadata Siap Unggah YouTube (SEO Optimized)\n\n**Tautan Resmi YouTube:** [{video_url}]({video_url})  \n"
                )
                with open(s_name, "w", encoding="utf-8") as sf:
                    sf.write(s_content)

    return video_id

def main():
    parser = argparse.ArgumentParser(description="Otomasi Unggah Video Perkuliahan Persamaan Diferensial ke YouTube")
    parser.add_argument("--week", type=str, default="all", help="Nomor minggu (misal: 1 atau 'all' atau '1-7' atau '3,4,5')")
    parser.add_argument("--privacy", type=str, default="public", choices=["unlisted", "public", "private"], help="Visibilitas video (default: public)")
    parser.add_argument("--dry-run", action="store_true", help="Uji coba parsing tanpa mengunggah")
    parser.add_argument("--skip-existing", action="store_true", help="Lewati minggu yang sudah ada di uploaded_youtube_videos.json")
    args = parser.parse_args()

    youtube = None
    if not args.dry_run:
        youtube = get_authenticated_service()

    if args.week == "all":
        weeks = list(range(1, 8)) + list(range(9, 16))
    elif "-" in args.week:
        start, end = map(int, args.week.split("-"))
        weeks = list(range(start, end + 1))
    else:
        weeks = [int(w.strip()) for w in args.week.split(",")]

    results = {}
    json_path = "uploaded_youtube_videos.json"
    if os.path.exists(json_path):
        try:
            results = json.load(open(json_path))
        except Exception:
            results = {}

    for w in weeks:
        if args.skip_existing and str(w) in results:
            print(f"[SKIP] Minggu {w:02d} sudah terunggah sebelumnya: {results[str(w)]}")
            continue
        try:
            vid_id = upload_video(youtube, w, privacy=args.privacy, dry_run=args.dry_run)
            if vid_id and vid_id != "DRY_RUN_ID":
                results[str(w)] = f"https://youtu.be/{vid_id}"
                with open(json_path, "w", encoding="utf-8") as jf:
                    json.dump(results, jf, indent=2)
        except Exception as e:
            print(f"[ERROR] Gagal mengunggah Minggu {w}: {e}")

    print("\n========================================================")
    print("RINGKASAN UNGGAHAN YOUTUBE PERSAMAAN DIFERENSIAL:")
    for w, url in sorted(results.items(), key=lambda x: int(x[0])):
        print(f"Minggu {int(w):02d} : {url}")
    print("========================================================\n")

if __name__ == "__main__":
    main()
