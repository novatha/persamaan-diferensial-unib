import os
import re

def clean_latex_to_md(tex_content, week_num=None):
    # Extract Title if exists
    title_match = re.search(r'\\title\{([^}]+)\}', tex_content, re.DOTALL)
    doc_title = ""
    if title_match:
        raw_title = title_match.group(1)
        raw_title = raw_title.replace(r'\\', ' - ')
        raw_title = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})?', ' ', raw_title)
        doc_title = ' '.join(raw_title.split())
    elif week_num:
        doc_title = f"Modul Minggu {week_num}"
        
    # Extract content between \begin{document} and \end{document}
    doc_match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', tex_content, re.DOTALL)
    if doc_match:
        body = doc_match.group(1)
    else:
        body = tex_content

    # Remove \maketitle, \tableofcontents, \newpage, \vspace{...}
    body = re.sub(r'\\maketitle', '', body)
    body = re.sub(r'\\tableofcontents', '', body)
    body = re.sub(r'\\newpage', '', body)
    body = re.sub(r'\\vspace\{[^}]+\}', '', body)
    body = re.sub(r'\\def\\[a-zA-Z]+(\{[^}]*\})?', '', body)

    # Convert \begin{definition}[Title] ... \end{definition} -> Admonition note
    def def_repl(match):
        title = match.group(1).strip() if match.group(1) else "Definisi"
        content = match.group(2).strip()
        # clean line breaks in content
        content = re.sub(r'\\\\\s*', '\n\n', content)
        lines = [("    " + line if line.strip() else "") for line in content.split('\n')]
        return f'!!! info "{title}"\n' + '\n'.join(lines) + '\n\n'
        
    body = re.sub(r'\\begin\{definition\}(?:\[(.*?)\])?(.*?)\\end\{definition\}', def_repl, body, flags=re.DOTALL)

    # Convert \begin{example}[Title] ... \end{example} -> Admonition example
    def ex_repl(match):
        title = match.group(1).strip() if match.group(1) else "Contoh Soal"
        content = match.group(2).strip()
        content = re.sub(r'\\\\\s*', '\n\n', content)
        lines = [("    " + line if line.strip() else "") for line in content.split('\n')]
        return f'!!! example "{title}"\n' + '\n'.join(lines) + '\n\n'
        
    body = re.sub(r'\\begin\{example\}(?:\[(.*?)\])?(.*?)\\end\{example\}', ex_repl, body, flags=re.DOTALL)

    # Convert sections and subsections
    body = re.sub(r'\\section\*?\{([^}]+)\}', r'## \1', body)
    body = re.sub(r'\\subsection\*?\{([^}]+)\}', r'### \1', body)
    body = re.sub(r'\\subsubsection\*?\{([^}]+)\}', r'#### \1', body)

    # Convert formatting
    body = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', body)
    body = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', body)
    body = re.sub(r'\\texttt\{([^}]+)\}', r'`\1`', body)
    body = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', body)
    body = re.sub(r'\\_', '_', body)

    # Convert itemize and enumerate
    body = re.sub(r'\\begin\{itemize\}', '', body)
    body = re.sub(r'\\end\{itemize\}', '', body)
    body = re.sub(r'\\begin\{enumerate\}(?:\[.*?\])?', '', body)
    body = re.sub(r'\\end\{enumerate\}', '', body)
    body = re.sub(r'\\item\s+', r'- ', body)

    # Convert remaining double backslashes
    body = re.sub(r'\\\\\s*', '\n\n', body)

    # Clean multiple blank lines
    body = re.sub(r'\n{3,}', '\n\n', body).strip()

    header = f"# {doc_title}\n\n" if doc_title else ""
    return header + body + "\n"

def main():
    os.makedirs('docs', exist_ok=True)
    
    # Process modul 1 to 15
    for i in range(1, 16):
        if i == 8:
            continue
        tex_file = f'modul_{i}.tex'
        prefix = f"{i:02d}"
        md_file = f'docs/{prefix}_modul_{i}.md'
        
        if os.path.exists(tex_file):
            with open(tex_file, 'r', encoding='utf-8') as f:
                raw_tex = f.read()
            
            md_out = clean_latex_to_md(raw_tex, week_num=i)
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(md_out)
            print(f"Generated {md_file} from {tex_file}")
            
    # Process studi kasus modern if exists
    if os.path.exists('modul_studi_kasus_modern.tex'):
        with open('modul_studi_kasus_modern.tex', 'r', encoding='utf-8') as f:
            raw_tex = f.read()
        md_out = clean_latex_to_md(raw_tex)
        with open('docs/modul_studi_kasus_modern.md', 'w', encoding='utf-8') as f:
            f.write(md_out)
        print("Generated docs/modul_studi_kasus_modern.md")

if __name__ == '__main__':
    main()
