import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import random as rd
from mpl_toolkits.mplot3d import Axes3D 

def test7(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max, fluxdensitylimit):
    
    # total tries for E and P
    N = 10000

    # list of variables
    # part 1
    L_P = []
    L_B = []
    L_T = []
    L_L = []

    # part 2
    L_D_lum = []
    L_Flux = []
    L_fluxdensitiy_limit = []

    Percentage_counter = 0.

    for n in range(N):
        
        # random B and P generated
        RN1 = rd.random() * (max_E - min_E) + min_E
        RN2 = rd.random() * (max_spinP - min_spinP) + min_spinP
        RN3 = rd.random() * (D_lum_max - D_lum_min) + D_lum_min

        Random_B = 10**(RN1) *10**-15 # B in 10^15
        Random_P = 10**(RN2) # P in 
        Random_D = 10**(RN3)
    
        # T and L are calculated
        L = (Random_B**2 * Random_P**(-4) * R * 10**(49)) #including multiplying factor
        T = ( 2.05 * (2/5. * M * R**2)*10**-45  * Random_B**(-2) * Random_P**2 * R) * 10**-3 # check factors agian?!?

        Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * Random_D**(-2) * Random_B **2 * R  * Random_P**(-4) * 10**3 # R is already 10 **6 (in mJy)

        # Added to lists
        L_B.append(Random_B)
        L_P.append(Random_P)
        
        L_L.append(L)
        L_T.append(T)

        L_Flux.append(Flux)
        L_D_lum.append(Random_D)

        L_fluxdensitiy_limit.append(fluxdensitylimit)

        if Flux >= fluxdensitylimit:
                Percentage_counter = Percentage_counter +1


    visible_percantage = Percentage_counter / (N) *100

    return L_P, L_B, L_L, L_T, L_Flux, L_D_lum, L_fluxdensitiy_limit, visible_percantage



# LIST OF CONSTANTS
M = 2.1*1.99*10**(30)
R = 10**6 # in cm
min_E = 14 # in log
max_E = 17 # in log
min_spinP = np.log10(0.55) # in log ms
max_spinP = np.log10(8300) # in log ms
V_obs = 150 #Mhz
epsilon_r = 10**-4
D_lum_min = np.log10(40) # in log Mpc
D_lum_max = np.log10(6701.1) # in log Mpc
fluxdensitylimit = 1.3 # lofar superterp 150 Mhz
# R = 1 # *10^6

data = test7(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max, fluxdensitylimit)

L_P, L_B, L_L, L_T, L_Flux, L_D_lum, L_fluxdensitiy_limit, visible_percantage = data

X, Y = np.meshgrid(L_D_lum, L_Flux)

zlist = X**2 + Y**2


from mpl_toolkits.mplot3d import Axes3D 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = L_P
y = L_B
z = L_D_lum


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

enablelog = True

snr=15
fig = plt.figure(figsize=(12,12))
ax = fig.gca(projection='3d')

realsnr = 10**(snr/10)
B,T = np.mgrid[100e3:10e6:100e3, 1:60:1]
C = .55 / (np.sqrt(2) * B * np.sqrt(B * T * realsnr) )
if enablelog: C = np.log10(C)
surf = ax.scatter(
   x, y, z, cmap='rainbow',linewidth=0,antialiased=False)
ax.set_xlabel("Bandwidth MHz")
ax.set_ylabel("Integration Time")
ax.set_zlabel("Cramer-Rao Lower Bound")
if enablelog:zticks = [1e-13,1e-12,1e-11,1e-10,1e-9]
if enablelog:ax.set_zticks(np.log10(zticks))
if enablelog:ax.set_zticklabels(zticks)
plt.show()

