import os
import re

base_dir = "/Users/novaliodaratha/Documents/2026/mengajar/Persamaan Diferensial"
docs_dir = os.path.join(base_dir, "docs")

for filename in os.listdir(docs_dir):
    if filename.endswith(".md"):
        tex_filename = filename.replace(".md", ".tex")
        tex_filepath = os.path.join(base_dir, tex_filename)
        md_filepath = os.path.join(docs_dir, filename)
        
        # Cari angka modul
        modul_num = re.findall(r'\d+', filename)
        num = modul_num[0] if modul_num else ""
        page_title = f"Modul {num}"
        
        # Coba ekstrak judul asli dari file .tex
        if os.path.exists(tex_filepath):
            with open(tex_filepath, "r", encoding="utf-8") as f_tex:
                tex_content = f_tex.read()
                # Cari tag \title{}
                match = re.search(r'\\title\{([^}]+)\}', tex_content)
                if match:
                    raw_title = match.group(1)
                    # Ganti LaTeX newline (\\) dengan spasi
                    raw_title = raw_title.replace(r'\\', ' - ')
                    
                    # Ambil bagian setelah "Minggu" jika ada
                    if "Minggu" in raw_title:
                        title_part = raw_title.split("Minggu")[-1].strip()
                        page_title = f"Modul {title_part}"
                    else:
                        page_title = raw_title
        
        # Baca konten markdown saat ini
        with open(md_filepath, "r", encoding="utf-8") as f_md:
            md_content = f_md.read()
            
        # Turunkan level heading lama (# Pendahuluan menjadi ## Pendahuluan)
        # Hal ini penting agar hanya ada satu H1 di setiap halaman (untuk MkDocs)
        md_content = re.sub(r'^# ', r'## ', md_content, flags=re.MULTILINE)
        
        # Tambahkan judul utama di paling atas
        final_content = f"# {page_title}\n\n{md_content}"
        
        with open(md_filepath, "w", encoding="utf-8") as f_md:
            f_md.write(final_content)
            
print("Judul berhasil diperbaiki!")
