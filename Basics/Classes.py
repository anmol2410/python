# Pascal Naming Convention 
class Point: #Blue print
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        print('move')
    
    def draw(self):
        print('draw')


# Object
# point1=Point()
# point1.draw()
# point1.x=10
# print(point1.x)


# point2=Point()
# point2.x=20
# print(point2.x)


# Constructor
point=Point(10,20)
point.x=90
print(point.x)

# Exercsie
class Person:
    def __init__(self,name): #Constructor
        self.name=name
        
    
    def talk(self):
        print(f'Hi, I am {self.name}')

Anmol=Person("Anmol Gupta")
Anmol.talk()

radhika=Person("Radhika Rani")
radhika.talk()
        