import numpy as np
import matplotlib.pyplot as plt

# Function to definte the initial conditions, ie a Bell curve
def initialBell(x):
    return np.where(x%1. < 0.5, np.power(np.sin(2*x*np.pi), 2), 0)

#set up x points, initial phi, courant number etc
nx = 40    #no. x points
c = 0.2    #the courant number
x=np.linspace(0.0, 1.0, nx+1) #setting up x values from 0-1 inclusive

#3 time levels of phi - create copies
phi=initialBell(x)
phiNew=phi.copy() #new timestep (n+1)
phiOld=phi.copy() #old timestep (n-1)

#FTCS for first timestep (since there is no n-1 value)
#loop over space
for j in xrange(1,nx):
    phi[j]=phiOld[j]-0.5*c*(phiOld[j+1]-phiOld[j-1])

#apply periodic bc's
phi[0]=phiOld[j]-0.5*c*(phiOld[1]-phiOld[nx-1])
phi[nx]=phi[0]

#loop over remaining timesteps using CTCS
nt=40
for n in xrange(1,nt):
    #loop over space
    for j in xrange(1,nx):
        phiNew[j]=phiOld[j]-c*(phi[j+1]-phi[j-1])
    #apply periodic bcs
    phiNew[0]=phiOld[0]-c*(phi[1]-phi[nx-1])
    phiNew[nx]=phiNew[0]

    #update for next timestep
    phiOld=phi.copy()
    phi=phiNew.copy()


#derived quantities
u=1.
dx=1./nx
dt=c*dx/u
t=nt*dt

#plot solution and compare to analytic solution (Bell curve)
plt.plot(x, initialBell(x-u*t), 'k', label='analytic')
plt.plot(x, phi, 'b', label='CTCS')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('$\phi$')
plt.axhline(0, linestyle=':', color='black')
plt.show()
