import numpy as np  
import scipy.integrate as s
from scipy.integrate import trapezoid
from scipy.constants import c

class Distances:
    """
    Class to compute cosmological distances given hubble function and cosmological parameters.  
    """
    def __init__(self, hubble_function):
        """
        Parameters
        ----------
        hubble_function : callable
            Function that computes the Hubble parameter as a function of redshift.
        cosmological_parameters : dict
            Dictionary of cosmological parameters.
        """
        
        
        self.hubble_function = hubble_function
    
    def comoving_distance(self, z):
        """
        Compute the comoving distance at redshift z.

        Parameters
        ----------
        z : float or array-like
            Redshift.

        Returns
        -------
        float or array-like
            Comoving distance in Mpc.
        """
        #passare qui integrale con funzioni numpy o scipy
        #H0=67.15 #km/s/Mpc
        c1=c/1000
        #c1 = 3.0857e19 SBAGLIATO
        integral,err_integral = s.quad(lambda x: c1/self.hubble_function(x), 0, z)
        return integral
      

      #diatnze angoilari    
    def angular_diameter_distance(self, z):
        Dc = self.comoving_distance(z)  # Usa la distanza comovente già implementata
        return Dc / (1 + z)  # Formula della distanza angolare

    def hubble_distance(self,z):
        return c / (1000 * self.hubble_function(z))  # Convertiamo la velocità della luce in km/s


    def luminosity_distance(self, z):
        Dc = self.comoving_distance(z)  # Usa la distanza comovente già implementata
        return Dc * (1 + z)  # Formula della distanza di luminosità

    def rhubble_distance(self, z):
        integral, err_integral = s.quad(lambda x: 1/self.hubble_function(x), z, np.inf)
        return integral
    
        