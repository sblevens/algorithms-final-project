
import turtle

def bresenham_alg(x1,y1,x2,y2,points):
   steep = False
   if(abs(y2-y1)>abs(x2-x1)):
      steep = True
   
   if(steep):
      x1,y1 = y1,x1
      x2,y2 = y2,x2
   

   if(x1>x2):
      x1,x2 = x2,x1
      y1,y2 = y2,y1
   

   dx = x2-x1
   dy = abs(y2-y1)
   y_inc = 1
   if(y1>y2):
      y_inc = -1
   

   error = dx >> 1
   y = y1

   for x in range(x1,x2+1):
      if(steep):
         print("C" + str(y) + "," + str(x) + ")")
         points.append(tuple((y,x)))
      else:
         print("C" + str(x) + "," + str(y) + ")")
         points.append(tuple((x,y)))
      error -= dy
      if(error < 0):
         y += y_inc
         error += dx


def drawLine(points,color):

    #q1, q2, q3, q4 = algorithm.midPointCircle(xCenter, yCenter, radius);
    #points = algorithm.midPointCircle(xCenter, yCenter, radius)

    s = turtle.Screen()
    t = turtle.Turtle()
    t.penup()

    t.color(color)
    t.speed(10)

    for i in range(len(points)):
      x, y = points[i]
      t.goto(x, y)
      t.pendown()
      t.forward(1)
      t.penup()

