import random as rd
import matplotlib.pyplot as plt
import numpy as np


R = 10.**4 # in m
min_B = 10.**14 # G
max_B = 10.**17 # G
min_spinP = 0.00055 # in s
max_spinP = 8.300 # in s
V_obs = 144 #Mhz
epsilon_r = 10**-4
D_lum_min = 0.04# in Gpc
D_lum_max = 6.7011 * 10**-3 # in Gpc
fluxdensitylimit = 1.7 # lofar superterp 150 Mhz

# R = 1 # *10^6

D = D_lum_min
B = max_B
P = min_spinP
R = R

B = B / 10**(15)
P = P / 10**(-3)
R = R / 10**(6)
print B 
print P 
print R 

Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * D**(-2) * B **2 * R**6 * P**(-4)# R is already 10 **6 (in mJy)
print 'hoi'
print Flux

R = 10.**6 # in cm
min_B = 10.**14 # G
max_B = 10.**17 # G
min_spinP = 0.00055 # in s
max_spinP = 8.300 # in s
V_obs = 144 * 10**6 #hz
epsilon_r = 10**-4
D_lum_min = 40 * 3.08568*10**24 # in cm 
D_lum_max = 6701.1 * 3.08568*10**24 # in cm 
fluxdensitylimit = 1.7 # lofar superterp 150 Mhz
c = 3 *10**10 # in cm/s

D = D_lum_min
B = max_B
P = min_spinP
R = R
print B 
print P 
print R 


Flux2 = 16*np.pi**(4) * B**2 * R**6 / (3 * V_obs * P**(4) * c**(3) * D**(2))
print 'hoi'
print Flux2



