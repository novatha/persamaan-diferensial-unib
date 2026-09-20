import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Output directory for 4:5 carousel slides
out_dir = "docs/images/instagram_minggu_5"
os.makedirs(out_dir, exist_ok=True)

# 4:5 Aspect Ratio (1080 x 1350 px)
W_INCH, H_INCH = 10.8, 13.5
DPI = 100 # Exact 1080 x 1350 px
BG_COLOR = "#0A1128"        # Deep UNIB Navy
CARD_BG = "#101F42"         # Sleek Card Blue
CARD_BORDER = "#1E3A8A"     # Subtle Indigo Border
ACCENT_CYAN = "#00D2FF"     # Neon Cyan
ACCENT_GOLD = "#FFD166"     # Vibrant UNIB Gold
ACCENT_RED = "#EF476F"      # Coral Red
ACCENT_GREEN = "#06D6A0"    # Emerald Mint
TEXT_WHITE = "#FFFFFF"
TEXT_MUTED = "#94A3B8"      # Slate Light

plt.rcParams["font.sans-serif"] = ["Helvetica", "Arial", "DejaVu Sans"]
plt.rcParams["font.family"] = "sans-serif"

def init_canvas():
    fig = plt.figure(figsize=(W_INCH, H_INCH), dpi=DPI, facecolor=BG_COLOR)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 1080)
    ax.set_ylim(0, 1350)
    ax.axis("off")
    return fig, ax

def add_header(ax, slide_num, total_slides=6):
    ax.text(80, 1295, "TEKNIK ELEKTRO UNIB", fontsize=18, weight="heavy", color=ACCENT_GOLD, ha="left", va="center")
    ax.text(80, 1270, "Persamaan Diferensial • Semester Genap", fontsize=14, color=TEXT_MUTED, ha="left", va="center")
    
    rect = patches.FancyBboxPatch((870, 1255), 130, 42, boxstyle="round,pad=5", facecolor="#162c52", edgecolor=ACCENT_CYAN, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(935, 1276, f"{slide_num} / {total_slides}", fontsize=17, weight="bold", color=TEXT_WHITE, ha="center", va="center")
    
    ax.plot([80, 1000], [1235, 1235], color="#1e3a63", lw=1.5)

def add_footer(ax):
    ax.plot([80, 1000], [85, 85], color="#1e3a63", lw=1.5)
    ax.text(540, 58, "pd.ndaratha.my.id   •   Geser ke kiri >>", fontsize=16, weight="bold", color=ACCENT_GOLD, ha="center", va="center")
    ax.text(540, 32, "Pengampu: Novalio Daratha, Ph.D. & Muhammad Arfan, M.T.", fontsize=13, color=TEXT_MUTED, ha="center", va="center")

# ==========================================
# SLIDE 1: COVER / HOOK (4:5)
# ==========================================
def make_slide_1():
    fig, ax = init_canvas()
    add_header(ax, 1)
    
    pill = patches.FancyBboxPatch((80, 1180), 260, 34, boxstyle="round,pad=6", facecolor="#D97706", edgecolor="none")
    ax.add_patch(pill)
    ax.text(210, 1197, "MINGGU 5: PDB ORDE 2", fontsize=13.5, weight="black", color=TEXT_WHITE, ha="center", va="center")
    
    ax.text(80, 1160, "KENAPA RANGKAIAN\nELEKTRONIKA BISA MELEDAK?", fontsize=34, weight="black", color=TEXT_WHITE, ha="left", va="top", linespacing=1.15)
    ax.text(80, 1065, "Rahasia Fisik PDB Non-Homogen & Resonansi RLC Seri", fontsize=18, weight="bold", color=ACCENT_CYAN, ha="left", va="top")
    
    # Visual Waveform Card (starts at 255, reaches 1005)
    card = patches.FancyBboxPatch((80, 255), 920, 750, boxstyle="round,pad=18", facecolor=CARD_BG, edgecolor=CARD_BORDER, lw=2)
    ax.add_patch(card)
    
    w_pill = patches.FancyBboxPatch((120, 940), 840, 40, boxstyle="round,pad=6", facecolor="#450A0A", edgecolor=ACCENT_RED, lw=1.5)
    ax.add_patch(w_pill)
    ax.text(540, 960, "PERINGATAN KRITIS: TEGANGAN MEMBENGKAK TANPA BATAS!", fontsize=14.5, weight="black", color=ACCENT_RED, ha="center", va="center")
    
    t = np.linspace(0.1, 4*np.pi, 600)
    wave_res = t * np.sin(2.5 * t)
    wave_norm = 135 * (wave_res / np.max(np.abs(wave_res)))
    env = 135 * (t / np.max(t))
    
    xs = 130 + (t / (4*np.pi)) * 820
    ys = 660 + wave_norm
    env_top = 660 + env
    env_bot = 660 - env
    
    ax.plot([130, 950], [660, 660], color="#2c4d75", linestyle="--", lw=1.5)
    ax.plot(xs, env_top, color=ACCENT_GOLD, linestyle=":", lw=2, alpha=0.8)
    ax.plot(xs, env_bot, color=ACCENT_GOLD, linestyle=":", lw=2, alpha=0.8)
    ax.plot(xs, ys, color=ACCENT_RED, lw=3.5, label="Respon Resonansi")
    
    ax.text(930, 815, "+ Amplitudo ~ t", fontsize=14, weight="bold", color=ACCENT_GOLD, ha="right")
    ax.text(930, 505, "- Amplitudo ~ t", fontsize=14, weight="bold", color=ACCENT_GOLD, ha="right")
    
    ax.text(540, 385, "Ketika frekuensi sumber luar sama persis dengan frekuensi alami sistem (w = w0),\nenergi terserap terus-menerus hingga komponen terbakar atau meledak!", 
            fontsize=16.5, color=TEXT_WHITE, ha="center", va="center", linespacing=1.35)
    
    # Bottom Callout Card
    bubble = patches.FancyBboxPatch((80, 105), 920, 125, boxstyle="round,pad=12", facecolor="#142C54", edgecolor=ACCENT_GOLD, lw=2)
    ax.add_patch(bubble)
    ax.text(540, 180, "Bagaimana cara matematika memprediksi", fontsize=17.5, color=TEXT_WHITE, ha="center")
    ax.text(540, 140, "dan mengamankan fenomena berbahaya ini?", fontsize=19.5, weight="black", color=ACCENT_GOLD, ha="center")
    
    add_footer(ax)
    plt.savefig(f"{out_dir}/slide_1.png", dpi=DPI)
    plt.close()
    print("Slide 1 (4:5) regenerated.")

# ==========================================
# SLIDE 2: STRUKTUR SOLUSI TOTAL (4:5)
# ==========================================
def make_slide_2():
    fig, ax = init_canvas()
    add_header(ax, 2)
    
    ax.text(80, 1195, "KONSEP KUNCI", fontsize=15, weight="bold", color=ACCENT_GOLD, ha="left", va="top")
    ax.text(80, 1170, "STRUKTUR SOLUSI TOTAL", fontsize=36, weight="black", color=TEXT_WHITE, ha="left", va="top")
    ax.text(80, 1115, "PDB Non-Homogen:  a y'' + b y' + c y = g(t)", fontsize=18, weight="bold", color=ACCENT_CYAN, ha="left", va="top")
    
    # Formula Box (top is 1055, reaches 960)
    f_box = patches.FancyBboxPatch((80, 960), 920, 95, boxstyle="round,pad=12", facecolor="#1A365D", edgecolor=ACCENT_GOLD, lw=2.5)
    ax.add_patch(f_box)
    ax.text(540, 1007, "y(t)  =  y_h(t)  +  y_p(t)", fontsize=36, weight="black", color="#FFD700", ha="center", va="center")
    
    # Card 1: y_h (from 575 to 935)
    c1 = patches.FancyBboxPatch((80, 575), 920, 360, boxstyle="round,pad=15", facecolor=CARD_BG, edgecolor="#2563EB", lw=2)
    ax.add_patch(c1)
    ax.text(120, 900, "[1] Solusi Homogen : y_h(t)", fontsize=21, weight="black", color=ACCENT_CYAN)
    ax.text(120, 860, "• Persamaan saat sumber padam : a y'' + b y' + c y = 0", fontsize=16, color=TEXT_WHITE)
    ax.text(120, 820, "• Karakter Elektro : RESPON ALAMI / TRANSIEN (Natural Response)", fontsize=16, weight="bold", color=ACCENT_GOLD)
    ax.text(120, 780, "• Menggambarkan pelepasan energi awal induktor (L) & kapasitor (C).", fontsize=15, color=TEXT_MUTED)
    ax.text(120, 740, "• Sifat Mutlak : Pasti MELURUH HABIS ke nol (t -> tak hingga)", fontsize=15, weight="bold", color=ACCENT_GREEN)
    ax.text(120, 705, "  karena seluruh energi terdisipasi menjadi panas pada resistor R.", fontsize=15, color=TEXT_MUTED)
    
    # Card 2: y_p (from 190 to 550)
    c2 = patches.FancyBboxPatch((80, 190), 920, 360, boxstyle="round,pad=15", facecolor=CARD_BG, edgecolor="#DC2626", lw=2)
    ax.add_patch(c2)
    ax.text(120, 515, "[2] Solusi Partikular : y_p(t)", fontsize=21, weight="black", color=ACCENT_RED)
    ax.text(120, 475, "• Menemukan satu fungsi khusus yang memuaskan ruas kanan g(t)", fontsize=16, color=TEXT_WHITE)
    ax.text(120, 435, "• Karakter Elektro : RESPON PAKSA / TUNAK (Steady-State)", fontsize=16, weight="bold", color=ACCENT_GOLD)
    ax.text(120, 395, "• Mengikuti frekuensi & pola gelombang generator luar.", fontsize=15, color=TEXT_MUTED)
    ax.text(120, 355, "• Sifat Mutlak : TETAP BERTAHAN selama generator menyala.", fontsize=15, weight="bold", color="#FCA5A5")
    ax.text(120, 320, "  Menentukan batas kapasitas aman operasi jangka panjang rangkaian.", fontsize=15, color=TEXT_MUTED)
    
    # Summary Capsule
    s_pill = patches.FancyBboxPatch((80, 110), 920, 55, boxstyle="round,pad=8", facecolor="#0F172A", edgecolor="#334155", lw=1.5)
    ax.add_patch(s_pill)
    ax.text(540, 137, "Solusi Lengkap = Respon Transien (Hilang) + Mantap (Kekal)", fontsize=16, weight="bold", color=TEXT_WHITE, ha="center", va="center")
    
    add_footer(ax)
    plt.savefig(f"{out_dir}/slide_2.png", dpi=DPI)
    plt.close()
    print("Slide 2 (4:5) regenerated.")

# ==========================================
# SLIDE 3: METODE KOEFISIEN TAK TENTU (4:5)
# ==========================================
def make_slide_3():
    fig, ax = init_canvas()
    add_header(ax, 3)
    
    ax.text(80, 1195, "METODE PRAKTIS", fontsize=15, weight="bold", color=ACCENT_GOLD, ha="left", va="top")
    ax.text(80, 1170, "TEBAK SOLUSI SEPERTI PRO!", fontsize=36, weight="black", color=TEXT_WHITE, ha="left", va="top")
    ax.text(80, 1115, "Metode Koefisien Tak Tentu (Undetermined Coefficients)", fontsize=17, weight="bold", color=ACCENT_CYAN, ha="left", va="top")
    
    # Table Box (top is 1050, from 545 to 1050)
    t_box = patches.FancyBboxPatch((80, 545), 920, 505, boxstyle="round,pad=12", facecolor=CARD_BG, edgecolor=CARD_BORDER, lw=2)
    ax.add_patch(t_box)
    
    ax.text(120, 1015, "Bentuk Sumber g(t)", fontsize=17, weight="black", color=ACCENT_GOLD)
    ax.text(520, 1015, "Tebakan Solusi Partikular y_p(t)", fontsize=17, weight="black", color=ACCENT_GOLD)
    ax.plot([110, 970], [990, 990], color="#2B4C7E", lw=1.5)
    
    rows = [
        ("Konstanta C", "A  (Konstanta)", 940),
        ("Eksponensial : e^(k t)", "A • e^(k t)", 870),
        ("Sinusoidal : sin(w t) / cos(w t)", "A cos(w t) + B sin(w t)", 800),
        ("Polinomial : a t^2 + b t + c", "A t^2 + B t + C", 730),
        ("Kombinasi : e^(k t) cos(w t)", "e^(k t) [A cos(w t) + B sin(w t)]", 660),
    ]
    
    for left, right, y_pos in rows:
        ax.text(120, y_pos, left, fontsize=16, color=TEXT_WHITE)
        ax.text(520, y_pos, right, fontsize=16, weight="bold", color="#7DD3FC")
        if y_pos > 670:
            ax.plot([110, 970], [y_pos - 32, y_pos - 32], color="#1E3A63", lw=1)
            
    ax.text(540, 575, "Catatan: Substitusi y_p ke PDB untuk mencari nilai konstanta A, B, C.", fontsize=13, color=TEXT_MUTED, ha="center", style="italic")
    
    # Golden Rule Warning Box (top is 520, from 110 to 520)
    w_box = patches.FancyBboxPatch((80, 110), 920, 410, boxstyle="round,pad=15", facecolor="#3B1212", edgecolor=ACCENT_RED, lw=2.5)
    ax.add_patch(w_box)
    
    ax.text(120, 485, "ATURAN MODIFIKASI (THE GOLDEN RULE):", fontsize=19, weight="black", color="#FCA5A5")
    ax.text(120, 445, "Jika tebakan y_p memuat suku yang SAMA PERSIS dengan solusi homogen y_h:", fontsize=15, color=TEXT_WHITE)
    ax.text(120, 405, ">> KALIKAN TEBAKAN ANDA DENGAN 't'!", fontsize=20, weight="black", color=ACCENT_GOLD)
    
    ex_box = patches.FancyBboxPatch((110, 220), 860, 140, boxstyle="round,pad=8", facecolor="#240D0D", edgecolor="#7F1D1D", lw=1.5)
    ax.add_patch(ex_box)
    ax.text(130, 325, "Contoh: Jika y_h memuat cos(2t) dan sumber g(t) = 4 cos(2t),", fontsize=14, color="#E2E8F0")
    ax.text(130, 290, "maka tebakan biasa GAGAL! Tebakan yang benar:", fontsize=14, color="#E2E8F0")
    ax.text(130, 250, "y_p(t) = t • [ A cos(2t) + B sin(2t) ]", fontsize=17, weight="black", color=ACCENT_CYAN)
    
    ax.text(120, 150, "Faktor 't' inilah yang memicu pertumbuhan amplitudo resonansi tanpa batas!", fontsize=14, weight="bold", color=ACCENT_GOLD)
    
    add_footer(ax)
    plt.savefig(f"{out_dir}/slide_3.png", dpi=DPI)
    plt.close()
    print("Slide 3 (4:5) regenerated.")

# ==========================================
# SLIDE 4: 3 WAJAH REDAMAN RLC (4:5)
# ==========================================
def make_slide_4():
    fig, ax = init_canvas()
    add_header(ax, 4)
    
    ax.text(80, 1195, "APLIKASI TEKNIK ELEKTRO", fontsize=15, weight="bold", color=ACCENT_GOLD, ha="left", va="top")
    ax.text(80, 1170, "3 WAJAH REDAMAN RLC", fontsize=36, weight="black", color=TEXT_WHITE, ha="left", va="top")
    ax.text(80, 1115, "Persamaan Rangkaian:  L i'' + R i' + (1/C) i = v_s'(t)", fontsize=17, weight="bold", color=ACCENT_CYAN, ha="left", va="top")
    
    # Generate waveforms
    t = np.linspace(0, 10, 500)
    y_under = np.exp(-0.45 * t) * np.sin(2.4 * t)
    y_crit = 1.3 * t * np.exp(-1.0 * t)
    y_over = 1.1 * (np.exp(-0.35 * t) - np.exp(-2.2 * t))
    
    # Plot card (top is 1050, from 655 to 1050)
    card = patches.FancyBboxPatch((80, 655), 920, 395, boxstyle="round,pad=12", facecolor=CARD_BG, edgecolor=CARD_BORDER, lw=2)
    ax.add_patch(card)
    
    ax.text(120, 1015, "Perbandingan Kurva Arus Transien RLC Seri :", fontsize=16, weight="black", color=TEXT_WHITE)
    
    def to_coords(t_arr, y_arr, y_scale=100, y_offset=790):
        xs = 130 + (t_arr / 10.0) * 810
        ys = y_offset + y_arr * y_scale
        return xs, ys
    
    ax.plot([130, 940], [790, 790], color="#2B4C7E", linestyle="--", lw=1.5)
    
    x_u, y_u = to_coords(t, y_under)
    x_c, y_c = to_coords(t, y_crit)
    x_o, y_o = to_coords(t, y_over)
    
    ax.plot(x_u, y_u, color=ACCENT_RED, lw=3.2, label="Underdamped")
    ax.plot(x_c, y_c, color=ACCENT_GOLD, lw=3.2, label="Critically Damped")
    ax.plot(x_o, y_o, color=ACCENT_GREEN, lw=3.2, label="Overdamped")
    
    ax.text(640, 985, "— Underdamped (R kecil)", color=ACCENT_RED, fontsize=13.5, weight="bold")
    ax.text(640, 955, "— Critical (R pas)", color=ACCENT_GOLD, fontsize=13.5, weight="bold")
    ax.text(640, 925, "— Overdamped (R besar)", color=ACCENT_GREEN, fontsize=13.5, weight="bold")
    
    # 3 Summary description cards
    u_c = patches.FancyBboxPatch((80, 475), 920, 155, boxstyle="round,pad=10", facecolor="#261014", edgecolor=ACCENT_RED, lw=1.5)
    ax.add_patch(u_c)
    ax.text(110, 590, "1. Underdamped (alpha < w0) — Kurang Redam", fontsize=16.5, weight="black", color=ACCENT_RED)
    ax.text(110, 555, "• Arus berosilasi bolak-balik frekuensi tinggi sebelum reda.", fontsize=14, color=TEXT_WHITE)
    ax.text(110, 525, "• Bahaya: Voltage overshoot rentan merusak komponen IC sensitif!", fontsize=13, color="#FDA4AF")
    ax.text(110, 498, "• Aplikasi: Rangkaian pemancar radio frekuensi & filter penala.", fontsize=13, color=TEXT_MUTED)
    
    c_c = patches.FancyBboxPatch((80, 295), 920, 155, boxstyle="round,pad=10", facecolor="#272111", edgecolor=ACCENT_GOLD, lw=1.5)
    ax.add_patch(c_c)
    ax.text(110, 410, "2. Critically Damped (alpha = w0) — Redam Kritis", fontsize=16.5, weight="black", color=ACCENT_GOLD)
    ax.text(110, 375, "• Waktu transien PALING CEPAT tanpa pernah terjadi overshoot.", fontsize=14, color=TEXT_WHITE)
    ax.text(110, 345, "• Stabil seketika, bebas dengung dan lonjakan getaran listrik.", fontsize=13, color="#FEF08A")
    ax.text(110, 318, "• Aplikasi: Saklar daya (circuit breaker) & jarum ukur analog.", fontsize=13, color=TEXT_MUTED)
    
    o_c = patches.FancyBboxPatch((80, 115), 920, 155, boxstyle="round,pad=10", facecolor="#0E2319", edgecolor=ACCENT_GREEN, lw=1.5)
    ax.add_patch(o_c)
    ax.text(110, 230, "3. Overdamped (alpha > w0) — Lebih Redam", fontsize=16.5, weight="black", color=ACCENT_GREEN)
    ax.text(110, 195, "• Arus meluruh sangat lambat dan lamban mencapai nilai mantap.", fontsize=14, color=TEXT_WHITE)
    ax.text(110, 165, "• Hambatan R yang besar menimbulkan disipasi rugi-rugi panas tinggi.", fontsize=13, color="#A7F3D0")
    ax.text(110, 138, "• Aplikasi: Peredam surja petir ekstrem pada transformator gardu induk.", fontsize=13, color=TEXT_MUTED)
    
    add_footer(ax)
    plt.savefig(f"{out_dir}/slide_4.png", dpi=DPI)
    plt.close()
    print("Slide 4 (4:5) regenerated.")

# ==========================================
# SLIDE 5: MINI QUIZ / BRAIN TEASER (4:5)
# ==========================================
def make_slide_5():
    fig, ax = init_canvas()
    add_header(ax, 5)
    
    ax.text(80, 1195, "UJI PEMAHAMAN ANDA", fontsize=15, weight="bold", color=ACCENT_GOLD, ha="left", va="top")
    ax.text(80, 1170, "BRAIN TEASER MINGGU 5", fontsize=36, weight="black", color=TEXT_WHITE, ha="left", va="top")
    ax.text(80, 1115, "Kuis Kilat Solusi Partikular & Resonansi RLC", fontsize=17, weight="bold", color=ACCENT_CYAN, ha="left", va="top")
    
    # Question box (top is 1050, from 760 to 1050)
    q_card = patches.FancyBboxPatch((80, 760), 920, 290, boxstyle="round,pad=15", facecolor="#162E52", edgecolor=ACCENT_GOLD, lw=2)
    ax.add_patch(q_card)
    ax.text(120, 1010, "[ SOAL KUIS ]", fontsize=17, weight="black", color=ACCENT_GOLD)
    ax.text(120, 965, "Diberikan persamaan osilator tak teredam:", fontsize=15, color=TEXT_WHITE)
    ax.text(120, 920, "y'' + 4 y = 6 cos(2t)", fontsize=27, weight="black", color=ACCENT_CYAN)
    ax.text(120, 875, "Solusi homogennya :  y_h(t) = C1 cos(2t) + C2 sin(2t)", fontsize=14.5, color=TEXT_MUTED)
    ax.text(120, 830, "Manakah bentuk tebakan solusi partikular y_p yang benar?", fontsize=15.5, weight="bold", color=TEXT_WHITE)
    
    # Option A (top is 738, from 650 to 738)
    opt_a = patches.FancyBboxPatch((80, 650), 920, 88, boxstyle="round,pad=10", facecolor=CARD_BG, edgecolor=CARD_BORDER, lw=1.5)
    ax.add_patch(opt_a)
    ax.text(120, 705, "PILIHAN A :", fontsize=14, weight="bold", color=ACCENT_RED)
    ax.text(120, 672, "y_p(t) = A cos(2t) + B sin(2t)", fontsize=17, weight="bold", color=TEXT_WHITE)
    
    # Option B (top is 634, from 542 to 634)
    opt_b = patches.FancyBboxPatch((80, 542), 920, 92, boxstyle="round,pad=10", facecolor=CARD_BG, edgecolor=ACCENT_GREEN, lw=2.2)
    ax.add_patch(opt_b)
    ax.text(120, 598, "PILIHAN B (KASUS RESONANSI) :", fontsize=14, weight="bold", color=ACCENT_GREEN)
    ax.text(120, 564, "y_p(t) = t • [ A cos(2t) + B sin(2t) ]", fontsize=18, weight="black", color=ACCENT_GREEN)
    
    # Answer reveal box (top is 515, from 110 to 515)
    rev = patches.FancyBboxPatch((80, 110), 920, 405, boxstyle="round,pad=12", facecolor="#102E20", edgecolor=ACCENT_GREEN, lw=2.2)
    ax.add_patch(rev)
    ax.text(120, 480, "[ JAWABAN BENAR : PILIHAN B ]", fontsize=19, weight="black", color=ACCENT_GREEN)
    ax.text(120, 440, "Alasan Matematis & Karakteristik Fisik:", fontsize=15, weight="bold", color=TEXT_WHITE)
    ax.text(120, 405, "1. Frekuensi sumber (w = 2 rad/s) PERSIS SAMA dengan", fontsize=14, color="#E2E8F0")
    ax.text(120, 380, "   frekuensi alami sistem (w0 = sqrt(4) = 2 rad/s).", fontsize=14, color="#E2E8F0")
    ax.text(120, 342, "2. Pilihan A sudah jadi solusi homogen y_h. Bila disubstitusi,", fontsize=14, color=TEXT_MUTED)
    ax.text(120, 318, "   ruas kiri menghasilkan 0 = 6 cos(2t) (KONTRAKSI / BUNTU!).", fontsize=14, color="#FECDD3")
    ax.text(120, 280, "3. Menurut Aturan Modifikasi, tebakan WAJIB dikalikan 't'.", fontsize=14.5, weight="bold", color=ACCENT_GOLD)
    ax.text(120, 242, "   Pengali 't' menyebabkan amplitudo arus/tegangan membesar", fontsize=13.5, color=TEXT_MUTED)
    ax.text(120, 218, "   linier seiring waktu, memicu ledakan fisik komponen!", fontsize=13.5, color="#FECDD3")
    
    add_footer(ax)
    plt.savefig(f"{out_dir}/slide_5.png", dpi=DPI)
    plt.close()
    print("Slide 5 (4:5) regenerated.")

# ==========================================
# SLIDE 6: CALL TO ACTION & PORTAL WEB (4:5)
# ==========================================
def make_slide_6():
    fig, ax = init_canvas()
    add_header(ax, 6)
    
    ax.text(80, 1195, "TERUS BELAJAR & PRAKTIK", fontsize=15, weight="bold", color=ACCENT_GOLD, ha="left", va="top")
    ax.text(80, 1170, "INGIN SIMULASI INTERAKTIF\nDI LAPTOP ANDA?", fontsize=30, weight="black", color=TEXT_WHITE, ha="left", va="top", linespacing=1.15)
    ax.text(80, 1085, "Unduh modul perkuliahan & coba simulasi komputasi Julia RK4 kami!", fontsize=16, weight="bold", color=ACCENT_CYAN, ha="left", va="top")
    
    # Feature 1 (top is 1035, from 880 to 1035)
    f1 = patches.FancyBboxPatch((80, 880), 920, 155, boxstyle="round,pad=10", facecolor=CARD_BG, edgecolor=CARD_BORDER, lw=1.8)
    ax.add_patch(f1)
    ax.text(120, 995, "[ DOKUMEN BELAJAR PDF ]", fontsize=13.5, weight="black", color=ACCENT_CYAN)
    ax.text(120, 965, "Modul Bacaan & Slide Presentasi Lengkap", fontsize=17, weight="bold", color=TEXT_WHITE)
    ax.text(120, 932, "• Modul 5 : Penurunan analitik metode koefisien tak tentu & RLC", fontsize=13.5, color=TEXT_MUTED)
    ax.text(120, 905, "• Slide Ch 5 : Presentasi kelas Beamer interaktif tingkat universitas", fontsize=13.5, color=TEXT_MUTED)
    
    # Feature 2 (top is 860, from 705 to 860)
    f2 = patches.FancyBboxPatch((80, 705), 920, 155, boxstyle="round,pad=10", facecolor=CARD_BG, edgecolor=ACCENT_GOLD, lw=2.0)
    ax.add_patch(f2)
    ax.text(120, 820, "[ SIMULASI KOMPUTASI ]", fontsize=13.5, weight="black", color=ACCENT_GOLD)
    ax.text(120, 790, "Notebook Julia : Simulasi_Transien_RLC.ipynb", fontsize=17, weight="bold", color=TEXT_WHITE)
    ax.text(120, 757, "• Eksperimen numerik menggunakan algoritma Runge-Kutta 4 (RK4)", fontsize=13.5, color=TEXT_MUTED)
    ax.text(120, 730, "• Ubah parameter R, L, C secara bebas & amati kurvanya seketika!", fontsize=13.5, weight="bold", color=ACCENT_GREEN)
    
    # Web Portal Card (top is 675, from 265 to 675)
    f3 = patches.FancyBboxPatch((80, 265), 920, 410, boxstyle="round,pad=18", facecolor="#122B54", edgecolor=ACCENT_CYAN, lw=2.5)
    ax.add_patch(f3)
    ax.text(540, 630, "KUNJUNGI PORTAL RESMI MATA KULIAH :", fontsize=15, weight="black", color=ACCENT_GOLD, ha="center")
    ax.text(540, 555, "pd.ndaratha.my.id", fontsize=40, weight="black", color=ACCENT_CYAN, ha="center")
    ax.text(540, 480, "Tersedia 15 Modul Web, Problem Set, LKM, & Bank Soal", fontsize=16, weight="bold", color=TEXT_WHITE, ha="center")
    ax.text(540, 435, "Dilengkapi rumus interaktif MathJax & akses responsif smartphone", fontsize=13.5, color=TEXT_MUTED, ha="center")
    ax.text(540, 385, "Akses gratis dari smartphone maupun laptop!", fontsize=14.5, weight="bold", color=ACCENT_GREEN, ha="center")
    
    ax.text(540, 195, "Simpan postingan ini & bagikan ke teman sekelasmu!", fontsize=16, weight="bold", color=TEXT_WHITE, ha="center")
    ax.text(540, 150, "#TeknikElektro #UniversitasBengkulu #PersamaanDiferensial #RLCCircuit", fontsize=13.5, color=TEXT_MUTED, ha="center")
    
    add_footer(ax)
    plt.savefig(f"{out_dir}/slide_6.png", dpi=DPI)
    plt.close()
    print("Slide 6 (4:5) regenerated.")

if __name__ == "__main__":
    make_slide_1()
    make_slide_2()
    make_slide_3()
    make_slide_4()
    make_slide_5()
    make_slide_6()
    print("ALL 6 INSTAGRAM CAROUSEL SLIDES (4:5) PERFECTLY REGENERATED!")
