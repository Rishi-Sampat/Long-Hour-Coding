import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    """Generate a unit step signal"""
    signal = np.array([1 if i >= 0 else 0 for i in n])
    plt.stem(n, signal)
    plt.title("Unit Step Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def unit_impulse(n):
    """Generate a unit impulse signal"""
    signal = np.array([1 if i == 0 else 0 for i in n])
    plt.stem(n, signal)
    plt.title("Unit Impulse Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def ramp_signal(n):
    """Generate a ramp signal"""
    signal = np.array([i if i >= 0 else 0 for i in n])
    plt.stem(n, signal)
    plt.title("Ramp Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal


if __name__ == "__main__":
    n = np.arange(-10, 10, 1)   # time vector from -10 to 9
    
    step = unit_step(n)
    impulse = unit_impulse(n)
    ramp = ramp_signal(n)

    # Print some values in the terminal
    print("Unit Step Signal:", step)
    print("Unit Impulse Signal:", impulse)
    print("Ramp Signal:", ramp)
