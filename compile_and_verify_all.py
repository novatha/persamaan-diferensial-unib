import subprocess
import os

weeks = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]

print("=" * 55)
print("STARTING BATCH COMPILATION AND VERIFICATION OF 14 DECKS")
print("=" * 55)

for w in weeks:
    tex_fn = f"ch{w}.tex"
    print(f"Compiling {tex_fn}...", end=" ", flush=True)
    res = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_fn],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print("FAILED!")
    else:
        print("SUCCESS!")

print("\n" + "=" * 55)
header = "{:<10} | {:<6} | {:<10} | {:<8}".format("File", "Pages", "Overfulls", "Status")
print(header)
print("-" * len(header))

all_ok = True
for w in weeks:
    pdf_name = f"ch{w}.pdf"
    log_name = f"ch{w}.log"
    pages = "0"
    try:
        out = subprocess.check_output(["pdfinfo", pdf_name], text=True)
        for line in out.splitlines():
            if "Pages:" in line:
                pages = line.split(":")[1].strip()
    except Exception as e:
        pages = "?"
    
    overfull_count = 0
    if os.path.exists(log_name):
        with open(log_name, "r", errors="ignore") as f:
            for line in f:
                if "Overfull \\hbox" in line or "Overfull \\vbox" in line:
                    overfull_count += 1
    
    status = "PERFECT" if pages == "15" and overfull_count == 0 else "CHECK"
    if status != "PERFECT":
        all_ok = False
    print("{:<10} | {:<6} | {:<10} | {:<8}".format(pdf_name, pages, overfull_count, status))

print("-" * len(header))
print("ALL 14 DECKS COMPILED WITH ZERO OVERFULLS & EXACTLY 15 PAGES:", all_ok)
print("=" * 55)
