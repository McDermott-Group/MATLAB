#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:00:25 2021

@author: robertmcdermott

Modified:
2022Jan
Chuanhong Liu

For recombination photon emission

Step:
1. Inject
2. Recombine
3. Diffuse

Ignore the scattering process, only energy at the gap,
"""

from pylab import plot, xlabel, ylabel, show
import matplotlib.pyplot as plt
import random
import time
import numpy as np
from scipy.linalg import expm
from scipy.sparse import diags
import cmath

Delta = 1  # energy gap
L = 40  # length in microns
tau0 = 400  # e-p coupling time, units of ns
Dn = 6e-2  # units of um^2/ns -- want to use 6 here for aluminum

nx = 2  # points in space grid
ne = 1  # points in energy grid
nt = 2# time steps

s = 1e-3  # sets time step; units of tau0 -- try 1e-4
dt = s * tau0
Gamma = 1e-3  # Dynes broadening

# spatial stuff
x = np.linspace(0, L, nx)
dx = x[1] - x[0]

# energy stuff
## IF NEED HIGHER RESOLUTION AT GAP, LOG SPACING FROM DELTA
de = 1.0 / ne  # energy increment in units of Delta = 1
# e = 1 + de * np.linspace(0, ne - 1, ne)
e = np.asarray([1.05])
broadened = complex(0, -Gamma)
Dynes = e + broadened
# rho = e/np.sqrt(e**2-Delta**2)
rho = Dynes / np.sqrt(Dynes ** 2 - Delta ** 2)
rho = rho.real

n = np.zeros((nx, ne))

# generate the diffusion matrix
Dmat = diags([1, -2, 1], [-1, 0, 1], shape=(nx, nx)).toarray()
Dmat[0, 0] = -1
Dmat[nx - 1, nx - 1] = -1

def diffuse(n, D, dx, dt):
    dn = D * dt / (dx ** 2) * np.matmul(Dmat, n)
    n = n + dn
    return n

def recombine(n, inj, dt, dx, i):
    print('n=', n)
    n.shape = (len(n), 1)
    # Gamma_rec = 1/(tau0)   # recombination rate, use the same rate as e-phonon coupling rate
    Gamma_rec = 1/(350)   # recombination rate, use the same rate as e-phonon coupling rate
    # print('n=', n)
    # absolute number of QPs to density conversion
    Vol = dx * 1.6 * 0.1    # Volume per segment    um^3
    n_cp=4e6    # cooper pair density um^(-3)
    # N_cp=n_cp*Vol   # cooper pair number per unit length
    N_cp = 6e4
    x_qp = n/(1.0*N_cp)   # normalized QP density array
    recombined = Gamma_rec*dt*x_qp*x_qp   # elementwise multiply
    # print('recombined=', recombined)
    x_qp = x_qp - recombined
    photon_emitted = np.sum(recombined)*N_cp/2.0
    n = x_qp * N_cp
    n = n + inj
    # density conversion ends
    # if i % 1000 == 0:
    #     print('N_cp=', N_cp)
    #     print('x_qp=', x_qp)
    #     print('recombined=', recombined)
    #     print('photon_emitted=', photon_emitted)



    # recombined = Gamma_rec*dt*n*n   # elementwise multiply
    # n = n - recombined
    # n = n + inj

    n.shape = (1, len(n))
    return n, photon_emitted
    # return n

# injection
E = 1.602*10**(-19) # elementary charge
Rn = 33.0e3   # resistance Ohm
# Vb = 1.45e-3  # bias voltage Volt
Vb = 1.0e-3  # bias voltage Volt
Delta_0 = 190*E*1e-6    # energy gap
G_inj = 0.57*(Vb**2/Rn)*(1/Delta_0)
G_inj_dt = G_inj*dt*1e-9    # injection QP number per time step

delta_inj = np.zeros(ne)
delta_inj.shape = (ne, 1)
delta_inj[0] = G_inj_dt

# used in case there is no injection
noinj = np.zeros(ne)
noinj.shape = (ne, 1)

# evolve in time
sum_temp = 0
for i in range(nt):
    for j in range(nx): # spatial step
        if j == nx // 2:
            inj = delta_inj
        else:
            inj = noinj
        # n[j, :] = recombine(n[j, :], inj, dt, dx)  #_p_e=photon emitted
        # n[j, :], p_e = recombine(n[j, :], inj, dt, dx, i)  #_p_e=photon emitted
        n[j], p_e = recombine(n[j], inj, dt, dx, i)  #_p_e=photon emitted

    D = Dn * np.sqrt(1 - (Delta / e[0]) ** 2)
    n = diffuse(n, D, dx, dt)

    if i % 1000 == 0:
        print('i=', i)
        # print('p_e=', p_e)
        # print('np.sum(n)-sum_temp=', np.sum(n)-sum_temp)
        # sum_temp = np.sum(n)

plt.plot(x, n)
plt.xlabel('Al lead (um)')
plt.ylabel('n_qp')
plt.show()









