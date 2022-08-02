from turtle import *

speed('slowest')
pencolor('red')
bgcolor('black')
width(5)

side= 3
size= 200
for i in range(side):
    fd(size)
    lt(360/side)

mainloop()