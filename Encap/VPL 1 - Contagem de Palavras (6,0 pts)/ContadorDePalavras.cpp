#include "ContadorDePalavras.hpp"
#include <iostream>
using namespace std;

ContadorDePalavras::ContadorDePalavras(){
   _lista_de_palavras.begin()= _lista_de_palavras.end();  
}
void ContadorDePalavras::Adicionar(string s){
     int ocorren = 0;
    
         for (list<Palavra>::iterator it =  _lista_de_palavras.begin(); it !=  _lista_de_palavras.end(); ++it) {

        if(it->palavra() == s){
            ocorren ++;
            it->Incrementar();}}

         if(ocorren == 0){
         Palavra p1(s);
         _lista_de_palavras.push_back(p1);
          }}

void ContadorDePalavras::ImprimirOrdenado(){
        _lista_de_palavras.sort();
	    for(Palavra it : _lista_de_palavras){
        cout<< it.palavra() << "  " << it.ocorrencias()<< endl;
	   }
}
