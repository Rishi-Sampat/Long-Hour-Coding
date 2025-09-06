import numpy as np
import matplotlib.pyplot as plt

def sine_wave(A, f, phi, t):
    """A-Amplitude, f-frequency, phi-phase(radians), t-time"""
    signal = A * np.sin(2 * np.pi * f * t + phi)
    plt.plot(t, signal)
    plt.title(f"Sine Wave: A={A}, f={f}Hz, phi={phi} rad")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal


def cosine_wave(A, f, phi, t):
    signal = A * np.cos(2 * np.pi * f * t + phi)
    plt.plot(t, signal)
    plt.title(f"Cosine Wave: A={A}, f={f}Hz, phi={phi} rad")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal


def exponential_signal(A, a, t):
    signal = A * np.exp(a * t)
    plt.plot(t, signal)
    plt.title(f"Exponential Signal: A={A}, a={a}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal


# MAIN EXECUTION
if __name__ == "__main__":
    t = np.linspace(0, 1, 500)   # time from 0 to 1 sec, 500 points

    sine_wave(1, 5, 0, t)        # Sine: amplitude=1, freq=5Hz, phase=0
    cosine_wave(1, 5, 0, t)      # Cosine: amplitude=1, freq=5Hz, phase=0
    exponential_signal(1, 2, t)  # Exponential: A=1, a=2
