#ifndef TRIANGULO_H
#define TRIANGULO_H
#include "Ponto2D.hpp"
#include <cmath>



struct Triangulo{
    Ponto2D* _p1 = new Ponto2D;
    Ponto2D* _p2 = new Ponto2D;
    Ponto2D* _p3 = new Ponto2D;
       double* dist_tri = new double[3];
       double* area_tri = new double;

Triangulo(Ponto2D p1,Ponto2D p2,Ponto2D p3);
    double calcular_area();
    double calcular_perimetro();

int comparar_area(Triangulo *triangulo);

};
#endif
