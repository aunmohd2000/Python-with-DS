from turtle import *
pensize(3)
for i in range(4):
    pencolor('red')
    fd(100)
    for i in range(6):
       pencolor("green")
       fd(60)
       pencolor('black')
       write(i, font=('arial',14,'normal'),align ='left')
       left(360/6)
    left(360/4)
mainloop()