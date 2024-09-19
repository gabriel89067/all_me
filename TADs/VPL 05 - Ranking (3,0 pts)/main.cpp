#include "Estudante.hpp"
#include <iostream>
#include <math.h>
#include <iomanip>


 int main() {
 Estudante aluno[2000];
 long int x, y,b,menorx[2000],menorma[2000],auxiliarmatr;
 float vetorsele[2000];

  std::cout << std::fixed << std::showpoint;
  std::cout << std::setprecision(2);


 for(x=0;x<10;x++){

  std::cin >> aluno[x].matricula;
  
  std::cin >> aluno[x].nome;

  std::cin >> aluno[x].notas[0]>> aluno[x].notas[1]>> aluno[x].notas[2]>> aluno[x].notas[3]>> aluno[x].notas[4];
 
      }

  float mediaaluno[20];

  for(x=0;x<10;x++){
    mediaaluno[x] = aluno[x].calcularRSG();
  
  
      
  }

  for(x=0;x<10;x++){

    vetorsele[x]= mediaaluno[x];}

   float auxiliar;

  for(y=0;y<9;y++){
     for(x= y + 1; x<10;x++){

       if(vetorsele[y] < vetorsele[x]){
       auxiliar = vetorsele[y];
       vetorsele[y] =  vetorsele[x];
       vetorsele[x] = auxiliar;}

      }}
//#############################################################################################################################
b=0;

for(y=0;y<10;y++){
  for(x=0;x<10;x++){
   if(vetorsele[y] == mediaaluno[x]){
    menorx[b] = x;
   b++;
   }
  }}



for(x=0;x<10;x++){

    menorma[x] = aluno[x].matricula;
}




if(b!=10){

    for(y=0;y<(b-1);y++){
  for(x=y+1;x<b;x++){
   if(menorma[menorx[y]] > menorma[menorx[x]]){

       auxiliarmatr = menorma[menorx[y]];
       menorma[menorx[y]] =  menorma[menorx[x]];
       menorma[menorx[x]] = auxiliarmatr;}
}}

for(y=0;y<3;y++){
  for(x=0;x<(b-1);x++){
   if(menorma[y] == aluno[x].matricula){
      std::cout << aluno[x].matricula << " ";

      std::cout << aluno[x].nome << " ";

     std::cout << mediaaluno[x] << " ";

      std::cout << std::endl;

      }

}}



  }






if(b==10){
for(y=0;y<3;y++){
  for(x=0;x<10;x++){
   if(vetorsele[y] == mediaaluno[x]){
      std::cout << aluno[x].matricula << " ";

      std::cout << aluno[x].nome << " ";

     std::cout << mediaaluno[x] << " ";

      std::cout << std::endl;

      }

}}}






  return 0;
  }
