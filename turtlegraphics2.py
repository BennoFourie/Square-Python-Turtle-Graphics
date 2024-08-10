
import turtle
t = turtle.Turtle()

def square(x,y):
    for i in range(4):
        t.forward(x)
        t.right(y)
        
for i in range (200):
    square(100,90)
    t.right(5)
    
t.done()
        
