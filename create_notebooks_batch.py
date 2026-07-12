import nbformat as nbf
import os

def create_notebook(filename, cells):
    nb = nbf.v4.new_notebook()
    nb['cells'] = cells
    with open(filename, 'w') as f:
        nbf.write(nb, f)
    print(f"Created {filename}")

# Notebook 1: Simulasi Transien RC & RL
cells_rc_rl = [
    nbf.v4.new_markdown_cell("# Week 3: Simulasi Transien Rangkaian RC dan RL\n\nPersamaan diferensial orde pertama untuk rangkaian RC seri dan RL seri.\n\n## Rangkaian RC Seri\n$R \\frac{dq}{dt} + \\frac{q}{C} = V(t)$\n\nAtau dalam arus $I(t)$:\n$R I + \\frac{1}{C} \\int I dt = V(t) \\implies R \\frac{dI}{dt} + \\frac{I}{C} = \\frac{dV}{dt}$\n\n## Rangkaian RL Seri\n$L \\frac{dI}{dt} + R I = V(t)$"),
    nbf.v4.new_code_cell("""import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

def simulasi_rc_rl(R=100.0, C=10.0, L=0.1, V0=5.0, tipe='RC'):
    t = np.linspace(0, 0.05, 500)
    
    if tipe == 'RC':
        # Kapasitor pengisian
        C_F = C * 1e-6
        tau = R * C_F
        vc = V0 * (1 - np.exp(-t/tau))
        i = (V0/R) * np.exp(-t/tau)
        
        fig, ax1 = plt.subplots(figsize=(8, 4))
        ax1.plot(t*1000, vc, 'b-', label=r'$V_C(t)$')
        ax1.set_xlabel('Waktu (ms)')
        ax1.set_ylabel('Tegangan (V)', color='b')
        ax1.tick_params(axis='y', labelcolor='b')
        
        ax2 = ax1.twinx()
        ax2.plot(t*1000, i*1000, 'r--', label=r'$I(t)$')
        ax2.set_ylabel('Arus (mA)', color='r')
        ax2.tick_params(axis='y', labelcolor='r')
        
        plt.title(rf"Respons Transien RC ($\\tau = {tau*1000:.2f}$ ms)")
        fig.tight_layout()
        plt.show()
        
    elif tipe == 'RL':
        # Induktor pengisian
        tau = L / R
        i = (V0/R) * (1 - np.exp(-t/tau))
        vl = V0 * np.exp(-t/tau)
        
        fig, ax1 = plt.subplots(figsize=(8, 4))
        ax1.plot(t*1000, i*1000, 'r-', label=r'$I(t)$')
        ax1.set_xlabel('Waktu (ms)')
        ax1.set_ylabel('Arus (mA)', color='r')
        ax1.tick_params(axis='y', labelcolor='r')
        
        ax2 = ax1.twinx()
        ax2.plot(t*1000, vl, 'b--', label=r'$V_L(t)$')
        ax2.set_ylabel('Tegangan (V)', color='b')
        ax2.tick_params(axis='y', labelcolor='b')
        
        plt.title(rf"Respons Transien RL ($\\tau = {tau*1000:.2f}$ ms)")
        fig.tight_layout()
        plt.show()

interact(simulasi_rc_rl, 
         R=FloatSlider(value=100.0, min=10.0, max=1000.0, step=10.0, description='R (Ohm)'),
         C=FloatSlider(value=10.0, min=1.0, max=100.0, step=1.0, description='C (uF)'),
         L=FloatSlider(value=0.1, min=0.01, max=1.0, step=0.01, description='L (H)'),
         V0=FloatSlider(value=5.0, min=1.0, max=24.0, step=1.0, description='V0 (V)'),
         tipe=['RC', 'RL']);""")
]

# Notebook 2: Simulasi Gelombang 1D
cells_gelombang_1d = [
    nbf.v4.new_markdown_cell("# Week 11: Persamaan Gelombang 1D\n\nPersamaan gelombang 1D memodelkan perambatan sinyal atau gelombang pada saluran transmisi tak merugi (lossless transmission line).\n\n$\\frac{\\partial^2 u}{\\partial t^2} = c^2 \\frac{\\partial^2 u}{\\partial x^2}$"),
    nbf.v4.new_code_cell("""import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

def simulasi_gelombang(c=1.0, t=0.0):
    L = 10.0
    nx = 200
    x = np.linspace(0, L, nx)
    
    # Kondisi awal: pulsa Gauss
    # Solusi d'Alembert: u(x,t) = 0.5 * [f(x-ct) + f(x+ct)]
    def f(x):
        return np.exp(-((x - L/2)**2) / 0.5)
    
    # Periodic boundary trick for simple visualization
    x_minus = (x - c*t) % L
    x_plus = (x + c*t) % L
    
    u = 0.5 * (f(x_minus) + f(x_plus))
    
    plt.figure(figsize=(8, 4))
    plt.plot(x, u, 'b-', lw=2)
    plt.ylim(-0.2, 1.2)
    plt.xlim(0, L)
    plt.xlabel('Posisi (x)')
    plt.ylabel('Amplitudo (u)')
    plt.title(rf"Perambatan Gelombang 1D pada t = {t:.2f} (c = {c})")
    plt.grid(True)
    plt.show()

interact(simulasi_gelombang, 
         c=FloatSlider(value=1.0, min=0.1, max=5.0, step=0.1, description='Kecepatan (c)'),
         t=FloatSlider(value=0.0, min=0.0, max=10.0, step=0.1, description='Waktu (t)'));""")
]

# Notebook 3: Simulasi Persamaan Panas/Difusi 1D
cells_panas_1d = [
    nbf.v4.new_markdown_cell("# Week 12: Persamaan Panas (Difusi) 1D\n\nPersamaan difusi/panas 1D dapat diterapkan pada konduksi panas, difusi muatan di semikonduktor, atau penyebaran polutan.\n\n$\\frac{\\partial u}{\\partial t} = \\alpha \\frac{\\partial^2 u}{\\partial x^2}$"),
    nbf.v4.new_code_cell("""import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, IntSlider

def simulasi_panas(alpha=0.1, max_waktu=2.0, langkah=50):
    L = 10.0
    nx = 50
    dx = L / (nx - 1)
    
    # Syarat kestabilan FTCS
    dt = (dx**2) / (2 * alpha * 1.5) 
    
    u = np.zeros(nx)
    # Kondisi awal: suhu tinggi di tengah
    u[int(nx/2)-5 : int(nx/2)+5] = 100.0
    
    x = np.linspace(0, L, nx)
    
    # Simulasi hingga waktu t
    waktu_target = max_waktu * (langkah / 100.0)
    n_steps = int(waktu_target / dt) if dt > 0 else 0
    
    u_baru = np.copy(u)
    for _ in range(n_steps):
        for i in range(1, nx-1):
            u_baru[i] = u[i] + alpha * dt / dx**2 * (u[i+1] - 2*u[i] + u[i-1])
        u = np.copy(u_baru)
        
    plt.figure(figsize=(8, 4))
    plt.plot(x, u, 'r-', lw=2, marker='o', markersize=4)
    plt.ylim(0, 110)
    plt.xlabel('Posisi (x)')
    plt.ylabel('Suhu (u)')
    plt.title(rf"Persamaan Panas 1D ($\\alpha$ = {alpha}) pada t = {waktu_target:.3f}")
    plt.grid(True)
    plt.show()

interact(simulasi_panas, 
         alpha=FloatSlider(value=0.5, min=0.1, max=2.0, step=0.1, description=r'$\\alpha$'),
         max_waktu=FloatSlider(value=5.0, min=1.0, max=10.0, step=1.0, description='Max t'),
         langkah=IntSlider(value=0, min=0, max=100, step=1, description='% Waktu'));""")
]

# Notebook 4: Simulasi Potensial Laplace 2D
cells_laplace_2d = [
    nbf.v4.new_markdown_cell("# Week 13: Persamaan Laplace 2D\n\nPersamaan Laplace memodelkan distribusi potensial listrik pada area bebas muatan.\n\n$\\nabla^2 V = \\frac{\\partial^2 V}{\\partial x^2} + \\frac{\\partial^2 V}{\\partial y^2} = 0$"),
    nbf.v4.new_code_cell("""import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider

def simulasi_laplace(iterasi=100):
    nx, ny = 30, 30
    V = np.zeros((ny, nx))
    
    # Syarat batas
    V[0, :] = 100.0  # Atas
    V[-1, :] = 0.0   # Bawah
    V[:, 0] = 0.0    # Kiri
    V[:, -1] = 0.0   # Kanan
    
    # Iterasi Jacobi
    for _ in range(iterasi):
        V_baru = np.copy(V)
        for i in range(1, ny-1):
            for j in range(1, nx-1):
                V_baru[i, j] = 0.25 * (V[i+1, j] + V[i-1, j] + V[i, j+1] + V[i, j-1])
        V = np.copy(V_baru)
        
    plt.figure(figsize=(6, 5))
    cp = plt.contourf(V, 20, cmap='inferno')
    plt.colorbar(cp, label='Potensial (V)')
    plt.title(rf"Distribusi Potensial Laplace (Iterasi: {iterasi})")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

interact(simulasi_laplace, 
         iterasi=IntSlider(value=10, min=0, max=500, step=10, description='Iterasi'));""")
]

if __name__ == '__main__':
    create_notebook('Simulasi_Transien_RC_RL.ipynb', cells_rc_rl)
    create_notebook('Simulasi_Gelombang_1D.ipynb', cells_gelombang_1d)
    create_notebook('Simulasi_Persamaan_Panas_1D.ipynb', cells_panas_1d)
    create_notebook('Simulasi_Potensial_Laplace_2D.ipynb', cells_laplace_2d)
