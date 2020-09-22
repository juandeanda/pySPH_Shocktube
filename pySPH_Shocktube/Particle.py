import numpy as np 

class Particle:
    def __init__(self,dim):
        self.pos = np.zeros(3)
        self.vel = np.zeros(3)
        self.A = np.zeros(3)
        self.rho = 0.0
        self.P = 0.0 
        self.mk = 0.0 
        self.dv = 0.0
        self.c = 0.0
        self.dim = dim
    def size(self):
        return self.dim



    