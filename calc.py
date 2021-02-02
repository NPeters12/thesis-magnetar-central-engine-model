
import random as rd
import matplotlib.pyplot as plt
import numpy as np



# LIST OF CONSTANTS
M = 2.1*1.99*10**(30)
R = 10**6 # in cm
min_E = 10**14 # in log
max_E = 10**17 # in log
min_spinP = (0.55) # in log ms
max_spinP = (8300.) # in log ms
V_obs = 144 #L_V_obs[freq] #input of choise for frequency is put as constant            #150 #Mhz
epsilon_r = 10**-4
D_lum_min = (0.04) # in log Mpc
D_lum_max = (6.7011) # in log Mpc
fluxdensitylimit = 1.7 #sensitivities[obs][freq]   #input as choise for sensitivity is put as constant   #1.3 # lofar superterp 150 Mhz
# R = 1 # *10^6




# Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * D_lum_max**(-2) * max_E **2 * Random_P**(-4) * 10**3 # R is already 10 **6 (in mJy)

P = ((8*10**(7) * V_obs**(-1) * epsilon_r * D_lum_max**(-2) * max_E **2 * 10**3) / fluxdensitylimit)**(1/4.)
print P 
