import random
import pgzrun

WIDTH = 1312
HEIGHT = 665
MAX_BULLETS = 3

level = 1
lives = 3
score = 0

bg = Actor("shooting",center =(300,500))
# player = Actor("player", (200, 580))
enemies = []
bullets = []
bombs = []

def draw():
   bg.draw()

pgzrun.go()