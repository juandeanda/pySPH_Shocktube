import pySPH_Shocktube.pyParticle as pa

objParticle = pa.pyParticle()
objParticle.setPos(0,2.5)
objParticle.setPos(1,5.5)
objParticle.setPos(2,10)

print(objParticle.getPos(0),objParticle.getPos(1),objParticle.getPos(2))
