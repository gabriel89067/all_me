#include "Cotacao.hpp"
#include <iostream>

string Cotacao::get_data(){
  return this->_data;
}

double Cotacao::get_valor(){
  return this->_valor;
}
