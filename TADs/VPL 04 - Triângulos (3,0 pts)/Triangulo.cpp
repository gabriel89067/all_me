#include "Triangulo.hpp"
#include "Ponto2D.hpp"




Triangulo::Triangulo(Ponto2D p1,Ponto2D p2,Ponto2D p3){
     *_p1=p1;
     *_p2=p2;
     *_p3=p3;
        dist_tri[0] = _p1->calcular_distancia(_p2);
        dist_tri[1] = _p2->calcular_distancia(_p3);
        dist_tri[2] = _p3->calcular_distancia(_p1);}

double Triangulo::calcular_area(){
    double p;
    double area;
       p = this->calcular_perimetro()/2;
       area = sqrt(p*(p-this->dist_tri[0] )*(p-this->dist_tri[1])*(p-this->dist_tri[2]));
         *this->area_tri = area;
return area;}

double Triangulo::calcular_perimetro(){
    return (this->dist_tri[0] + this->dist_tri[1] + this->dist_tri[2]);}

int Triangulo::comparar_area(Triangulo *triangulo){
    int comp = 0;
        if(*this->area_tri == *triangulo->area_tri){
        comp = 0;}
          if(*this->area_tri < *triangulo->area_tri){
          comp = -1;}
            if(*this->area_tri > *triangulo->area_tri){
            comp = 1;}
return comp;}



