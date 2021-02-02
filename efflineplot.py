# Plotting D-F and calculating visible percentage at 150Hz and fdl of 1.3 mjy. of lofar terp at different efficiencies


import random as rd
import matplotlib.pyplot as plt
import numpy as np


def test7(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max, fluxdensitylimit):
    
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

    for n in range(N):
        
        # random B and P generated
        RN1 = rd.random() * (max_E - min_E) + min_E
        RN2 = rd.random() * (max_spinP - min_spinP) + min_spinP
        RN3 = rd.random() * (D_lum_max - D_lum_min) + D_lum_min

        Random_B = 10**(RN1) *10**-15 # B in 10^15
        Random_P = 10**(RN2) # P in 
        Random_D = 10**(RN3)

        Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * Random_D**(-2) * Random_B **2 * Random_P**(-4) * 10**3 # R is already 10 **6, (in mJy)

        # Added to lists
        L_B.append(Random_B)
        L_P.append(Random_P)
        
        L_Flux.append(Flux)
        L_D_lum.append(Random_D)

        L_fdl.append(fluxdensitylimit)

        if Flux >= fluxdensitylimit:
                Percentage_counter = Percentage_counter +1


    visible_percantage = Percentage_counter / (N) *100
    print visible_percantage

    return L_P, L_B, L_L, L_T, L_Flux, L_D_lum, L_fdl, visible_percantage



# LIST OF CONSTANTS
M = 2.1*1.99*10**(30)
R = 10**6 # in cm
min_E = 14 # in log
max_E = 17 # in log
min_spinP = np.log10(0.55) # in log ms
max_spinP = np.log10(8300) # in log ms
V_obs = 144 #input of choise for frequency is put as constant            #150 #Mhz
epsilon0 = 10**-4
D_lum_min = np.log10(0.04000) # in log Gpc
D_lum_max = np.log10(6.7011) # in log Gpc
fluxdensitylimit =  1.7 #sensitivities[obs][freq]   #input as choise for sensitivity is put as constant   #1.3 # lofar superterp 150 Mhz
# R = 1 # *10^6


data = test7(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon0, D_lum_min, D_lum_max, fluxdensitylimit)
L_P, L_B, L_L, L_T, L_Flux, L_D_lum, L_fdl, visible_percantage = data

visible_percantage_epsilon0 = visible_percantage

L_efficiencies = np.logspace(-10,-2,num = 50, dtype='float')
L_efficiencies= [6*10**-8]
L_percentages = []
print L_percentages

# y_upper = []
# y_lower = []

L_lijnx = []
L_lijny = []

for i in range(len(L_efficiencies)):
    epsilon_r = L_efficiencies[i]
    print epsilon_r

    data = test7(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max, fluxdensitylimit)
    L_P, L_B, L_L, L_T, L_Flux, L_D_lum, L_fdl, visible_percantage = data
    L_percentages.append(visible_percantage)

    if i == 0 or i == 49:
        L_lijnx.append(epsilon_r)
        L_lijny.append(visible_percantage)



    # y_upper.append(0.1)
    # y_lower.append(0.1)
  
plt.plot(L_efficiencies, L_percentages, )
# plt.plot(epsilon0, visible_percantage_epsilon0, 'ro')
# plt.axvline(x=epsilon0, color='purple', ls='--')
# plt.yscale('log')
plt.plot(L_lijnx, L_lijny, 'r')


plt.axvline(x=epsilon0,  color='purple', ls='--', label='Expected efficiency of {}'.format(epsilon0))
plt.xscale('log')
plt.ylabel('Detectable percentage')
plt.xlabel('Efficiency')


colors = ['purple']



plt.legend()

plt.show()



# import plotly.graph_objs as go

# x = L_efficiencies
# y = L_percentages



# fig = go.Figure([
#     go.Scatter(
#         x=x,
#         y=y,
#         line=dict(color='rgb(0,100,80)'),
#         mode='lines'
#     ),
#     go.Scatter(
#         x=x+x[::-1], # x, then x reversed
#         y=y_upper+y_lower[::-1], # upper, then lower reversed
#         fill='toself',
#         fillcolor='rgba(0,100,80,0.2)',
#         line=dict(color='rgba(255,255,255,0)'),
#         hoverinfo="skip",
#         showlegend=False,
#     )
# ])
# fig.show()

