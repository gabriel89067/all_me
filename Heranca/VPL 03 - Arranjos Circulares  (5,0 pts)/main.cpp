#include <iostream>

#include "RingArray.h"

void fer_assert(const bool expr, const char* msg) {
  if (!expr) {
    std::cout << msg << std::endl;
    exit(1);
  }
}

template <class T, unsigned N>
void RingArray<T, N>::add(T value) {
    int cont = 0;
    
    if(num_elem == 0){
    if(indice == N){
      indice--;
    }
    buf[indice] = value;
    num_elem++;
    indice++;
    cont++;  
    
    }
     
    if(cont == 0){
    if(num_elem<=(N-1)){    
    buf[indice] = value;
    _last = indice;
    indice++;
    num_elem++;
    cont++;
    }}
     
     
     if(num_elem == N){
       std::cout<<"Erro: anel cheio.";
       exit(1);
     }
    
}

template <class T, unsigned N>
T RingArray<T, N>::get() {
  unsigned title = _first;
  
  if(num_elem == 0){
     std::cout<<"Erro: anel vazio."; 
     exit(1);
      
  }
  
  if(title == N){
      title--;
      _first--;
  }
  
  _first = title + 1;
  num_elem --;
  
  return buf[title];
    
}

template <class T, unsigned N>
bool RingArray<T, N>::isFull() const {

    return (num_elem == N-1);
}

template <class T, unsigned N>
bool RingArray<T, N>::isEmpty() const {

    return (num_elem==0);
}

template <class T>
void test_add_then_get() {
  RingArray<T, 8> r;
  T value;
  while (std::cin >> value) {
    r.add(value);
  }
  while (!r.isEmpty()) {
    std::cout << r.get() << std::endl;
  }
}

template <class T>
void test_add_or_get() {
  RingArray<T, 8> r;
  T value;
  char c;
  while (std::cin >> c) {
    if (c == '+') {
      std::cin >> value;
      r.add(value);
    } else if (c == '-') {
      std::cout << r.get() << std::endl;
    } else {
      std::cout << "Invalid operation\n";
    }
  }
}

int main () {
  char data;
  while (std::cin >> data) {
    switch (data) {
      case 'd': test_add_then_get<double>();
                break;
      case 's': test_add_then_get<std::string>();
                break;
      case 'D': test_add_or_get<double>();
                break;
      case 'S': test_add_or_get<std::string>();
                break;
      default: std::cout << "Invalid type\n";
    }
  }
  return 0;
}