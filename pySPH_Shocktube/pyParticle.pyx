cdef extern from "Particle.hpp":
    cdef cppclass Particle:
        Particle()
        void setPos(int index,double val)
        void setVel(int index, double val)
        void setA(int index, double val)
        void setRho(double val)
        void setP(double presion)
        void setmMk(double mass)
        void setDv(double val)
        void setSoundSpeed(double val)
        double getPos(int index)
        double getVel(int index)
        double getA(int index)
        double getRho()
        double getP()
        double getMk()
        double getDv()
        double getSoundSpeed()

cdef class pyParticle:
    cdef Particle *objPar
    def __cinit__(self):
      self.objPar = new Particle()
    def __dealloc__(self):
      del self.objPar
    def setPos(self, int index,double val):
      self.objPar.setPos(index,val)
    def setVel(self,int index, double val):
       self.objPar.setVel(index,val)
    def setA(self,int index, double val):
       self.objPar.setA(index,val)
    def setRho(self,double val):
       self.objPar.setRho(val)
    def setP(self,double presion):
       self.objPar.setP(presion)
    def setmMk(self,double mass):
       self.objPar.setmMk(mass)
    def setDv(self,double val):
       self.objPar.setDv(val)
    def setSoundSpeed(self,double val):
       self.objPar.setSoundSpeed(val)
    def getPos(self,int index):
       return self.objPar.getPos(index)
    def getVel(self,int index):
       return self.objPar.getVel(index)
    def getA(self,int index):
       return self.objPar.getA(index)
    def getRho(self):
       return self.objPar.getRho()
    def getP(self):
       return self.objPar.getP()
    def getMk(self):
       return self.objPar.getMk()
    def getDv(self):
       return self.objPar.getDv()
    def getSoundSpeed(self):
       return self.objPar.getSoundSpeed()
