import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

# ----------------------------------------
# Frequency Reuse Simulation
# ----------------------------------------

fig, ax = plt.subplots(figsize=(10,8))

radius = 1

colors = ['red','green','blue','orange','purple','cyan','yellow']

frequencies = ['A','B','C','D','E','F','G']

positions = [
(0,0),
(2,0),
(4,0),
(1,1.73),
(3,1.73),
(5,1.73),
(2,3.46),

(6,0),
(8,0),
(10,0),
(7,1.73),
(9,1.73),
(11,1.73),
(8,3.46)
]

for i,(x,y) in enumerate(positions):

    freq = i % 7

    hexagon = RegularPolygon(
        (x,y),
        numVertices=6,
        radius=radius,
        orientation=np.radians(30),
        facecolor=colors[freq],
        edgecolor='black'
    )

    ax.add_patch(hexagon)
    ax.text(
        x,
        y,
        frequencies[freq],
        fontsize=14,
        ha='center',
        va='center',
        color='white',
        weight='bold'
    )

ax.set_xlim(-2,13)
ax.set_ylim(-2,6)

ax.set_aspect('equal')
ax.set_title("Frequency Reuse in Cellular Network")
plt.grid(True)
plt.show()
