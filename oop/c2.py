class Cat:
    def __init__(self,breed,fur_color,gender='F',age=1,w=1,h=1,is_tamed=True):
        self.breed=breed
        self.fur_color=fur_color
        self.gender='M'
        self.age=age
        self.w=w
        self.h=h
        self.is_tamed=is_tamed

    def eat(self,food='catfood'):
        print(f'🐈 is eating')

    def play(self):
        print('🐈 is playing')

    def sleep(self):
        print('🐈 is sleeping')
    
    def info(self):
        print('--*15')
        print(f'Breed:{self.breed}')
        print(f'Age:{self.age}year')
        print(f'Weight:{self.w}kg')
        print(f'Height:{self.h}ft')
        print(f'Gender:{self.gender}')
        print(f'Color:{self.fur_color}')
        print(f'Tamed:{self.is_tamed}')
        print(f'--'*15)         #optional design

tom=Cat('street cat','grey',age=100,gender='M')
soni=Cat('house cat','brown',age=3)
snowbell=Cat('persian','white',age=3,w=4)
spike=Cat('jungle cat','black',age=2,w=1,h=1.2,is_tamed=False)

print('TOM')
tom.info()
tom.eat('jerry')

print('SNOWBELL')
snowbell.info()
snowbell.eat('stuart')



