import numpy as np
import matplotlib.pyplot as plt


def plot_signal_and_fft(fs, f):
    """
    绘制信号和其傅里叶变换结果
    :param fs: 采样率
    :param f: 信号频率
    """
    # 生成信号
    t = np.arange(0, 1, 1/fs)  # 时间向量
    signal = np.sin(2 * np.pi * f * t)
    
    # 傅里叶变换
    signal_fft = np.fft.fft(signal)
    freq = np.fft.fftfreq(len(signal), 1/fs)
    
    # 绘制信号和频谱
    plt.figure(figsize=(12, 6))
    
    # 原信号
    plt.subplot(2, 1, 1)
    plt.plot(t, signal)
    plt.title(f'Signal (Frequency: {f} Hz, Sampling Rate: {fs} Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    
    # 傅里叶变换
    plt.subplot(2, 1, 2)
    plt.plot(freq[:len(freq)//2], np.abs(signal_fft[:len(signal)//2]))
    plt.title('Signal Frequency Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # 第一组：保持采样率为 10000 Hz，依次改变信号频率
    fs = 10000
    for f in [50, 100, 200, 500]:
        print(f"Running with fs={fs}, f={f}")
        plot_signal_and_fft(fs, f)
    
    # 第二组：保持信号频率为 2 Hz，依次改变采样率
    f = 2
    for fs in [10, 20, 50, 100]:
        print(f"Running with fs={fs}, f={f}")
        plot_signal_and_fft(fs, f)
