#include "Aluno.hpp"
#include <iostream>
Aluno::Aluno(){
    
}
Aluno::Aluno(int matricula,std::string nome){
}

void Aluno::imprimir_dados(){//retorna a partir do 'this' , pois e mandado um ponteiro
  std::cout<<this->matricula<<" "<<this->nome;
}

