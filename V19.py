# Monte Carlo sampling radio magnetar remnants and varieng the cosmological spectral index
import random as rd
import matplotlib.pyplot as plt
import numpy as np
import inquirer

from astropy.cosmology import Planck13, z_at_value  
from astropy.cosmology import FlatLambdaCDM
import astropy.units as u

cosmo = FlatLambdaCDM(H0=70 * u.km / u.s / u.Mpc, Tcmb0=2.725 * u.K, Om0=0.3) # cosmo constants

# with cosmo astropy yeah

# overruling freqcuency and observation questions to use 1.7 mJy limit at 144 MHz coming from Rowlinson 2020
questions = [
  inquirer.List('overrule',
                message="Overrule other questions and use 144 MHz with 1.7 mJy limit?",
                choices=['Yes', 'No'],
            ),
] 
answers = inquirer.prompt(questions)

#translation of answer in binary code
overrule_d = {'Yes':int(1), 'No':int(0)}
overrule = overrule_d[answers["overrule"]]

# acting on previous question
if overrule < 1:

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
    [ 5.7, 4.7, 3.9, 6.8, 0.3, 0.3, 0.3, 0.48, 0.48, 1.1], #FUll NL
    [ 3.8, 3.1, 2.6, 4.5, 0.2, 0.16, 0.20, 0.16, 0.2, 0.32, 0.32, 0.73]]) # full eu

    #list of observing frequencies in Mhz
    L_V_obs = [30., 45., 60., 75., 120., 150., 180., 200., 210., 240.]

    V_obs = L_V_obs[freq] #input of choise for frequency is put as constant
    fluxdensitylimit = sensitivities[obs][freq] # finding flux density limit

else: 
    V_obs = 144 #MHz
    fluxdensitylimit = 1.7 #mJy



def test7(M, R, min_B, max_B, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max, fluxdensitylimit, alpha):
    
    # total tries for E and P
    N = 1000000

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

    inpatient = 0

    for n in range(N):
        
        # random B and P generated
        RN1 = rd.random() * (max_B - min_B) + min_B
        RN2 = rd.random() * (max_spinP - min_spinP) + min_spinP
        RN3 = rd.random() * (D_lum_max - D_lum_min) + D_lum_min

        Random_B = 10**(RN1) *10**-15 # B in 10^15
        Random_P = 10**(RN2) # P in 
        Random_D = 10**(RN3)

        # calculating redshift
        z = z_at_value(cosmo.luminosity_distance, Random_D*10**3 * u.Mpc) # 1-**3 for getting from Mpc to Gpc


        # T and L are calculated
        L = (Random_B**2 * Random_P**(-4) * R * 10**(49)) #including multiplying factor
        T = ( 2.05 * (2/5. * M * R**2)*10**-45  * Random_B**(-2) * Random_P**2 * R) * 10**-3 # check factors agian?!?

        # with cosmo effect
        Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * Random_D**(-2) * Random_B **2 * Random_P**(-4) *  (1./(1+z))**(-alpha) * 10**3  # R is already 10 **6 (in mJy)
       
        # print '%f flux' % (Flux - Flux2)
      
        # Added to lists
        L_B.append(Random_B)
        L_P.append(Random_P)
        
        L_L.append(L)
        L_T.append(T)

        L_Flux.append(Flux)
        L_D_lum.append(Random_D *10**3) # to get in Mpc

        L_fdl.append(fluxdensitylimit)

        if Flux >= fluxdensitylimit:
                Percentage_counter = Percentage_counter +1


        # inpatient = inpatient + 1
        # # if inpatient == 500:
        # #     print ' %3f %%' % ((n / float(N)) * 100)
        # #     inpatient = 0


    visible_percantage = Percentage_counter / (N) *100
    print visible_percantage

    return L_P, L_B, L_L, L_T, L_Flux, L_D_lum, L_fdl, visible_percantage



# LIST OF CONSTANTS
M = 2.1*1.99*10**(30)
R = 10**6 # in cm
min_B = 14 # in log G
max_B = 17 # in log g
min_spinP = np.log10(0.55) # in log ms
max_spinP = np.log10(8300) # in log ms
epsilon_r = 10**-4
D_lum_min = np.log10(0.04000) # in log Gpc
D_lum_max = np.log10(6.7011) # in log Gpc

L_alpha = [-1, -1.5, -2., -3.] # list of different possible spectral indeces alpha

L_observatories = ['Superterp', 'NL Core', 'Full NL', 'Full EU']


def plotting(L_alpha):
    Colums = len(L_alpha)

    fig, axs = plt.subplots(1, Colums, sharey=True, sharex=True)
    fig.suptitle('Possible Flux densities at different luminoscity distances with varying alpha. At a flux density limit of %.2f mJy at %.1f Mhz.' % (fluxdensitylimit, V_obs), fontsize = 17)
    for i in range(Colums):
        
        data = test7(M, R, min_B, max_B, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max, fluxdensitylimit, L_alpha[i])
        L_P, L_B, L_L, L_T, L_Flux, L_D_lum, L_fdl, visible_percantage = data

        x = L_D_lum
        y = L_Flux
        # Create four polar axes and access them through the returned array
        axs[i].plot(x, y, 'bo', markersize = 0.01)
        axs[i].plot(x, L_fdl, 'r') # creating the flux limitline
        plt.yscale('log')
        plt.xscale('log')
       
        axs[i].set_title('alpha = %.2f, %.1f%% detectable' % (L_alpha[i], visible_percantage))
    
    # Adding labels to the axes
    fig.add_subplot(111, frameon=False)
    # hide tick and tick label of the big axis
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    plt.xlabel('Luminosity distance (Mpc)', fontsize = 17)
    plt.ylabel("Flux density F in (mJy)", fontsize = 17)
    plt.show()


plotting(L_alpha)

