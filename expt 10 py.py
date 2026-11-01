import matplotlib.pyplot as plt
import numpy as np

# Distance from router in metres
distance = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Average RSSI obtained from experiment
rssi = np.array([-45, -49, -43, -55, -47, -62, -51, -46])

plt.figure(figsize=(9, 5))

plt.plot(
    distance,
    rssi,
    marker='o',
    linewidth=2
)

plt.xlabel("Distance from Router (m)")
plt.ylabel("Average RSSI (dBm)")
plt.title("Analysis of Multipath Effects")

plt.grid(True)

# More negative RSSI = weaker signal
plt.gca().invert_yaxis()

plt.show()

