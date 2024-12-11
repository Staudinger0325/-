import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

def fractional_fourier_transform(f, t, a):
    """
    根据定义计算f(t)的a阶分数傅立叶变换F_a(u)。
    a为分数阶。
    """
    alpha = a * np.pi / 2

    # 避免 alpha = k*pi 导致 sin(alpha)=0 的情况（仅对于非零a）
    if np.isclose(np.sin(alpha), 0, atol=1e-15) and not np.isclose(a,0,atol=1e-15):
        epsilon = 1e-10
        if np.isclose(alpha, 0, atol=1e-15):
            alpha = epsilon
        elif np.isclose(alpha, np.pi, atol=1e-15):
            alpha = np.pi - epsilon
    
    sin_alpha = np.sin(alpha)
    cos_alpha = np.cos(alpha)
    cot_alpha = cos_alpha / sin_alpha
    
    u = t.copy()
    prefactor = np.sqrt(1/(2*np.pi*np.abs(sin_alpha)))
    F_a = np.zeros_like(u, dtype=complex)

    for idx, u_val in enumerate(u):
        phase_t = 1j * ( (t**2)*cot_alpha/2 - (u_val * t)/sin_alpha )
        integrand = f * np.exp(phase_t)
        integral_val = simpson(integrand, x=t)
        F_a[idx] = prefactor * np.exp(1j*(u_val**2)*cot_alpha/2)* integral_val

    return u, F_a

def frft_at_zero(f, t, epsilon=1e-6):
    # 通过对 a=+delta 和 a=-delta 的FRFT求平均来逼近 a=0
    a_pos = epsilon/(np.pi/2)   # alpha ~ epsilon
    a_neg = -epsilon/(np.pi/2)  # alpha ~ -epsilon
    u_pos, F_a_pos = fractional_fourier_transform(f, t, a_pos)
    u_neg, F_a_neg = fractional_fourier_transform(f, t, a_neg)
    return u_pos, 0.5*(F_a_pos + F_a_neg)

if __name__ == "__main__":
    # 定义时间轴与信号
    t_max = 10
    N = 2048
    t = np.linspace(-t_max, t_max, N)
    f0 = 1.0
    f = np.sin(2*np.pi*f0*t)

    # 分数阶列表
    a_list = [0, 0.5, 0.7, 0.9, 1]

    plt.figure(figsize=(12,8))

    # 原始信号
    plt.subplot(2,3,1)
    plt.plot(t, f, label='f(t)')
    plt.title('Original Signal')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.grid(True)
    plt.legend()

    # a=0特殊处理
    a = 0
    u0, F_a0 = frft_at_zero(f, t, epsilon=1e-6)
    plt.subplot(2,3,2)
    plt.plot(u0, np.real(F_a0), label='Real')
    plt.plot(u0, np.imag(F_a0), label='Imag')
    plt.title('FRFT (a=0)')
    plt.xlabel('u')
    plt.ylabel('F_0(u)')
    plt.grid(True)
    plt.legend()

    # 其他分数阶
    # a=0.5 -> subplot(2,3,3)
    # a=0.7 -> subplot(2,3,4)
    # a=0.9 -> subplot(2,3,5)
    # a=1   -> subplot(2,3,6)
    for i, a in enumerate(a_list[1:], start=3):
        u_val, F_a = fractional_fourier_transform(f, t, a)
        plt.subplot(2,3,i)
        plt.plot(u_val, np.abs(F_a), label='|F_{a}(u)|')
        plt.title('FRFT (a={})'.format(a))
        plt.xlabel('u')
        plt.ylabel('|F_a(u)|')
        plt.grid(True)
        plt.legend()

    plt.tight_layout()
    plt.show()
