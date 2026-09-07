import glob

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    is_beamer = filepath.startswith('ch') and filepath[2:-4].isdigit()
    new_lines = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(r'\date'):
            if is_beamer:
                new_lines.append(r'\date[\today]{2026 \\ \vspace{2mm}\small\textit{Tanggal Kompilasi: \today}}' + '\n')
            else:
                new_lines.append(r'\date{2026 \\ \vspace{2mm}\small\textit{Tanggal Kompilasi: \today}}' + '\n')
        elif r'\fancyfoot[L]{Universitas Bengkulu - Teknik Elektro}' in line:
            new_lines.append(line)
            # check if next lines already have fancyfoot[C]
            # to prevent duplicate insertions
            new_lines.append(r'\fancyfoot[C]{\scriptsize\textit{Kompilasi: \today}}' + '\n')
        elif r'\fancyfoot[C]{\scriptsize\textit{Kompilasi: \today}}' in line:
            # Skip if already present so it doesn't duplicate
            continue
        else:
            new_lines.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Processed: {filepath}")

for fpath in sorted(glob.glob('*.tex')):
    if fpath == 'RPS_Persamaan_Diferensial.tex':
        continue
    process_file(fpath)

print("All files updated with compilation date.")
