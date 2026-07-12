import os
import re

docs_dir = "/Users/novaliodaratha/Documents/2026/mengajar/Persamaan Diferensial/docs"

def clean_latex(content):
    # Buang semua header (preamble) sebelum \begin{document}
    if r"\begin{document}" in content:
        content = content.split(r"\begin{document}")[1]
        
    # Hapus command khusus dokumen LaTeX
    commands_to_remove = [
        r"\maketitle", r"\tableofcontents", r"\newpage", r"\end{document}",
        r"\begin{itemize}", r"\end{itemize}", r"\begin{enumerate}", r"\end{enumerate}"
    ]
    for cmd in commands_to_remove:
        content = content.replace(cmd, "")
        
    # Konversi \item menjadi list Markdown
    content = re.sub(r"\\item\s*", "- ", content)
    
    # Konversi \textbf{} menjadi bold markdown
    content = re.sub(r"\\textbf\{([^}]+)\}", r"**\1**", content)
    
    # Konversi \textit{} menjadi italic markdown
    content = re.sub(r"\\textit\{([^}]+)\}", r"*\1*", content)
    
    # Konversi section dan subsection yang mungkin terlewat
    content = re.sub(r"\\section\*?\{([^}]+)\}", r"# \1", content)
    content = re.sub(r"\\subsection\*?\{([^}]+)\}", r"## \1", content)
    content = re.sub(r"\\subsubsection\*?\{([^}]+)\}", r"### \1", content)
    
    # Perbaiki line breaks berlebih
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content.strip()

if os.path.exists(docs_dir):
    for filename in os.listdir(docs_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(docs_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            cleaned_content = clean_latex(content)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(cleaned_content)
                
    print("Berhasil membersihkan sisa kode LaTeX di semua file Markdown!")
else:
    print("Folder docs tidak ditemukan.")
