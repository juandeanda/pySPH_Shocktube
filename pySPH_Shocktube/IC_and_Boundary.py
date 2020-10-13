import json


class IC_and_Boundary:
    def __init__(self,fileIC):
        self.read(fileIC)

    def read(self,fileIC):
        f = open(fileIC)
        IC = json.load(f)
        self.np = IC["n_particle"]
        self.rhol = IC["rho"][0]["left"]
        self.rhor = IC["rho"][0]["right"]
        self.vell = IC["vel"][0]["left"]
        self.velr = IC["vel"][0]["right"]
        self.Pl = IC["pressure"][0]["left"]
        self.Pr = IC["pressure"][0]["right"]
        self.Al = IC["Entropy"][0]["left"]
        self.Ar = IC["Entropy"][0]["right"]
        self.mk = IC["mass"]
        f.close()
    def n_particle(self):
        return self.np

    def InitParticle1D(self,Particles):
        gate = IC["gate"]
        l1 = 0.5
        x = 0.0
        dx1 = ((self.rhol+self.rhor)*l1)/float(rhol*self.np)
        dx2 = ((self.rhol+self.rhor)*l1)/float(rhor*self.np)
        for i in range(0,len(Particles)):
           if x<0 :
             Paticles[i].pos[0] = x
             Paticles[i].rho = self.rhol
             Paticles[i].vel[0] = self.vell
             Paticles[i].P = self.Pl
             Paticles[i].A[0] = self.Al
             Paticles[i].mk = self.mk
             x += dx1
           if x >= 0
             Paticles[i].pos[0] = x
             Paticles[i].rho = self.rhor
             Paticles[i].vel[0] = self.velr
             Paticles[i].P = self.Pr
             Paticles[i].A[0] = self.Ar
             Paticles[i].mk = self.mk
             x += dx2
