import pgzrun

HEIGHT = 500
WIDTH = 600

p= Actor('ironman',pos=(100,100))

def draw():
    screen.clear()
    screen.draw.text("Welcome to pgzero",(20,10),color='red',fontsize=60)
    screen.draw.text("Created by aun",(10,50),color='White')
    p.draw()

pgzrun.go()