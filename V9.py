import random as rd
import matplotlib.pyplot as plt

import numpy as np


def test7(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max, fluxdensitylimit):
    
    # total tries for E and P
    N = 10000

    # list of variables
    # part 1
    L_all_variables = [['nummer','random B', 'random P', 'Plateau time', 'luminosity']]
    L_P = []
    L_B = []
    L_T = []
    L_L = []

    # part 2
    L_D_lum = []
    L_Flux = []

    Percentage_counter = 0.
    
    # part 1
    for n in range(N):
        
        # random B and P generated
        RN1 = rd.random() * (max_E - min_E) + min_E
        RN2 = rd.random() * (max_spinP - min_spinP) + min_spinP

        Random_B = 10**(RN1) *10**-15 # B in 10^15
        Random_P = 10**(RN2) # P in ms
        
        
        # T and L are calculated
        L = (Random_B**2 * Random_P**(-4) * R * 10**(49)) #including multiplying factor
    
        T = ( 2.05 * (2/5. * M * R**2)*10**-45  * Random_B**(-2) * Random_P**2 * R) * 10**-3 # check factors agian?!?

        # Added to lists
        L_B.append(Random_B)
        L_P.append(Random_P)
        
        L_L.append(L)
        L_T.append(T)

        L_fluxdensitiy_limit = []

        L_all_variables.append([n + 1, Random_B, Random_P, T, L])

    
    N2 = 10 # total tests with distance
    for i in range(N):
       
        L_Flux_line = [] # lists to create lines on plots
        L_D_lum_line = []

        for x in range(N2):

            # random distance created
            RN3 = rd.random() * (D_lum_max - D_lum_min) + D_lum_min
            Random_D = 10**(RN3)

            # Flux calculated
            Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * Random_D**(-2) * L_B[i] **2 * R  * L_P[i]**(-4) * 10**3 # R is already 10 **6 (in mJy)
           
            L_Flux.append(Flux)
            L_D_lum.append(Random_D)
            
            L_Flux_line.append(Flux)
            L_D_lum_line.append(Random_D)

            L_fluxdensitiy_limit.append(fluxdensitylimit)

            if Flux >= fluxdensitylimit:
                Percentage_counter = Percentage_counter +1

    visible_percantage = Percentage_counter / (N*N2) *100
            
        

    

    return L_P, L_B, L_L, L_T, L_Flux, L_D_lum, L_D_lum_line, L_Flux_line, L_fluxdensitiy_limit, visible_percantage



# LIST OF CONSTANTS
# LIST OF CONSTANTS
M = 2.1*1.99*10**(30)
R = 10**6 # in cm
min_E = 14 # in log
max_E = 17 # in log
min_spinP = np.log10(0.55) # in log ms
max_spinP = np.log10(8300) # in log ms
V_obs = 144 #Mhz
epsilon_r = 10**-4
D_lum_min = 40
D_lum_max = 6701.1
fluxdensitylimit = 1.3 #mJy
# R = 1 # *10^6

data = test7(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, np.log10(D_lum_min), np.log10(D_lum_max), fluxdensitylimit)


L_P, L_B, L_L, L_T, L_Flux, L_D_lum, L_D_lum_line, L_Flux_line, L_fluxdensitiy_limit, visible_percantage = data

print visible_percantage

plt.plot(L_D_lum, L_Flux, 'bo', markersize = 2)
plt.plot(L_D_lum, L_fluxdensitiy_limit, 'r')
plt.yscale('log')
plt.xscale('log')
plt.ylabel('FLux density (mJy)')
plt.xlabel('Luminosity distance (Mpc)')
plt.suptitle('Possible Flux densities at different luminoscity distances')
plt.show()
