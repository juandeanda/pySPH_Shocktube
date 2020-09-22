from pySPH_Shocktube.Particle import *
from pySPH_Shocktube.IC_and_Boundary import *



IC = IC_and_Boundary("IC.json") 
particles = []
for i in range(0,IC.n_particle()):
   particle = Particle(1)
   particles.append(particle)


