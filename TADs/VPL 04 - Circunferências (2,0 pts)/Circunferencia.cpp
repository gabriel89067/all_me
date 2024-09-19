#include "Circunferencia.hpp"
#include <math.h>


 Circunferencia::Circunferencia(double x,double y,double _raio){
 xc = x;
 yc = y;
 raio = _raio;
}

double Circunferencia::calcularArea() {

 return 3.14 * pow(raio,2);

}

bool Circunferencia::possuiIntersecao(Circunferencia* p1) {

bool teste;

 double distx = (p1->xc - this->xc);
 double disty = (p1->yc - this->yc);


if(distx < 0) {
 distx = distx * (-1);
}

if(disty < 0) {
 disty = disty * (-1);
}

 double dist1a2  = sqrt((pow(distx,2) + pow(disty,2)));

if ((p1->raio + this->raio) > dist1a2){

 
     teste = 1;
     return teste;
    
}



if ((p1->raio + this->raio) == dist1a2){
 teste = 1;
 return teste;
}


if ((p1->raio + this->raio) < dist1a2){
  teste = 0;
  return teste;
}




}
