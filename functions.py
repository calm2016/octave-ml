import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
x = np.linspace(0, 2 * pi, 100)
sin = np.sin(x)
cos = np.cos(x)

plt.plot(x, sin)
plt.plot(x, cos)

plt.xlabel('x')
plt.ylabel('y')

plt.show()
