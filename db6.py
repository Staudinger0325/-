import pywt
import matplotlib.pyplot as plt

# 获取 db6 小波函数和尺度函数数据
wavelet = pywt.Wavelet('db6')
phi, psi, x = wavelet.wavefun(level=10)

# 绘制小波函数（psi）和尺度函数（phi）
plt.figure(figsize=(12, 6))

# 绘制尺度函数 phi
plt.subplot(1, 2, 1)
plt.plot(x, phi, label="Scaling function (phi)")
plt.title("Scaling Function (phi) of db6")
plt.xlabel("x")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()

# 绘制小波函数 psi
plt.subplot(1, 2, 2)
plt.plot(x, psi, label="Wavelet function (psi)", color="orange")
plt.title("Wavelet Function (psi) of db6")
plt.xlabel("x")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()

# 显示图像
plt.tight_layout()
plt.show()
