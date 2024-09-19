#include "Estudante.hpp"
#include <math.h>




float Estudante::calcularRSG(){
      int x;
      long double somanota, mediaaluno;
      somanota= 0;
      for(x=0;x<5;x++){
       somanota = somanota + notas[x];
      }
    mediaaluno = somanota/5;

  return mediaaluno;

  }
