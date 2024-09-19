#include <iostream>

 int main() {
 int numero;
 int vetorpar[100];
 int vetorimpar[100];
 int p = 0;
 int i = 0;

 while(std::cin >> numero){

if((numero%2) == 0){
    vetorpar[p] = numero;
    p++;
}
else{vetorimpar[i] = numero;
i++;}
 }

 int conpar = 0;
 int conimpar = 0;
 int con = 0;

 for(int x = 0; x < p;x++){
    for(int y = x + 1; y < p;y++){
            if(vetorpar[x] == vetorpar[y]){
               vetorpar[y] = 0;
               }}}

for(int x = 0; x < i;x++){
    for(int y = x + 1; y < i;y++){
            if(vetorimpar[x] == vetorimpar[y]){
               vetorimpar[y] = 0;
               }}}

while(con<p){
    if(vetorpar[con] != 0){
    std::cout << vetorpar[con] << std::endl;
    }
    con ++;
}
 std::cout << std::endl;
 con = 0;
 while(con<i){
        if(vetorimpar[con] != 0){
    std::cout << vetorimpar[con] << std::endl;}
    con ++;
}

 return 0;
 }
