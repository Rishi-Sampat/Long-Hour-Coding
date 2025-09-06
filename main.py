import numpy as np
import matplotlib.pyplot as plt

from signal_ICT_RishiSampat_169 import unitary_signals as us
from signal_ICT_RishiSampat_169 import trigonometric_signals as ts
from signal_ICT_RishiSampat_169.operations import time_shift, signal_addition, signal_multiplication as op

n = np.arange(-20, 21)
step_signal = us.unit_step(n)
impulse_signal = us.unit_impulse(n)
ramp_signal_val = us.ramp_signal(n)

t = np.linspace(0, 1, 500)
sine_signal = ts.sine_wave(2, 5, 0, t)
cosine_signal = ts.cosine_wave(2, 5, 0, t)

sine_shifted, _ = op.time_shift(sine_signal, t, 0.01)
plt.figure()
plt.plot(t, sine_signal, label="Original Sine")
plt.plot(t, sine_shifted, label="Shifted Sine")
plt.title("Sine Wave - Original vs Shifted")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

added_signal = op.signal_addition(step_signal, ramp_signal_val, n)
plt.figure()
plt.stem(n, added_signal, basefmt=" ")
plt.title("Addition of Step and Ramp Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

multiplied_signal = op.signal_multiplication(sine_signal, cosine_signal, t)
plt.figure()
plt.plot(t, multiplied_signal, label="Sine * Cosine")
plt.title("Multiplication of Sine and Cosine Signals")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()
