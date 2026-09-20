#!/usr/bin/env python3
import subprocess
import pypdf
import os

weeks = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]

print(f"{'Week':<6} | {'Status':<6} | {'Pages':<6} | {'Overfull H':<10} | {'Overfull V':<10} | {'Notes'}")
print("-" * 65)

all_passed = True

for w in weeks:
    tex = f"problem_set{w}.tex"
    pdf = f"problem_set{w}.pdf"
    log = f"problem_set{w}.log"
    
    # 2 passes for cross-references / page numbers
    subprocess.run(["pdflatex", "-interaction=nonstopmode", tex], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    res = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Check page count
    pages = 0
    if os.path.exists(pdf):
        reader = pypdf.PdfReader(pdf)
        pages = len(reader.pages)
    
    # Check log for overfulls
    overfull_h = 0
    overfull_v = 0
    overfull_details = []
    if os.path.exists(log):
        with open(log, "r", encoding="latin-1") as f:
            for line in f:
                if "Overfull \\hbox" in line:
                    overfull_h += 1
                    overfull_details.append(line.strip())
                elif "Overfull \\vbox" in line:
                    overfull_v += 1
                    overfull_details.append(line.strip())
    
    status = "OK" if (res.returncode == 0 and pages == 2 and overfull_h == 0 and overfull_v == 0) else "WARN"
    notes = "Perfect (2 Pages, 0 Overfull)" if status == "OK" else f"Exit={res.returncode}"
    print(f"W{w:<5} | {status:<6} | {pages:<6} | {overfull_h:<10} | {overfull_v:<10} | {notes}")
    if overfull_details:
        for d in overfull_details[:3]:
            print(f"       -> {d}")
    
    if status != "OK":
        all_passed = False

print("-" * 65)
if all_passed:
    print("ALL 14 PROBLEM SETS PASSED VERIFICATION WITH ZERO OVERFULLS AND EXACTLY 2 PAGES!")
else:
    print("SOME PROBLEM SETS NEED ADJUSTMENT.")
