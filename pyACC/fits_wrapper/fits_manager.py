from astropy.io import fits#per aprire fits
import numpy as numpy #per gestire array
#voglio impostare modulo allo stesso livello, voglio 
from ..helpers.logger import Logger #vado a prendere helpers che si trova a due punti (..) di distanza. Cosa vogliono dire i due punti?

#definisco oggetto, se faccio classe definisco oggetto e suoi attributi (studente, che ha sua matricola, altezza, ..)
class FitsManager:
  """to manage fits usando astropy.io.fits module
  """
   #definisco costrutture, la prima cosa che succede quando definisco oggetto, in python posso cresare un solo costruttore
  def __init__(self, input_file):
    self.input_file=input_file#prende un solo parametro in input che salvo come parametro
    self.hdulist=fits.open(input_file)
    self.logger=Logger("FitsManager")
    self.logger("Fits open succesfully") #poi guarda file prof!!!!!

  def get_hdu_count(self):#quanti hdu sono in questo fits
    return len(self.hdulist) 
  
  def get_get_header(self, hdu_index):#gli passo indice, quello dell'hdu voglio aprire, e mi restituisce header di quell'hdu
    if hdu_index <0 or hdu_index>=len(self.hdulist):
      raise ValueError("invalid hdu index")
    return self.hdulist[hdu_index].header
  
  def get_data(self, hdu_index):#get the data of the hdu tramite index dell'hdu
    if hdu_index <0 or hdu_index>=len(self.hdulist):
      self.logger.error("Invalid hdu index", ValueError)
    return self.hdulist[hdu_index].data
  