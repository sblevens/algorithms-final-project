//----------------------------------------------------------------------
// Name: Sami Blevens
// File: bresenham.cpp
// Date: Spring 2021
// Desc: Bresenham Line Algorithm.
//----------------------------------------------------------------------

#include <iostream>
#include <CTurtle.hpp>

using namespace std;
namespace ct = cturtle;

// only works for slopes <= 1 in first quadrant
void draw(int x1, int y1, int x2, int y2){
   bool steep = false;
   //check if slope is steep, ie >1
   if(abs(y2-y1)>abs(x2-x1)){
      steep = true;
   }
   if(steep){
      swap(x1,y1);
      swap(x2,y2);
   }
   
   //make coordinates move left to right
   if(x1>x2){
      swap(x1,x2);
      swap(y1,y2);
   }


   int dx = x2-x1;
   int dy = abs(y2-y1);
   //pos or neg slope
   int y_inc = 1;
   if(y1 > y2){
      y_inc = -1;
   }
   
   int error = dx >> 1;
   int y = y1;

   for(int x = x1; x <= x2; ++x){
      if(steep){
         //draw(y,x);
         cout << "(" << y <<","<<x<<")"<<endl;
      } else {
         //draw(x,y);
         cout << "(" << x <<","<<y<<")"<<endl;
      }
      error -= dy;
      if(error < 0){
         y += y_inc;
         error += dx;
      }
   }
}

void test(){
   ct::TurtleScreen scr;
   ct::Turtle turtle(scr);
   turtle.speed(ct::TS_SLOWEST);
   turtle.fillcolor({"purple"});
   turtle.begin_fill();
   for(int i=0; i < 4; ++i){
      turtle.forward(50);
      turtle.right(90);
   }
   turtle.end_fill();
   scr.bye();
}

int main(){
   cout<<"(0,0) to (1,1)"<<endl;
   draw(0,0,1,1);
   cout << endl;
   cout<<"(0,0) to (3,3)"<<endl;
   draw(0,0,3,3);
   cout << endl;
   cout<<"(0,0) to (5,4)"<<endl;
   draw(0,0,5,4);
   cout << endl;
   cout<<"(0,0) to (3,8)"<<endl;
   draw(0,0,3,8);
   cout << endl;
   cout<<"(3,8) to (7,2)"<<endl;
   draw(3,8,7,2);
   cout << endl;
   cout<<"(7,2) to (3,8)"<<endl;
   draw(7,2,3,8);
   test();
}