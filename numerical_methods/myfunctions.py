import numpy as np

# Function to definte the initial conditions, ie a Bell curve
def initialBell(x):
    return np.where(x%1. < 0.5, np.power(np.sin(2*x*np.pi), 2), 0)

def coefficient(nx, K, dt):
    dx=1./nx
    D=(K*dt)/(dx**2)
    return D
