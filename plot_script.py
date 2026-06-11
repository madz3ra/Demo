import matplotlib.pyplot as plt
import numpy as np

# Тестовые данные (позже заменю на CSV)
x = np.linspace(0, 10, 20)
y1 = np.sin(x)
y2 = np.cos(x) * 100

fig, ax1 = plt.subplots()

# Левая ось Y
color1 = 'tab:blue'
ax1.set_xlabel('Время, с')
ax1.set_ylabel('sin(x)', color=color1)
ax1.plot(x, y1, color=color1, marker='o', linestyle='-', label='sin')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, linestyle='--', alpha=0.7)

# Правая ось Y (twinx)
ax2 = ax1.twinx()
color2 = 'tab:red'
ax2.set_ylabel('100*cos(x)', color=color2)
ax2.plot(x, y2, color=color2, marker='s', linestyle='--', label='cos')
ax2.tick_params(axis='y', labelcolor=color2)

plt.title('Две оси Y: пример')
fig.tight_layout()
plt.show()
