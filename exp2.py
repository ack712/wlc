import numpy as np
import matplotlib.pyplot as plt

fs = 5000 
t = np.arange(0, 0.04, 1/fs)
fm = 100 


message = np.sin(2 * np.pi * fm * t)

# Real-world channels add Additive White Gaussian Noise (AWGN)
noise_power = 0.4 
noise = np.random.normal(0, noise_power, len(t))


Channel_output = message + noise

# to suppress high-frequency noise spikes and recover the original signal.
window_size = 10
Rx_recovered = np.convolve(Channel_output,
np.ones(window_size)/window_size, mode='same')

# Transmitter Output
plt.subplot(3, 1, 1)
plt.plot(t, message, color='green', linewidth=2)
plt.title('Transmitter o/p')
plt.ylabel('Amplitude')
plt.grid(True)
# Channel Output (Corrupted Signal)
plt.subplot(3, 1, 2)
plt.plot(t, Channel_output, color='red', linewidth=1)
plt.title(f'Channel o/p when Noise Power = {noise_power}')
plt.ylabel('Amplitude')
plt.grid(True)
# Receiver Output
plt.subplot(3, 1, 3)
plt.plot(t, Rx_recovered, color='blue', linewidth=2, label='Filtered Output')
plt.plot(t, message, 'g--', alpha=0.5, label='Original Reference')
plt.title('Receiver (Rx): Recovered/Filtered Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
plt.show()
