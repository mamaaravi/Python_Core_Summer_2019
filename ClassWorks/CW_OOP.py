#creating class Animal and inheriting classes Cow and Eagle

class Animal:
    def __init__(self, spec="None", leg=0):
        self.spec=spec
        self.leg=leg
    def name(self):
        print("Im a "+ self.spec)
    def walk(self):
        print("I can walk!")

class Cow(Animal):
    def __init__(self):
        super().__init__("cow", 4)
    def name(self):
        print("Im a cow") 

class Eagle(Animal):
    def __init__(self):
        super().__init__("eagle", 2)
    def name(self):
        print("Im an eagle") 

a1=Cow()
a1.walk()
a1.name()

a2=Eagle()
a2.walk()
a2.name()


# Створити батьківський клас Figure з методами init: ініціалізується колір, 

#   get_color: повертає колір фігури,
#  info: надає інформацію про фігуру та колір,  
# від якого наслідуються такі класи як Rectangle, Square, які мають інформацію про ширину,
#  висоту фігури, метод square, який знаходить площу фігури.

class Figure:
    def __init__(self, color="transp", sides=0):
        self.color=color
        self.sides=sides
    def get_color(self):
        return self.color
    def info(self):
        print("I'm "+self.color)

class Rectangle(Figure):
    def __init__(self, height=0, width=0):
        super().__init__("red", 4)
        self.height=height
        self.width=width
    def square(self):
        return int(self.height*self.width)
    def info(self):
        print("I'm "+self.color+" rectangle")

    
class Square(Figure):
    def __init__(self, height=0):
        super().__init__("blue", 4)
        self.height=height
    def square(self):
        return self.height**2
    def info(self):
        print("I'm "+self.color+" square")


r=Rectangle(2, 4)
print(r.square())
print(r.info())

s=Square(5)
print(s.square())
print(s.info())