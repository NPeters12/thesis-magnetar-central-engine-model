import random as rd
import matplotlib.pyplot as plt
import numpy as np
import inquirer
import matplotlib.colors as colors
import random as rd
import matplotlib.pyplot as plt
import numpy as np
import inquirer

import astropy.units as u
from astropy.cosmology import Planck13, z_at_value
  
from astropy.cosmology import FlatLambdaCDM
import astropy.units as u

cosmo = FlatLambdaCDM(H0=69.6 * u.km / u.s / u.Mpc, Tcmb0=2.725 * u.K, Om0=0.286) # cosmo constants


dlum_mid = 40

z = z_at_value(cosmo.luminosity_distance, dlum_mid * u.Mpc)

print z