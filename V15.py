# plotting B-P relation with colormap of flux with redshift encounted (closest)


import random as rd
import matplotlib.pyplot as plt
import numpy as np
import inquirer
import matplotlib.colors as colors



# asking about which observatory and which frequency we want to use
questions = [
  inquirer.List('observatory',
                message="Which observatory do you want to use?",
                choices=['Superterp', 'NL Core', 'Full NL', 'Full EU'],
            ),
]
answers = inquirer.prompt(questions)
print answers["observatory"]

# translation of observatories
obs_d = {'Superterp':int(0), 'NL Core':int(1), 'Full NL':int(2), 'Full EU':int(3)}
obs = obs_d[answers["observatory"]]



questions = [
  inquirer.List('frequency',
                message="And at what frequency?",
                choices=['30 Mhz', '45 Mhz', '60 Mhz', '75 Mhz', '120 Mhz', '150 Mhz', '180 Mhz', '200 Mhz', '210 Mhz', '240 Mhz'],
            ),
]
answers = inquirer.prompt(questions)
print answers["frequency"]

# translation of frequencies
freq_d = {'30 Mhz': int(0), '45 Mhz':int(1), '60 Mhz':int(2), '75 Mhz':int(3), '120 Mhz':int(4), '150 Mhz':int(5), '180 Mhz':int(6), '200 Mhz':int(7), '210 Mhz':int(8), '240 Mhz':int(9)}
freq = freq_d[answers["frequency"]]


# array of all sensitivities per observatory
sensitivities = np.array([[ 36.0, 29.0, 25.0, 44.0, 1.5, 1.3, 1.5, 2.5, 2.5, 5.6], #superterp
[ 9.0, 7.4, 6.2, 10.8, 0.38, 0.31, 0.38, 0.62, 0.62, 1.4], #NL core
[ 5.7, 4.7, 3.9, 6.8, 0.3, 0.24, 0.3, 0.48, 0.48, 1.1], #FUll NL
[ 3.8, 3.1, 2.6, 4.5, 0.2, 0.16, 0.20, 0.16, 0.2, 0.32, 0.32, 0.73]]) # full eu

#list of observing frequencies in Mhz
L_V_obs = [30., 45., 60., 75., 120., 150., 180., 200., 210., 240.]



def test7(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max, fluxdensitylimit, alpha):

    dlum_mid = (D_lum_max + D_lum_min) / 2
    
    # total tries for E and P
    N = 500

    # list of variables
    # part 1
    L_P = []
    L_B = []
    L_T = []
    L_L = []

    # part 2
    L_D_lum = []
    L_Flux = []
    L_fdl = []

    Percentage_counter = 0.

    for n in range(N):
 
        # random B and P generated
        RN1 = rd.random() *((np.log10(max_E) - np.log10(min_E)) + np.log10(min_E))
        RN2 = rd.random() * (np.log10((max_spinP) - np.log10(min_spinP)) + np.log10(min_spinP))
        RN3 = rd.random() * (D_lum_max - D_lum_min) + D_lum_min

        Random_B = 10**(RN1) *10**-15 # B in 10^15
        Random_P = 10**(RN2) # P in ms
        Random_D = 10**(RN3)
    
        # T and L are calculated
        L = (Random_B**2 * Random_P**(-4) * R * 10**(49)) #including multiplying factor
        T = ( 2.05 * (2/5. * M * R**2)*10**-45  * Random_B**(-2) * Random_P**2 * R) * 10**-3 # check factors agian?!?

        Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * (10**(D_lum_min))**(-2) * Random_B**2 * R  * Random_P**(-4) * 10**3 * (np.sqrt(D_lum_min/39.231))**(-alpha) # R is already 10 **6 (in mJy), last is cosmo redshift
        
        # Added to lists
        L_B.append(Random_B)
        L_P.append(Random_P)
        
        L_L.append(L)
        L_T.append(T)

        L_Flux.append(Flux)
        L_D_lum.append(Random_D)

        L_fdl.append(fluxdensitylimit)

        if Flux >= fluxdensitylimit:
                Percentage_counter = Percentage_counter +1

    # calculating visible percantage
    visible_percantage = Percentage_counter / (N) *100

    #making meshgrid sheis
    bmesh, pmesh = np.meshgrid(L_B, L_P)
    fmesh = (8*10**(7) * V_obs**(-1) * epsilon_r * (10**(D_lum_min))**(-2) * bmesh **2 * R  * pmesh**(-4) * 10**3) * (np.sqrt(D_lum_min/39.231))**(-alpha)

    return L_P, L_B, L_L, L_T, L_Flux, L_D_lum, L_fdl, visible_percantage, bmesh, pmesh, fmesh

# LIST OF CONSTANTS
M = 2.1*1.99*10**(30)
R = 10**6 # in cm
min_E = 14 # in log
max_E = 17 # in log
min_spinP = 0.55 # in log ms
max_spinP = 8300 # in log ms
V_obs = L_V_obs[freq] #input of choise for frequency is put as constant            #150 #Mhz
epsilon_r = 10**-4
D_lum_min = np.log10(40) # in log Mpc
D_lum_max = np.log10(6701.1) # in log Mpc
fluxdensitylimit = sensitivities[obs][freq]   #input as choise for sensitivity is put as constant   #1.3 # lofar superterp 150 Mhz
alpha = -1.
# R = 1 # *10^

def line(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max, fluxdensitylimit, alpha):

    # min_spinP = 10**min_spinP
    # max_spinP = 10**max_spinP

    B_line_min = np.sqrt(fluxdensitylimit/ (8*10**(7) * V_obs**(-1) * epsilon_r * (10**(D_lum_min))**(-2) * R  * min_spinP**(-4) * 10**3 * (np.sqrt(D_lum_min/39.231))**(-alpha))) # R is already 10 **6 (in mJy), last is cosmo redshift
    B_line_max = np.sqrt(fluxdensitylimit/ (8*10**(7) * V_obs**(-1) * epsilon_r * (10**(D_lum_min))**(-2) * R  * max_spinP**(-4) * 10**3 * (np.sqrt(D_lum_min/39.231))**(-alpha))) # R is already 10 **6 (in mJy), last is cosmo redshift
    L_B_Line = [B_line_min, B_line_max]
    L_P_Line = [min_spinP, max_spinP]

    
    return L_P_Line, L_B_Line

L_efficiencies = np.linspace(10**-6, 10**-2, 4) # list of different possible efficiencies (epsilon R)

data = test7(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max, fluxdensitylimit, alpha)

L_P, L_B, L_L, L_T, L_Flux, L_D_lum, L_fdl, visible_percantage, bmesh, pmesh, fmesh = data

L_P_Line, L_B_Line = line(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max, fluxdensitylimit, alpha)

L_observatories = ['Superterp', 'NL Core', 'Full NL', 'Full EU']


cm = plt.cm.get_cmap('viridis')

plt.scatter(pmesh, bmesh, c=fmesh, cmap=cm, norm = colors.LogNorm(vmin=min(L_Flux), vmax=max(L_Flux)))

plt.ylabel('Field strength B (10^15 G)')
plt.xlabel('Spin period P (ms)')

plt.suptitle('Flux density at different field strengths and spin periods of the %s array %.2f mJy at %.1f Mhz.' % (L_observatories[obs], fluxdensitylimit, V_obs))
plt.yscale('log')
plt.xscale('log')
# v = np.linspace(min(L_Flux), max(L_Flux), num=10)
cbar = plt.colorbar()
cbar.set_label('Flux density (mjy)', rotation=270)
# cbar.set_ticks(v)
# cbar.set_ticklabels(v)
plt.show()

