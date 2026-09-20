import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Output directory
out_dir = "docs/images/instagram_minggu_5"
os.makedirs(out_dir, exist_ok=True)

# Common styling constants
W_INCH, H_INCH = 10.8, 19.2
DPI = 100 # Exact 1080 x 1920 px (9:16 aspect ratio)
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
    ax.set_ylim(0, 1920)
    ax.axis("off")
    return fig, ax

def add_header(ax, slide_num, total_slides=6):
    ax.text(80, 1835, "TEKNIK ELEKTRO UNIB", fontsize=20, weight="heavy", color=ACCENT_GOLD, ha="left", va="center")
    ax.text(80, 1805, "Persamaan Diferensial • Semester Genap", fontsize=15, color=TEXT_MUTED, ha="left", va="center")
    
    rect = patches.FancyBboxPatch((870, 1790), 130, 50, boxstyle="round,pad=6", facecolor="#162c52", edgecolor=ACCENT_CYAN, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(935, 1815, f"{slide_num} / {total_slides}", fontsize=18, weight="bold", color=TEXT_WHITE, ha="center", va="center")
    
    ax.plot([80, 1000], [1760, 1760], color="#1e3a63", lw=2)

def add_footer(ax):
    ax.plot([80, 1000], [150, 150], color="#1e3a63", lw=2)
    ax.text(540, 105, "pd.ndaratha.my.id   •   Geser ke kiri >>", fontsize=18, weight="bold", color=ACCENT_GOLD, ha="center", va="center")
    ax.text(540, 70, "Pengampu: Novalio Daratha, Ph.D. & Muhammad Arfan, M.T.", fontsize=14, color=TEXT_MUTED, ha="center", va="center")

# ==========================================
# SLIDE 1: COVER / HOOK
# ==========================================
def make_slide_1():
    fig, ax = init_canvas()
    add_header(ax, 1)
    
    # Tag pill
    pill = patches.FancyBboxPatch((80, 1680), 300, 46, boxstyle="round,pad=8", facecolor="#D97706", edgecolor="none")
    ax.add_patch(pill)
    ax.text(230, 1703, "MINGGU 5: PDB ORDE 2", fontsize=16, weight="black", color=TEXT_WHITE, ha="center", va="center")
    
    # Main Headline (va='top' prevents upward overlap)
    ax.text(80, 1640, "KENAPA RANGKAIAN\nELEKTRONIKA BISA\nMELEDAK?", fontsize=46, weight="black", color=TEXT_WHITE, ha="left", va="top", linespacing=1.2)
    ax.text(80, 1440, "Rahasia Fisik PDB Non-Homogen & Resonansi RLC Seri", fontsize=22, weight="bold", color=ACCENT_CYAN, ha="left", va="top")
    
    # Visual Card: Explosive resonance waveform
    card = patches.FancyBboxPatch((80, 480), 920, 890, boxstyle="round,pad=20", facecolor=CARD_BG, edgecolor=CARD_BORDER, lw=2)
    ax.add_patch(card)
    
    w_pill = patches.FancyBboxPatch((130, 1290), 820, 48, boxstyle="round,pad=8", facecolor="#450A0A", edgecolor=ACCENT_RED, lw=1.5)
    ax.add_patch(w_pill)
    ax.text(540, 1314, "PERINGATAN KRITIS: TEGANGAN MEMBENGKAK TANPA BATAS!", fontsize=16, weight="black", color=ACCENT_RED, ha="center", va="center")
    
    t = np.linspace(0.1, 4*np.pi, 600)
    wave_res = t * np.sin(2.5 * t)
    wave_norm = 175 * (wave_res / np.max(np.abs(wave_res)))
    env = 175 * (t / np.max(t))
    
    xs = 130 + (t / (4*np.pi)) * 820
    ys = 960 + wave_norm
    env_top = 960 + env
    env_bot = 960 - env
    
    ax.plot([130, 950], [960, 960], color="#2c4d75", linestyle="--", lw=1.5)
    ax.plot(xs, env_top, color=ACCENT_GOLD, linestyle=":", lw=2, alpha=0.8)
    ax.plot(xs, env_bot, color=ACCENT_GOLD, linestyle=":", lw=2, alpha=0.8)
    ax.plot(xs, ys, color=ACCENT_RED, lw=3.8, label="Respon Resonansi")
    
    ax.text(930, 1155, "+ Amplitudo ~ t", fontsize=15, weight="bold", color=ACCENT_GOLD, ha="right")
    ax.text(930, 765, "- Amplitudo ~ t", fontsize=15, weight="bold", color=ACCENT_GOLD, ha="right")
    
    ax.text(540, 630, "Ketika frekuensi sumber listrik luar sama persis\ndengan frekuensi alami sistem (w = w0), energi terserap\nterus-menerus hingga komponen terbakar atau meledak!", 
            fontsize=21, color=TEXT_WHITE, ha="center", va="center", linespacing=1.4)
    
    bubble = patches.FancyBboxPatch((80, 230), 920, 170, boxstyle="round,pad=15", facecolor="#142C54", edgecolor=ACCENT_GOLD, lw=2)
    ax.add_patch(bubble)
    ax.text(540, 335, "Bagaimana cara matematika memprediksi", fontsize=22, color=TEXT_WHITE, ha="center")
    ax.text(540, 285, "dan mengamankan fenomena berbahaya ini?", fontsize=24, weight="black", color=ACCENT_GOLD, ha="center")
    
    add_footer(ax)
    plt.savefig(f"{out_dir}/slide_1.png", dpi=DPI)
    plt.close()
    print("Slide 1 regenerated.")

# ==========================================
# SLIDE 2: STRUKTUR SOLUSI TOTAL
# ==========================================
def make_slide_2():
    fig, ax = init_canvas()
    add_header(ax, 2)
    
    ax.text(80, 1710, "KONSEP KUNCI", fontsize=18, weight="bold", color=ACCENT_GOLD, ha="left", va="top")
    ax.text(80, 1675, "STRUKTUR SOLUSI TOTAL", fontsize=44, weight="black", color=TEXT_WHITE, ha="left", va="top")
    ax.text(80, 1610, "PDB Non-Homogen:  a y'' + b y' + c y = g(t)", fontsize=22, weight="bold", color=ACCENT_CYAN, ha="left", va="top")
    
    f_box = patches.FancyBboxPatch((80, 1400), 920, 140, boxstyle="round,pad=15", facecolor="#1A365D", edgecolor=ACCENT_GOLD, lw=3)
    ax.add_patch(f_box)
    ax.text(540, 1470, "y(t)  =  y_h(t)  +  y_p(t)", fontsize=44, weight="black", color="#FFD700", ha="center", va="center")
    
    c1 = patches.FancyBboxPatch((80, 860), 920, 480, boxstyle="round,pad=18", facecolor=CARD_BG, edgecolor="#2563EB", lw=2)
    ax.add_patch(c1)
    ax.text(120, 1280, "[1] Solusi Homogen : y_h(t)", fontsize=26, weight="black", color=ACCENT_CYAN)
    ax.text(120, 1225, "• Persamaan saat sumber padam : a y'' + b y' + c y = 0", fontsize=19, color=TEXT_WHITE)
    ax.text(120, 1170, "• Fisika Elektro : RESPON ALAMI / TRANSIEN (Natural)", fontsize=20, weight="bold", color=ACCENT_GOLD)
    ax.text(120, 1115, "• Karakter : Reaksi awal pelepasan energi induktor (L) & kapasitor (C).", fontsize=18, color=TEXT_MUTED)
    ax.text(120, 1065, "• Sifat Mutlak : Pasti MELURUH HABIS menuju nol (t -> tak hingga)", fontsize=18, weight="bold", color=ACCENT_GREEN)
    ax.text(120, 1015, "  akibat adanya disipasi daya pada resistor R.", fontsize=18, color=TEXT_MUTED)
    
    c2 = patches.FancyBboxPatch((80, 330), 920, 480, boxstyle="round,pad=18", facecolor=CARD_BG, edgecolor="#DC2626", lw=2)
    ax.add_patch(c2)
    ax.text(120, 750, "[2] Solusi Partikular : y_p(t)", fontsize=26, weight="black", color=ACCENT_RED)
    ax.text(120, 695, "• Menemukan satu fungsi yang memuaskan ruas kanan g(t)", fontsize=19, color=TEXT_WHITE)
    ax.text(120, 640, "• Fisika Elektro : RESPON PAKSA / TUNAK (Steady-State)", fontsize=20, weight="bold", color=ACCENT_GOLD)
    ax.text(120, 585, "• Karakter : Mengikuti frekuensi & pola sumber listrik dari luar.", fontsize=18, color=TEXT_MUTED)
    ax.text(120, 535, "• Sifat Mutlak : TETAP ADA SELAMANYA selama generator menyala.", fontsize=18, weight="bold", color="#FCA5A5")
    ax.text(120, 485, "  Menentukan keadaan operasional jangka panjang rangkaian.", fontsize=18, color=TEXT_MUTED)
    
    s_pill = patches.FancyBboxPatch((80, 205), 920, 85, boxstyle="round,pad=10", facecolor="#0F172A", edgecolor="#334155", lw=1.5)
    ax.add_patch(s_pill)
    ax.text(540, 247, "Solusi Lengkap = Respon Transien (Hilang) + Mantap (Kekal)", fontsize=20, weight="bold", color=TEXT_WHITE, ha="center")
    
    add_footer(ax)
    plt.savefig(f"{out_dir}/slide_2.png", dpi=DPI)
    plt.close()
    print("Slide 2 regenerated.")

# ==========================================
# SLIDE 3: METODE KOEFISIEN TAK TENTU
# ==========================================
def make_slide_3():
    fig, ax = init_canvas()
    add_header(ax, 3)
    
    ax.text(80, 1710, "METODE PRAKTIS", fontsize=18, weight="bold", color=ACCENT_GOLD, ha="left", va="top")
    ax.text(80, 1675, "TEBAK SOLUSI SEPERTI PRO!", fontsize=42, weight="black", color=TEXT_WHITE, ha="left", va="top")
    ax.text(80, 1610, "Metode Koefisien Tak Tentu (Undetermined Coefficients)", fontsize=21, weight="bold", color=ACCENT_CYAN, ha="left", va="top")
    
    t_box = patches.FancyBboxPatch((80, 770), 920, 780, boxstyle="round,pad=15", facecolor=CARD_BG, edgecolor=CARD_BORDER, lw=2)
    ax.add_patch(t_box)
    
    ax.text(120, 1485, "Bentuk Sumber g(t)", fontsize=21, weight="black", color=ACCENT_GOLD)
    ax.text(520, 1485, "Tebakan Solusi Partikular y_p(t)", fontsize=21, weight="black", color=ACCENT_GOLD)
    ax.plot([110, 970], [1455, 1455], color="#2B4C7E", lw=2)
    
    rows = [
        ("Konstanta C", "A  (Konstanta)", 1385),
        ("Eksponensial : e^(k t)", "A • e^(k t)", 1275),
        ("Sinusoidal : sin(w t) / cos(w t)", "A cos(w t) + B sin(w t)", 1165),
        ("Polinomial : a t^2 + b t + c", "A t^2 + B t + C", 1055),
        ("Kombinasi : e^(k t) cos(w t)", "e^(k t) [A cos(w t) + B sin(w t)]", 945),
    ]
    
    for left, right, y_pos in rows:
        ax.text(120, y_pos, left, fontsize=19, color=TEXT_WHITE)
        ax.text(520, y_pos, right, fontsize=19, weight="bold", color="#7DD3FC")
        if y_pos > 950:
            ax.plot([110, 970], [y_pos - 40, y_pos - 40], color="#1E3A63", lw=1)
            
    ax.text(540, 830, "Catatan: Substitusi y_p ke PDB untuk mencari nilai konstanta A, B, C.", fontsize=16, color=TEXT_MUTED, ha="center", style="italic")
    
    w_box = patches.FancyBboxPatch((80, 220), 920, 500, boxstyle="round,pad=18", facecolor="#3B1212", edgecolor=ACCENT_RED, lw=2.5)
    ax.add_patch(w_box)
    
    ax.text(120, 665, "ATURAN MODIFIKASI (THE GOLDEN RULE):", fontsize=23, weight="black", color="#FCA5A5")
    ax.text(120, 605, "Jika tebakan y_p memuat suku yang SAMA PERSIS\ndengan salah satu suku pada solusi homogen y_h...", fontsize=20, color=TEXT_WHITE, linespacing=1.3)
    ax.text(120, 505, ">> KALIKAN TEBAKAN ANDA DENGAN 't'!", fontsize=24, weight="black", color=ACCENT_GOLD)
    
    ex_box = patches.FancyBboxPatch((110, 310), 860, 150, boxstyle="round,pad=10", facecolor="#240D0D", edgecolor="#7F1D1D", lw=1.5)
    ax.add_patch(ex_box)
    ax.text(130, 415, "Contoh: Jika y_h memuat cos(2t) dan sumber g(t) = 4 cos(2t),", fontsize=18, color="#E2E8F0")
    ax.text(130, 370, "maka tebakan biasa GAGAL! Tebakan yang benar:", fontsize=18, color="#E2E8F0")
    ax.text(130, 325, "y_p(t) = t • [ A cos(2t) + B sin(2t) ]", fontsize=20, weight="black", color=ACCENT_CYAN)
    
    ax.text(120, 250, "Faktor 't' inilah yang memicu pertumbuhan resonansi tanpa batas!", fontsize=17, weight="bold", color=ACCENT_GOLD)
    
    add_footer(ax)
    plt.savefig(f"{out_dir}/slide_3.png", dpi=DPI)
    plt.close()
    print("Slide 3 regenerated.")

# ==========================================
# SLIDE 4: 3 WAJAH REDAMAN RLC
# ==========================================
def make_slide_4():
    fig, ax = init_canvas()
    add_header(ax, 4)
    
    ax.text(80, 1710, "APLIKASI TEKNIK ELEKTRO", fontsize=18, weight="bold", color=ACCENT_GOLD, ha="left", va="top")
    ax.text(80, 1675, "3 WAJAH REDAMAN RLC", fontsize=44, weight="black", color=TEXT_WHITE, ha="left", va="top")
    ax.text(80, 1610, "Persamaan:  L i'' + R i' + (1/C) i = v_s'(t)", fontsize=21, weight="bold", color=ACCENT_CYAN, ha="left", va="top")
    
    t = np.linspace(0, 10, 500)
    y_under = np.exp(-0.45 * t) * np.sin(2.4 * t)
    y_crit = 1.3 * t * np.exp(-1.0 * t)
    y_over = 1.1 * (np.exp(-0.35 * t) - np.exp(-2.2 * t))
    
    card = patches.FancyBboxPatch((80, 970), 920, 580, boxstyle="round,pad=15", facecolor=CARD_BG, edgecolor=CARD_BORDER, lw=2)
    ax.add_patch(card)
    
    ax.text(120, 1495, "Perbandingan Kurva Arus Transien RLC Seri :", fontsize=20, weight="black", color=TEXT_WHITE)
    
    def to_coords(t_arr, y_arr, y_scale=150, y_offset=1180):
        xs = 130 + (t_arr / 10.0) * 810
        ys = y_offset + y_arr * y_scale
        return xs, ys
    
    ax.plot([130, 940], [1180, 1180], color="#2B4C7E", linestyle="--", lw=1.5)
    
    x_u, y_u = to_coords(t, y_under)
    x_c, y_c = to_coords(t, y_crit)
    x_o, y_o = to_coords(t, y_over)
    
    ax.plot(x_u, y_u, color=ACCENT_RED, lw=3.5, label="Underdamped")
    ax.plot(x_c, y_c, color=ACCENT_GOLD, lw=3.5, label="Critically Damped")
    ax.plot(x_o, y_o, color=ACCENT_GREEN, lw=3.5, label="Overdamped")
    
    ax.text(620, 1435, "— Underdamped (R kecil)", color=ACCENT_RED, fontsize=17, weight="bold")
    ax.text(620, 1390, "— Critical (R pas)", color=ACCENT_GOLD, fontsize=17, weight="bold")
    ax.text(620, 1345, "— Overdamped (R besar)", color=ACCENT_GREEN, fontsize=17, weight="bold")
    
    u_c = patches.FancyBboxPatch((80, 725), 920, 215, boxstyle="round,pad=12", facecolor="#261014", edgecolor=ACCENT_RED, lw=1.5)
    ax.add_patch(u_c)
    ax.text(110, 885, "1. Underdamped (alpha < w0) — Kurang Redam", fontsize=20, weight="black", color=ACCENT_RED)
    ax.text(110, 835, "• Arus berosilasi bolak-balik frekuensi tinggi sebelum reda.", fontsize=18, color=TEXT_WHITE)
    ax.text(110, 790, "• Bahaya: Lonjakan tegangan (overshoot) rentan merusak komponen IC!", fontsize=17, color=TEXT_MUTED)
    ax.text(110, 750, "• Aplikasi: Rangkaian pemancar radio & filter frekuensi tertentu.", fontsize=17, color="#FDA4AF")
    
    c_c = patches.FancyBboxPatch((80, 480), 920, 215, boxstyle="round,pad=12", facecolor="#272111", edgecolor=ACCENT_GOLD, lw=1.5)
    ax.add_patch(c_c)
    ax.text(110, 640, "2. Critically Damped (alpha = w0) — Redam Kritis", fontsize=20, weight="black", color=ACCENT_GOLD)
    ax.text(110, 590, "• Waktu transien PALING CEPAT tanpa pernah terjadi overshoot.", fontsize=18, color=TEXT_WHITE)
    ax.text(110, 545, "• Stabil seketika dan tidak menimbulkan gangguan dengung.", fontsize=17, color=TEXT_MUTED)
    ax.text(110, 505, "• Aplikasi: Saklar pemutus daya (breaker) & jarum ukur analog.", fontsize=17, color="#FEF08A")
    
    o_c = patches.FancyBboxPatch((80, 235), 920, 215, boxstyle="round,pad=12", facecolor="#0E2319", edgecolor=ACCENT_GREEN, lw=1.5)
    ax.add_patch(o_c)
    ax.text(110, 395, "3. Overdamped (alpha > w0) — Lebih Redam", fontsize=20, weight="black", color=ACCENT_GREEN)
    ax.text(110, 345, "• Arus meluruh sangat lambat dan lamban mencapai nilai mantap.", fontsize=18, color=TEXT_WHITE)
    ax.text(110, 300, "• Hambatan R besar menyebabkan rugi-rugi panas yang tinggi.", fontsize=17, color=TEXT_MUTED)
    ax.text(110, 260, "• Aplikasi: Peredam kejut transien ekstrem pada transformator daya.", fontsize=17, color="#A7F3D0")
    
    add_footer(ax)
    plt.savefig(f"{out_dir}/slide_4.png", dpi=DPI)
    plt.close()
    print("Slide 4 regenerated.")

# ==========================================
# SLIDE 5: MINI QUIZ / BRAIN TEASER
# ==========================================
def make_slide_5():
    fig, ax = init_canvas()
    add_header(ax, 5)
    
    ax.text(80, 1710, "UJI PEMAHAMAN ANDA", fontsize=18, weight="bold", color=ACCENT_GOLD, ha="left", va="top")
    ax.text(80, 1675, "BRAIN TEASER MINGGU 5", fontsize=44, weight="black", color=TEXT_WHITE, ha="left", va="top")
    ax.text(80, 1610, "Kuis Kilat Solusi Partikular & Resonansi", fontsize=21, weight="bold", color=ACCENT_CYAN, ha="left", va="top")
    
    q_card = patches.FancyBboxPatch((80, 1160), 920, 400, boxstyle="round,pad=18", facecolor="#162E52", edgecolor=ACCENT_GOLD, lw=2.5)
    ax.add_patch(q_card)
    ax.text(120, 1500, "[ SOAL KUIS ]", fontsize=22, weight="black", color=ACCENT_GOLD)
    ax.text(120, 1435, "Diberikan persamaan osilator tak teredam:", fontsize=20, color=TEXT_WHITE)
    ax.text(120, 1365, "y'' + 4 y = 6 cos(2t)", fontsize=36, weight="black", color=ACCENT_CYAN)
    ax.text(120, 1295, "Solusi homogennya :  y_h(t) = C1 cos(2t) + C2 sin(2t)", fontsize=19, color=TEXT_MUTED)
    ax.text(120, 1230, "Manakah bentuk tebakan solusi partikular y_p yang benar?", fontsize=20, weight="bold", color=TEXT_WHITE)
    
    opt_a = patches.FancyBboxPatch((80, 990), 920, 140, boxstyle="round,pad=12", facecolor=CARD_BG, edgecolor=CARD_BORDER, lw=1.5)
    ax.add_patch(opt_a)
    ax.text(120, 1075, "PILIHAN A :", fontsize=18, weight="bold", color=ACCENT_RED)
    ax.text(120, 1030, "y_p(t) = A cos(2t) + B sin(2t)", fontsize=22, weight="bold", color=TEXT_WHITE)
    
    opt_b = patches.FancyBboxPatch((80, 815), 920, 145, boxstyle="round,pad=12", facecolor=CARD_BG, edgecolor=ACCENT_GREEN, lw=2.2)
    ax.add_patch(opt_b)
    ax.text(120, 905, "PILIHAN B (KASUS RESONANSI) :", fontsize=18, weight="bold", color=ACCENT_GREEN)
    ax.text(120, 855, "y_p(t) = t • [ A cos(2t) + B sin(2t) ]", fontsize=23, weight="black", color=ACCENT_GREEN)
    
    rev = patches.FancyBboxPatch((80, 230), 920, 545, boxstyle="round,pad=15", facecolor="#102E20", edgecolor=ACCENT_GREEN, lw=2.5)
    ax.add_patch(rev)
    ax.text(120, 715, "[ JAWABAN BENAR : PILIHAN B ]", fontsize=24, weight="black", color=ACCENT_GREEN)
    ax.text(120, 650, "Alasan Matematis & Karakteristik Fisik:", fontsize=20, weight="bold", color=TEXT_WHITE)
    ax.text(120, 595, "1. Frekuensi sumber luar (w = 2 rad/s) PERSIS SAMA dengan", fontsize=18, color="#E2E8F0")
    ax.text(120, 555, "   frekuensi alami sistem (w0 = sqrt(4) = 2 rad/s).", fontsize=18, color="#E2E8F0")
    ax.text(120, 500, "2. Tebakan Pilihan A sudah menjadi solusi homogen y_h.", fontsize=18, color=TEXT_MUTED)
    ax.text(120, 460, "   Bila disubstitusi, ruas kiri jadi 0 = 6 cos(2t) (KONTRAKSI!).", fontsize=18, color="#FECDD3")
    ax.text(120, 405, "3. Menurut Aturan Modifikasi, tebakan WAJIB dikalikan 't'.", fontsize=18, weight="bold", color=ACCENT_GOLD)
    ax.text(120, 355, "   Pengali 't' menyebabkan amplitudo membesar linier terhadap waktu,", fontsize=17, color=TEXT_MUTED)
    ax.text(120, 315, "   membuktikan kenapa resonansi tak diredam dapat membakar rangkaian!", fontsize=17, color="#FECDD3")
    
    add_footer(ax)
    plt.savefig(f"{out_dir}/slide_5.png", dpi=DPI)
    plt.close()
    print("Slide 5 regenerated.")

# ==========================================
# SLIDE 6: CALL TO ACTION & PORTAL WEB
# ==========================================
def make_slide_6():
    fig, ax = init_canvas()
    add_header(ax, 6)
    
    ax.text(80, 1710, "TERUS BELAJAR & PRAKTIK", fontsize=18, weight="bold", color=ACCENT_GOLD, ha="left", va="top")
    ax.text(80, 1665, "INGIN SIMULASI INTERAKTIF\nDI LAPTOP ANDA?", fontsize=40, weight="black", color=TEXT_WHITE, ha="left", va="top", linespacing=1.2)
    ax.text(80, 1530, "Unduh bahan kuliah lengkap & coba simulasi komputasi kami!", fontsize=20, weight="bold", color=ACCENT_CYAN, ha="left", va="top")
    
    f1 = patches.FancyBboxPatch((80, 1240), 920, 240, boxstyle="round,pad=15", facecolor=CARD_BG, edgecolor=CARD_BORDER, lw=2)
    ax.add_patch(f1)
    ax.text(120, 1420, "[ DOKUMEN BELAJAR PDF ]", fontsize=18, weight="black", color=ACCENT_CYAN)
    ax.text(120, 1370, "Modul Bacaan & Slide Presentasi Lengkap", fontsize=22, weight="bold", color=TEXT_WHITE)
    ax.text(120, 1315, "• Modul 5 : Penurunan analitik metode koefisien tak tentu & RLC", fontsize=17, color=TEXT_MUTED)
    ax.text(120, 1275, "• Slide Ch 5 : Presentasi kelas Beamer interaktif tingkat universitas", fontsize=17, color=TEXT_MUTED)
    
    f2 = patches.FancyBboxPatch((80, 950), 920, 250, boxstyle="round,pad=15", facecolor=CARD_BG, edgecolor=ACCENT_GOLD, lw=2.2)
    ax.add_patch(f2)
    ax.text(120, 1140, "[ SIMULASI KOMPUTASI ]", fontsize=18, weight="black", color=ACCENT_GOLD)
    ax.text(120, 1090, "Notebook Julia : Simulasi_Transien_RLC.ipynb", fontsize=22, weight="bold", color=TEXT_WHITE)
    ax.text(120, 1035, "• Eksperimen numerik menggunakan algoritma Runge-Kutta 4 (RK4)", fontsize=17, color=TEXT_MUTED)
    ax.text(120, 995, "• Ubah parameter R, L, C secara bebas & amati kurvanya seketika!", fontsize=17, weight="bold", color=ACCENT_GREEN)
    
    f3 = patches.FancyBboxPatch((80, 480), 920, 420, boxstyle="round,pad=20", facecolor="#122B54", edgecolor=ACCENT_CYAN, lw=3)
    ax.add_patch(f3)
    ax.text(540, 840, "KUNJUNGI PORTAL RESMI MATA KULIAH :", fontsize=20, weight="black", color=ACCENT_GOLD, ha="center")
    ax.text(540, 750, "pd.ndaratha.my.id", fontsize=48, weight="black", color=ACCENT_CYAN, ha="center")
    ax.text(540, 660, "Tersedia 15 Modul Web, Problem Set, LKM, & Bank Soal", fontsize=20, weight="bold", color=TEXT_WHITE, ha="center")
    ax.text(540, 605, "Dilengkapi rumus interaktif MathJax & akses responsif", fontsize=18, color=TEXT_MUTED, ha="center")
    ax.text(540, 545, "Akses gratis dari smartphone maupun laptop!", fontsize=18, weight="bold", color=ACCENT_GREEN, ha="center")
    
    ax.text(540, 360, "Simpan postingan ini & bagikan ke teman sekelasmu!", fontsize=22, weight="bold", color=TEXT_WHITE, ha="center")
    ax.text(540, 300, "#TeknikElektro #UniversitasBengkulu #PersamaanDiferensial #RLCCircuit", fontsize=17, color=TEXT_MUTED, ha="center")
    
    add_footer(ax)
    plt.savefig(f"{out_dir}/slide_6.png", dpi=DPI)
    plt.close()
    print("Slide 6 regenerated.")

if __name__ == "__main__":
    make_slide_1()
    make_slide_2()
    make_slide_3()
    make_slide_4()
    make_slide_5()
    make_slide_6()
    print("ALL 6 INSTAGRAM CAROUSEL SLIDES PERFECTLY REGENERATED!")
