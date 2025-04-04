import random

class Heart:
    def __init__(self):
        self.bpm = 72

    def beat(self):
        print("Lub-dub")
        self.bpm = random.randint(70, 75)

    def __str__(self):
        return f"Heart is beating at {self.bpm}bpm."

    def __eq__(self, other):
        return self.bpm == other.bpm




