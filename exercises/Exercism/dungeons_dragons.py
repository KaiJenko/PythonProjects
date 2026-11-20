import math
import random

class Character:
    def __init__(self):
        self.strength = self.generate_state()
        self.dexterity = self.generate_state()
        self.constitution = self.generate_state()
        self.intelligence = self.generate_state()
        self.wisdom = self.generate_state()
        self.charisma = self.generate_state()
        self.hitpoints = 10 + modifier(self.constitution)

    def generate_state(self):
        stats = []
        for x in range(4):
            stats.append(random.randrange(1,6))
        stats.sort()
        stats.pop(0)
        return sum(stats)

def modifier(value):
    return math.floor((value - 10) / 2)

Kai = Character()
Kai.generate_state()
print(Kai.hitpoints)
