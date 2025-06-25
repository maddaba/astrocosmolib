import numpy as np
from scipy.integrate import quad
from scipy.constants import c  # m/s  

class Distances:

    def __init__(self, hubble_function, Omega_m, H0, w0=-1.0, wa=0.0):
        """
        Parametri cosmologici:
        - hubble_function: funzione H(z)
        - Omega_m: densità di materia
        - H0: Hubble a z=0 in km/s/Mpc
        - w0, wa: parametri dell'equazione di stato dell'energia oscura
        """
        self.hubble_function = hubble_function
        self.Omega_m = Omega_m
        self.H0 = H0
        self.w0 = w0
        self.wa = wa
        self.c_kms = c / 1000  # in km/s

    def hubble(self, z):
        """Ridà H(z) in km/s/Mpc"""
        return self.hubble_function(z, self.Omega_m, self.H0, self.w0, self.wa)

    def comoving_distance(self, z):
        """Distanza comovente Dc(z) = integ(dz' c / H(z')) """
        integrand = lambda x: self.c_kms / self.hubble(x)
        integral, _ = quad(integrand, 0, z)
        return integral  # in Mpc

    def transverse_comoving_distance(self, z):
        """Assumo universo piatto : D_M = D_C"""
        return self.comoving_distance(z)

    def angular_diameter_distance(self, z):
        """Distanza angolare: D_A = D_M / (1 + z)"""
        return self.transverse_comoving_distance(z) / (1 + z)

    def hubble_distance(self, z):
        """Distanza di Hubble: D_H = c / H(z)"""
        return self.c_kms / self.hubble(z)

    def volume_distance(self, z):
        """
        Distanza di volume:
        D_V(z) = [ z * D_M(z)^2 * D_H(z) ]^(1/3)
        """
        Dm = self.transverse_comoving_distance(z)
        Dh = self.hubble_distance(z)
        return (z * Dm**2 * Dh)**(1/3)
