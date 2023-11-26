import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,np.pi*2)
x = [m*(np.pi/180) for m in t]
plt.plot(x,np.sin(x))
plt.show