#ifndef kernelhGauss_H
#define kernelhGauss_H
#include<math.h>
#define pi 3.1416
class kernelhGauss{
public:
 double wij(double xi, double xj, double h);
 double dwij(double xi, double xj, double h);
};
#endif
