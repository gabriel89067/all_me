#ifndef ALUNO_H
#define ALUNO_H
#include <iostream>

struct Aluno{
      //dados/atibuiçoes
      int matricula;
      std::string nome;
      Aluno* esq;
      Aluno* dir;
//operaçoes
Aluno();

Aluno(int matricula,std::string nome);

void imprimir_dados();
};
#endif