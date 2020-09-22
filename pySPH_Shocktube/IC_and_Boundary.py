import json


class IC_and_Boundary:
    def __init__(self,fileIC):
        self.read(fileIC)

    def read(self,fileIC):
        f = open(fileIC)
        IC = json.load(f)
        print(IC["rho"][0]["right"])
        self.np = IC["n_particle"]
        f.close()
    def n_particle(self):
        return self.np


