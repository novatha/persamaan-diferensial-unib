import os
import re
import time
from playwright.sync_api import sync_playwright

def upload_file(page, section_id, filepath, title, desc):
    print(f"Mengunggah {title} ke Topik {section_id}...")
    try:
        if "edit=1" not in page.url and "course/view.php" not in page.url:
            page.goto("https://elearning.unib.ac.id/course/view.php?id=5383", timeout=60000)
            time.sleep(1)

        section_locator = page.locator(f"li#section-{section_id}")
        section_locator.scroll_into_view_if_needed()
        time.sleep(1)
        
        add_btn = section_locator.get_by_role("link", name=re.compile("Tambahkan sebuah aktivitas", re.IGNORECASE)).first
        add_btn.click()
        
        time.sleep(1.5)
        page.locator("span").filter(has_text=re.compile(r"^Berkas$", re.IGNORECASE)).first.click()
        page.get_by_role("button", name=re.compile("Tambahkan", re.IGNORECASE)).first.click()
        
        time.sleep(2)
        try:
            page.get_by_role("textbox", name=re.compile("Nama", re.IGNORECASE)).first.fill(title)
        except:
            page.locator("input[name='name']").fill(title)
            
        try:
            page.get_by_role("textbox", name=re.compile("Deskripsi", re.IGNORECASE)).first.fill(desc)
        except:
            pass 
            
        page.locator(".dndupload-arrow").first.click()
        time.sleep(2)
        
        try:
            page.get_by_role("button", name=re.compile("Lampiran", re.IGNORECASE)).first.click(timeout=1000)
        except:
            pass
            
        try:
            page.get_by_role("button", name=re.compile("Lampiran", re.IGNORECASE)).first.set_input_files(filepath, timeout=2000)
        except:
            page.locator("input[type='file']").first.set_input_files(filepath)
            
        page.get_by_role("button", name=re.compile("Unggah file ini", re.IGNORECASE)).first.click()
        
        time.sleep(4) # Beri waktu lebih lama
        
        page.get_by_role("button", name=re.compile("Simpan dan kembali", re.IGNORECASE)).first.click()
        time.sleep(3)
        print(f" > BERHASIL: {title}")
        
    except Exception as e:
        print(f" > GAGAL: {title} | Error: {str(e)[:50]}...")
        page.goto("https://elearning.unib.ac.id/course/view.php?id=5383", timeout=60000)
        time.sleep(2)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        # Set default timeout lebih lama karena server agak lambat
        context.set_default_timeout(60000) 
        page = context.new_page()

        print("Melakukan Login otomatis (Resume)...")
        page.goto("https://elearning.unib.ac.id/login/index.php", timeout=60000)
        page.get_by_placeholder("Masukkan NIP/NIM").fill("197911132003121002")
        page.get_by_placeholder("Password").fill("N0v4th4#")
        page.locator("#submit").click()
        time.sleep(3)
        
        print("Membuka Halaman Course...")
        page.goto("https://elearning.unib.ac.id/course/view.php?id=5383", timeout=60000)
        time.sleep(3)
        
        print("Menghidupkan Mode Ubah...")
        try:
            page.get_by_role("link", name=re.compile("Hidupkan Mode Ubah", re.IGNORECASE)).first.click(timeout=3000)
            time.sleep(2)
        except:
            pass
            
        # HANYA FILE YANG TERSISA (Minggu 14 - 16)
        files = [
            (14, "problem_set14.pdf", "Tugas Terstruktur", "Instrumen evaluasi bab 14"),
            (14, "worksheet14.pdf", "Lembar Kerja Mahasiswa (LKM) Minggu 14", "LKM evaluasi kelas bab 14"),
            (15, "ch15.pdf", "Slide Presentasi Minggu 15", "Slide perkuliahan bab 15"),
            (15, "modul_15.pdf", "Modul Bacaan Minggu 15", "Bahan bacaan mandiri mahasiswa bab 15"),
            (15, "problem_set15.pdf", "Panduan Team-Based Project", "Instrumen evaluasi bab 15"),
            (15, "worksheet15.pdf", "Lembar Kerja Mahasiswa (LKM) Minggu 15", "LKM evaluasi kelas bab 15"),
            (16, "uas.pdf", "Soal Ujian Akhir Semester (UAS)", "Bahan evaluasi UAS")
        ]

        base_dir = "/Users/novaliodaratha/Documents/2026/mengajar/Persamaan Diferensial"
        
        for sec, filename, title, desc in files:
            filepath = os.path.join(base_dir, filename)
            if os.path.exists(filepath):
                upload_file(page, sec, filepath, title, desc)
                
        print("\nSISA FILE TELAH SELESAI DIUNGGAH!")
        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    main()
