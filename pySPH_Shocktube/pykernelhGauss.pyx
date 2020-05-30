cdef extern from "kernelhGauss.hpp":
    cdef cppclass kernelhGauss:
         double wij(double xi, double xj, double h)
         double dwij(double xi, double xj, double h)
cdef class pykernelhGauss:
    cdef kernelhGauss *objKernel
    def __cinit__(self):
       self.objKernel = new kernelhGauss()
    def __dealloc__(self):
       del self.objKernel
    def wij(self, double xi, double xj, double h):
       return self.objKernel.wij(xi,xj,h)
    def dwij(self,double xi, double xj, double h):
       return self.objKernel.dwij(xi,xj,h)
