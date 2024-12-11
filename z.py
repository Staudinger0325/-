import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify, apart, expand, pi, sin

z, n_sym = symbols('z n', integer=True)
b = [1]  # Numerator coefficients
a = [1, -0.5, 0.25]  # Denominator coefficients

numerator = sum(b[i] * z**(-i) for i in range(len(b)))
denominator = sum(a[i] * z**(-i) for i in range(len(a)))
H_z = simplify(numerator / denominator)

omega = 0.2 * pi
x_z = simplify(1 / (1 - sin(omega) * z**(-1)))  # Z 变换公式（正弦信号）

y_z = simplify(H_z * x_z)

# 部分分式展开
y_z_apart = apart(y_z)

# 手动逆 Z 变换
y_n_term1 = 0.5 * (0.5**n_sym)  # 1st term
y_n_term2 = -0.25 * (0.25**n_sym)  # 2nd term
y_n_sym_manual = expand(y_n_term1 + y_n_term2)

# 数值计算时域响应
n = np.arange(0, 20)
x = np.sin(0.2 * np.pi * n) / 2  # 输入正弦信号
y = np.zeros_like(n, dtype=float)
for i in range(len(n)):
    y[i] = x[i] + (0.5 * y[i - 1] if i - 1 >= 0 else 0) - (0.25 * y[i - 2] if i - 2 >= 0 else 0)

# 零极点图计算
from scipy.signal import tf2zpk
zeros, poles, _ = tf2zpk(b, a)

# 绘制零极点图和离散信号图
plt.figure(figsize=(12, 6))

# 零极点图
plt.subplot(1, 2, 1)
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.scatter(np.real(zeros), np.imag(zeros), s=100, label='Zeros', marker='o', facecolors='none', edgecolors='b')
plt.scatter(np.real(poles), np.imag(poles), s=100, label='Poles', marker='x', color='r')
unit_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
plt.gca().add_artist(unit_circle)
equation_text = r"$y[n] - 0.5y[n-1] + 0.25y[n-2] = x[n]$"
z_transform_text = rf"$H(z) = {H_z}$"
plt.text(-1.2, 1.3, equation_text, fontsize=12, bbox=dict(facecolor='white', alpha=0.8))
plt.text(-1.2, 1.1, z_transform_text, fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Pole-Zero Diagram')
plt.legend()
plt.grid()

# 离散信号图
plt.subplot(1, 2, 2)
plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt=" ", label='Input x[n] (Normalized)')
plt.stem(n, y, linefmt='r--', markerfmt='ro', basefmt=" ", label='Output y[n]')
plt.xlabel('n (samples)')
plt.ylabel('Amplitude')
plt.title('Discrete Signal (Normalized Input)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# 对比时域计算和解析结果
plt.figure(figsize=(10, 5))
plt.stem(n, y, linefmt='r--', markerfmt='ro', basefmt=" ", label='time field response $y[n]$')
plt.title('time field response vs Z-field response')
plt.xlabel('n (samples)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()
plt.show()
