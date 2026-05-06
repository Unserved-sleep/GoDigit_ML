class Animal:
    def __init__(self, name, movement_type):
        self.name = name
        self.movement_type = movement_type

    def move(self):
        self.movement_type.move(self.name)

class SwimmingMovement:
    def move(self, name):
        print(f"{name} is swimming")

class FlyingMovement:
    def move(self, name):
        print(f"{name} is flying")

class WalkingMovement:
    def move(self, name):
        print(f"{name} is walking")

class EggLaying:
    def lay_egg(self, name):
        print(f"{name} laid an egg")

class Fish:
    def __init__(self, name):
        self.animal = Animal(name, SwimmingMovement())

    def move(self):
        self.animal.move()

class Bird:
    def __init__(self, name):
        self.animal = Animal(name, FlyingMovement())
        self.egg_laying = EggLaying()

    def move(self):
        self.animal.move()

    def lay_egg(self):
        self.egg_laying.lay_egg(self.animal.name)

class Penguin:
    def __init__(self, name):
        self.animal = Animal(name, WalkingMovement())
        self.egg_laying = EggLaying()

    def move(self):
        self.animal.move()

    def lay_egg(self):
        self.egg_laying.lay_egg(self.animal.name)


penguin = Penguin("Pingu")
penguin.move()
penguin.lay_egg()