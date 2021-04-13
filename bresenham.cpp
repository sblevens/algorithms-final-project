//----------------------------------------------------------------------
// Name: Sami Blevens
// File: bresenham.cpp
// Date: Spring 2021
// Desc: Bresenham Line Algorithm.
//----------------------------------------------------------------------

#include <iostream>

using namespace std;

// only works for slopes <= 1 in first quadrant
void draw(int x1, int y1, int x2, int y2){
   //cout << "(" << x1 <<","<<y1<<")"<<endl;
   int dx = x2-x1;
   int dy = y2-y1;
   float m = ((float)y2-y1)/((float)x2-x1);
   float error = 0;
   int y = y1;
   for(int x = x1; x <= x2; ++x){
      //draw(x,y);
      cout << "(" << x <<","<<y<<")"<<endl;
      error += m;
      if(error >= .5){
         y++;
         error -= 1;
      }
   }
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
   
}