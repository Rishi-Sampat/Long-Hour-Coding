import numpy as np
import matplotlib.pyplot as plt

def time_shift(signal, n, k):
    """
    Shifts the signal by k units.
    signal: numpy array (signal values)
    n: numpy array (time indices)
    k: shift amount (positive = right shift, negative = left shift)
    """
    n_shifted = n + k
    plt.stem(n_shifted, signal)
    plt.title(f"Time Shifted Signal (k={k})")
    plt.xlabel("n (Time Index)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal, n_shifted


def time_scale(signal, n, k):
    """
    Scales the time axis of the signal by factor k.
    signal: numpy array (signal values)
    n: numpy array (time indices)
    k: scaling factor (>1 compresses, <1 expands)
    """
    n_scaled = n * k
    plt.stem(n_scaled, signal)
    plt.title(f"Time Scaled Signal (k={k})")
    plt.xlabel("n (Time Index)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal, n_scaled


def signal_addition(signal1, signal2, n):
    """
    Performs addition of two signals (assumes same time index n).
    """
    added_signal = signal1 + signal2
    plt.stem(n, added_signal)
    plt.title("Signal Addition")
    plt.xlabel("n (Time Index)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return added_signal


def signal_multiplication(signal1, signal2, n):
    """
    Performs point-wise multiplication of two signals (assumes same time index n).
    """
    multiplied_signal = signal1 * signal2
    plt.stem(n, multiplied_signal)
    plt.title("Signal Multiplication")
    plt.xlabel("n (Time Index)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return multiplied_signal


if __name__ == "__main__":
    n = np.arange(-5, 6, 1)   # time index from -5 to 5

    # Example base signals
    x1 = np.array([1 if i >= 0 else 0 for i in n])   # unit step
    x2 = np.array([i if i >= 0 else 0 for i in n])   # ramp

    # Time Shift
    print("Testing Time Shift (right shift by 2)...")
    shifted_signal, n_shifted = time_shift(x1, n, 2)
    print("Shifted Indices:", n_shifted)
    print("Shifted Signal:", shifted_signal)

    # Time Scale
    print("\nTesting Time Scale (compress by factor 2)...")
    scaled_signal, n_scaled = time_scale(x2, n, 2)
    print("Scaled Indices:", n_scaled)
    print("Scaled Signal:", scaled_signal)

    # Signal Addition
    print("\nTesting Signal Addition (Unit Step + Ramp)...")
    added_signal = signal_addition(x1, x2, n)
    print("Indices:", n)
    print("Added Signal:", added_signal)

    # Signal Multiplication
    print("\nTesting Signal Multiplication (Unit Step × Ramp)...")
    multiplied_signal = signal_multiplication(x1, x2, n)
    print("Indices:", n)
    print("Multiplied Signal:", multiplied_signal)
