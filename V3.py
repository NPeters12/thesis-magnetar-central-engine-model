# import random as rd
# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.pylab as plt
# import random
# import matplotlib.gridspec as gridspec
# import seaborn as sns
# import pandas as pd
# sns.set()


# def test7(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max):
    
#     # total tries for E and P
#     N = 100

#     # list of variables
#     # part 1
#     L_all_variables = [['nummer','random B', 'random P', 'Plateau time', 'luminosity']]
#     L_P = []
#     L_B = []
#     L_T = []
#     L_L = []

#     # part 2
#     L_D_lum = []
#     L_Flux = []
    
#     # part 1
#     for n in range(N):
        
#         # random B and P generated
#         RN1 = rd.random() * (max_E - min_E) + min_E
#         RN2 = rd.random() * (max_spinP - min_spinP) + min_spinP

#         Random_B = 10**(RN1) *10**-15 # B in 10^15
#         Random_P = 10**(RN2) # P in ms
        
        
#         # T and L are calculated
#         L = (Random_B**2 * Random_P**(-4) * R * 10**(49)) #including multiplying factor
    
#         T = ( 2.05 * (2/5. * M * R**2)*10**-45  * Random_B**(-2) * Random_P**2 * R) * 10**-3 # check factors agian?!?

#         # Added to lists
#         L_B.append(Random_B)
#         L_P.append(Random_P)
        
#         L_L.append(L)
#         L_T.append(T)

#         L_fluxdensitiy_limit = []

#         L_all_variables.append([n + 1, Random_B, Random_P, T, L])

    
#     N2 = 1 # total tests with distance
#     for i in range(N):
       
#         L_Flux_line = [] # lists to create lines on plots
#         L_D_lum_line = []

#         for x in range(N2):

#             # random distance created
#             RN3 = rd.random() * (D_lum_max - D_lum_min) + D_lum_min
#             Random_D = 10**(RN3)

#             # Flux calculated
#             Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * Random_D**(-2) * L_B[i] **2 * R  * L_P[i]**(-4) * 10**3 # R is already 10 **6 (in mJy)
           
#             L_Flux.append(Flux)
#             L_D_lum.append(Random_D)
            
#             L_Flux_line.append(Flux)
#             L_D_lum_line.append(Random_D)

#             L_fluxdensitiy_limit. append(0.153)

#     return L_P, L_B, L_L, L_T, L_Flux, L_D_lum



# # LIST OF CONSTANTS
# M = 2.1*1.99*10**(30)
# R = 10**6 # in cm
# min_E = 14 # in log
# max_E = 17 # in log
# min_spinP = np.log10(0.55) # in log ms
# max_spinP = np.log10(8300) # in log ms
# V_obs = 144 #Mhz
# epsilon_r = 10**-4
# D_lum_min = 40
# D_lum_max = 6701.1
# # R = 1 # *10^6

# # test7(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, np.log(D_lum_min), np.log(D_lum_max))


# # random.seed(20)
# # data1 = [random.random() for i in range(10)]
# # data2 = [random.random()*1000 for i in range(10)]

# # print data1

# # gs = gridspec.GridSpec(2,2)
# # fig = plt.figure()

# # ax = fig.add_subplot(gs[0])
# # ax.plot(data1)
# # ax.set_ylabel(r'Label One', size =16)

# # ax = fig.add_subplot(gs[1])
# # ax.plot(data2)
# # ax.set_ylabel(r'Label Two', size =16)

# # plt.show()


# L_x1 = [1., 2.,3.,4.,6.,34.,5.,4.,4]
# L_y1 = [1., 2.,3.,4.,6.,34.,5.,4.,4]

# L_x2 = [1., 2.,3.,4.,6.,34.,5.,4.,4]
# L_y2 = [1., 2.,3.,4.,6.,34.,5.,4.,4]

# L_x3 = [1., 2.,3.,4.,6.,34.,5.,4.,4]
# L_y3 = [1., 2.,3.,4.,6.,34.,5.,4.,4]

# L_x4 = [1., 2.,3.,4.,6.,34.,5.,4.,400]
# L_y4 = [1., 2.,3.,-54.,6.,34.,5000.,4.,4]

# gs = gridspec.GridSpec(2,2)

# fig = plt.figure()

# ax = fig.add_subplot(gs[0])
# ax.plot(L_x1, L_y1)
# ax.set_ylabel(r'Label One', size =16)

# ax = fig.add_subplot(gs[1])
# ax.plot(L_x2, L_y2)
# ax.set_ylabel(r'Label Two', size =16)

# ax = fig.add_subplot(gs[2])
# ax.plot(L_x3, L_y3)
# ax.set_ylabel(r'Label three', size =16)

# ax = fig.add_subplot(gs[3])
# ax.plot(L_x4, L_y4)
# ax.set_ylabel(r'Label four', size =16)


# for j in range(2):
#     axs[j, 1].yaxis.set_label_coords(labelx, 0.5)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt


def make_plot(axs):
    box = dict(facecolor='yellow', pad=5, alpha=0.2)

    # Fixing random state for reproducibility
    np.random.seed(19680801)
    ax1 = axs[0, 0]
    ax1.plot(2000*np.random.rand(10))
    ax1.set_title('ylabels not aligned')
    ax1.set_ylabel('misaligned 1', bbox=box)
    ax1.set_ylim(0, 2000)

    ax3 = axs[1, 0]
    ax3.set_ylabel('misaligned 2', bbox=box)
    ax3.plot(np.random.rand(10))

    ax2 = axs[0, 1]
    ax2.set_title('ylabels aligned')
    ax2.plot(2000*np.random.rand(10))
    ax2.set_ylabel('aligned 1', bbox=box)
    ax2.set_ylim(0, 2000)

    ax4 = axs[1, 1]
    ax4.plot(np.random.rand(10))
    ax4.set_ylabel('aligned 2', bbox=box)


# Plot 1:
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)

make_plot(axs)

labelx = -0.3  # axes coords

for j in range(2):
    axs[j, 1].yaxis.set_label_coords(labelx, 0.5)

plt.show()