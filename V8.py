import matplotlib.pyplot as plt
import numpy as np 
import random as rd 

def test8(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max, fluxdensitylimit):
    
    # total tries for E and P
    N = 100

    # list of variables
    # part 1

    L_P = []
    L_B = []
    L_T = []
    L_L = []

    # part 2

    #list of testable distances
    L_D_lum = [50.,1000.,2000., 3000. ,4000. , 6050. ]
    FLux_matrix = []
    P_matrix = []
    B_matrix = []
    T_matrix = []
    L_matrix = []

    # part 1
    #steps in distances
    for i in range(len(L_D_lum)):

        L_Flux = []

        L_P = []
        L_B = []
        L_T = []
        L_L = []

        # lists to create fluxdensity limit line in plots
        L_fdl = []
       
        distance = L_D_lum[i]

        # random B and P generated
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
            
            # Flux calculated
            Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * distance**(-2) * L_B[n] **2 * R  * L_P[n]**(-4) * 10**3 # R is already 10 **6 (in mJy)
            
            L_Flux.append(Flux)

            L_fdl.append(fluxdensitylimit)

        FLux_matrix.append(L_Flux)
        P_matrix.append(L_P)
        B_matrix.append(L_B)
        T_matrix.append(L_T)
        L_matrix.append(L_L)



   
    return L_D_lum, B_matrix, P_matrix, FLux_matrix, L_fdl



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
fluxdensitylimit = 153
# R = 1 # *10^6

data = test8(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, np.log(D_lum_min), np.log(D_lum_max), fluxdensitylimit)

L_D_lum, B_matrix, P_matrix, FLux_matrix, L_fdl = data

import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt


delta = 0.025
# x = np.arange(-3.0, 3.0, delta)
# y = np.arange(-2.0, 2.0, delta)

x = B_matrix[0]
y = P_matrix[0]
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
print Z 

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('Simplest default with labels')
plt.yscale('log')
plt.xscale('log')
plt.show()