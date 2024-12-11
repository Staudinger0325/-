from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np

def time_domain_signal(t, alpha):
    return np.exp(-alpha * t) * (t >= 0)

def laplace_transform(f, s, alpha):
    result, _ = quad(lambda tau: f(tau, alpha)*np.exp(-s*tau), 0, np.inf)
    return result

def plot_signals(s_values, H_s_numeric, H_s_analytic, alpha):
    plt.figure(figsize=(8,6))
    plt.plot(s_values, H_s_numeric.real, label="Numeric")
    plt.plot(s_values, H_s_analytic.real, 'r--', label="Analytic")
    plt.title(f"H(s) Along Real Axis (alpha={alpha})")
    plt.xlabel("s (Real)")
    plt.ylabel("H(s)")
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    for alpha in [1,2]:
        # 沿实轴选择 s，起点要大于 -alpha 以保证收敛
        s_values = np.linspace(-alpha+0.1, 10, 500)

        # 数值求拉普拉斯变换
        H_s_numeric = np.array([laplace_transform(time_domain_signal, s, alpha) for s in s_values])

        # 解析解
        H_s_analytic = 1.0/(s_values + alpha)

        # 绘制
        plot_signals(s_values, H_s_numeric, H_s_analytic, alpha)
