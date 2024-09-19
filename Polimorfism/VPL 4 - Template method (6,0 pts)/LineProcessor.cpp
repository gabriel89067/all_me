#include <regex>
#include <math.h>
#include <string>
#include <vector>
#include <sstream>

#include "LineProcessor.hpp"

void LinePrinter::processaLinha(const std::string &str) {
  std::cout << str << std::endl;
}

bool ContadorPopRural::linhaValida(const std::string &str) const {
  // Neste exemplo usaremos expressoes regulares para verificar se uma linha
  // eh valida ou nao.
  //
  // Esta expressao regular eh formada por cinco partes. Cada uma dessas
  // partes eh um dos tres tipos de padrao regular abaixo:
  //
  // \\w+ eh qualquer palavra com um ou mais digitos, letras e sublinhas (_)
  // \\s* eh qualquer sequencia de zero ou mais espacos (inclui tab)
  // \\d+ eh qualquer sequencia de um ou mais digitos
  std::regex regularExpr("\\w+\\s*\\d+\\s*\\d+");

  // A funcao regex_match vai retornar verdadeiro se a string str casa-se com
  // a expressao regular que acabamos de criar:
  return std::regex_match(str, regularExpr);
}

void ContadorPopRural::processaLinha(const std::string &str) {
  //
  // Em geral eh mais facil ler dados de uma string se a string eh transformada
  // em um objeto do tipo stringstream:
  std::stringstream ss(str);
  //
  // Iremos ler os dados da string nestas tres variaveis abaixo:
  std::string nomePais;
  unsigned populacao, percUrbana;
  //
  // Como sabemos que a linha contem string int int, podemos fazer a leitura
  // facilmente usando o operador de streaming:
  ss >> nomePais >> populacao >> percUrbana;
  //
  // Note que precisamos arredondar o valor que serah impresso. O arredondamento
  // serah feito via a funcao floor. Ou seja, decimais serao sempre
  // arredondados para baixo:
  unsigned popRural = floor(populacao - (populacao * (percUrbana/100.0)));
  //
  // Uma vez encontrados os valores que precisam ser impressos, seguimos o
  // modelo do enunciado do exercicio:
  std::cout << popRural << " pessoas vivem no campo no " << nomePais <<
    std::endl;
}

bool ContadorNumNaturais::linhaValida(const std::string &str) const {
 std::regex Num_N("\\s*\\d*\\s*\\d*\\s*\\d*\\s*\\d*\\s*\\d*\\s*\\d*\\s*\\d*\\s*\\d*\\s*\\d*\\s*\\d*");
  
  return std::regex_match(str,Num_N);
}

void ContadorNumNaturais::processaLinha(const std::string &str) {
  std::stringstream num(str);
  int num_nn;
  int total=0;
  
  while(num >> num_nn){
  total = total + num_nn;
  }
  std::cout << total << std::endl;
}

bool LeitorDeFutebol::linhaValida(const std::string &str) const {
 std::regex fut("\\s*[[:alpha:]]*\\s+\\d+\\s+[[:alpha:]]*\\s+\\d+");
  
  
   return std::regex_match(str,fut);
}

void LeitorDeFutebol::processaLinha(const std::string &str) {
  std::stringstream fut(str);
  std::string time1,time2;
  int gols1 = 0;
  int gols2 = 0;
  
  fut >> time1 >> gols1 >> time2 >> gols2;
  
   if(gols1 == gols2){
    
    std::cout << "Empate" << std::endl;
  }else if(gols1 > gols2){
  std::cout << "Vencedor: " << time1 << std::endl;
  }else{
  std::cout << "Vencedor: " << time2 << std::endl;
  }
}

void ContadorDePalavras::processaLinha(const std::string &str) {
 std::stringstream pala(str);
  std::string non;
  int contador = 0;
  
  while(pala >> non){
    contador++;
  }
  
  
  std::cout << contador << std::endl;
}

bool InversorDeFrases::linhaValida(const std::string &str) const {
  std::regex fras("\\s*[[:alpha:]]*\\s*[[:alpha:]]*\\s*[[:alpha:]]*\\s*[[:alpha:]]*\\s*[[:alpha:]]*\\s*[[:alpha:]]*\\s*");

  return std::regex_match(str,fras);
}

void InversorDeFrases::processaLinha(const std::string &str) {
  std::stringstream fras(str);
  std::string non = "";
  std::string s1, s2, s3, s4, s5, s6;
  fras >> s1 >> s2 >> s3 >> s4 >> s5 >> s6;
  non = (s6 + " ") + (s5 + " ") + (s4 + " ") + (s3 + " ") + (s2 + " ") + (s1 + " ");
  std::cout << non << std::endl;
}

bool EscritorDeDatas::linhaValida(const std::string &str) const {
  std::regex dat("\\s*\\d\\d?/\\d\\d?/\\d{4}");
 
 return std::regex_match(str,dat);
}

void EscritorDeDatas::processaLinha(const std::string &str) {
  int mod = 0;
  std::string dia ="";
  std::string mes ="";
  std::string ano ="";
  for(int i=0; i<str.length(); i++){

        if(str[i] == '/'){
        mod++;
        }else if(mod == 0){
         dia = dia + str[i];
        }else if(mod == 1){
          mes = mes + str[i];
        }else if(mod == 2){
          ano = ano + str[i];
        }}
        
  if(mes == "1"||mes == "01"){
      std::cout << "Jan" << std::endl;
  }
   if(mes == "2"||mes == "02"){
      std::cout << "Fev" << std::endl;
   }
   if(mes == "3"||mes == "03"){
      std::cout << "Mar" << std::endl;
   }
   if(mes == "4"||mes == "04"){
      std::cout << "Abr" << std::endl;
   }
    if(mes == "5"||mes == "05"){
      std::cout << "Mai" << std::endl;
    }
   if(mes == "6"||mes == "06"){
      std::cout << "Jun" << std::endl;
   }
    if(mes == "7"||mes == "07"){
      std::cout << "Jul" << std::endl;
    }
     if(mes == "8"||mes == "08"){
      std::cout << "Ago" << std::endl;
     }
    if(mes == "9"||mes == "09"){
      std::cout << "Set" << std::endl;
    }
     if(mes == "10"){
      std::cout << "Out" << std::endl;
     }
     if(mes == "11"){
      std::cout << "Nov" << std::endl;
     }
     if(mes == "12"){
      std::cout << "Dez" << std::endl;
  }

}