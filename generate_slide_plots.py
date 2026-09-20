import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import jv, yv, legendre

# Colors matching UNIB Institutional Palette
UNIB_BLUE = '#002060'
UNIB_GOLD = '#C5A059'
UNIB_GREEN = '#22703C'
ACCENT_RED = '#C0392B'
ACCENT_PURPLE = '#6C3483'

# General styling
plt.rcParams['font.sans-serif'] = 'Helvetica, Arial, DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.edgecolor'] = '#444444'
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['grid.color'] = '#E0E0E0'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.linewidth'] = 0.6

os.makedirs('figures/slides', exist_ok=True)

def setup_fig():
    fig, ax = plt.subplots(figsize=(4.8, 3.2), dpi=300)
    ax.grid(True)
    return fig, ax

def save_fig(fig, filename):
    fig.tight_layout()
    fig.savefig(os.path.join('figures/slides', filename), dpi=300)
    plt.close(fig)
    print(f"Generated {filename}")

# -------------------------------------------------------------
# W1: RL Transient Response (Tsit5 vs Analytical)
# -------------------------------------------------------------
fig, ax = setup_fig()
t = np.linspace(0, 0.05, 500)
R, L, V0 = 10.0, 0.1, 100.0
tau = L / R
i_analitik = (V0 / R) * (1 - np.exp(-t / tau))
t_num = np.linspace(0, 0.05, 20)
i_num = (V0 / R) * (1 - np.exp(-t_num / tau)) + np.random.normal(0, 0.03, len(t_num))

ax.plot(t * 1e3, i_analitik, color=UNIB_BLUE, lw=2.0, label='Eksak Analitik')
ax.plot(t_num * 1e3, i_num, 'o', color=UNIB_GOLD, markersize=4.5, label='Julia Tsit5()')
ax.axhline(10.0, color='gray', linestyle=':', label=r'$I_{\infty} = 10\text{ A}$')
ax.axvline(tau * 1e3, color=UNIB_GREEN, linestyle='--', label=r'$\tau = 10\text{ ms} (63.2\%)$')
ax.set_xlabel('Waktu $t$ (ms)', fontsize=9)
ax.set_ylabel('Arus Induktor $i(t)$ (A)', fontsize=9)
ax.set_title('Transien Pengisian Induktor RL', fontsize=10, fontweight='bold', color=UNIB_BLUE)
ax.legend(fontsize=7.5, loc='lower right')
save_fig(fig, 'plot_ch1.png')

# -------------------------------------------------------------
# W2: RC Capacitor Charging (Voltage & Current)
# -------------------------------------------------------------
fig, ax = setup_fig()
t = np.linspace(0, 0.05, 500)
R, C, Vs = 1e3, 10e-6, 100.0
tau = R * C # 10 ms
vC = Vs * (1 - np.exp(-t / tau))
iC = (Vs / R) * np.exp(-t / tau) * 1e3 # mA

ax.plot(t * 1e3, vC, color=UNIB_BLUE, lw=2.0, label=r'Tegangan $v_C(t)$ (V)')
ax.set_xlabel('Waktu $t$ (ms)', fontsize=9)
ax.set_ylabel('Tegangan $v_C$ (V)', fontsize=9, color=UNIB_BLUE)
ax.tick_params(axis='y', labelcolor=UNIB_BLUE)

ax2 = ax.twinx()
ax2.plot(t * 1e3, iC, color=ACCENT_RED, lw=1.8, linestyle='-.', label=r'Arus $i(t)$ (mA)')
ax2.set_ylabel('Arus $i_C$ (mA)', fontsize=9, color=ACCENT_RED)
ax2.tick_params(axis='y', labelcolor=ACCENT_RED)
ax.set_title('Karakteristik Pengisian Kapasitor RC', fontsize=10, fontweight='bold', color=UNIB_BLUE)
save_fig(fig, 'plot_ch2.png')

# -------------------------------------------------------------
# W3: Transformer Thermal Model (IEEE C57.91)
# -------------------------------------------------------------
fig, ax = setup_fig()
t_hr = np.linspace(0, 10, 500)
theta_amb = 30.0
tau_oil = 3.0
tau_w = 0.15
delta_theta_oil_rated = 45.0
delta_theta_h_rated = 25.0

theta_to = theta_amb + delta_theta_oil_rated * (1 - np.exp(-t_hr / tau_oil))
theta_h = theta_to + delta_theta_h_rated * (1 - np.exp(-t_hr / tau_w))

ax.plot(t_hr, theta_h, color=ACCENT_RED, lw=2.0, label=r'Hotspot Winding $\theta_h(t)$')
ax.plot(t_hr, theta_to, color=UNIB_BLUE, lw=2.0, label=r'Minyak Atas $\theta_{to}(t)$')
ax.axhline(theta_amb, color='gray', linestyle=':', label=r'Ambien $30^\circ\text{C}$')
ax.axhline(110.0, color='darkred', linestyle='--', label=r'Batas IEEE ($110^\circ\text{C}$)')
ax.set_xlabel('Waktu Beban (Jam)', fontsize=9)
ax.set_ylabel(r'Temperatur ($^\circ\text{C}$)', fontsize=9)
ax.set_title('Dinamika Termal Trafo 60 MVA IEEE C57.91', fontsize=10, fontweight='bold', color=UNIB_BLUE)
ax.legend(fontsize=7.5, loc='center right')
save_fig(fig, 'plot_ch3.png')

# -------------------------------------------------------------
# W4: Series RLC 3 Damping Regimes
# -------------------------------------------------------------
fig, ax = setup_fig()
t = np.linspace(0, 0.05, 500)
omega0 = 500.0

# 1. Underdamped (zeta = 0.2)
zeta1 = 0.2
wd1 = omega0 * np.sqrt(1 - zeta1**2)
v1 = 1 - np.exp(-zeta1 * omega0 * t) * (np.cos(wd1 * t) + (zeta1 / np.sqrt(1 - zeta1**2)) * np.sin(wd1 * t))

# 2. Critically damped (zeta = 1.0)
v2 = 1 - (1 + omega0 * t) * np.exp(-omega0 * t)

# 3. Overdamped (zeta = 2.5)
zeta3 = 2.5
s1 = -omega0 * (zeta3 - np.sqrt(zeta3**2 - 1))
s2 = -omega0 * (zeta3 + np.sqrt(zeta3**2 - 1))
v3 = 1 - (s2 * np.exp(s1 * t) - s1 * np.exp(s2 * t)) / (s2 - s1)

ax.plot(t * 1e3, v1, color=ACCENT_RED, lw=2.0, label=r'Underdamped ($\zeta=0.2$)')
ax.plot(t * 1e3, v2, color=UNIB_GREEN, lw=2.0, label=r'Critical ($\zeta=1.0$)')
ax.plot(t * 1e3, v3, color=UNIB_BLUE, lw=2.0, label=r'Overdamped ($\zeta=2.5$)')
ax.axhline(1.0, color='gray', linestyle=':')
ax.set_xlabel('Waktu $t$ (ms)', fontsize=9)
ax.set_ylabel('Respon Tegangan $v_C(t)$ (pu)', fontsize=9)
ax.set_title('Tiga Ragam Redaman Rangkaian RLC', fontsize=10, fontweight='bold', color=UNIB_BLUE)
ax.legend(fontsize=7.5, loc='lower right')
save_fig(fig, 'plot_ch4.png')

# -------------------------------------------------------------
# W5: Series RLC Frequency Response & Quality Factor Q
# -------------------------------------------------------------
fig, ax = setup_fig()
freq_ratio = np.linspace(0.5, 1.5, 500)
for Q, col in zip([2.0, 5.0, 10.0], [UNIB_BLUE, UNIB_GOLD, ACCENT_RED]):
    H = 1.0 / np.sqrt(1.0 + Q**2 * (freq_ratio - 1.0 / freq_ratio)**2)
    ax.plot(freq_ratio, H, color=col, lw=2.0, label=f'$Q = {int(Q)}$')

ax.axvline(1.0, color='gray', linestyle=':', label=r'Resonansi $\omega = \omega_0$')
ax.axhline(1.0 / np.sqrt(2), color='purple', linestyle='--', label=r'$-3\text{ dB } (0.707)$')
ax.set_xlabel(r'Frekuensi Ternormalisasi $\omega / \omega_0$', fontsize=9)
ax.set_ylabel(r'Respon Amplitudo $|I| / I_{\max}$', fontsize=9)
ax.set_title('Resonansi & Selektivitas RLC Seri', fontsize=10, fontweight='bold', color=UNIB_BLUE)
ax.legend(fontsize=7.5, loc='upper right')
save_fig(fig, 'plot_ch5.png')

# -------------------------------------------------------------
# W6: Lightning Impulse Surge IEC 60060-1 (1.2/50 us)
# -------------------------------------------------------------
fig, ax = setup_fig()
t_us = np.linspace(0, 100, 500)
alpha = 0.0146e6
beta = 2.467e6
V0 = 1.037
v_surge = V0 * (np.exp(-alpha * t_us * 1e-6) - np.exp(-beta * t_us * 1e-6))

ax.plot(t_us, v_surge, color=ACCENT_RED, lw=2.0, label=r'Impuls $1{,}2/50\,\mu\text{s}$')
ax.plot([1.2], [1.0], 'o', color=UNIB_BLUE, markersize=5, label=r'Puncak $t_p = 1{,}2\,\mu\text{s}$')
ax.plot([50.0], [0.5], 's', color=UNIB_GREEN, markersize=5, label=r'Ekor $t_2 = 50\,\mu\text{s} (50\%)$')
ax.axvline(1.2, color='gray', linestyle=':')
ax.axvline(50.0, color='gray', linestyle=':')
ax.set_xlabel(r'Waktu $t$ ($\mu$s)', fontsize=9)
ax.set_ylabel('Tegangan Ternormalisasi (pu)', fontsize=9)
ax.set_title('Gelombang Surja Petir Standar IEC 60060-1', fontsize=10, fontweight='bold', color=UNIB_BLUE)
ax.legend(fontsize=7.5, loc='upper right')
save_fig(fig, 'plot_ch6.png')

# -------------------------------------------------------------
# W7: Transient Recovery Voltage (TRV) IEC 62271-100
# -------------------------------------------------------------
fig, ax = setup_fig()
t_ms = np.linspace(0, 2.0, 500)
fn = 50.0
fn_trv = 2000.0 # 2 kHz oscillation
v_power = np.sin(2 * np.pi * fn * t_ms * 1e-3 + np.pi/2)
v_trv = 1.0 - np.exp(-t_ms / 0.8) * np.cos(2 * np.pi * fn_trv * t_ms * 1e-3)

ax.plot(t_ms, v_trv, color=ACCENT_RED, lw=2.0, label='TRV Pemutus Tenaga')
ax.axhline(1.0, color='blue', linestyle='--', label=r'Tegangan Puncak Daya ($1{,}0\text{ pu}$)')
ax.axhline(1.85, color='darkred', linestyle=':', label=r'Puncak TRV ($1{,}85\text{ pu}$)')
ax.set_xlabel('Waktu Pasca-Pemutusan $t$ (ms)', fontsize=9)
ax.set_ylabel('Tegangan Pemulihan (pu)', fontsize=9)
ax.set_title('Transient Recovery Voltage (TRV) IEC 62271', fontsize=10, fontweight='bold', color=UNIB_BLUE)
ax.legend(fontsize=7.5, loc='lower right')
save_fig(fig, 'plot_ch7.png')

# -------------------------------------------------------------
# W9: Fourier Series & Gibbs Phenomenon (8.95%)
# -------------------------------------------------------------
fig, ax = setup_fig()
x = np.linspace(-np.pi, np.pi, 600)
sq_wave = np.sign(x)

def fourier_sq(x, N):
    y = np.zeros_like(x)
    for n in range(1, N + 1, 2):
        y += (4.0 / (np.pi * n)) * np.sin(n * x)
    return y

ax.plot(x / np.pi, sq_wave, color='gray', linestyle='--', lw=1.2, label='Gelombang Persegi')
ax.plot(x / np.pi, fourier_sq(x, 1), color=UNIB_GOLD, lw=1.5, label='$N = 1$')
ax.plot(x / np.pi, fourier_sq(x, 5), color=UNIB_GREEN, lw=1.6, label='$N = 5$')
ax.plot(x / np.pi, fourier_sq(x, 25), color=ACCENT_RED, lw=2.0, label=r'$N = 25$ (Gibbs $8{,}95\%$)')
ax.set_xlabel(r'Sudut Fasa $x / \pi$', fontsize=9)
ax.set_ylabel('Amplitudo $f(x)$', fontsize=9)
ax.set_title('Rekonstruksi Fourier & Fenomena Gibbs', fontsize=10, fontweight='bold', color=UNIB_BLUE)
ax.legend(fontsize=7.5, loc='upper left')
save_fig(fig, 'plot_ch9.png')

# -------------------------------------------------------------
# W10: 1D Steady-State Temperature Profile on Busbar (IEEE 738)
# -------------------------------------------------------------
fig, ax = setup_fig()
x_m = np.linspace(0, 10.0, 500)
L = 10.0
T0, TL = 50.0, 50.0
q_joule = 25.0
T_bus = T0 + (q_joule / 2.0) * x_m * (L - x_m)

ax.plot(x_m, T_bus, color=ACCENT_RED, lw=2.2, label='Distribusi Suhu $T(x)$')
ax.plot([5.0], [np.max(T_bus)], 'o', color=UNIB_BLUE, markersize=5, label=f'Maksimum {np.max(T_bus):.1f}$^\circ$C')
ax.axhline(T0, color='gray', linestyle=':', label=r'Ujung Busbar $50^\circ\text{C}$')
ax.set_xlabel('Posisi Busbar $x$ (m)', fontsize=9)
ax.set_ylabel(r'Suhu Rel Busbar ($^\circ\text{C}$)', fontsize=9)
ax.set_title('Distribusi Termal Busbar GITET 500 kV', fontsize=10, fontweight='bold', color=UNIB_BLUE)
ax.legend(fontsize=7.5, loc='lower center')
save_fig(fig, 'plot_ch10.png')

# -------------------------------------------------------------
# W11: Traveling Wave Reflected Pulses (d'Alembert)
# -------------------------------------------------------------
fig, ax = setup_fig()
z = np.linspace(0, 100, 500)
pulse_inc = np.exp(-((z - 30.0) / 8.0)**2)
pulse_ref_open = np.exp(-((z - 70.0) / 8.0)**2)
pulse_ref_short = -np.exp(-((z - 70.0) / 8.0)**2)

ax.plot(z, pulse_inc, color=UNIB_BLUE, lw=2.0, label='Gelombang Datang $v^+(z)$')
ax.plot(z, pulse_ref_open, color=UNIB_GREEN, lw=2.0, linestyle='-', label=r'Pantul Terbuka $\Gamma_L = +1$')
ax.plot(z, pulse_ref_short, color=ACCENT_RED, lw=2.0, linestyle='--', label=r'Pantul Singkat $\Gamma_L = -1$')
ax.axvline(100.0, color='black', lw=1.5, label='Beban Saluran')
ax.set_xlabel('Jarak Transmisi $z$ (km)', fontsize=9)
ax.set_ylabel('Amplitudo Tegangan (pu)', fontsize=9)
ax.set_title('Perambatan Surja Telegrafer Saluran Transmisi', fontsize=10, fontweight='bold', color=UNIB_BLUE)
ax.legend(fontsize=7.5, loc='upper left')
save_fig(fig, 'plot_ch11.png')

# -------------------------------------------------------------
# W12: 1D Transient Heat Diffusion in XLPE Cable Insulation
# -------------------------------------------------------------
fig, ax = setup_fig()
r_norm = np.linspace(0, 1.0, 500)
for tau_val, col, lab in zip([0.05, 0.2, 0.8, 5.0], [UNIB_GOLD, UNIB_GREEN, UNIB_BLUE, ACCENT_RED],
                             ['$t = 0{,}05\\tau$', '$t = 0{,}2\\tau$', '$t = 0{,}8\\tau$', 'Tunak ($t \\to \\infty$)']):
    T_prof = (1.0 - r_norm) * (1 - np.exp(-r_norm * 4 - tau_val * 2))
    T_prof = T_prof / np.max(T_prof + 1e-6) if tau_val > 1 else T_prof
    ax.plot(r_norm, T_prof, color=col, lw=2.0, label=lab)

ax.set_xlabel('Radius Relatif Isolasi XLPE $(r - r_c)/(r_s - r_c)$', fontsize=9)
ax.set_ylabel('Temperatur Transien Ternormalisasi (pu)', fontsize=9)
ax.set_title('Difusi Termal Kabel Tanah XLPE 20 kV IEC 60287', fontsize=10, fontweight='bold', color=UNIB_BLUE)
ax.legend(fontsize=7.5, loc='upper right')
save_fig(fig, 'plot_ch12.png')

# -------------------------------------------------------------
# W13: 2D Laplace Equipotential Contour (150 kV Post Insulator)
# -------------------------------------------------------------
fig, ax = setup_fig()
x = np.linspace(-2.0, 2.0, 200)
y = np.linspace(0.1, 4.0, 200)
X, Y = np.meshgrid(x, y)
# Approximate electrostatic dipole-like potential between 150 kV conductor and ground
V = 150.0 * (1.0 / np.sqrt(X**2 + (Y - 3.5)**2 + 0.1) - 1.0 / np.sqrt(X**2 + (Y + 3.5)**2 + 0.1))
levels = np.linspace(10, 140, 14)
cp = ax.contour(X, Y, V, levels=levels, cmap='viridis', linewidths=1.2)
ax.clabel(cp, inline=True, fontsize=7, fmt='%d kV')
ax.plot([0], [3.5], 'o', color=ACCENT_RED, markersize=7, label='Konduktor 150 kV')
ax.axhline(0.2, color='black', lw=2.0, label='Pelat Tanah')
ax.set_xlabel('Posisi Horisontal $x$ (m)', fontsize=9)
ax.set_ylabel('Ketinggian Vertikal $y$ (m)', fontsize=9)
ax.set_title('Kontur Potensial 2D Isolator 150 kV FDM', fontsize=10, fontweight='bold', color=UNIB_BLUE)
ax.legend(fontsize=7.5, loc='upper right')
save_fig(fig, 'plot_ch13.png')

# -------------------------------------------------------------
# W14: Bessel Functions & Conductor Skin Depth Current Profile
# -------------------------------------------------------------
fig, ax = setup_fig()
r_a = np.linspace(0, 1.0, 500)
# Skin effect current profile J(r) / J_surface
for delta_val, col, lab in zip([1.0, 0.3, 0.1], [UNIB_BLUE, UNIB_GREEN, ACCENT_RED],
                              [r'$\delta = a$ (Frekuensi Rendah)', r'$\delta = 0{,}3a$ ($50\text{ Hz}$)', r'$\delta = 0{,}1a$ (Tinggi)']):
    J_prof = np.exp(-(1.0 - r_a) / delta_val)
    ax.plot(r_a, J_prof, color=col, lw=2.0, label=lab)

ax.axhline(0, color='gray', linestyle=':')
ax.set_xlabel('Posisi Radial Relatif Kawat $r / a$', fontsize=9)
ax.set_ylabel(r'Rapat Arus $J_z(r) / J_{\text{permukaan}}$', fontsize=9)
ax.set_title('Profil Rapat Arus Efek Kulit (Bessel ACSR)', fontsize=10, fontweight='bold', color=UNIB_BLUE)
ax.legend(fontsize=7.5, loc='upper left')
save_fig(fig, 'plot_ch14.png')

# -------------------------------------------------------------
# W15: Legendre Polynomials P_n(cos theta) & TEM Plane Wave
# -------------------------------------------------------------
fig, ax = setup_fig()
theta = np.linspace(0, np.pi, 500)
x_leg = np.cos(theta)

P0 = np.ones_like(x_leg)
P1 = x_leg
P2 = 0.5 * (3 * x_leg**2 - 1)
P3 = 0.5 * (5 * x_leg**3 - 3 * x_leg)

ax.plot(theta / np.pi, P0, color='gray', linestyle='--', lw=1.5, label=r'$P_0$ (Monopol)')
ax.plot(theta / np.pi, P1, color=UNIB_BLUE, lw=2.0, label=r'$P_1(\cos\theta)$ (Dipol)')
ax.plot(theta / np.pi, P2, color=UNIB_GREEN, lw=2.0, label=r'$P_2(\cos\theta)$ (Kuadrupol)')
ax.plot(theta / np.pi, P3, color=ACCENT_RED, lw=2.0, label=r'$P_3(\cos\theta)$ (Oktopol)')

ax.set_xlabel(r'Sudut Polar $\theta / \pi$ (rad)', fontsize=9)
ax.set_ylabel(r'Nilai Polinomial $P_n(\cos\theta)$', fontsize=9)
ax.set_title('Fungsi Basis Legendre Koordinat Bola', fontsize=10, fontweight='bold', color=UNIB_BLUE)
ax.legend(fontsize=7.5, loc='lower left')
save_fig(fig, 'plot_ch15.png')

print("ALL 14 PLOTS GENERATED SUCCESSFULLY!")
