from turtle import *
speed('fastest')
value=300

while value>0:
     fd(value)
     left(90)
     value-=10
     write(value)
     
mainloop()