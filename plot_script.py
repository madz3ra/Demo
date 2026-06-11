import matplotlib.pyplot as plt
import pandas as pd

# Чтение CSV
df = pd.read_csv('s_params_ch1.csv')

freq = df['freq']
s21 = df['S21']
s11 = df['S11']  # или df['S22']

fig, ax1 = plt.subplots()

# Левая ось: S21
color1 = 'tab:blue'
ax1.set_xlabel('Частота, Гц')
ax1.set_ylabel('S21, дБ', color=color1)
ax1.plot(freq, s21, color=color1, marker='o', linestyle='-', markersize=4)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, linestyle='--', alpha=0.7)

# Правая ось: S11 (или S22)
ax2 = ax1.twinx()
color2 = 'tab:red'
ax2.set_ylabel('S11, дБ', color=color2)   # или 'S22, дБ'
ax2.plot(freq, s11, color=color2, marker='s', linestyle='--', markersize=4)
ax2.tick_params(axis='y', labelcolor=color2)

plt.title('S-параметры (S21 и S11)')
fig.tight_layout()
plt.show()