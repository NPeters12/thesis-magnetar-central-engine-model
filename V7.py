import matplotlib.pyplot as plt
import numpy as np 
import random as rd 

def test8(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max, fluxdensitylimit):
    
    # total tries for E and P
    N = 1000000
    # part 2

    #list of testable distances
    L_D_lum = [50., 2000., 4000., 6050. ]
    FLux_matrix = []
    P_matrix = []
    B_matrix = []
    T_matrix = []
    L_matrix = []

    L_percentage = []

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

        # counter to calculate percentage of

        Percentage_counter = 0

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
            Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * distance**(-2) * Random_B **2 * R  * Random_P**(-4) * 10**3 # R is already 10 **6 (in mJy)
            
            L_Flux.append(Flux)

            L_fdl.append(fluxdensitylimit)

            if Flux > fluxdensitylimit:
                Percentage_counter = Percentage_counter + 1

        #calculating percange and adding them to list
        if Percentage_counter == 0:
            L_percentage.append(0)
        else:
            L_percentage.append((float(Percentage_counter)/ N) * 100)

        FLux_matrix.append(L_Flux)
        P_matrix.append(L_P)
        B_matrix.append(L_B)
        T_matrix.append(L_T)
        L_matrix.append(L_L)

    return L_D_lum, B_matrix, P_matrix, FLux_matrix, L_fdl, L_percentage


# LIST OF CONSTANTS
M = 2.1*1.99*10**(30)
R = 10**6 # in cm
min_E = 14 # in log
max_E = 17 # in log
min_spinP = np.log10(0.55) # in log ms
max_spinP = np.log10(8300) # in log mszzz
V_obs = 144 #Mhz
epsilon_r = 10**-4
D_lum_min = 40
D_lum_max = 6701.1
fluxdensitylimit = 0.3
# R = 1 # *10^6

test8(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, np.log(D_lum_min), np.log(D_lum_max), fluxdensitylimit)

data = test8(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, np.log(D_lum_min), np.log(D_lum_max), fluxdensitylimit)

L_D_lum, B_matrix, P_matrix, FLux_matrix, L_fdl, L_percentage = data

Colums = len(L_D_lum)




# Plotting B-F relation at different distances
fig, axs = plt.subplots(1, Colums, sharey=True, sharex=True)
fig.suptitle('Flux density F (mJy) versus the field strength B (10^15 G) at different Luminosity distances. The red line indicates the current Lofar detection limit.')
for i in range(Colums):
    x = B_matrix[i]
    y = FLux_matrix[i]
    # Create four polar axes and access them through the returned array
    axs[i].plot(x, y, 'bo', markersize = 2)
    axs[i].plot(x, L_fdl, 'r') # creating the flux limitline
    plt.yscale('log')
    plt.xscale('log')
    axs[i].set_title('At %d Mpc. %d %% visible' % (L_D_lum[i], L_percentage[i]))

# Adding labels to the axes
fig.add_subplot(111, frameon=False)
# hide tick and tick label of the big axis
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
plt.xlabel("field strength B (10^15 G)")
plt.ylabel("Flux density F in (mJy)")
plt.show() 

# Plotting P-F relation at different distances
fig, axs = plt.subplots(1, Colums, sharey=True, sharex=True)
fig.suptitle('Flux density F (mJy) versus the Spin P (ms) at different Luminosity distances. The red line indicates the current Lofar detection limit.')
for i in range(Colums):
    x = P_matrix[i]
    y = FLux_matrix[i]
    # Create four polar axes and access them through the returned array
    axs[i].plot(x, y, 'bo', markersize = 0.01)
    axs[i].plot(x, L_fdl, 'r') # creating the flux limitline
    plt.yscale('log')
    plt.xscale('log')
    axs[i].set_title('At %d Mpc. %d %% visible' % (L_D_lum[i], L_percentage[i]))

# Adding labels to the axes
fig.add_subplot(111, frameon=False)
# hide tick and tick label of the big axis
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
plt.xlabel("Spin P (ms)")
plt.ylabel("Flux density F in (mJy)")
plt.show()

