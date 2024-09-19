// NÃO ALTERE ESSA LINHA
#include "avaliacao_basica_bst.hpp"

int main() {
  
    // NÃO ALTERE ESSA LINHA
    avaliacao_basica();

 
  Aluno aluno;
  BST bst;

  while(std::cin>>aluno.matricula>>aluno.nome){
    
    bst.inserir_aluno(aluno);
    
  }

   bst.imprimir_arvore();

    return 0;
}