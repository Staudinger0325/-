from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np

# Define alpha parameter for the exponential decay
alpha = 2

# Define the time domain signal h(t) = e^(-alpha * t) * u(t)
def time_domain_signal(t, alpha):
    return np.exp(-alpha * t) * (t >= 0)

# Define the Laplace transform of the signal (analytical for validation)
def laplace_transform(f, s, alpha):
    """Numerical Laplace transform using integration."""
    result, _ = quad(lambda t: f(t, alpha) * np.exp(-s * t), 0, np.inf)
    return result




def plot(**kwargs):
# Plot the time-domain signal
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, h_t, label=f"Time-Domain Signal: $e^{{-{alpha}t}}$")
    plt.title("Time-Domain Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.legend()

# Plot the frequency-domain signal
    plt.subplot(2, 1, 2)
    plt.plot(s_values.imag, np.abs(H_s_numeric), label="Laplace Transform Magnitude (Numeric)")
    plt.title("Frequency-Domain Response")
    plt.xlabel("Frequency (rad/s)")
    plt.ylabel("|H(s)|")
    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    for alpha in [1,2]:
        # Generate time-domain signal
        t = np.linspace(0, 10, 500)
        h_t = time_domain_signal(t, alpha)
        # Frequency-domain calculation
        s_values = 1j * np.linspace(0.01, 20, 500)  # Purely imaginary axis for frequency response
        H_s_numeric = np.array([laplace_transform(time_domain_signal, s, alpha) for s in s_values])
        plot()