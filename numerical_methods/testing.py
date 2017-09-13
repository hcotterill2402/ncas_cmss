import numpy as np
import matplotlib.pyplot as plt
import myfunctions as fn

nx = 100  
x=np.linspace(0.0, 1.0, nx+1)

def initialSquare(x):
    return np.where(x%1. < 0.5, 0.5, 0)






plt.plot(x, initialSquare(x), 'G', label='square')
plt.plot(x, fn.initialBell(x), 'k', label='analytic')
plt.show()
