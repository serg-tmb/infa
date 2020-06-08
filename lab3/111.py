from graph import *

def row ( y ):
  x = 40
  for i in range(5):
    circle(x, y, 40)
    x += 80
    
y = 40
for k in range(3):
  row(y)
  y += 80

run()