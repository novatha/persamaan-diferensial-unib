import sys
from playwright.sync_api import sync_playwright

def main():
    print("Memulai Playwright Inspector...")
    with sync_playwright() as p:
        # Buka browser secara visual (headless=False)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Buka halaman e-learning
        course_url = "https://elearning.unib.ac.id/course/view.php?id=5383"
        print(f"Membuka {course_url}...")
        page.goto(course_url)
        
        print("\n========================================================")
        print("1. Silakan login ke e-learning UNIB di browser Chromium yang terbuka.")
        print("2. Gunakan jendela 'Playwright Inspector' yang muncul.")
        print("3. Pastikan tombol 'Record' (ikon lingkaran merah) di Inspector aktif.")
        print("4. Lakukan proses upload 1 buah file (misalnya file RPS) seperti biasa di browser.")
        print("5. Setelah selesai 1 file, COPY kode Python yang dihasilkan oleh Inspector, dan PASTE ke chat kita!")
        print("6. Anda boleh menutup browser setelah menyalin kodenya.")
        print("========================================================\n")
        
        # Membuka Playwright Inspector dan menghentikan eksekusi script
        # sampai user menekan tombol 'Resume' atau menutup browser
        page.pause()
        
        browser.close()

if __name__ == "__main__":
    main()
