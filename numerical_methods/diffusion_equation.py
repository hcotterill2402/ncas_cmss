import numpy as np
import matplotlib.pyplot as plt
import myfunctions as fn


#set up x points, initial phi, courant number etc
nx = 100    #no. x points
nt = 35  #no. timesteps
x=np.linspace(0.0, 1.0, nx+1) #setting up x values from 0-1 inclusive

A=fn.coefficient(nx, 0.00002, 0.5)
print (A)

#A=0.252

#3 time levels of phi - create copies
B=fn.initialBell(x)
S=fn.initialSquare(x)

C=fn.diffusion_FTCS(B, nx, nt, A)

#D=fn.diffusion_FTCS(S, nx, nt, A)

E=fn.diffusion_CTCS(B, nx, nt, A)

#plot solution and compare to analytic solution (Bell curve)
plt.plot(x, fn.initialBell(x), 'k', label='bell curve')
#plt.plot(x, fn.initialSquare(x), 'G', label='square')
plt.plot(x, C, 'B', label='FTCS bell curve')
#plt.plot(x, D, 'R', label='FTCS square')
plt.plot(x, E, 'C', label='CTCS bell curve')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('$\phi$')
plt.axhline(0, linestyle=':', color='black')
plt.show()

