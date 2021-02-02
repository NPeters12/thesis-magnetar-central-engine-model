import random as rd
import matplotlib.pyplot as plt
import numpy as np
import inquirer

import astropy.units as u
from astropy.cosmology import Planck13, z_at_value
  
from astropy.cosmology import FlatLambdaCDM
import astropy.units as u


# LIST OF CONSTANTS
M = 2.1*1.99*10**(30)
R = 10**6 # in cm
min_E = 14 # in log
max_E = 17 # in log
min_spinP = np.log10(0.55) # in log ms
max_spinP = np.log10(8300) # in log ms
V_obs = 144 #L_V_obs[freq] #input of choise for frequency is put as constant            #150 #Mhz
epsilon_r = 10**-4
D_lum_min = np.log10(40000) # in log Mpc
D_lum_max = np.log10(6701100) # in log Mpc
fluxdensitylimit = 1.7 #sensitivities[obs][freq]   #input as choise for sensitivity is put as constant   #1.3 # lofar superterp 150 Mhz
alpha = -3
# R = 1 # *10^6f

L_flux = []
L_flux2 = []
L_D = []


for i in range(1000):

    # random B and P generated
    RN1 = max_E
    RN2 = min_spinP
    RN3 = rd.random() * (D_lum_max - D_lum_min) + D_lum_min

    Random_B = 10**(RN1) *10**-15 # B in 10^15
    Random_P = 10**(RN2) # P in 
    Random_D = 10**(RN3)

    cosmo = FlatLambdaCDM(H0=70 * u.km / u.s / u.Mpc, Tcmb0=2.725 * u.K, Om0=0.3) # cosmo constants

    z = z_at_value(cosmo.luminosity_distance, (Random_D/1000) * u.Mpc)
    # print z 

    Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * Random_D**(-2) * Random_B **2 * R  * Random_P**(-4) * 10**3 * (1./(1+z))**(-alpha) # R is already 10 **6 (in mJy)
    Flux2 = 8*10**(7) * V_obs**(-1) * epsilon_r * Random_D**(-2) * Random_B **2 * R  * Random_P**(-4) * 10**3 

    L_flux.append(Flux)
    L_flux2.append(Flux2)
    L_D.append(Random_D)

    

plt.plot(L_D,L_flux, 'ro', markersize = 1)
plt.plot(L_D,L_flux2,  'go', markersize = 1)
plt.yscale('log')
plt.xscale('log')

plt.show()

print "\u03B1"

print('Omega: \u03A9')