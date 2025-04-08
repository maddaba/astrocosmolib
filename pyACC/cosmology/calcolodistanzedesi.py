import numpy as np  
import scipy.integrate as s
from scipy.integrate import trapezoid
from scipy.constants import c

class Distances:

    def __init__(self, hubble_function, Omega_m, H0, w0, wa):       

        self.hubble_function = hubble_function
        self.Omega_m = Omega_m
        self.H0 = H0
        self.w0 = w0
        self.wa = wa    
      
        
    def hubble(self, z):
        return self.hubble_function(z, self.Omega_m, self.H0, self.w0, self.wa)  
    
    def comoving_distance(self, z): 
        c1=c/1000
        integral,err_integral = s.quad(lambda x: c1/self.hubble_function(x,self.Omega_m,self.H0, self.w0, self.wa), 0, z)
        return integral

    def angular_diameter_distance(self, z):
        Dc = self.comoving_distance(z)
        return Dc / (1 + z)

    def hubble_distance(self, z):
        c1=c/1000
        integral= c1/self.hubble_function(z, self.Omega_m, self.H0, self.w0, self.wa)
        #integral, _ = s.quad(lambda x: 1./self.hubble_function(x,self.Omega_m,self.H0, self.w0, self.wa), z, np.inf)  #QUALE è LA FORMULA GIUSTA PER D_H?
        return integral 
    
    def volume_distance(self, z):
        # Volume distance formula: D_V(z) = (z*Dm**2*Dh)**1/3
        Dm = self.angular_diameter_distance(z)
        Dh = self.hubble_distance(z)
        return (z * Dm**2 * Dh)**(1/3)

    