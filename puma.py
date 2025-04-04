from mammal import Mammal

class Puma(Mammal):
    def __init__(self, age, tick=None):
        super().__init__(age)
        if tick:
            self.tick = tick

    def speak(self):
        print("Roar")

    def __str__(self):
        return f"Puma is {self.age} years old."

    def claw(self):
        print("The puma takes a swipe!")



