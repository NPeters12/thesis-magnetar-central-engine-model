import random as rd
import matplotlib.pyplot as plt 
import math 
import numpy as np 
plt.style.use('classic')
import pandas as pd
import seaborn as sns
sns.set()


def test8(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max):
    
    # total tries for E and P
    N = 1000

    # list of variables
    # part 1
    L_all_variables = [['nummer','random B', 'random P', 'Plateau time', 'luminosity']]

    L_P = []
    L_B = []
    L_T = []
    L_L = []

    # part 2

    #list of testable distances
    L_D_lum = [50.,1000.,2000., 3000. ,4000. , 6050. ]
    L_Flux = []
    
    # part 1
    

    #steps in distances
    for i in range(len(L_D_lum)):
       
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

            L_fluxdensitiy_limit = []

            L_all_variables.append([n + 1, Random_B, Random_P, T, L])
            
            # Flux calculated
            Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * distance**(-2) * L_B[n] **2 * R  * L_P[n]**(-4) * 10**3 # R is already 10 **6 (in mJy)
            
            L_Flux.append(Flux)

            L_fluxdensitiy_limit. append(0.153)

        L_D_lum.append(distance)

    return L_P, L_B, L_L, L_T, L_Flux, L_D_lum



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
# R = 1 # *10^6

test8(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, np.log(D_lum_min), np.log(D_lum_max))


def seaborntest(data):

    L_P, L_B, L_L, L_T, L_Flux, L_D_lum = data

    # rng = np.random.RandomState(0)
    
    plt.figure(1)
    plt.plot(L_P,L_B,'ro' )
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('Field strength B (10^15 G)')
    plt.xlabel('Spin period P (ms)')
    # plt.legend('', ncol=2, loc='upper left');
    plt.show()

    plt.figure(2)
    plt.plot(L_D_lum,L_Flux, 'bo', markersize = 2)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('FLux density (mJy)')
    plt.xlabel('Luminosity distance (Mpc)')
    # plt.legend('', ncol=2, loc='upper left');
    plt.show()

    plt.figure(3)
    plt.plot(L_P, L_Flux, 'go', markersize = 2)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('FLux density (mJy)')
    plt.xlabel('Spin period P (ms)')
    # plt.legend('', ncol=2, loc='upper left');
    plt.show()

    plt.figure(4)
    plt.plot(L_B, L_Flux, 'go', markersize = 2)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('FLux density (mJy)')
    plt.xlabel('Field strength B (10^15 G)')
    # plt.legend('', ncol=2, loc='upper left');
    plt.show()

    plt.figure(5)
    plt.plot(L_T, L_L, 'go', markersize = 2)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('LogLx(Ta)')
    plt.xlabel('Log(T*a)')
    plt.show()

    plt.figure(6)
    plt.plot(L_T, L_Flux, 'go', markersize = 2)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('FLux density (mJy)')
    plt.xlabel('Log(T*a)')
    plt.show()
   
    plt.figure(7)
    plt.plot(L_L, L_Flux, 'go', markersize = 2)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('FLux density (mJy)')
    plt.xlabel('LogLx(Ta)')
    plt.show()

data = test8(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, np.log(D_lum_min), np.log(D_lum_max))


seaborntest(data)