import os
import re
import time
from playwright.sync_api import sync_playwright

def upload_file(page, section_id, filepath, title, desc):
    print(f"Mengunggah {title} ke Topik {section_id}...")
    try:
        # Pastikan halaman course terbuka
        if "edit=1" not in page.url and "course/view.php" not in page.url:
            page.goto("https://elearning.unib.ac.id/course/view.php?id=5383")
            time.sleep(1)

        # Cari container section berdasarkan ID
        section_locator = page.locator(f"li#section-{section_id}")
        
        # Scroll agar elemen terlihat
        section_locator.scroll_into_view_if_needed()
        time.sleep(0.5)
        
        # Klik Tambah Aktivitas
        add_btn = section_locator.get_by_role("link", name=re.compile("Tambahkan sebuah aktivitas", re.IGNORECASE)).first
        add_btn.click()
        
        # Modal muncul, pilih Berkas
        time.sleep(1)
        page.locator("span").filter(has_text=re.compile(r"^Berkas$", re.IGNORECASE)).first.click()
        page.get_by_role("button", name=re.compile("Tambahkan", re.IGNORECASE)).first.click()
        
        # Form Berkas
        time.sleep(1.5)
        try:
            page.get_by_role("textbox", name=re.compile("Nama", re.IGNORECASE)).first.fill(title)
        except:
            page.locator("input[name='name']").fill(title)
            
        try:
            page.get_by_role("textbox", name=re.compile("Deskripsi", re.IGNORECASE)).first.fill(desc)
        except:
            pass # abaikan deskripsi jika sulit
            
        # Dialog file upload
        page.locator(".dndupload-arrow").first.click()
        time.sleep(1.5)
        
        # Upload dari picker
        try:
            # Fallback 1: Klik tombol lampiran dulu
            page.get_by_role("button", name=re.compile("Lampiran", re.IGNORECASE)).first.click(timeout=1000)
        except:
            pass
            
        try:
            # Sesuai rekaman
            page.get_by_role("button", name=re.compile("Lampiran", re.IGNORECASE)).first.set_input_files(filepath, timeout=2000)
        except:
            # Fallback universal
            page.locator("input[type='file']").first.set_input_files(filepath)
            
        # Eksekusi unggah
        page.get_by_role("button", name=re.compile("Unggah file ini", re.IGNORECASE)).first.click()
        
        # Tunggu progress bar
        time.sleep(3)
        
        # Submit
        page.get_by_role("button", name=re.compile("Simpan dan kembali", re.IGNORECASE)).first.click()
        time.sleep(2)
        print(f" > BERHASIL: {title}")
        
    except Exception as e:
        print(f" > GAGAL: {title} | Error: {str(e)[:50]}...")
        # Reset posisi jika nyangkut
        page.goto("https://elearning.unib.ac.id/course/view.php?id=5383")
        time.sleep(2)

def main():
    with sync_playwright() as p:
        # Buka browser agar pengguna bisa melihat keajaibannya
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()

        print("Melakukan Login otomatis...")
        page.goto("https://elearning.unib.ac.id/login/index.php")
        page.get_by_placeholder("Masukkan NIP/NIM").fill("197911132003121002")
        page.get_by_placeholder("Password").fill("N0v4th4#")
        page.locator("#submit").click()
        time.sleep(3)
        
        print("Membuka Halaman Course...")
        page.goto("https://elearning.unib.ac.id/course/view.php?id=5383")
        time.sleep(2)
        
        print("Menghidupkan Mode Ubah...")
        try:
            page.get_by_role("link", name=re.compile("Hidupkan Mode Ubah", re.IGNORECASE)).first.click(timeout=3000)
            time.sleep(2)
        except:
            pass
            
        # Membuat daftar file
        files = []
        files.append((0, "RPS_Persamaan_Diferensial.pdf", "RPS Persamaan Diferensial", "Rencana Pembelajaran Semester PDB/PDP"))
        
        for i in range(1, 17):
            if i == 8:
                files.append((8, "uts.pdf", "Soal Ujian Tengah Semester (UTS)", "Bahan evaluasi UTS"))
                continue
            if i == 16:
                files.append((16, "uas.pdf", "Soal Ujian Akhir Semester (UAS)", "Bahan evaluasi UAS"))
                continue
                
            files.append((i, f"ch{i}.pdf", f"Slide Presentasi Minggu {i}", f"Slide perkuliahan bab {i}"))
            files.append((i, f"modul_{i}.pdf", f"Modul Bacaan Minggu {i}", f"Bahan bacaan mandiri mahasiswa bab {i}"))
            
            ps_title = "Tugas Terstruktur"
            if i in [3, 5, 11]:
                ps_title = f"Case Method (Tugas Kelompok) Minggu {i}"
            elif i == 15:
                ps_title = "Panduan Team-Based Project"
            files.append((i, f"problem_set{i}.pdf", ps_title, f"Instrumen evaluasi bab {i}"))
            
            files.append((i, f"worksheet{i}.pdf", f"Lembar Kerja Mahasiswa (LKM) Minggu {i}", f"LKM evaluasi kelas bab {i}"))

        base_dir = "/Users/novaliodaratha/Documents/2026/mengajar/Persamaan Diferensial"
        
        for sec, filename, title, desc in files:
            filepath = os.path.join(base_dir, filename)
            if os.path.exists(filepath):
                upload_file(page, sec, filepath, title, desc)
                
        print("\nSELURUH FILE TELAH SELESAI DIUNGGAH!")
        browser.close()

if __name__ == "__main__":
    main()
