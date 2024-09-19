#ifndef BST_H
#define BST_H
#include "Aluno.hpp"
struct BST {
  Aluno* root = nullptr;//raiz da arvore

  void auxiliar_de_insercao(Aluno* root, int matricula,std::string nome);

  void inserir_aluno(Aluno aluno);
  Aluno* procurar_aluno(int matricula);
  void imprimir_arvore();
};
#endif