#ifndef FIGURAS_H
#define FIGURAS_H
#include <math.h>

/**
 * \class Figure
 *
 * \brief Esta eh a interface de qualquer figura desta aplicacao. O que
 * caracteriza uma figura eh a habilidade de decidir se ela contem ou nao um
 * ponto. Note que figuras e pontos sao representados sempre em duas dimensoes.
 */
class Figure {
  public:
    /**
     * \brief Este metodo determina se o ponto (x, y) esta contido na figura.
     * \param x Coordenada X do ponto.
     * \param y Coordenada Y do ponto.
     */
    virtual bool contains(double x, double y) const = 0;
    /**
     * \brief A classe prove um destrutor virtual, pois ela foi feita para ser
     * implementada por outras classes, via heranca.
     */
    virtual ~Figure() {}
};

/**
 * \class Rectangle
 *
 * \brief Um retangulo eh uma figura unicamente determinada por um canto
 * inferior esquerdo, mais largura e altura.
 */
class Rectangle: public Figure {
  public:
    
     const double _x; ///< Coordenada X do lado inferior-esquerdo do retangulo
    const double _y; ///< Coordenada Y do lado inferior-esquerdo do retangulo
    const double _l; ///< Largura do Retangulo
    const double _a; ///< Altura do Retangulo
    /**
     * \brief Metodo construtor que cria um retangulo com canto inferior
     * esquerdo na coordenada (xx, yy), largura igual a ll e altura igual ao
     * parametro aa.
     * \param xx Canto esquerdo do retangulo
     * \param yy Canto inferior do relangulo
     * \param ll A largura do retangulo
     * \param aa A altura do retangulo
     */
    Rectangle(double xx, double yy, double ll, double aa): _x(xx), _y(yy), _l(ll), _a(aa) {}
    
    /**
     * \brief Determina se o ponto (x, y) estah contido dentro deste retangulo.
     */
    bool contains(double x, double y) const {
   double rep_y = this->_a+this->_y;
   double rep_x = this->_l+this->_x;
   int x_x = 0;
    if(x >= this->_x && x <= (rep_x)){
        x_x++;
    }
    if(x_x != 0){
   if(y >= this->_y && y <= (rep_y)){
    return true; 
    }
     
    }
        return false;
    }
   
};


/**
 * \class Circle
 *
 * \brief Um circulo eh uma figura determinada por um centro e um raio.
 */
class Circle: public Figure {
  public:
    /**
     * \brief Metodo contrutor que produz um circulo com centro no ponto
     * (xx, yy) e raio rr.
     * \param xx Coordenada X do centro do circulo
     * \param yy Coordenada Y do centro do circulo
     * \param rr Raio do circulo
     */
    Circle(double xx, double yy, double rr): _x(xx), _y(yy), _r(rr) {}
    Circle() : _x(0), _y(0), _r(0) {}
    /**
     * \brief Determina se o ponto (x, y) estah contido dentro deste circulo.
     */
    bool contains(double x, double y) const {
      double Ds_P_C = sqrt((pow((x-_x),2))+(pow((y-_y),2)));
      if(Ds_P_C <= _r){
        return true;
      }
      return false;
    }
    const double _x; ///< Coordenada X do centro do circulo
    const double _y; ///< Coordenada Y do centro do circulo
    const double _r; ///< O raio do circulo
};

class Fusion: public Figure {
  public:
    
  const Figure& _rhs ;
  const Figure& _chs ;
    double _opera;
    //Fusion(double xc, double yc, double rc,double xr, double yr, double lr, double ar): _xc(xc), _yc(yc), _rc(rc), _xr(xr),_yr(yr) ,_lr(lr) ,_ar(ar) {}
   Fusion( const Figure& rhs ,const Figure& chs, double opera) : _rhs(rhs) , _chs(chs) , _opera(opera) {}
   
    bool contains(double x, double y) const {

    
    
    
    if(this->_opera == 1){
    
    
    if(this->_rhs.contains(x,y) || this->_chs.contains(x,y)){
   
    return true;
    }
    
    return false;
    }
    
    if(_opera == 2){
    
    
    
    if(_chs.contains(x,y)){
        return false;
       }
    if(_rhs.contains(x,y)){ 
    return true;}
    }
    
    }
    
   
};
/**
 * \brief Cria uma nova figura formada pela uniao de lhs e rhs. Esta nova
 * figura F deve ter a seguinte invariante: F.contains(px, py) eh verdade se
 * o ponto (px, py) estiver contido em lhs ou em rhs.
 */
Figure* operator+(const Figure& lhs, const Figure& rhs) {

   Figure* sum = new Fusion(lhs , rhs , 1);
 
  return sum;
}

/**
 * \brief Cria uma nova figura formada pela diferenca entre lhs e rhs.
 * Est nova figura, F, possui a seguinte invariante: F.contains(x, y) eh
 * verdade se o ponto (x, y) estiver contido em lhs, mas nao estiver contido
 * em rhs.
 */
Figure* operator-(const Figure& lhs, const Figure& rhs) {
 
    Figure* sub = new Fusion(lhs , rhs , 2);
 
  return sub;
}

#endif