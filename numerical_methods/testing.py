import numpy as np
import matplotlib.pyplot as plt
import myfunctions as fn

nt = 1000
dt = 0.5
t=np.linspace(0.0, 1.0, nt+1)
f=0.1

A=f*dt

u=fn.initialBell(t)
v=fn.initialBell(t)

#FTCS
uNew=u.copy()
vNew=v.copy()

for i in xrange (1,nt):
    uNew[i]=u[i] + A*v[i]
    vNew[i]=v[i] - A*u[i]

    u=uNew.copy()
    v=vNew.copy()


plt.plot(t, fn.initialBell(t), 'k', label='bell curve')
plt.plot(t, u, 'B', label='u')
plt.plot(t, v, 'C', label='v')
plt.legend(loc='best')
plt.xlabel('t')

plt.show()
