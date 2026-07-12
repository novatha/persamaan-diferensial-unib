import os
import re

def convert():
    os.makedirs('docs', exist_ok=True)
    
    for i in range(1, 16):
        tex_file = f'modul_{i}.tex'
        md_file = f'docs/modul_{i}.md'
        
        if os.path.exists(tex_file):
            with open(tex_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic conversions
            # Replace \section{...} with # ...
            content = re.sub(r'\\section\{([^}]+)\}', r'# \1', content)
            # Replace \section*{...} as well just in case
            content = re.sub(r'\\section\*\{([^}]+)\}', r'# \1', content)
            
            # Replace \subsection{...} with ## ...
            content = re.sub(r'\\subsection\{([^}]+)\}', r'## \1', content)
            content = re.sub(r'\\subsection\*\{([^}]+)\}', r'## \1', content)
            
            # Math equations $$...$$ are kept intact automatically by not changing them
            
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Converted {tex_file} to {md_file}')
        else:
            print(f'{tex_file} does not exist. Skipping.')

if __name__ == '__main__':
    convert()
