import matplotlib.pyplot as plt

plt.rcParams['mathtext.fontset'] = 'dejavusans'
fig, ax = plt.subplots(figsize=(6, 6))

test_strings = [
    r"PDB: $a y'' + b y' + c y = g(t)$",
    r"Solusi: $y(t) = y_h(t) + y_p(t)$",
    r"$y_h(t) = C_1 \cos(2t) + C_2 \sin(2t)$",
    r"$y_p(t) = t \cdot [A \cos(2t) + B \sin(2t)]$",
    r"$L i'' + R i' + \frac{1}{C} i = v_s'(t)$",
    r"Underdamped: $\alpha < \omega_0$",
    r"Critical: $\alpha = \omega_0$",
    r"Overdamped: $\alpha > \omega_0$",
    r"$\omega = 2\ \mathrm{rad/s}$ dan $\omega_0 = \sqrt{4} = 2\ \mathrm{rad/s}$",
    r"Eksponensial: $e^{kt} \to A e^{kt}$",
    r"Polinomial: $a t^2 + b t + c \to A t^2 + B t + C$",
    r"$t \to \infty$"
]

for i, s in enumerate(test_strings):
    ax.text(0.1, 0.92 - i*0.075, s, fontsize=14)

fig.savefig("test_mathtext_rendered.png")
print("Rendered properly!")
