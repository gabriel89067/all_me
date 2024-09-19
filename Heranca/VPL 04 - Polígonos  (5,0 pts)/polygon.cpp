/**
 * Todas as tarefas deste exercicio devem ser feitas sobre esse arquivo.
 * Os metodos e operacoes marcados com a tag "TODO" devem ser editados.
 */

#include <iostream>
#include "polygon.h"

std::ostream& operator << (std::ostream &out, const Polygon &poly) {
  for (const Point& p: poly.limits) {
    out << " " << p;
  }
  return out;
}

bool operator == (const Polygon &lhs, const Polygon &rhs) {
 int tru = 0;
 
      for(const Point &p2 : (const std::vector<Point>)rhs){
         if(lhs.contains(p2)){
           tru++;  
            }}
            
     
            
            
      
      
if(tru >= 2){
return true;
}

return false;
}


bool Point::contains(const Point& p) const {
  return p.x == this->x && p.y == this->y;
}


std::ostream& operator << (std::ostream &out, const Point &p) {
  out << "(" << p.x << ", " << p.y << ")";
  return out;
}


bool RightRectangle::contains(const Point& p) const {
  
  
   
   int x_x = 0;
    if((p.x >= this->limits[0].x && p.x <= this->limits[1].x)||(p.x >= this->limits[1].x && p.x <= this->limits[0].x)){
        x_x++;
    }
    if(x_x != 0){
       if((p.y >= this->limits[0].y && p.y <= this->limits[1].y)||(p.y >= this->limits[1].y && p.y <= this->limits[0].y)){
       return true; 
     }
     
    }
        return false;
    }
   

Point::Point(int xx, int yy): x(xx), y(yy) {
  
  limits.push_back(*this);
}

RightRectangle::RightRectangle(int x0, int y0, int x1, int y1) {
   Point inser1(x0,y0);
   Point inser2(x1,y1);
   this->limits.push_back(inser1);
   this->limits.push_back(inser2);
}