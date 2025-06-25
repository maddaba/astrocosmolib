import numpy as np
from scipy.integrate import quad
from scipy.constants import c 

class Distances:

    #def __init__(self, hubble_function, h_units=True):
    def __init__(self, hubble_function, h_units=True):
        self.hubble_function = hubble_function
        self.h_units = h_units

    def comoving_distance(self, z):

        # Definisce 1/E(z) da integrare
        inverse_E = lambda zz: 1.0 / self.hubble_function.E(zz)

        # Integrazione da 0 a z
        integral, _ = quad(inverse_E, 0, z, epsrel=1e-6, epsabs=1e-8)

        # Conversione in Mpc a seconda del sistema di unità
        if self.h_units:
            return integral * c / 1e3 / 100
        else:
            return integral * c / 1e3 / self.hubble_function.H0


    def luminosity_distance(self, z):
 
        # Definisce 1/E(z)
        inverse_E = lambda zz: 1.0 / self.hubble_function.E(zz)

        # Integrazione da 0 a z con precisione fissata
        integral, _ = quad(inverse_E, 0, z, epsrel=1e-6, epsabs=1e-8)

        # Calcola la distanza comovente
        if self.h_units:
            dc = integral * c / 1e3 / 100
        else:
            dc = integral * c / 1e3 / self.hubble_function.H0

        # Restituisce la distanza di luminosità: d_L = (1+z) * d_C
        return (1 + z) * dc


    def transverse_comoving_distance(self, z):

        # Calcolo distanza comovente
        inverse_E = lambda zz: 1.0 / self.hubble_function.E(zz)
        integral, _ = quad(inverse_E, 0, z, epsrel=1e-6, epsabs=1e-8)

        if self.h_units:
            dc = integral * c / 1e3 / 100
        else:
            dc = integral * c / 1e3 / self.hubble_function.H0

        # Comportamento in base alla curvatura
        ok = self.hubble_function.Omega_k
        if ok == 0:
            return dc
        elif ok > 0:
            sqrt_ok = np.sqrt(ok)
            return dc / sqrt_ok * np.sinh(sqrt_ok * dc)
        else:
            sqrt_ok = np.sqrt(-ok)
            return dc / sqrt_ok * np.sin(sqrt_ok * dc)


    def angular_diameter_distance(self, z):

        return self.transverse_comoving_distance(z) / (1 + z)

    def hubble_distance(self, z):

        if self.h_units:
            return c / 1.e3 / (100 * self.hubble_function.E(z))
        else:
            return c / 1.e3 / self.hubble_function.H(z)


    def isotropic_volume_distance(self, z):

        dm = self.transverse_comoving_distance(z)
        dh = self.hubble_distance(z)
        return ( z  * dm**2 * dh)**(1./3)