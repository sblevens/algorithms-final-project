from bresenham import bresenham_alg
from bresenham import drawLine

def line_slope_one():
   points = []
   bresenham_alg(0,0,30,30,points)
   drawLine(points,'black')

def line_steep_slope():
   points = []
   bresenham_alg(0,0,90,270,points)
   drawLine(points, 'purple')

def line_not_steep_slope():
   points = []
   bresenham_alg(0,0,250,100,points)
   drawLine(points, 'blue')

def negative_steep_slope_third_quadrant():
   points = []
   bresenham_alg(-90,-10,0,-150,points)
   drawLine(points, 'green')



def main():
   line_slope_one()
   line_steep_slope()
   line_not_steep_slope()
   negative_steep_slope_third_quadrant()


main()