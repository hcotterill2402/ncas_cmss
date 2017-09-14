import numpy as np
import matplotlib.pyplot as plt
import myfunctions as fn

#set up x points, initial phi, courant number etc
nx = 100    #no. x points
nt=200
c = 0.2    #the courant number
x=np.linspace(0.0, 1.0, nx+1) #setting up x values from 0-1 inclusive

#derived quantities
u=1.
dx=1./nx
dt=c*dx/u
t=nt*dt

#3 time levels of phi - create copies
B=fn.initialBell(x)

C=fn.linradvection_CTCS(B, nx, nt, c)
D=fn.linradvection_FTCS(B,nx,nt,c)

#plot solution and compare to analytic solution (Bell curve)
plt.plot(x, fn.initialBell(x-u*t), 'k', label='analytic')
plt.plot(x, C, 'b', label='CTCS')
plt.plot(x, D, 'c', label='FTCS')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('$\phi$')
plt.axhline(0, linestyle=':', color='black')
plt.show()
