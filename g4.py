import pgzrun

HEIGHT =500
WIDTH = 600

p = Actor("ironman", pos=(100,100))

speed=8


def draw():
    screen.clear()
    p.draw()

def update():
    player_control()

    def player_control():
        print("moving")
        for i in range(0,10):
           p.y+=randint(1,20)
           p.y-=randint(1,20)

pgrun.go()

        

#outside function the fuction
pgzrun.go()