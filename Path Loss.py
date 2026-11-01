#study of path loss
import numpy as np
import matplotlib.pyplot as plt
f1 = 800e6 #first frequency in Hz
f2 = 950e6 #second frequency in Hz
c = 3e8 #velocity of light in m/s
d = np.arange(1,50,0.01)
PL1 = 20*np.log10(4*np.pi/c)+20*np.log10(f1)+20*np.log10(d)
PL2 = 20*np.log10(4*np.pi/c)+20*np.log10(f2)+20*np.log10(d)
plt.plot(d,PL1,"k-",label = "at 800MHz")
plt.plot(d,PL2,"k--",label = "at 950MHz")
plt.xlabel("distance in meter")
plt.ylabel("path loss in dB")
plt.title("path loss")
plt.legend()
plt.show()
