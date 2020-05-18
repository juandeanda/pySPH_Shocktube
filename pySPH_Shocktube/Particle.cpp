#include "Particle.hpp"

Particle::Particle(){
  pos = new double [3];
  vel = new double [3];
  A = new double [3];
}
void Particle::setPos(int index,double val){
  pos[index] = val;
}
void Particle::setVel(int index, double val){
  vel[index] = val;
}
void Particle::setA(int index, double val){
  A[index] = val;
}
void Particle::setRho(double val){
  rho = val;
}
void Particle::setP(double presion){
  P = presion;
}
void Particle::setmMk(double mass){
  mk = mass;
}
void Particle::setDv(double val){
  dv = val;
}
void Particle::setSoundSpeed(double val){
  c = val;
}
double Particle::getPos(int index){
  return pos[index];
}
double Particle::getVel(int index){
  return vel[index];
}
double Particle::getA(int index){
  return A[index];
}
double Particle::getRho(){
  return rho;
}
double Particle::getP(){
  return P;
}
double Particle::getMk(){
  return mk;
}
double Particle::getDv(){
  return dv;
}
double Particle::getSoundSpeed(){
  return c;
}
