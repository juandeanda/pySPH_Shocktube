#include "kernelhGauss.hpp"

double kernelhGauss::wij(double xi, double xj, double h){
  return (1/((sqrt(pi)*h)))*(exp(-1.0*pow(xi-xj,2)/pow(h,2))*(1.5-(pow(xi-xj,2)/pow(h,2))));
 }
 double kernelhGauss::dwij(double xi, double xj, double h){
  return (1/((sqrt(pi)*pow(h,5))))*(exp(-1.0*pow(xi-xj,2)/pow(h,2))*((2*pow(xi-xj,3))-(5*pow(h,2)*(xi-xj))));
 }
