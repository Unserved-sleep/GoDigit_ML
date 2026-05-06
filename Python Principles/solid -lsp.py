from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        print("I can fly")

class NonFlyingBird(Bird):
    def move(self):
        print("I can run")

def make_bird_move(bird):
    bird.move()


sparrow = FlyingBird()
ostrich = NonFlyingBird()

make_bird_move(sparrow)
make_bird_move(ostrich) 