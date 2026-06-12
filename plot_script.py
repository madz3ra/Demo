import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('s_params_ch1.csv')

freq = df['freq']
s21 = df['S21']
s11 = df['S11']
s22 = df['S22']

fig, ax1 = plt.subplots()

# Левая ось: S21
color1 = 'tab:blue'
ax1.set_xlabel('Частота, Гц')
ax1.set_ylabel('S21, дБ', color=color1)
ax1.plot(freq, s21, color=color1, marker='o', linestyle='-', markersize=2, label='S21')
ax1.tick_params(axis='y', labelcolor=color1)

# Фиксированный масштаб левой оси
ax1.set_ylim(14, 22)

# Дополнительная сетка через маркеры для левой оси
ax1.vlines(freq, ymin=14, ymax=s21, colors='blue', linestyles='dotted', linewidth=0.5, alpha=0.3)
ax1.hlines(s21, xmin=freq.min(), xmax=freq.max(), colors='blue', linestyles='dotted', linewidth=0.5, alpha=0.3)

# Основная сетка
ax1.grid(True, linestyle='--', alpha=0.7)

# Правая ось: S11 и S22
ax2 = ax1.twinx()
color2 = 'tab:red'
color3 = 'tab:green'
ax2.set_ylabel('S11, S22', color='black')
ax2.plot(freq, s11, color=color2, marker='s', linestyle='-', markersize=2, label='S11')
ax2.plot(freq, s22, color=color3, marker='^', linestyle='-', markersize=2, label='S22')
ax2.tick_params(axis='y', labelcolor='black')

# Фиксированный масштаб правой оси
ax2.set_ylim(1.0, 2.8)

# Дополнительная сетка через маркеры для правой оси
ax2.vlines(freq, ymin=1.0, ymax=2.8, colors='gray', linestyles='dotted', linewidth=0.3, alpha=0.3)
ax2.hlines(s11, xmin=freq.min(), xmax=freq.max(), colors=color2, linestyles='dotted', linewidth=0.3, alpha=0.3)
ax2.hlines(s22, xmin=freq.min(), xmax=freq.max(), colors=color3, linestyles='dotted', linewidth=0.3, alpha=0.3)

# Легенда
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='best')

plt.title('S-параметры (S21, S11, S22)')
fig.tight_layout()
plt.show()