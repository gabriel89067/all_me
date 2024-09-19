#include "fila_de_prioridade.h"
#include <string>

using namespace std;



  FilaDePrioridade::FilaDePrioridade(){
   primeiro_= nullptr;
   ultimo_=nullptr;

  }

  // Retorna o elemento de maior prioridade.
  // PRECONDIÇÃO: a fila tem pelo menos um elemento.
  string FilaDePrioridade::primeiro() const{
   return primeiro_->_nome;
  }

  // Retorna o número de elementos na fila.
  int FilaDePrioridade::tamanho() const{
   return tamanho_;
  }

  // Testa se a fila está vazia.
  bool FilaDePrioridade::vazia() const{
  return primeiro_ == nullptr;
  }

  // Remove o elemento de maior prioridade.
  // PRECONDIÇÃO: a fila tem pelo menos um elemento.
  void FilaDePrioridade::RemoverPrimeiro(){
        if(primeiro_!=nullptr){
       No* aux;
       aux = primeiro_->next;
     primeiro_ = aux;
  }}

  // Insere um elemento s fila com prioridade p;
  // OBS: Pode haver repetição de elementos.
  // Neste caso, os elementos podem ter prioridades iguais ou diferentes.
  void FilaDePrioridade::Inserir(int idade, string nome){

  No* aux = new No;
   aux->_idade = idade;
   aux->_nome = nome;
   aux->next = nullptr;
    aux->antes = nullptr;
    int tam=0;

   if(primeiro_== nullptr){
    primeiro_= aux;
    ultimo_=aux;
   }else{
       int con = 0;

       No* inser = primeiro_;
       No* pap = primeiro_;

           if(aux->_idade > primeiro_->_idade){
            primeiro_->antes = aux;
            aux->next = primeiro_;
            primeiro_ = aux;
            tamanho_++;
            con++;
            }

           if(aux->_idade == ultimo_->_idade){
                aux->antes=ultimo_;
                ultimo_->next= aux;
                ultimo_= aux;
                 tamanho_++;
                 con++;

            }else if(aux->_idade == pap->_idade){
                aux->next = pap->next;
                aux->antes = pap->next->antes;
                pap->next->antes = aux;
                pap->next = aux;
                tamanho_++;
                con++;

           }


           if(aux->_idade < ultimo_->_idade){
                ultimo_->next=aux;
                aux->antes = ultimo_;
                ultimo_=aux;
                tamanho_++;
                con++;

                }

          if(con == 0){

            while(inser!= nullptr){
            if(aux->_idade < inser->_idade && aux->_idade == inser->next->_idade){
                    aux->antes = inser->next;
                    aux->next = inser->next->next;
                    inser->next->next->antes = aux;
                    inser->next->next = aux;
                    tamanho_++;
             }

            if(aux->_idade < inser->_idade && aux->_idade > inser->next->_idade){
                aux->antes = inser;
                aux->next = inser->next;
                inser->next->antes = aux;
                inser->next = aux;
                 tamanho_++;}




           inser = inser->next;

          }}


     

  }
   }



  // Remove todos os elementos da fila.
  void FilaDePrioridade::Limpar(){
       No* limpa;
  limpa = primeiro_;


  while(limpa != nullptr){
    delete limpa;
    limpa = limpa->next;
  }

      
  }

 
