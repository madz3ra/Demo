import matplotlib.pyplot as plt
import pandas as pd

# Чтение CSV
df = pd.read_csv('s_params_ch1.csv')

freq = df['freq']
s21 = df['S21']
s11 = df['S11']
s22 = df['S22']

fig, ax1 = plt.subplots()

# Левая ось: S21
color1 = 'tab:blue'
ax1.set_xlabel('Частота, Гц')
ax1.set_ylabel('S21', color=color1)
ax1.plot(freq, s21, color=color1, marker='o', linestyle='-', markersize=4, label='S21')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, linestyle='--', alpha=0.7)

# Правая ось: S11 и S22
ax2 = ax1.twinx()
color2 = 'tab:red'
color3 = 'tab:green'
ax2.set_ylabel('S11, S22', color='black')
ax2.plot(freq, s11, color=color2, marker='s', linestyle='-', markersize=4, label='S11')
ax2.plot(freq, s22, color=color3, marker='^', linestyle='-', markersize=4, label='S22')
ax2.tick_params(axis='y', labelcolor='black')

# Легенда
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='best')

plt.title('S-параметры (S21, S11, S22)')
fig.tight_layout()
plt.show()