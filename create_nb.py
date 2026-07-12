import nbformat as nbf
import os

nb = nbf.v4.new_notebook()

text1 = r"""# ⚡ Simulasi Transien Rangkaian RLC Seri (Interaktif)
Selamat datang di modul simulasi komputasi untuk **Persamaan Diferensial Orde 2** pada aplikasi rangkaian RLC seri.

## 📌 Persamaan Diferensial
Berdasarkan Hukum Tegangan Kirchhoff (KVL) pada rangkaian RLC seri tanpa sumber tegangan luar (respons alami):
$$ L \frac{d^2i}{dt^2} + R \frac{di}{dt} + \frac{1}{C} i = 0 $$

Tingkat peredaman (*damping*) rangkaian ditentukan oleh parameter $R$, $L$, dan $C$:
- **Underdamped (Kurang Redam):** Berosilasi sebelum stabil menuju nol.
- **Critically Damped (Redam Kritis):** Menurun menuju nol paling cepat tanpa berosilasi.
- **Overdamped (Lebih Redam):** Menurun menuju nol secara perlahan tanpa berosilasi.

### 🚀 Instruksi:
Jalankan *cell* kode di bawah ini dengan menekan tombol **Play** (atau `Shift + Enter`). Setelah itu, Anda bisa **menggeser slider** nilai $R, L,$ dan $C$ secara interaktif untuk melihat bagaimana kurva peredaman berubah secara *real-time*!"""

code1 = r"""import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import ipywidgets as widgets
from IPython.display import display

# Fungsi PDB Orde 2 (dipecah menjadi sistem orde 1)
def rlc_circuit(y, t, R, L, C):
    i, didt = y
    d2idt2 = -(R/L)*didt - (1/(L*C))*i
    return [didt, d2idt2]

# Fungsi visualisasi dan analisis damping
def plot_rlc(R=20, L=1.0, C=0.01):
    t = np.linspace(0, 1.5, 500)
    # Kondisi awal: Arus awal = 0, Laju perubahan arus = 10 A/s
    y0 = [0.0, 10.0]
    
    # Selesaikan PDB
    sol = odeint(rlc_circuit, y0, t, args=(R, L, C))
    i = sol[:, 0]
    
    # Hitung koefisien redaman dan frekuensi natural
    alpha = R / (2 * L)
    omega_0 = 1 / np.sqrt(L * C)
    
    if alpha < omega_0:
        status = "Underdamped (Kurang Redam)"
        color = 'royalblue'
    elif np.isclose(alpha, omega_0, rtol=1e-2):
        status = "Critically Damped (Redam Kritis)"
        color = 'forestgreen'
    else:
        status = "Overdamped (Lebih Redam)"
        color = 'crimson'
        
    plt.figure(figsize=(10, 5))
    plt.plot(t, i, label=f'Arus $i(t)$ - {status}', color=color, linewidth=2.5)
    plt.axhline(0, color='black', linewidth=1, linestyle='--')
    
    # PERBAIKAN: Menggunakan raw f-string (rf"") agar LaTeX \alpha dan \omega dibaca dengan benar
    plt.title(rf'Respons Transien RLC Seri ($\alpha={alpha:.2f}$, $\omega_0={omega_0:.2f}$)', fontsize=14, fontweight='bold')
    
    plt.xlabel('Waktu $t$ (detik)', fontsize=12)
    plt.ylabel('Arus $i(t)$ (Ampere)', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(fontsize=12, loc='upper right')
    plt.xlim(0, 1.5)
    plt.ylim(-0.5, max(i)+0.5)
    plt.show()

# Membuat antarmuka UI Slider
widgets.interact(plot_rlc, 
                 R=widgets.FloatSlider(value=10, min=0, max=50, step=1, description='R (Ohm):'),
                 L=widgets.FloatSlider(value=1.0, min=0.1, max=5.0, step=0.1, description='L (Henry):'),
                 C=widgets.FloatSlider(value=0.01, min=0.001, max=0.1, step=0.001, description='C (Farad):', readout_format='.3f'))
"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(text1),
    nbf.v4.new_code_cell(code1)
]

output_path = '/Users/novaliodaratha/Documents/2026/mengajar/Persamaan Diferensial/Simulasi_Transien_RLC.ipynb'
with open(output_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
print(f"File Jupyter Notebook berhasil diperbarui: {output_path}")
