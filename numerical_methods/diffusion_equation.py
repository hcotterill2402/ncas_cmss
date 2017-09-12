import numpy as np
import matplotlib.pyplot as plt
import myfunctions as fn


#set up x points, initial phi, courant number etc
nx = 100    #no. x points
nt = 2000  #no. timesteps
x=np.linspace(0.0, 1.0, nx+1) #setting up x values from 0-1 inclusive

A=fn.coefficient(nx, 0.00002, 0.5)
print (A)

#3 time levels of phi - create copies
B=fn.initialBell(x)

C=fn.diffusion_FTCS(B, nx, nt, A)




#plot solution and compare to analytic solution (Bell curve)
plt.plot(x, fn.initialBell(x), 'k', label='analytic')
plt.plot(x, C, 'b', label='FTCS')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('$\phi$')
plt.axhline(0, linestyle=':', color='black')
plt.show()

