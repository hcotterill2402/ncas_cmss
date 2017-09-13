import numpy as np

# Function to definte the initial conditions, ie a Bell curve
def initialBell(x):
    return np.where(x%1. < 0.5, np.power(np.sin(2*x*np.pi), 2), 0)

def initialSquare(x):
    return np.where(x%1. < 0.5, 0.5, 0)

def coefficient(nx, K, dt):
    dx=1./nx
    D=(K*dt)/(dx**2)
    return D

def diffusion_FTCS(phi, nx, nt, A):
    phiNew=phi.copy() #new timestep (n+1)
    phiOld=phi.copy() #old timestep (n-1)

    #FTCS for first timestep
    for j in xrange(1,nx):
        phi[j]=phiOld[j]+A*(phiOld[j+1]-2*phiOld[j]+phiOld[j-1])

    #apply periodic bc's
    phi[0]=phiOld[0]+A*(phiOld[1]-2*phiOld[0]+phiOld[nx-1])
    phi[nx]=phi[0]

    #loop over remaining timesteps using FTCS
    for n in xrange(1,nt):
        #loop over space
        for j in xrange(1,nx):
            phiNew[j]=phi[j]+A*(phi[j+1]-2*phi[j]+phi[j-1])
        #apply periodic bcs
        phiNew[0]=phi[0]+A*(phi[1]-2*phi[0]+phi[nx-1])
        phiNew[nx]=phiNew[0]

        #update for next timestep
        phiOld=phi.copy()
        phi=phiNew.copy()

    return phi

def diffusion_CTCS(phi, nx, nt, A):
    phiNew=phi.copy() #new timestep (n+1)
    phiOld=phi.copy() #old timestep (n-1)

    #FTCS for first timestep
    for j in xrange(1,nx):
        phi[j]=phiOld[j]+A*(phiOld[j+1]-2*phiOld[j]+phiOld[j-1])

    #apply periodic bc's
    phi[0]=phiOld[0]+A*(phiOld[1]-2*phiOld[0]+phiOld[nx-1])
    phi[nx]=phi[0]

    #loop over remaining timesteps using CTCS
    for n in xrange(1,nt):
        #loop over space
        for j in xrange(1,nx):
            phiNew[j]=phi[j]+2*A*(phi[j+1]-2*phi[j]+phi[j-1])
        #apply periodic bcs
        phiNew[0]=phi[0]+2*A*(phi[1]-2*phi[0]+phi[nx-1])
        phiNew[nx]=phiNew[0]

        #update for next timestep
        phiOld=phi.copy()
        phi=phiNew.copy()

    return phi    
