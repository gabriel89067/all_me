
// NÃO ALTERE ESSA LINHA
#include "avaliacao_basica_bovespa.hpp"

int main() {
  
    // NÃO ALTERE ESSA LINHA
    avaliacao_basica();


     HistoricoBovespa historico;
    string key;
    string data;
    double valor;
    
    while(cin >> key >> data >> valor){
    historico.inserir_cotacao(key,data,valor);
    }

    historico.imprimir_estatisticas_completas();

    return 0;
}