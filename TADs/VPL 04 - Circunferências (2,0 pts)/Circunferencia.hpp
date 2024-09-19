#ifndef M_PI
#define M_PI 3,14

#endif

#ifndef CIRCUNFERENCIA_H
#define CIRCUNFERENCIA_H

#include <math.h>

struct Circunferencia{

  double xc, yc, raio;

Circunferencia(double,double,double);

    double calcularArea();

    bool possuiIntersecao(Circunferencia* c);

};

#endif
