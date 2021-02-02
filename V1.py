import random as rd
import matplotlib.pyplot as plt 
import math 
import numpy as np 


# function creating a random sample of magnetars
def test1(M, R, L, T, x1, x2, y1, y2):
    
    # lists magnetic field and Spin periods
    N = 20 

    L_B = []
    L_P = []
    for n in range(N):
        
        RN1 = rd.random() * (x2 - x1) + x1
        RN2 = rd.random() * (y2 - y1) + y1

        Random_B = 10**(RN1)
        Random_P = 10**(RN2)

        L_B.append(Random_B)
        L_P.append(Random_P)

    plt.plot(L_B, L_P,'ro')
    plt.yscale('log')
    plt.xscale('log')
    plt.xlim(10**-2, 10**x2+50)
    plt.ylim(10**-2, 10**y2+50)
    plt.show()




# function creating a random sample of magnetars
def test2(M, R, L, T, x1, x2, y1, y2):
    
    # lists magnetic field and Spin periods
    N = 100

    L_all_variables = [['nummer','random B', 'random P']]
    L_B = []
    L_P = []
    for n in range(N):
        
        RN1 = rd.random() * (x2 - x1) + x1
        RN2 = rd.random() * (y2 - y1) + y1

        Random_B = 10**(RN1)
        Random_P = 10**(RN2)

        L_B.append(Random_B)
        L_P.append(Random_P)

        L_all_variables.append([n, Random_B, Random_P,])


    print L_all_variables

    plt.plot(L_B, L_P,'ro')
    plt.yscale('log')
    plt.xscale('log')
    plt.xlim(10**-2, 10**x2+50)
    plt.ylim(10**-2, 10**y2+50)
    plt.show()


# test2(1,1,1,1,-1,3,-1,3)


def test3(M, R, x1, x2, y1, y2):
    
    # lists magnetic field and Spin periods
    N = 100

    # list of variables
    L_all_variables = [['nummer','random B', 'random P', 'Plateau time', 'luminosity']]
    L_P = []
    L_B = []
    L_T = []
    L_L = []

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

        L_all_variables.append([n + 1, Random_B, Random_P, T, L])

    # print L_all_variables

    # plot P-B
    plt.plot(L_P, L_B,'ro')
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('Field strength B (10^15 G)')
    plt.xlabel('Spin period P (ms)')
    plt.show()
   
    # Plot L-T
    plt.plot(L_T, L_L, 'go')
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('LogLx(Ta)')
    plt.xlabel('Log(T*a)')
    plt.show() 

    return L_P, L_B,


# LIST OF CONSTANTS
M = 2.1*1.99*10**(30)
R = 10**6 # in cm
min_E = 14 # in log
max_E = 17 # in log
min_spinP = np.log10(0.55) # in log ms
max_spinP = np.log10(8300) # in log ms



# test3(M, R, min_E, max_E, min_spinP, max_spinP)



def test4(V_obs, epsilon_r, D_lum, B, R, P):
    
    N = 100 
    L_Flux = []
    L_D_lum = []

    for n in range(N):
        RN1 = rd.random()



        Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * D_lum**(-2) * B**2 * R**(6) * P**(-4)



V_obs = 144 #Mhz
epsilon_r = 10**-4
D_lum_min = 1
D_lum_max = 1
B = 10
P = 100
R = 1 # *10^6

R = 1


# test4(V_obs, epsilon_r, D_lum, B, R, P)


def test5(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max):
    
    # total tries for E and P
    N = 20

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

        L_all_variables.append([n + 1, Random_B, Random_P, T, L])

    
    N2 = 1000 # total tests with distance
    for i in range(N):
       
        L_Flux_line = [] # lists to create lines on plots
        L_D_lum_line = []

        for x in range(N2):

            # random distance created
            RN3 = rd.random() * (D_lum_max - D_lum_min) + D_lum_min
            Random_D = 10**(RN3)

            # Flux calculated
            Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * Random_D**(-2) * L_B[i] **2 * R  * L_P[i]**(-4) # R is already 10 **6
           
            L_Flux.append(Flux)
            L_D_lum.append(Random_D)
            
            L_Flux_line.append(Flux)
            L_D_lum_line.append(Random_D)
        plt.plot(L_D_lum_line, L_Flux_line, 'r-')
        plt.yscale('log')
        plt.xscale('log')
        plt.ylabel('FLux density (Jy)')
        plt.xlabel('Luminosity distance (Mpc)')
    plt.show()


    plt.plot(L_D_lum, L_Flux, 'bo')
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('FLux density (Jy)')
    plt.xlabel('Luminosity distance (Mpc)')
    plt.show()
   
    # plot P-B
    plt.plot(L_P, L_B,'ro')
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('Field strength B (10^15 G)')
    plt.xlabel('Spin period P (ms)')
    plt.show()
   
    # Plot L-T                                                                Plot L-T
    # plt.plot(L_T, L_L, 'go') 
    # plt.yscale('log')
    # plt.xscale('log')
    # plt.ylabel('LogLx(Ta)')
    # plt.xlabel('Log(T*a)')
    # plt.show() 



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

# test5(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, np.log(D_lum_min), np.log(D_lum_max))


def test6(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max):
    
    # total tries for E and P
    N = 20

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

    
    N2 = 1000 # total tests with distance
    for i in range(N):
       
        L_Flux_line = [] # lists to create lines on plots
        L_D_lum_line = []

        for x in range(N2):

            # random distance created
            RN3 = rd.random() * (D_lum_max - D_lum_min) + D_lum_min
            Random_D = 10**(RN3)

            # Flux calculated
            Flux = 8*10**(7) * V_obs**(-1) * epsilon_r * Random_D**(-2) * L_B[i] **2 * R  * L_P[i]**(-4) # R is already 10 **6
           
            L_Flux.append(Flux)
            L_D_lum.append(Random_D)
            
            L_Flux_line.append(Flux)
            L_D_lum_line.append(Random_D)

            L_fluxdensitiy_limit. append(0.153)

    #     plt.figure(1)
    #     plt.plot(L_D_lum_line, L_Flux_line, 'r-')
    #     plt.yscale('log')
    #     plt.xscale('log')
    #     plt.ylabel('FLux density (Jy)')
    #     plt.xlabel('Luminosity distance (Mpc)')

    # plt.plot(L_D_lum, L_fluxdensitiy_limit, 'b-')
    # plt.show()


    # # plt.contour(L_D_lum, L_Flux, L_P, colors='black')
    # plt.yscale('log')
    # plt.xscale('log')
    # plt.show()


    # plt.figure(2)
    # plt.plot(L_D_lum, L_Flux, 'bo')
    # plt.yscale('log')
    # plt.xscale('log')
    # plt.ylabel('FLux density (Jy)')
    # plt.xlabel('Luminosity distance (Mpc)')
    # plt.show()
   
    # # plot P-B
    # plt.figure(3)
    # plt.plot(L_P, L_B,'ro')
    # plt.yscale('log')
    # plt.xscale('log')
    # plt.ylabel('Field strength B (10^15 G)')
    # plt.xlabel('Spin period P (ms)')
    # plt.show()
   
    # Plot L-T                                                                Plot L-T
    # plt.plot(L_T, L_L, 'go') 
    # plt.yscale('log')
    # plt.xscale('log')
    # plt.ylabel('LogLx(Ta)')
    # plt.xlabel('Log(T*a)')
    # plt.show() 
    return L_P, L_B



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

# test6(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, np.log(D_lum_min), np.log(D_lum_max))


# SEABORN TEST


# import matplotlib.pyplot as plt
# plt.style.use('classic')
# import numpy as np
# import pandas as pd
# import seaborn as sns
# sns.set()



def test7(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, D_lum_min, D_lum_max):
    
    # total tries for E and P
    N = 100000

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

    
    N2 = 1 # total tests with distance
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

            L_fluxdensitiy_limit. append(153)

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

test7(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, np.log(D_lum_min), np.log(D_lum_max))


def seaborntest(data):

    L_P, L_B, L_L, L_T, L_Flux, L_D_lum = data

    # rng = np.random.RandomState(0)
    
    
    plt.figure(1)
    plt.plot(L_P,L_B,'ro', markersize = 1)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('Field strength B (10^15 G)')
    plt.xlabel('Spin period P (ms)')
    # plt.legend('', ncol=2, loc='upper left');
    plt.show()

    plt.figure(2)
    plt.plot(L_D_lum,L_Flux, 'bo', markersize = 1)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('FLux density (mJy)')
    plt.xlabel('Luminosity distance (Mpc)')
    # plt.legend('', ncol=2, loc='upper left');
    plt.show()

    plt.figure(3)
    plt.plot(L_P, L_Flux, 'go', markersize = 1)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('FLux density (mJy)')
    plt.xlabel('Spin period P (ms)')
    # plt.legend('', ncol=2, loc='upper left');
    plt.show()

    plt.figure(4)
    plt.plot(L_B, L_Flux, 'go', markersize = 1)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('FLux density (mJy)')
    plt.xlabel('Field strength B (10^15 G)')
    # plt.legend('', ncol=2, loc='upper left');
    plt.show()

    plt.figure(5)
    plt.plot(L_T, L_L, 'go', markersize = 1)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('LogLx(Ta)')
    plt.xlabel('Log(T*a)')
    plt.show()

    plt.figure(6)
    plt.plot(L_T, L_Flux, 'go', markersize = 1)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('FLux density (mJy)')
    plt.xlabel('Log(T*a)')
    plt.show()
    plt.figure(6)
    plt.plot(L_L, L_Flux, 'go', markersize = 1)
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('FLux density (mJy)')
    plt.xlabel('LogLx(Ta)')
    plt.show()




data = test7(M, R, min_E, max_E, min_spinP, max_spinP, V_obs, epsilon_r, np.log(D_lum_min), np.log(D_lum_max))


seaborntest(data)

