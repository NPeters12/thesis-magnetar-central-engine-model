import random as rd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as plt
import random
import matplotlib.gridspec as gridspec
import seaborn as sns
import pandas as pd
sns.set()


def test8(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max):
    
    # total tries for E and P
    N = 100

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

        FLux_matrix.append(L_Flux)
        P_matrix.append(L_P)
        B_matrix.append(L_B)
        T_matrix.append(L_T)
        L_matrix.append(L_L)

    


        
   
    return L_D_lum, B_matrix, P_matrix, FLux_matrix



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

data = test8(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, np.log(D_lum_min), np.log(D_lum_max))

def make_plot(axs, data):

    L_D_lum, B_matrix, P_matrix, FLux_matrix = data
    
    
    box = dict(facecolor='yellow', pad=5, alpha=0.2)

    # Fixing random state for reproducibility
    ax1 = axs[0, 0]
    ax1.scatter(B_matrix[0],FLux_matrix[0], s = 2)
    ax1.set_title('ylabels not aligned')
    ax1.set_ylabel('misaligned 1', bbox=box)
    ax1.set_ylim(0, 2000)
 

    ax3 = axs[1, 0]
    ax3.set_ylabel('misaligned 2', bbox=box)
    ax3.scatter(B_matrix[1],FLux_matrix[1], s = 2)


    ax2 = axs[0, 1]
    ax2.set_title('ylabels aligned')
    ax2.scatter(B_matrix[2],FLux_matrix[2], s = 2)
    ax2.set_ylabel('aligned 1', bbox=box)
    ax2.set_ylim(0, 2000)


    ax4 = axs[1, 1]
    ax4.scatter(B_matrix[3],FLux_matrix[3], s = 2)
    ax4.set_ylabel('aligned 2', bbox=box)


    ax5 = axs[2, 0]
    ax5.scatter(B_matrix[4],FLux_matrix[4], s = 2)
    ax5.set_ylabel('aligned 3', bbox=box)


    ax6 = axs[2, 1]
    ax6.scatter(B_matrix[5],FLux_matrix[5], s = 2)
    ax6.set_ylabel('aligned 4', bbox=box)


# Plot 1:
fig, axs = plt.subplots(3, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)

make_plot(axs, data)

labelx = -0.3  # axes coords

for j in range(2):
    axs[j, 1].yaxis.set_label_coords(labelx, 0.5)
    plt.yscale('log')
    plt.xscale('log')

plt.show()