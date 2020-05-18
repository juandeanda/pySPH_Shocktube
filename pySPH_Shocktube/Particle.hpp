#ifndef Particle_H
#define Particle_H
class Particle{
private:
double *pos;
double *vel;
double *A;
double rho =0;
double P=0;
double mk=0;
double dv=0;
double c=0;
public:
  Particle();
  void setPos(int index,double val);
  void setVel(int index, double val);
  void setA(int index, double val);
  void setRho(double val);
  void setP(double presion);
  void setmMk(double mass);
  void setDv(double val);
  void setSoundSpeed(double val);
  double getPos(int index);
  double getVel(int index);
  double getA(int index);
  double getRho();
  double getP();
  double getMk();
  double getDv();
  double getSoundSpeed();
};
#endif
