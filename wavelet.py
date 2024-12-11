import numpy as np
import matplotlib.pyplot as plt
import pywt

# 1. 构造理想信号：例如一个正弦波加上某种低频成分
fs = 500      # 采样率
t = np.linspace(0, 1, fs, endpoint=False)
f0 = 5        # 信号频率
ideal_signal = np.sin(2 * np.pi * f0 * t)  # 理想信号

# 2. 构造噪声信号：高频随机噪声(白噪声)
noise_amplitude = 0.5
noise = noise_amplitude * np.random.randn(len(t))  # 随机高频噪声信号

# 有噪声的信号
noisy_signal = ideal_signal + noise

# 3. 使用小波变换去噪
# 使用离散小波分解
wavelet = 'db6'  # 可尝试其他小波基
level = 4        # 分解层数
coeffs = pywt.wavedec(noisy_signal, wavelet, level=level)

# 使用硬阈值/软阈值去除噪声
# 通常阈值可依据统计特性设定，这里简单设置阈值为噪声标准差的某倍数
sigma = np.median(np.abs(coeffs[-1])) / 0.6745  # 通常用中位数绝对偏差估计噪声水平
threshold = sigma * np.sqrt(2 * np.log(len(t)))

# 对细节系数进行阈值化
denoised_coeffs = [coeffs[0]]  # 保留近似系数不进行阈值
for c in coeffs[1:]:
    denoised_coeffs.append(pywt.threshold(c, threshold, mode='soft'))

# 重建去噪后的信号
denoised_signal = pywt.waverec(denoised_coeffs, wavelet)

# 如果重建后长度与原始信号不一样，可截断
denoised_signal = denoised_signal[:len(t)]

# 4. 绘图
plt.figure(figsize=(12, 8))

plt.subplot(4,1,1)
plt.plot(t, ideal_signal, label='Ideal Signal')
plt.title('ideal signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.subplot(4,1,2)
plt.plot(t, noise, label='Noise', color='red')
plt.title('noise signal(mainly high-frequency)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.subplot(4,1,3)
plt.plot(t, noisy_signal, label='Noisy Signal', color='orange')
plt.title('original signal(noise added)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.subplot(4,1,4)
plt.plot(t, denoised_signal, label='Denoised Signal', color='green')
plt.title('signal after denoising')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# 5. 数值比较去噪前后信号与理想信号的差异
# 均方误差
mse_noisy = np.mean((noisy_signal - ideal_signal)**2)
mse_denoised = np.mean((denoised_signal - ideal_signal)**2)

print("添加噪声前的信号与理想信号的 MSE: ", np.mean((ideal_signal - ideal_signal)**2))  # 基准为0
print("添加噪声后的信号与理想信号的 MSE: ", mse_noisy)
print("小波去噪后的信号与理想信号的 MSE: ", mse_denoised)
