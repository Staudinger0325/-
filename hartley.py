import numpy as np
import matplotlib.pyplot as plt

def gaussian_2d(N, sigma):
    """生成一个中心在(N/2, N/2)处的二维高斯信号"""
    x = np.arange(N)
    y = np.arange(N)
    X, Y = np.meshgrid(x, y)
    x0 = N/2
    y0 = N/2
    f = np.exp(-((X - x0)**2 + (Y - y0)**2) / (2 * sigma**2))
    return f

def dht2(f):
    """
    计算二维哈特莱变换(含归一化因子1/N)
    H(u,v) = (1/N)* sum_x sum_y f(x,y)*[cos(2π(xu+ yv)/N) + sin(2π(xu+ yv)/N)]
    假设f为N×N的正方形阵列。
    """
    N = f.shape[0]
    H = np.zeros((N,N), dtype=np.float64)
    # u,v 频域坐标
    for u in range(N):
        for v in range(N):
            # 这里的频率项 (2π/N)(x u + y v)
            # 利用向量化减少部分计算量
            x = np.arange(N)
            y = np.arange(N)
            X, Y = np.meshgrid(x, y)
            arg = 2 * np.pi * (X * u + Y * v) / N
            cos_term = np.cos(arg)
            sin_term = np.sin(arg)
            # 累加求和
            H[u,v] = (1.0/N) * np.sum(f * (cos_term + sin_term))
    return H

# 参数设置
N = 64
sigma = 1

# 1. 生成二维高斯信号
f = gaussian_2d(N, sigma)

# 2. 对f进行哈特莱变换
Hf = dht2(f)

# 3. 对Hf再进行一次哈特莱变换
f_recovered = dht2(Hf)

# 绘制结果
fig, axes = plt.subplots(1, 3, figsize=(12,4))

# 原始信号
axes[0].imshow(f, cmap='jet')
axes[0].set_title("Original Gaussian")

# 变换后的图像
axes[1].imshow(Hf, cmap='jet')
axes[1].set_title("Hartley Transform")

# 再次变换后的图像（应该接近原始）
axes[2].imshow(f_recovered, cmap='jet')
axes[2].set_title("Double Hartley Transform")

for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()
