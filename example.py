import pySPH_Shocktube.pyParticle as pa
import pySPH_Shocktube.pykernelhGauss as kr
part = []
kernel = kr.pykernelhGauss()
part.append(pa.pyParticle())
part.append(pa.pyParticle())
part[0].setPos(0,2.5)
part[1].setPos(0,5.5)
print(part[0].getPos(0),part[1].getPos(0))
print(kernel.dwij(part[0].getPos(0), part[1].getPos(0), 0.5))
