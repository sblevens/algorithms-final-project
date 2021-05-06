import unittest
from bresenham import bresenham_alg
from bresenham import drawLine

class TestBresenham(unittest.TestCase):

   def test_line_slope_one(self):
      points = []
      bresenham_alg(0,0,10,10,points)
      for i in range(10):
         self.assertEqual(points[i],(i,i),"should be postitive slope of 1")

   def test_line_steep_slope(self):
      points = []
      bresenham_alg(0,0,90,270,points)
      for i in range(1,91):
         x,y = points[i]
         x0,y0 = points[i-1]
         self.assertGreaterEqual(x,x0)
         self.assertGreaterEqual(y,y0)


   def test_line_not_steep_slope(self):
      points = []
      bresenham_alg(0,0,250,100,points)
      for i in range(1,251):
         x,y = points[i]
         x0,y0 = points[i-1]
         self.assertGreaterEqual(x,x0)
         self.assertGreaterEqual(y,y0)

   def test_line_negative_steep_slope(self):
      points = []
      points = []
      bresenham_alg(0,0,90,-200,points)
      for i in range(1,91):
         x,y = points[i]
         x0,y0 = points[i-1]
         #runs lowest y value to largest y value
         self.assertLessEqual(x,x0)
         self.assertGreaterEqual(y,y0)

   def test_line_negative_not_steep_slope(self):
      points = []
      points = []
      bresenham_alg(0,0,150,-90,points)
      for i in range(1,151):
         x,y = points[i]
         x0,y0 = points[i-1]
         self.assertGreaterEqual(x,x0)
         self.assertLessEqual(y,y0)
   
   def test_line_second_quadrant(self):
      points = []
      bresenham_alg(-90,0,0,270,points)
      for i in range(1,91):
         x,y = points[i]
         x0,y0 = points[i-1]
         self.assertGreaterEqual(x,x0)
         self.assertGreaterEqual(y,y0)

   def test_line_third_quadrant(self):
      points = []
      bresenham_alg(-90,-270,0,0,points)
      for i in range(1,91):
         x,y = points[i]
         x0,y0 = points[i-1]
         self.assertGreaterEqual(x,x0)
         self.assertGreaterEqual(y,y0)

   def test_line_fourth_quadrant(self):
      points = []
      bresenham_alg(0,-270,90,0,points)
      for i in range(1,91):
         x,y = points[i]
         x0,y0 = points[i-1]
         self.assertGreaterEqual(x,x0)
         self.assertGreaterEqual(y,y0)
   

if __name__ == '__main__':
   unittest.main()