#include "HistoricoBovespa.hpp"


void HistoricoBovespa::inserir_cotacao(string sigla, string data, double valor){
       p1._data=data;
       p1._valor=valor;

         keys.insert(sigla);//regista todas a key possiveis(como é um set nao tem como ter keys repetidas).
    
        _sigla[sigla].push_back(p1);//crio o map com a chave ao mesmo tempo que insiro na traseira do vector respectivo do map. 
   }


double HistoricoBovespa::calcular_valor_medio_acao(string sigla){
      double _quant;
      double _soma;
      double _med;

      _quant = _sigla[sigla].size();//tamanho do vector respectivo da sigla.
  
        for(double i = 0; i<_quant;++i){
            _soma = _soma + _sigla[sigla][i]._valor;
             }
             
  _med = _soma / _quant;

  return _med;//media
   }


Cotacao* HistoricoBovespa::recuperar_cotacao_maxima_acao(string sigla){
       double _quant;
       Cotacao* _max = new Cotacao;
       _max->_data = _sigla[sigla][0]._data;
       _max->_valor = _sigla[sigla][0]._valor;
  //utilizo a forma mais simples de determinar o maior termo "por substituiçao sucessiva"

        _quant = _sigla[sigla].size();

      for(double i = 0; i<_quant;++i){
        if(_sigla[sigla][i]._valor > _max->_valor){
            _max->_data = _sigla[sigla][i]._data;
            _max->_valor = _sigla[sigla][i]._valor;
        }
      }

   return _max;//retorna o ponteiro da cotaçao do maior valor
   }


Cotacao* HistoricoBovespa::recuperar_cotacao_minima_acao(string sigla){
        double _quant;
       Cotacao* _min = new Cotacao;
       _min->_data = _sigla[sigla][0]._data;
       _min->_valor = _sigla[sigla][0]._valor;
//utilizo a forma mais simples de determinar o menor termo "por substituiçao sucessiva"

        _quant = _sigla[sigla].size();

      for(double i = 0; i<_quant;++i){
        if(_sigla[sigla][i]._valor < _min->_valor){
            _min->_data = _sigla[sigla][i]._data;
            _min->_valor = _sigla[sigla][i]._valor;
        }
      }

   return _min;//retorna o ponteiro da cotaçao do menor valor
   }


void HistoricoBovespa::imprimir_estatisticas_completas(){

  for(string n : keys){//percorro as keys e utilizo as keys guardadas no set para imprimir.
    cout<< n <<" ";
    for(Cotacao it : _sigla[n]){//percorro todo o vector do respectivo map da key
        cout<< it._valor<<" ";
    }

    cout<< "| ";
    cout<< recuperar_cotacao_minima_acao(n)->_valor<<" ";
    cout<< recuperar_cotacao_maxima_acao(n)->_valor<<" ";
    cout<< calcular_valor_medio_acao(n)<<" ";
    cout<< endl;

  }

   }

