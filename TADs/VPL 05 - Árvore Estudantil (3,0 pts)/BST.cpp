#include "BST.hpp"

Aluno* criar_aluno(int matricula,std::string nome) {//inicializa um aluno 

  Aluno* aux = new Aluno;
  aux->nome = nome;
  aux->matricula = matricula;
  aux->esq = nullptr;
  aux->dir = nullptr;

  return aux;
}

void BST::inserir_aluno(Aluno aluno) {

  if (root != nullptr) {
      auxiliar_de_insercao(root, aluno.matricula, aluno.nome);
         } else {
            root = criar_aluno(aluno.matricula,aluno.nome);
                }

}

void BST::auxiliar_de_insercao(Aluno* n, int matricula,std::string nome) {//auxilia se tem que colocar a direita ou a esquerda da arvore

   if (matricula < n->matricula ) {
       if (n->esq == nullptr) {
          n->esq = criar_aluno( matricula, nome);
           } else {
             auxiliar_de_insercao(n->esq, matricula, nome);
           }
             } else if (matricula> n->matricula) {
     if (n->dir == nullptr) {
       n->dir = criar_aluno( matricula, nome);
     } else {
        auxiliar_de_insercao(n->dir, matricula, nome);
      }}}

void inorder(Aluno* n){
 if(n==nullptr){
    return;
 }
  inorder(n->esq);
  std::cout<<n->matricula<< " " << n->nome<<std::endl;
  inorder(n->dir);
}


void BST::imprimir_arvore(){

 inorder(root);
 std::cout<<std::endl;

 }



Aluno* BST::procurar_aluno(int matricula){
  Aluno* r;
     r=root;

      while (r != nullptr && r->matricula != matricula) {
       if (r->matricula > matricula)
          r = r->esq;
       else
          r = r->dir;
    }

    return r;
}
