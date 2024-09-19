#include<iostream>
#include<string>

  int main(){

  int numero,x,y,b,c;
  std::string estrela = "*";
  std::cin >> numero;

  for(x=1;x<=numero;x++){

    for(y=0;y!=x;y++){
        std::cout << estrela;
    }
  std::cout << std::endl;

  }

    for(b=(numero-1);b>=1;b--){

    for(y=0;y!=b;y++){
        std::cout << estrela;
    }
    std::cout << std::endl;
}



  return 0;
  }
